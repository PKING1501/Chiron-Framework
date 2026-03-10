#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Type inference engine for ChironLang

import sys
from chirontypes import Type
from ChironAST.ChironAST import AST, Sum, Div

class TypeInferenceError(Exception):
    pass

class TypeInference:
    def __init__(self):
        self.symbols = {}          # var name -> inferred type
        self.input_vars = set()    # variables that come from command line
        self.used_vars = set()
        self.errors = []            # list of error messages
        self.current_function = None   # not used (no functions yet)

    def add_input_variable(self, var_name, var_type):
        """Add a command-line input variable to the symbol table."""
        self.symbols[var_name] = var_type
        self.input_vars.add(var_name)

    def infer(self, ast_root):
        """Main entry point: walk the instruction list and infer types."""
        for instr_tuple in ast_root:
            instr = instr_tuple[0]
            self.visit(instr)
        
        # Warn about unused input variables
        for var_name in self.input_vars:
            if var_name not in self.used_vars:
                print(f"Warning: Input variable '{var_name}' was never used")
        
        return len(self.errors) == 0

    def error(self, node, message):
        """Record a type error."""
        self.errors.append(f"Type error at {str(node)}: {message}")

    # ----------------------------------------------------------------------
    # Visiting methods
    # ----------------------------------------------------------------------

    def visit(self, node):
        """Dispatch to the appropriate visit_ method."""
        method_name = 'visit_' + node.__class__.__name__
        print(f"Visiting {node.__class__.__name__}")   # ← debug
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        """Fallback for unknown node types."""
        # Visit children, but return UNKNOWN for this node
        for attr in dir(node):
            if attr.startswith('_'):
                continue
            value = getattr(node, attr)
            if isinstance(value, AST):
                self.visit(value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, AST):
                        self.visit(item)
        return Type.UNKNOWN   # ← add this line
    # ----------------------------------------------------------------------
    # Instruction nodes
    # ----------------------------------------------------------------------

    def visit_AssignmentCommand(self, node):
        # First visit the right-hand side expression (to infer its type)
        rhs_type = self.visit(node.rexpr)

        print(f"Assignment: LHS={node.lvar.varname}, RHS type={rhs_type}, RHS node={type(node.rexpr).__name__}")   # ← debug
        
        # Get the left-hand side variable
        var_node = node.lvar
        var_name = var_node.varname
        declared_type = var_node.declared_type

        # Determine the actual type to assign
        if declared_type is not None:
            # Check compatibility: RHS type must be assignable to declared type
            if not self.is_assignable(rhs_type, declared_type):
                self.error(node, f"Cannot assign {rhs_type.value} to variable '{var_name}' of type {declared_type.value}")
                inferred = declared_type   # fallback to declared type to continue
            else:
                inferred = declared_type
        else:
            # No declaration: variable gets the RHS type (inference)
            inferred = rhs_type

        # Update symbol table
        self.symbols[var_name] = inferred
        var_node.inferred_type = inferred
        return inferred

    def visit_ConditionCommand(self, node):
        cond_type = self.visit(node.cond)
        if cond_type != Type.BOOLEAN:
            self.error(node, f"Condition must be boolean, got {cond_type.value}")
        # Return type not used for instructions
        return None

    def visit_MoveCommand(self, node):
        expr_type = self.visit(node.expr)
        if not expr_type.is_numeric():
            self.error(node, f"Move command requires numeric argument, got {expr_type.value}")
        return None

    def visit_PenCommand(self, node):
        # No expression, always valid
        return None

    def visit_GotoCommand(self, node):
        x_type = self.visit(node.xcor)
        y_type = self.visit(node.ycor)
        if not x_type.is_numeric():
            self.error(node, f"goto x-coordinate must be numeric, got {x_type.value}")
        if not y_type.is_numeric():
            self.error(node, f"goto y-coordinate must be numeric, got {y_type.value}")
        return None

    def visit_NoOpCommand(self, node):
        return None

    def visit_PauseCommand(self, node):
        return None

    # ----------------------------------------------------------------------
    # Expression nodes
    # ----------------------------------------------------------------------

    def visit_Num(self, node):
        # inferred_type already set by builder
        return node.inferred_type

    def visit_FloatLiteral(self, node):
        return node.inferred_type

    def visit_DoubleLiteral(self, node):
        return node.inferred_type

    def visit_StringLiteral(self, node):
        return node.inferred_type

    def visit_BoolLiteral(self, node):
        return node.inferred_type

    def visit_Var(self, node):
        var_name = node.varname
        if var_name not in self.symbols:
            self.error(node, f"Variable '{var_name}' used before assignment")
            return Type.ERROR
        
        # Mark as used
        self.used_vars.add(var_name)
        
        node.inferred_type = self.symbols[var_name]
        return node.inferred_type

    # Binary arithmetic operations
    def visit_Sum(self, node):
        return self._handle_binary_arith(node, node.lexpr, node.rexpr)

    def visit_Diff(self, node):
        return self._handle_binary_arith(node, node.lexpr, node.rexpr)

    def visit_Mult(self, node):
        return self._handle_binary_arith(node, node.lexpr, node.rexpr)

    def visit_Div(self, node):
        return self._handle_binary_arith(node, node.lexpr, node.rexpr)

    def _handle_binary_arith(self, node, left, right):
        left_type = self.visit(left)
        right_type = self.visit(right)

        # If either is error, propagate error
        if left_type == Type.ERROR or right_type == Type.ERROR:
            result_type = Type.ERROR

        # String concatenation for '+' only
        elif isinstance(node, Sum) and (left_type == Type.STRING or right_type == Type.STRING):
            if left_type != Type.STRING or right_type != Type.STRING:
                self.error(node, f"String concatenation requires both operands to be strings, got {left_type.value} and {right_type.value}")
                result_type = Type.ERROR
            else:
                result_type = Type.STRING

        # Division always produces at least a float
        elif isinstance(node, Div):
            if left_type.is_numeric() and right_type.is_numeric():
                if left_type == Type.INT and right_type == Type.INT:
                    result_type = Type.FLOAT
                else:
                    result_type = self.promote_numeric(left_type, right_type)
            else:
                self.error(node, f"Invalid operands for division: {left_type.value} and {right_type.value}")
                result_type = Type.ERROR

        # Other numeric operations
        elif left_type.is_numeric() and right_type.is_numeric():
            result_type = self.promote_numeric(left_type, right_type)

        else:
            self.error(node, f"Invalid operands for arithmetic: {left_type.value} and {right_type.value}")
            result_type = Type.ERROR

        node.inferred_type = result_type
        return result_type

    # Unary minus
    def visit_UMinus(self, node):
        expr_type = self.visit(node.expr)
        if expr_type.is_numeric():
            result_type = expr_type   # same type
        else:
            self.error(node, f"Unary minus requires numeric operand, got {expr_type.value}")
            result_type = Type.ERROR
        node.inferred_type = result_type
        return result_type

    # Boolean binary operators
    def visit_AND(self, node):
        return self._handle_binary_bool(node, node.lexpr, node.rexpr)

    def visit_OR(self, node):
        return self._handle_binary_bool(node, node.lexpr, node.rexpr)

    def _handle_binary_bool(self, node, left, right):
        left_type = self.visit(left)
        right_type = self.visit(right)
        if left_type == Type.BOOLEAN and right_type == Type.BOOLEAN:
            result_type = Type.BOOLEAN
        else:
            self.error(node, f"Logical operator requires boolean operands, got {left_type.value} and {right_type.value}")
            result_type = Type.ERROR
        node.inferred_type = result_type
        return result_type

    # Comparison operators
    def visit_LT(self, node):
        return self._handle_comparison(node, node.lexpr, node.rexpr)

    def visit_GT(self, node):
        return self._handle_comparison(node, node.lexpr, node.rexpr)

    def visit_LTE(self, node):
        return self._handle_comparison(node, node.lexpr, node.rexpr)

    def visit_GTE(self, node):
        return self._handle_comparison(node, node.lexpr, node.rexpr)

    def visit_EQ(self, node):
        return self._handle_comparison(node, node.lexpr, node.rexpr, allow_bool=True)

    def visit_NEQ(self, node):
        return self._handle_comparison(node, node.lexpr, node.rexpr, allow_bool=True)

    def _handle_comparison(self, node, left, right, allow_bool=False):
        left_type = self.visit(left)
        right_type = self.visit(right)

        # Both must be comparable: either both numeric, or both boolean (if allowed), or both string
        comparable = False
        if left_type.is_numeric() and right_type.is_numeric():
            comparable = True
        elif allow_bool and left_type == Type.BOOLEAN and right_type == Type.BOOLEAN:
            comparable = True
        elif left_type == Type.STRING and right_type == Type.STRING:
            comparable = True
        else:
            self.error(node, f"Cannot compare {left_type.value} and {right_type.value}")

        result_type = Type.BOOLEAN if comparable else Type.ERROR
        node.inferred_type = result_type
        return result_type

    def visit_NOT(self, node):
        expr_type = self.visit(node.expr)
        if expr_type == Type.BOOLEAN:
            result_type = Type.BOOLEAN
        else:
            self.error(node, f"NOT requires boolean operand, got {expr_type.value}")
            result_type = Type.ERROR
        node.inferred_type = result_type
        return result_type

    def visit_PenStatus(self, node):
        node.inferred_type = Type.BOOLEAN
        return Type.BOOLEAN

    def visit_BoolTrue(self, node):
        node.inferred_type = Type.BOOLEAN
        return Type.BOOLEAN

    def visit_BoolFalse(self, node):
        node.inferred_type = Type.BOOLEAN
        return Type.BOOLEAN

    # ----------------------------------------------------------------------
    # Helper methods
    # ----------------------------------------------------------------------

    def is_assignable(self, source_type, target_type):
        """Check if source_type can be assigned to target_type."""
        if source_type == target_type:
            return True
        # Numeric promotions
        if source_type.is_numeric() and target_type.is_numeric():
            # Allow promotion to wider type (e.g., int -> float, int -> double, float -> double)
            return target_type in [Type.FLOAT, Type.DOUBLE] and source_type.can_promote_to(target_type)
        # No other implicit conversions (e.g., no int->string)
        return False

    def promote_numeric(self, t1, t2):
        """Return the common numeric type after promotion (wider wins)."""
        # Order: INT < FLOAT < DOUBLE
        if t1 == Type.DOUBLE or t2 == Type.DOUBLE:
            return Type.DOUBLE
        if t1 == Type.FLOAT or t2 == Type.FLOAT:
            return Type.FLOAT
        return Type.INT