#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ChironLang Abstract Syntax Tree Builder

import os
import sys
sys.path.insert(0, os.path.join("..", "turtparse"))

from turtparse.tlangParser import tlangParser
from turtparse.tlangVisitor import tlangVisitor

from ChironAST import ChironAST
from chirontypes import Type


class astGenPass(tlangVisitor):

    def __init__(self):
        self.repeatInstrCount = 0 # keeps count for no of 'repeat' instructions

    # ----------------------------------------------------------------------
    # Instruction-level visitors
    # ----------------------------------------------------------------------

    def visitStart(self, ctx: tlangParser.StartContext):
        stmtList = self.visit(ctx.instruction_list())
        return stmtList

    def visitInstruction_list(self, ctx: tlangParser.Instruction_listContext):
        instrList = []
        for instr in ctx.instruction():
            instrList.extend(self.visit(instr))
        return instrList

    def visitStrict_ilist(self, ctx: tlangParser.Strict_ilistContext):
        instrList = []
        for instr in ctx.instruction():
            visvalue = self.visit(instr)
            instrList.extend(visvalue)
        return instrList

    def visitArrayDecl(self, ctx: tlangParser.ArrayDeclContext):
        var_name = ctx.VAR().getText()
        if not var_name.startswith(':'):
            var_name = ':' + var_name
            
        type_text = ctx.type_().getText()
        elem_type = self._get_type_from_text(type_text)
        
        arr_var = ChironAST.Var(var_name, Type.UNKNOWN)
        sizes = [ChironAST.Num(n.getText()) for n in ctx.NUM()]
        return [(ChironAST.ArrayAllocation(arr_var, elem_type, sizes), 1)]

    def _get_type_from_text(self, type_text):
        type_map = {
            'int': Type.INT,
            'float': Type.FLOAT,
            'double': Type.DOUBLE,
            'string': Type.STRING,
            'boolean': Type.BOOLEAN
        }
        return type_map.get(type_text, type_text) # returns string if it's a struct name

    def visitStructDecl(self, ctx: tlangParser.StructDeclContext):
        name = ctx.NAME(0).getText()
        fields = []
        # NAME type (',' NAME type)*
        for i in range(1, len(ctx.NAME())):
            field_name = ctx.NAME(i).getText()
            field_type_text = ctx.type_(i-1).getText()
            field_type = self._get_type_from_text(field_type_text)
            fields.append((field_name, field_type))
        return [(ChironAST.StructDefinition(name, fields), 1)]

    def visitFieldAssignment(self, ctx: tlangParser.FieldAssignmentContext):
        if ctx.VAR():
            var_name = ctx.VAR().getText()
            if not var_name.startswith(':'):
                var_name = ':' + var_name
            obj_expr = ChironAST.Var(var_name)
        else:
            obj_expr = self.visit(ctx.arrayAccess())

        fields = [n.getText() for n in ctx.NAME()]
        rexpr = self.visit(ctx.expr())
        return [(ChironAST.FieldAssignmentCommand(obj_expr, fields, rexpr), 1)]

    def visitArrayAccess(self, ctx: tlangParser.ArrayAccessContext):
        var_name = ctx.VAR().getText()
        if not var_name.startswith(':'):
            var_name = ':' + var_name
        arr_var = ChironAST.Var(var_name)
        indices = [self.visit(e) for e in ctx.expr()]
        return ChironAST.ArrayAccess(arr_var, indices)

    def visitArrayAssignment(self, ctx: tlangParser.ArrayAssignmentContext):
        var_name = ctx.VAR().getText()
        if not var_name.startswith(':'):
            var_name = ':' + var_name
            
        arr_var = ChironAST.Var(var_name, Type.UNKNOWN)
        all_exprs = [self.visit(e) for e in ctx.expr()]
        indices = all_exprs[:-1]
        value_expr = all_exprs[-1]
        return [(ChironAST.ArrayAssignmentCommand(arr_var, indices, value_expr), 1)]

    def visitAssignment(self, ctx: tlangParser.AssignmentContext):
        var_name = ctx.VAR().getText()
        if not var_name.startswith(':'):
            var_name = ':' + var_name
        
        declared_type = None

        # Check if a type annotation exists
        if ctx.typeAnnotation():
            type_text = ctx.typeAnnotation().getText()
            declared_type = self._get_type_from_text(type_text)

        lval = ChironAST.Var(var_name, declared_type)
        rval = self.visit(ctx.expr())          # changed from ctx.expression()
        print(f"RVAL: {rval} ({type(rval)})")   # debug
        return [(ChironAST.AssignmentCommand(lval, rval), 1)]

    def visitIfConditional(self, ctx: tlangParser.IfConditionalContext):
        condObj = ChironAST.ConditionCommand(self.visit(ctx.expr()))   # changed
        thenInstrList = self.visit(ctx.strict_ilist())
        return [(condObj, len(thenInstrList) + 1)] + thenInstrList

    def visitIfElseConditional(self, ctx: tlangParser.IfElseConditionalContext):
        condObj = ChironAST.ConditionCommand(self.visit(ctx.expr()))   # changed
        thenInstrList = self.visit(ctx.strict_ilist(0))
        elseInstrList = self.visit(ctx.strict_ilist(1))
        jumpOverElseBlock = [(ChironAST.ConditionCommand(ChironAST.BoolFalse()), len(elseInstrList) + 1)]
        return [(condObj, len(thenInstrList) + 2)] + thenInstrList + jumpOverElseBlock + elseInstrList

    def visitGotoCommand(self, ctx: tlangParser.GotoCommandContext):
        xcor = self.visit(ctx.expr(0))          # changed
        ycor = self.visit(ctx.expr(1))          # changed
        return [(ChironAST.GotoCommand(xcor, ycor), 1)]

    def visitLoop(self, ctx: tlangParser.LoopContext):
        self.repeatInstrCount += 1
        repeatNum = self.visit(ctx.value())
        counterVar = ChironAST.Var(":__rep_counter_" + str(self.repeatInstrCount))
        counterVarInitInstr = ChironAST.AssignmentCommand(counterVar, repeatNum)
        constZero = ChironAST.Num(0)
        constOne = ChironAST.Num(1)
        loopCond = ChironAST.ConditionCommand(ChironAST.GT(counterVar, constZero))
        counterVarDecrInstr = ChironAST.AssignmentCommand(counterVar, ChironAST.Diff(counterVar, constOne))

        thenInstrList = []
        for instr in ctx.strict_ilist().instruction():
            temp = self.visit(instr)
            thenInstrList.extend(temp)

        boolFalse = ChironAST.ConditionCommand(ChironAST.BoolFalse())
        return [(counterVarInitInstr, 1), (loopCond, len(thenInstrList) + 3)] + thenInstrList +\
            [(counterVarDecrInstr, 1), (boolFalse, -len(thenInstrList) - 2)]

    def visitMoveCommand(self, ctx: tlangParser.MoveCommandContext):
        mvcommand = ctx.moveOp().getText()
        mvexpr = self.visit(ctx.expr())          # changed
        return [(ChironAST.MoveCommand(mvcommand, mvexpr), 1)]

    def visitPenCommand(self, ctx: tlangParser.PenCommandContext):
        return [(ChironAST.PenCommand(ctx.getText()), 1)]

    def visitPauseCommand(self, ctx):
        return [(ChironAST.PauseCommand(), 1)]

    # ----------------------------------------------------------------------
    # Value visitors (unchanged – already handle labeled alternatives)
    # ----------------------------------------------------------------------

    def visitNumValue(self, ctx):
        node = ChironAST.Num(ctx.NUM().getText())
        node.type = Type.INT
        return node

    def visitFloatValue(self, ctx):
        node = ChironAST.FloatLiteral(ctx.FLOAT().getText())
        node.type = Type.FLOAT
        return node

    def visitDoubleValue(self, ctx):
        node = ChironAST.DoubleLiteral(ctx.DOUBLE().getText())
        node.type = Type.DOUBLE
        return node

    def visitStringValue(self, ctx):
        node = ChironAST.StringLiteral(ctx.STRING().getText())
        node.type = Type.STRING
        return node

    def visitBooleanValue(self, ctx):
        node = ChironAST.BoolLiteral(ctx.BOOLEAN().getText())
        node.type = Type.BOOLEAN
        return node

    def visitVarValue(self, ctx):
        raw = ctx.VAR().getText()
        # Normalize: ensure variable names always have colon for internal storage
        if not raw.startswith(':'):
            raw = ':' + raw
        node = ChironAST.Var(raw)
        node.type = Type.UNKNOWN
        return node

    # ----------------------------------------------------------------------
    # Unified expression visitors (new hierarchy)
    # ----------------------------------------------------------------------

    def visitOrExpr(self, ctx: tlangParser.OrExprContext):
        # orExpr : andExpr ( OR andExpr )* ;
        operands = ctx.andExpr()
        result = self.visit(operands[0])
        for i in range(1, len(operands)):
            # get the i-1th OR token
            op = ctx.OR(i-1)
            right = self.visit(operands[i])
            result = ChironAST.OR(result, right)
        return result

    def visitAndExpr(self, ctx: tlangParser.AndExprContext):
        operands = ctx.equalityExpr()
        result = self.visit(operands[0])
        for i in range(1, len(operands)):
            op = ctx.AND(i-1)
            right = self.visit(operands[i])
            result = ChironAST.AND(result, right)
        return result

    def visitEqualityExpr(self, ctx: tlangParser.EqualityExprContext):
        operands = ctx.relationalExpr()
        result = self.visit(operands[0])
        for i in range(1, len(operands)):
            # There are two possible operators: EQ or NEQ
            if ctx.EQ(i-1):
                right = self.visit(operands[i])
                result = ChironAST.EQ(result, right)
            else:  # ctx.NEQ(i-1)
                right = self.visit(operands[i])
                result = ChironAST.NEQ(result, right)
        return result

    def visitRelationalExpr(self, ctx: tlangParser.RelationalExprContext):
        operands = ctx.additiveExpr()
        result = self.visit(operands[0])
        for i in range(1, len(operands)):
            if ctx.LT(i-1):
                right = self.visit(operands[i])
                result = ChironAST.LT(result, right)
            elif ctx.GT(i-1):
                right = self.visit(operands[i])
                result = ChironAST.GT(result, right)
            elif ctx.LTE(i-1):
                right = self.visit(operands[i])
                result = ChironAST.LTE(result, right)
            else:  # ctx.GTE(i-1)
                right = self.visit(operands[i])
                result = ChironAST.GTE(result, right)
        return result

    def visitAdditiveExpr(self, ctx: tlangParser.AdditiveExprContext):
        operands = ctx.multiplicativeExpr()
        result = self.visit(operands[0])
        for i in range(1, len(operands)):
            if ctx.PLUS(i-1):
                right = self.visit(operands[i])
                result = ChironAST.Sum(result, right)
            else:  # ctx.MINUS(i-1)
                right = self.visit(operands[i])
                result = ChironAST.Diff(result, right)
        return result

    def visitMultiplicativeExpr(self, ctx: tlangParser.MultiplicativeExprContext):
        operands = ctx.unaryExpr()
        result = self.visit(operands[0])
        for i in range(1, len(operands)):
            if ctx.MUL(i-1):
                right = self.visit(operands[i])
                result = ChironAST.Mult(result, right)
            else:  # ctx.DIV(i-1)
                right = self.visit(operands[i])
                result = ChironAST.Div(result, right)
        return result

    def visitUnaryExpr(self, ctx: tlangParser.UnaryExprContext):
        # unaryExpr : (MINUS | NOT)? primary ;
        if ctx.MINUS():
            expr = self.visit(ctx.primary())
            return ChironAST.UMinus(expr)
        elif ctx.NOT():
            expr = self.visit(ctx.primary())
            return ChironAST.NOT(expr)
        else:
            return self.visit(ctx.primary())

    def visitPrimaryValue(self, ctx: tlangParser.PrimaryValueContext):
        return self.visit(ctx.value())

    def visitParenExpr(self, ctx: tlangParser.ParenExprContext):
        return self.visit(ctx.expr())

    def visitPenCondition(self, ctx: tlangParser.PenConditionContext):
        return ChironAST.PenStatus()

    def visitCastExpr(self, ctx: tlangParser.CastExprContext):
        type_text = ctx.type_().getText()
        type_map = {
            'int': Type.INT,
            'float': Type.FLOAT,
            'double': Type.DOUBLE,
            'string': Type.STRING,
            'boolean': Type.BOOLEAN
        }
        target_type = type_map.get(type_text, Type.TYPE_ERROR)
        expr = self.visit(ctx.primary())
        return ChironAST.Cast(target_type, expr)

    def visitArrayAccessExpr(self, ctx: tlangParser.ArrayAccessExprContext):
        var_name = ctx.VAR().getText()
        if not var_name.startswith(':'):
            var_name = ':' + var_name
            
        arr_var = ChironAST.Var(var_name, Type.UNKNOWN)
        indices = [self.visit(e) for e in ctx.expr()]
        return ChironAST.ArrayAccess(arr_var, indices)

    def visitFieldAccessExpr(self, ctx: tlangParser.FieldAccessExprContext):
        obj_expr = self.visit(ctx.primary())
        field_name = ctx.NAME().getText()
        return ChironAST.FieldAccess(obj_expr, field_name)

    def visitStructLiteralExpr(self, ctx: tlangParser.StructLiteralExprContext):
        values = [self.visit(e) for e in ctx.expr()]
        return ChironAST.StructLiteral(values)