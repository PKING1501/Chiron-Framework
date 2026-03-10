# Generated from tlang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .tlangParser import tlangParser
else:
    from tlangParser import tlangParser

# This class defines a complete generic visitor for a parse tree produced by tlangParser.

class tlangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by tlangParser#start.
    def visitStart(self, ctx:tlangParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#instruction_list.
    def visitInstruction_list(self, ctx:tlangParser.Instruction_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#strict_ilist.
    def visitStrict_ilist(self, ctx:tlangParser.Strict_ilistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#instruction.
    def visitInstruction(self, ctx:tlangParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#conditional.
    def visitConditional(self, ctx:tlangParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#ifConditional.
    def visitIfConditional(self, ctx:tlangParser.IfConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#ifElseConditional.
    def visitIfElseConditional(self, ctx:tlangParser.IfElseConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#loop.
    def visitLoop(self, ctx:tlangParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#gotoCommand.
    def visitGotoCommand(self, ctx:tlangParser.GotoCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#assignment.
    def visitAssignment(self, ctx:tlangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#typeAnnotation.
    def visitTypeAnnotation(self, ctx:tlangParser.TypeAnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#type.
    def visitType(self, ctx:tlangParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#moveCommand.
    def visitMoveCommand(self, ctx:tlangParser.MoveCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#moveOp.
    def visitMoveOp(self, ctx:tlangParser.MoveOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#penCommand.
    def visitPenCommand(self, ctx:tlangParser.PenCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#pauseCommand.
    def visitPauseCommand(self, ctx:tlangParser.PauseCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#expr.
    def visitExpr(self, ctx:tlangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#orExpr.
    def visitOrExpr(self, ctx:tlangParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#andExpr.
    def visitAndExpr(self, ctx:tlangParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#equalityExpr.
    def visitEqualityExpr(self, ctx:tlangParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#relationalExpr.
    def visitRelationalExpr(self, ctx:tlangParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:tlangParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#multiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:tlangParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#unaryExpr.
    def visitUnaryExpr(self, ctx:tlangParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#primaryValue.
    def visitPrimaryValue(self, ctx:tlangParser.PrimaryValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#parenExpr.
    def visitParenExpr(self, ctx:tlangParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#penCondition.
    def visitPenCondition(self, ctx:tlangParser.PenConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#numValue.
    def visitNumValue(self, ctx:tlangParser.NumValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#floatValue.
    def visitFloatValue(self, ctx:tlangParser.FloatValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#doubleValue.
    def visitDoubleValue(self, ctx:tlangParser.DoubleValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#stringValue.
    def visitStringValue(self, ctx:tlangParser.StringValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#booleanValue.
    def visitBooleanValue(self, ctx:tlangParser.BooleanValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#varValue.
    def visitVarValue(self, ctx:tlangParser.VarValueContext):
        return self.visitChildren(ctx)



del tlangParser