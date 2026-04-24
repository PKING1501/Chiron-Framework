#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Abstract syntax tree for ChironLang
from chirontypes import Type

class AST(object):
    def __init__(self):
        self.type = Type.UNKNOWN


# --Instruction Classes-----------------------------------------------

class Instruction(AST):
    pass


class AssignmentCommand(Instruction):
    def __init__(self, leftvar, rexpr):
        self.lvar = leftvar
        self.rexpr = rexpr

    def __str__(self):
        return self.lvar.__str__() + " = " + self.rexpr.__str__()

class ArrayAllocation(Instruction):
    def __init__(self, arr_var, elem_type, sizes):
        self.avar = arr_var
        self.elem_type = elem_type
        self.sizes = sizes

    def __str__(self):
        dims = "".join(["[" + s.__str__() + "]" for s in self.sizes])
        et = self.elem_type.value if hasattr(self.elem_type, 'value') else str(self.elem_type)
        return self.avar.__str__() + " " + et + dims

class ArrayAssignmentCommand(Instruction):
    def __init__(self, arr_var, indices, rexpr):
        self.avar = arr_var
        self.indices = indices
        self.rexpr = rexpr

    def __str__(self):
        dims = "".join(["[" + i.__str__() + "]" for i in self.indices])
        return self.avar.__str__() + dims + " = " + self.rexpr.__str__()

class FieldAssignmentCommand(Instruction):
    def __init__(self, obj_expr, fields, rexpr):
        """
        :param obj_expr: The struct object expression (Var, ArrayAccess, or FieldAccess)
        :param fields: List of field names (strings) representing the access path
        :param rexpr: The expression to assign
        """
        self.obj_expr = obj_expr
        self.fields = fields
        self.rexpr = rexpr

    def __str__(self):
        fields_str = ".".join(self.fields)
        return f"{self.obj_expr}.{fields_str} = {self.rexpr}"

class StructDefinition(Instruction):
    def __init__(self, name, fields):
        """
        :param name: Struct name
        :param fields: List of (field_name, type) tuples
        """
        self.name = name
        self.fields = fields

    def __str__(self):
        fields_str = ", ".join([f"{n} {t.value if hasattr(t, 'value') else str(t)}" for n, t in self.fields])
        return f"struct {self.name} {{ {fields_str} }}"


class ConditionCommand(Instruction):
    def __init__(self, condition):
        self.cond = condition

    def __str__(self):
        return self.cond.__str__()

# Not Implemented Yet.
class AssertCommand(Instruction):
    def __init__(self, condition):
        self.cond = condition

    def __str__(self):
        return self.cond.__str__()

class MoveCommand(Instruction):
    def __init__(self, motion, expr):
        self.direction = motion
        self.expr = expr

    def __str__(self):
        return self.direction + " " + self.expr.__str__()


class PenCommand(Instruction):
    def __init__(self, penstat):
        self.status = penstat

    def __str__(self):
        return self.status

class GotoCommand(Instruction):
    def __init__(self, x, y):
        self.xcor = x
        self.ycor = y

    def __str__(self):
        return "goto " + str(self.xcor) + " " + str(self.ycor)

class NoOpCommand(Instruction):
    def __init__(self):
        pass

    def __str__(self):
        return "NOP"

class PauseCommand(Instruction):
    def __init__(self):
        pass

    def __str__(self):
        return "pause"

class Expression(AST):
    def __init__(self):
        super().__init__()
        self.type = Type.UNKNOWN

class Cast(Expression):
    def __init__(self, target_type, expr):
        super().__init__()
        self.target_type = target_type
        self.expr = expr

    def __str__(self):
        type_map = {
            Type.INT: "int",
            Type.FLOAT: "float",
            Type.DOUBLE: "float",
            Type.STRING: "str",
            Type.BOOLEAN: "bool"
        }
        func = type_map.get(self.target_type, "id")
        return f"{func}({self.expr.__str__()})"


# --Arithmetic Expressions--------------------------------------------

class ArithExpr(Expression):
    pass


class BinArithOp(ArithExpr):
    def __init__(self, expr1, expr2, opsymbol):
        self.lexpr = expr1
        self.rexpr = expr2
        self.symbol = opsymbol

    def __str__(self):
        return "(" + self.lexpr.__str__() + " " + self.symbol + " " + self.rexpr.__str__() + ")"


class UnaryArithOp(ArithExpr):
    def __init__(self, expr1, opsymbol):
        self.expr = expr1
        self.symbol = opsymbol

    def __str__(self):
        return self.symbol + self.expr.__str__()


class UMinus(UnaryArithOp):
    def __init__(self, lexpr):
        super().__init__(lexpr, "-")


class Sum(BinArithOp):
    def __init__(self, lexpr, rexpr):
        super().__init__(lexpr, rexpr, "+")


class Diff(BinArithOp):
    def __init__(self, lexpr, rexpr):
        super().__init__(lexpr, rexpr, "-")


class Mult(BinArithOp):
    def __init__(self, lexpr, rexpr):
        super().__init__(lexpr, rexpr, "*")

class Div(BinArithOp):
    def __init__(self, lexpr, rexpr):
        super().__init__(lexpr, rexpr, "/")


# --Boolean Expressions-----------------------------------------------

class BoolExpr(Expression):
    pass


class BinCondOp(BoolExpr):
    def __init__(self, expr1, expr2, opsymbol):
        self.lexpr = expr1
        self.rexpr = expr2
        self.symbol = opsymbol

    def __str__(self):
        return "(" + self.lexpr.__str__() + ' ' + self.symbol + ' ' + self.rexpr.__str__() + ")"


class AND(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "and")

class OR(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "or")


class LT(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "<")


class GT(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, ">")


class LTE(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "<=")


class GTE(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, ">=")


class EQ(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "==")


class NEQ(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "!=")


class NOT(BoolExpr):
    def __init__(self, uexpr):
        self.expr = uexpr
        self.symbol = "not"

    def __str__(self):
        return self.symbol + " " + self.expr.__str__()   # ← add a space


class PenStatus(BoolExpr):
    def __init__(self):
        pass

    def __str__(self):
        return "pendown?"


class BoolTrue(BoolExpr):
    def __init__(self):
        super().__init__()
        self.type = Type.BOOLEAN

    def __str__(self):
        return "True"


class BoolFalse(BoolExpr):
    def __init__(self):
        super().__init__()
        self.type = Type.BOOLEAN

    def __str__(self):
        return "False"


class Value(Expression):
    pass

class ArrayAccess(Value):
    def __init__(self, arr_var, indices):
        super().__init__()
        self.avar = arr_var
        self.indices = indices

    def __str__(self):
        dims = "".join(["[" + i.__str__() + "]" for i in self.indices])
        return self.avar.__str__() + dims

class FieldAccess(Value):
    def __init__(self, obj_expr, field_name):
        super().__init__()
        self.obj_expr = obj_expr
        self.field_name = field_name

    def __str__(self):
        return f"{self.obj_expr}.{self.field_name}"

class StructLiteral(Value):
    def __init__(self, values):
        """
        :param values: List of expressions in order of struct definition
        """
        super().__init__()
        self.values = values

    def __str__(self):
        return "{" + ", ".join([v.__str__() for v in self.values]) + "}"

class Num(Value):
    def __init__(self, v):
        super().__init__()
        self.val = int(v)
        self.type = Type.INT

    def __str__(self):
        return str(self.val)


class Var(Value):
    def __init__(self, vname, declared_type=None):
        super().__init__()
        self.varname = vname
        self.type = declared_type if declared_type else Type.UNKNOWN

    def __str__(self):
        return self.varname


class FloatLiteral(Value):
    def __init__(self, v):
        super().__init__()
        v_clean = v.rstrip('fF')
        self.val = float(v_clean)
        self.type = Type.FLOAT

    def __str__(self):
        return str(self.val)

class DoubleLiteral(Value):
    def __init__(self, v):
        super().__init__()
        v_clean = v.rstrip('dD')
        self.val = float(v_clean)
        self.type = Type.DOUBLE

    def __str__(self):
        return str(self.val)


class StringLiteral(Value):
    def __init__(self, v):
        super().__init__()
        self.val = v[1:-1]  # strip quotes
        self.type = Type.STRING
    
    def __str__(self):
        return '"' + self.val + '"'


class BoolLiteral(Value):
    def __init__(self, v):
        super().__init__()
        self.val = (v.lower() == "true")
        self.type = Type.BOOLEAN
    
    def __str__(self):
        return str(self.val)


