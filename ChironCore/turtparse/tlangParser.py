# Generated from tlang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,46,200,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,1,0,1,
        0,1,1,5,1,57,8,1,10,1,12,1,60,9,1,1,2,4,2,63,8,2,11,2,12,2,64,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,74,8,3,1,4,1,4,3,4,78,8,4,1,5,1,5,
        1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,
        1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,3,9,111,8,9,
        1,9,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,14,1,
        14,1,15,1,15,1,16,1,16,1,17,1,17,1,17,5,17,134,8,17,10,17,12,17,
        137,9,17,1,18,1,18,1,18,5,18,142,8,18,10,18,12,18,145,9,18,1,19,
        1,19,1,19,5,19,150,8,19,10,19,12,19,153,9,19,1,20,1,20,1,20,5,20,
        158,8,20,10,20,12,20,161,9,20,1,21,1,21,1,21,5,21,166,8,21,10,21,
        12,21,169,9,21,1,22,1,22,1,22,5,22,174,8,22,10,22,12,22,177,9,22,
        1,23,3,23,180,8,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,3,24,
        190,8,24,1,25,1,25,1,25,1,25,1,25,1,25,3,25,198,8,25,1,25,0,0,26,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        46,48,50,0,8,1,0,11,15,1,0,16,19,1,0,20,21,1,0,26,27,2,0,24,25,28,
        29,1,0,33,34,1,0,35,36,2,0,32,32,34,34,197,0,52,1,0,0,0,2,58,1,0,
        0,0,4,62,1,0,0,0,6,73,1,0,0,0,8,77,1,0,0,0,10,79,1,0,0,0,12,85,1,
        0,0,0,14,95,1,0,0,0,16,101,1,0,0,0,18,108,1,0,0,0,20,115,1,0,0,0,
        22,117,1,0,0,0,24,119,1,0,0,0,26,122,1,0,0,0,28,124,1,0,0,0,30,126,
        1,0,0,0,32,128,1,0,0,0,34,130,1,0,0,0,36,138,1,0,0,0,38,146,1,0,
        0,0,40,154,1,0,0,0,42,162,1,0,0,0,44,170,1,0,0,0,46,179,1,0,0,0,
        48,189,1,0,0,0,50,197,1,0,0,0,52,53,3,2,1,0,53,54,5,0,0,1,54,1,1,
        0,0,0,55,57,3,6,3,0,56,55,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,
        59,1,0,0,0,59,3,1,0,0,0,60,58,1,0,0,0,61,63,3,6,3,0,62,61,1,0,0,
        0,63,64,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,5,1,0,0,0,66,74,3,
        18,9,0,67,74,3,8,4,0,68,74,3,14,7,0,69,74,3,24,12,0,70,74,3,28,14,
        0,71,74,3,16,8,0,72,74,3,30,15,0,73,66,1,0,0,0,73,67,1,0,0,0,73,
        68,1,0,0,0,73,69,1,0,0,0,73,70,1,0,0,0,73,71,1,0,0,0,73,72,1,0,0,
        0,74,7,1,0,0,0,75,78,3,10,5,0,76,78,3,12,6,0,77,75,1,0,0,0,77,76,
        1,0,0,0,78,9,1,0,0,0,79,80,5,1,0,0,80,81,3,32,16,0,81,82,5,2,0,0,
        82,83,3,4,2,0,83,84,5,3,0,0,84,11,1,0,0,0,85,86,5,1,0,0,86,87,3,
        32,16,0,87,88,5,2,0,0,88,89,3,4,2,0,89,90,5,3,0,0,90,91,5,4,0,0,
        91,92,5,2,0,0,92,93,3,4,2,0,93,94,5,3,0,0,94,13,1,0,0,0,95,96,5,
        5,0,0,96,97,3,50,25,0,97,98,5,2,0,0,98,99,3,4,2,0,99,100,5,3,0,0,
        100,15,1,0,0,0,101,102,5,6,0,0,102,103,5,7,0,0,103,104,3,32,16,0,
        104,105,5,8,0,0,105,106,3,32,16,0,106,107,5,9,0,0,107,17,1,0,0,0,
        108,110,5,42,0,0,109,111,3,20,10,0,110,109,1,0,0,0,110,111,1,0,0,
        0,111,112,1,0,0,0,112,113,5,10,0,0,113,114,3,32,16,0,114,19,1,0,
        0,0,115,116,3,22,11,0,116,21,1,0,0,0,117,118,7,0,0,0,118,23,1,0,
        0,0,119,120,3,26,13,0,120,121,3,32,16,0,121,25,1,0,0,0,122,123,7,
        1,0,0,123,27,1,0,0,0,124,125,7,2,0,0,125,29,1,0,0,0,126,127,5,22,
        0,0,127,31,1,0,0,0,128,129,3,34,17,0,129,33,1,0,0,0,130,135,3,36,
        18,0,131,132,5,31,0,0,132,134,3,36,18,0,133,131,1,0,0,0,134,137,
        1,0,0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,35,1,0,0,0,137,135,1,
        0,0,0,138,143,3,38,19,0,139,140,5,30,0,0,140,142,3,38,19,0,141,139,
        1,0,0,0,142,145,1,0,0,0,143,141,1,0,0,0,143,144,1,0,0,0,144,37,1,
        0,0,0,145,143,1,0,0,0,146,151,3,40,20,0,147,148,7,3,0,0,148,150,
        3,40,20,0,149,147,1,0,0,0,150,153,1,0,0,0,151,149,1,0,0,0,151,152,
        1,0,0,0,152,39,1,0,0,0,153,151,1,0,0,0,154,159,3,42,21,0,155,156,
        7,4,0,0,156,158,3,42,21,0,157,155,1,0,0,0,158,161,1,0,0,0,159,157,
        1,0,0,0,159,160,1,0,0,0,160,41,1,0,0,0,161,159,1,0,0,0,162,167,3,
        44,22,0,163,164,7,5,0,0,164,166,3,44,22,0,165,163,1,0,0,0,166,169,
        1,0,0,0,167,165,1,0,0,0,167,168,1,0,0,0,168,43,1,0,0,0,169,167,1,
        0,0,0,170,175,3,46,23,0,171,172,7,6,0,0,172,174,3,46,23,0,173,171,
        1,0,0,0,174,177,1,0,0,0,175,173,1,0,0,0,175,176,1,0,0,0,176,45,1,
        0,0,0,177,175,1,0,0,0,178,180,7,7,0,0,179,178,1,0,0,0,179,180,1,
        0,0,0,180,181,1,0,0,0,181,182,3,48,24,0,182,47,1,0,0,0,183,190,3,
        50,25,0,184,185,5,7,0,0,185,186,3,32,16,0,186,187,5,9,0,0,187,190,
        1,0,0,0,188,190,5,23,0,0,189,183,1,0,0,0,189,184,1,0,0,0,189,188,
        1,0,0,0,190,49,1,0,0,0,191,198,5,37,0,0,192,198,5,38,0,0,193,198,
        5,39,0,0,194,198,5,40,0,0,195,198,5,41,0,0,196,198,5,42,0,0,197,
        191,1,0,0,0,197,192,1,0,0,0,197,193,1,0,0,0,197,194,1,0,0,0,197,
        195,1,0,0,0,197,196,1,0,0,0,198,51,1,0,0,0,14,58,64,73,77,110,135,
        143,151,159,167,175,179,189,197
    ]

class tlangParser ( Parser ):

    grammarFileName = "tlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'['", "']'", "'else'", "'repeat'", 
                     "'goto'", "'('", "','", "')'", "'='", "'int'", "'float'", 
                     "'double'", "'string'", "'boolean'", "'forward'", "'backward'", 
                     "'left'", "'right'", "'penup'", "'pendown'", "'pause'", 
                     "'pendown?'", "'<'", "'>'", "'=='", "'!='", "'<='", 
                     "'>='", "'&&'", "'||'", "'!'", "'+'", "'-'", "'*'", 
                     "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "PENCOND", 
                      "LT", "GT", "EQ", "NEQ", "LTE", "GTE", "AND", "OR", 
                      "NOT", "PLUS", "MINUS", "MUL", "DIV", "NUM", "FLOAT", 
                      "DOUBLE", "STRING", "BOOLEAN", "VAR", "NAME", "LINE_COMMENT", 
                      "BLOCK_COMMENT", "Whitespace" ]

    RULE_start = 0
    RULE_instruction_list = 1
    RULE_strict_ilist = 2
    RULE_instruction = 3
    RULE_conditional = 4
    RULE_ifConditional = 5
    RULE_ifElseConditional = 6
    RULE_loop = 7
    RULE_gotoCommand = 8
    RULE_assignment = 9
    RULE_typeAnnotation = 10
    RULE_type = 11
    RULE_moveCommand = 12
    RULE_moveOp = 13
    RULE_penCommand = 14
    RULE_pauseCommand = 15
    RULE_expr = 16
    RULE_orExpr = 17
    RULE_andExpr = 18
    RULE_equalityExpr = 19
    RULE_relationalExpr = 20
    RULE_additiveExpr = 21
    RULE_multiplicativeExpr = 22
    RULE_unaryExpr = 23
    RULE_primary = 24
    RULE_value = 25

    ruleNames =  [ "start", "instruction_list", "strict_ilist", "instruction", 
                   "conditional", "ifConditional", "ifElseConditional", 
                   "loop", "gotoCommand", "assignment", "typeAnnotation", 
                   "type", "moveCommand", "moveOp", "penCommand", "pauseCommand", 
                   "expr", "orExpr", "andExpr", "equalityExpr", "relationalExpr", 
                   "additiveExpr", "multiplicativeExpr", "unaryExpr", "primary", 
                   "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    PENCOND=23
    LT=24
    GT=25
    EQ=26
    NEQ=27
    LTE=28
    GTE=29
    AND=30
    OR=31
    NOT=32
    PLUS=33
    MINUS=34
    MUL=35
    DIV=36
    NUM=37
    FLOAT=38
    DOUBLE=39
    STRING=40
    BOOLEAN=41
    VAR=42
    NAME=43
    LINE_COMMENT=44
    BLOCK_COMMENT=45
    Whitespace=46

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruction_list(self):
            return self.getTypedRuleContext(tlangParser.Instruction_listContext,0)


        def EOF(self):
            return self.getToken(tlangParser.EOF, 0)

        def getRuleIndex(self):
            return tlangParser.RULE_start

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = tlangParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.instruction_list()
            self.state = 53
            self.match(tlangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instruction_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.InstructionContext)
            else:
                return self.getTypedRuleContext(tlangParser.InstructionContext,i)


        def getRuleIndex(self):
            return tlangParser.RULE_instruction_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction_list" ):
                return visitor.visitInstruction_list(self)
            else:
                return visitor.visitChildren(self)




    def instruction_list(self):

        localctx = tlangParser.Instruction_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruction_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4398054834274) != 0):
                self.state = 55
                self.instruction()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Strict_ilistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.InstructionContext)
            else:
                return self.getTypedRuleContext(tlangParser.InstructionContext,i)


        def getRuleIndex(self):
            return tlangParser.RULE_strict_ilist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStrict_ilist" ):
                return visitor.visitStrict_ilist(self)
            else:
                return visitor.visitChildren(self)




    def strict_ilist(self):

        localctx = tlangParser.Strict_ilistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_strict_ilist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 61
                self.instruction()
                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4398054834274) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(tlangParser.AssignmentContext,0)


        def conditional(self):
            return self.getTypedRuleContext(tlangParser.ConditionalContext,0)


        def loop(self):
            return self.getTypedRuleContext(tlangParser.LoopContext,0)


        def moveCommand(self):
            return self.getTypedRuleContext(tlangParser.MoveCommandContext,0)


        def penCommand(self):
            return self.getTypedRuleContext(tlangParser.PenCommandContext,0)


        def gotoCommand(self):
            return self.getTypedRuleContext(tlangParser.GotoCommandContext,0)


        def pauseCommand(self):
            return self.getTypedRuleContext(tlangParser.PauseCommandContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_instruction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction" ):
                return visitor.visitInstruction(self)
            else:
                return visitor.visitChildren(self)




    def instruction(self):

        localctx = tlangParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_instruction)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.assignment()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.conditional()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.loop()
                pass
            elif token in [16, 17, 18, 19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 69
                self.moveCommand()
                pass
            elif token in [20, 21]:
                self.enterOuterAlt(localctx, 5)
                self.state = 70
                self.penCommand()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 6)
                self.state = 71
                self.gotoCommand()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 7)
                self.state = 72
                self.pauseCommand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifConditional(self):
            return self.getTypedRuleContext(tlangParser.IfConditionalContext,0)


        def ifElseConditional(self):
            return self.getTypedRuleContext(tlangParser.IfElseConditionalContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_conditional

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = tlangParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_conditional)
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.ifConditional()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.ifElseConditional()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(tlangParser.ExprContext,0)


        def strict_ilist(self):
            return self.getTypedRuleContext(tlangParser.Strict_ilistContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_ifConditional

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfConditional" ):
                return visitor.visitIfConditional(self)
            else:
                return visitor.visitChildren(self)




    def ifConditional(self):

        localctx = tlangParser.IfConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifConditional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(tlangParser.T__0)
            self.state = 80
            self.expr()
            self.state = 81
            self.match(tlangParser.T__1)
            self.state = 82
            self.strict_ilist()
            self.state = 83
            self.match(tlangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfElseConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(tlangParser.ExprContext,0)


        def strict_ilist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.Strict_ilistContext)
            else:
                return self.getTypedRuleContext(tlangParser.Strict_ilistContext,i)


        def getRuleIndex(self):
            return tlangParser.RULE_ifElseConditional

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElseConditional" ):
                return visitor.visitIfElseConditional(self)
            else:
                return visitor.visitChildren(self)




    def ifElseConditional(self):

        localctx = tlangParser.IfElseConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifElseConditional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(tlangParser.T__0)
            self.state = 86
            self.expr()
            self.state = 87
            self.match(tlangParser.T__1)
            self.state = 88
            self.strict_ilist()
            self.state = 89
            self.match(tlangParser.T__2)
            self.state = 90
            self.match(tlangParser.T__3)
            self.state = 91
            self.match(tlangParser.T__1)
            self.state = 92
            self.strict_ilist()
            self.state = 93
            self.match(tlangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(tlangParser.ValueContext,0)


        def strict_ilist(self):
            return self.getTypedRuleContext(tlangParser.Strict_ilistContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = tlangParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(tlangParser.T__4)
            self.state = 96
            self.value()
            self.state = 97
            self.match(tlangParser.T__1)
            self.state = 98
            self.strict_ilist()
            self.state = 99
            self.match(tlangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GotoCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.ExprContext)
            else:
                return self.getTypedRuleContext(tlangParser.ExprContext,i)


        def getRuleIndex(self):
            return tlangParser.RULE_gotoCommand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGotoCommand" ):
                return visitor.visitGotoCommand(self)
            else:
                return visitor.visitChildren(self)




    def gotoCommand(self):

        localctx = tlangParser.GotoCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_gotoCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(tlangParser.T__5)
            self.state = 102
            self.match(tlangParser.T__6)
            self.state = 103
            self.expr()
            self.state = 104
            self.match(tlangParser.T__7)
            self.state = 105
            self.expr()
            self.state = 106
            self.match(tlangParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(tlangParser.VAR, 0)

        def expr(self):
            return self.getTypedRuleContext(tlangParser.ExprContext,0)


        def typeAnnotation(self):
            return self.getTypedRuleContext(tlangParser.TypeAnnotationContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = tlangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(tlangParser.VAR)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 63488) != 0):
                self.state = 109
                self.typeAnnotation()


            self.state = 112
            self.match(tlangParser.T__9)
            self.state = 113
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeAnnotationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(tlangParser.TypeContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_typeAnnotation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeAnnotation" ):
                return visitor.visitTypeAnnotation(self)
            else:
                return visitor.visitChildren(self)




    def typeAnnotation(self):

        localctx = tlangParser.TypeAnnotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_typeAnnotation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return tlangParser.RULE_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = tlangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 63488) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoveCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def moveOp(self):
            return self.getTypedRuleContext(tlangParser.MoveOpContext,0)


        def expr(self):
            return self.getTypedRuleContext(tlangParser.ExprContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_moveCommand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoveCommand" ):
                return visitor.visitMoveCommand(self)
            else:
                return visitor.visitChildren(self)




    def moveCommand(self):

        localctx = tlangParser.MoveCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_moveCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.moveOp()
            self.state = 120
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoveOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return tlangParser.RULE_moveOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoveOp" ):
                return visitor.visitMoveOp(self)
            else:
                return visitor.visitChildren(self)




    def moveOp(self):

        localctx = tlangParser.MoveOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_moveOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 983040) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PenCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return tlangParser.RULE_penCommand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPenCommand" ):
                return visitor.visitPenCommand(self)
            else:
                return visitor.visitChildren(self)




    def penCommand(self):

        localctx = tlangParser.PenCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_penCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            _la = self._input.LA(1)
            if not(_la==20 or _la==21):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PauseCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return tlangParser.RULE_pauseCommand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPauseCommand" ):
                return visitor.visitPauseCommand(self)
            else:
                return visitor.visitChildren(self)




    def pauseCommand(self):

        localctx = tlangParser.PauseCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_pauseCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(tlangParser.T__21)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def orExpr(self):
            return self.getTypedRuleContext(tlangParser.OrExprContext,0)


        def getRuleIndex(self):
            return tlangParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = tlangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.orExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.AndExprContext)
            else:
                return self.getTypedRuleContext(tlangParser.AndExprContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(tlangParser.OR)
            else:
                return self.getToken(tlangParser.OR, i)

        def getRuleIndex(self):
            return tlangParser.RULE_orExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)




    def orExpr(self):

        localctx = tlangParser.OrExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_orExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.andExpr()
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 131
                self.match(tlangParser.OR)
                self.state = 132
                self.andExpr()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.EqualityExprContext)
            else:
                return self.getTypedRuleContext(tlangParser.EqualityExprContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(tlangParser.AND)
            else:
                return self.getToken(tlangParser.AND, i)

        def getRuleIndex(self):
            return tlangParser.RULE_andExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)




    def andExpr(self):

        localctx = tlangParser.AndExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_andExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.equalityExpr()
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 139
                self.match(tlangParser.AND)
                self.state = 140
                self.equalityExpr()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.RelationalExprContext)
            else:
                return self.getTypedRuleContext(tlangParser.RelationalExprContext,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(tlangParser.EQ)
            else:
                return self.getToken(tlangParser.EQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(tlangParser.NEQ)
            else:
                return self.getToken(tlangParser.NEQ, i)

        def getRuleIndex(self):
            return tlangParser.RULE_equalityExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpr" ):
                return visitor.visitEqualityExpr(self)
            else:
                return visitor.visitChildren(self)




    def equalityExpr(self):

        localctx = tlangParser.EqualityExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_equalityExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.relationalExpr()
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26 or _la==27:
                self.state = 147
                _la = self._input.LA(1)
                if not(_la==26 or _la==27):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 148
                self.relationalExpr()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.AdditiveExprContext)
            else:
                return self.getTypedRuleContext(tlangParser.AdditiveExprContext,i)


        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(tlangParser.LT)
            else:
                return self.getToken(tlangParser.LT, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(tlangParser.GT)
            else:
                return self.getToken(tlangParser.GT, i)

        def LTE(self, i:int=None):
            if i is None:
                return self.getTokens(tlangParser.LTE)
            else:
                return self.getToken(tlangParser.LTE, i)

        def GTE(self, i:int=None):
            if i is None:
                return self.getTokens(tlangParser.GTE)
            else:
                return self.getToken(tlangParser.GTE, i)

        def getRuleIndex(self):
            return tlangParser.RULE_relationalExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpr" ):
                return visitor.visitRelationalExpr(self)
            else:
                return visitor.visitChildren(self)




    def relationalExpr(self):

        localctx = tlangParser.RelationalExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_relationalExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.additiveExpr()
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 855638016) != 0):
                self.state = 155
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 855638016) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 156
                self.additiveExpr()
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.MultiplicativeExprContext)
            else:
                return self.getTypedRuleContext(tlangParser.MultiplicativeExprContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(tlangParser.PLUS)
            else:
                return self.getToken(tlangParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(tlangParser.MINUS)
            else:
                return self.getToken(tlangParser.MINUS, i)

        def getRuleIndex(self):
            return tlangParser.RULE_additiveExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpr" ):
                return visitor.visitAdditiveExpr(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpr(self):

        localctx = tlangParser.AdditiveExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_additiveExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.multiplicativeExpr()
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33 or _la==34:
                self.state = 163
                _la = self._input.LA(1)
                if not(_la==33 or _la==34):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 164
                self.multiplicativeExpr()
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.UnaryExprContext)
            else:
                return self.getTypedRuleContext(tlangParser.UnaryExprContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(tlangParser.MUL)
            else:
                return self.getToken(tlangParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(tlangParser.DIV)
            else:
                return self.getToken(tlangParser.DIV, i)

        def getRuleIndex(self):
            return tlangParser.RULE_multiplicativeExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpr" ):
                return visitor.visitMultiplicativeExpr(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpr(self):

        localctx = tlangParser.MultiplicativeExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_multiplicativeExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.unaryExpr()
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35 or _la==36:
                self.state = 171
                _la = self._input.LA(1)
                if not(_la==35 or _la==36):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 172
                self.unaryExpr()
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(tlangParser.PrimaryContext,0)


        def MINUS(self):
            return self.getToken(tlangParser.MINUS, 0)

        def NOT(self):
            return self.getToken(tlangParser.NOT, 0)

        def getRuleIndex(self):
            return tlangParser.RULE_unaryExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpr(self):

        localctx = tlangParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_unaryExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32 or _la==34:
                self.state = 178
                _la = self._input.LA(1)
                if not(_la==32 or _la==34):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 181
            self.primary()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return tlangParser.RULE_primary

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrimaryValueContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self):
            return self.getTypedRuleContext(tlangParser.ValueContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryValue" ):
                return visitor.visitPrimaryValue(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(tlangParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class PenConditionContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PENCOND(self):
            return self.getToken(tlangParser.PENCOND, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPenCondition" ):
                return visitor.visitPenCondition(self)
            else:
                return visitor.visitChildren(self)



    def primary(self):

        localctx = tlangParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_primary)
        try:
            self.state = 189
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37, 38, 39, 40, 41, 42]:
                localctx = tlangParser.PrimaryValueContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.value()
                pass
            elif token in [7]:
                localctx = tlangParser.ParenExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.match(tlangParser.T__6)
                self.state = 185
                self.expr()
                self.state = 186
                self.match(tlangParser.T__8)
                pass
            elif token in [23]:
                localctx = tlangParser.PenConditionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 188
                self.match(tlangParser.PENCOND)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return tlangParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StringValueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(tlangParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringValue" ):
                return visitor.visitStringValue(self)
            else:
                return visitor.visitChildren(self)


    class VarValueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(tlangParser.VAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarValue" ):
                return visitor.visitVarValue(self)
            else:
                return visitor.visitChildren(self)


    class FloatValueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(tlangParser.FLOAT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatValue" ):
                return visitor.visitFloatValue(self)
            else:
                return visitor.visitChildren(self)


    class BooleanValueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(tlangParser.BOOLEAN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanValue" ):
                return visitor.visitBooleanValue(self)
            else:
                return visitor.visitChildren(self)


    class DoubleValueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DOUBLE(self):
            return self.getToken(tlangParser.DOUBLE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoubleValue" ):
                return visitor.visitDoubleValue(self)
            else:
                return visitor.visitChildren(self)


    class NumValueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(tlangParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumValue" ):
                return visitor.visitNumValue(self)
            else:
                return visitor.visitChildren(self)



    def value(self):

        localctx = tlangParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_value)
        try:
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                localctx = tlangParser.NumValueContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.match(tlangParser.NUM)
                pass
            elif token in [38]:
                localctx = tlangParser.FloatValueContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.match(tlangParser.FLOAT)
                pass
            elif token in [39]:
                localctx = tlangParser.DoubleValueContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 193
                self.match(tlangParser.DOUBLE)
                pass
            elif token in [40]:
                localctx = tlangParser.StringValueContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 194
                self.match(tlangParser.STRING)
                pass
            elif token in [41]:
                localctx = tlangParser.BooleanValueContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 195
                self.match(tlangParser.BOOLEAN)
                pass
            elif token in [42]:
                localctx = tlangParser.VarValueContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 196
                self.match(tlangParser.VAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





