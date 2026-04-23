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
        4,1,50,308,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,1,0,1,0,1,1,5,1,67,8,
        1,10,1,12,1,70,9,1,1,2,4,2,73,8,2,11,2,12,2,74,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,88,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,5,4,98,8,4,10,4,12,4,101,9,4,3,4,103,8,4,1,4,1,4,1,5,1,5,3,5,
        109,8,5,1,5,1,5,4,5,113,8,5,11,5,12,5,114,1,5,1,5,1,5,1,6,1,6,1,
        6,1,6,1,6,4,6,125,8,6,11,6,12,6,126,1,7,1,7,1,7,1,7,1,7,4,7,134,
        8,7,11,7,12,7,135,1,8,1,8,1,8,1,8,1,8,4,8,143,8,8,11,8,12,8,144,
        1,8,1,8,1,8,1,9,1,9,3,9,152,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,
        12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,3,14,185,
        8,14,1,14,1,14,1,14,1,15,1,15,1,16,1,16,1,17,1,17,1,17,1,18,1,18,
        1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,22,5,22,208,8,22,10,22,
        12,22,211,9,22,1,23,1,23,1,23,5,23,216,8,23,10,23,12,23,219,9,23,
        1,24,1,24,1,24,5,24,224,8,24,10,24,12,24,227,9,24,1,25,1,25,1,25,
        5,25,232,8,25,10,25,12,25,235,9,25,1,26,1,26,1,26,5,26,240,8,26,
        10,26,12,26,243,9,26,1,27,1,27,1,27,5,27,248,8,27,10,27,12,27,251,
        9,27,1,28,3,28,254,8,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,4,29,275,
        8,29,11,29,12,29,276,1,29,1,29,1,29,1,29,5,29,283,8,29,10,29,12,
        29,286,9,29,1,29,1,29,3,29,290,8,29,1,29,1,29,1,29,5,29,295,8,29,
        10,29,12,29,298,9,29,1,30,1,30,1,30,1,30,1,30,1,30,3,30,306,8,30,
        1,30,0,1,58,31,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,60,0,8,2,0,15,19,47,47,1,0,20,
        23,1,0,24,25,1,0,30,31,2,0,28,29,32,33,1,0,37,38,1,0,39,40,2,0,36,
        36,38,38,317,0,62,1,0,0,0,2,68,1,0,0,0,4,72,1,0,0,0,6,87,1,0,0,0,
        8,89,1,0,0,0,10,108,1,0,0,0,12,119,1,0,0,0,14,128,1,0,0,0,16,137,
        1,0,0,0,18,151,1,0,0,0,20,153,1,0,0,0,22,159,1,0,0,0,24,169,1,0,
        0,0,26,175,1,0,0,0,28,182,1,0,0,0,30,189,1,0,0,0,32,191,1,0,0,0,
        34,193,1,0,0,0,36,196,1,0,0,0,38,198,1,0,0,0,40,200,1,0,0,0,42,202,
        1,0,0,0,44,204,1,0,0,0,46,212,1,0,0,0,48,220,1,0,0,0,50,228,1,0,
        0,0,52,236,1,0,0,0,54,244,1,0,0,0,56,253,1,0,0,0,58,289,1,0,0,0,
        60,305,1,0,0,0,62,63,3,2,1,0,63,64,5,0,0,1,64,1,1,0,0,0,65,67,3,
        6,3,0,66,65,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,
        3,1,0,0,0,70,68,1,0,0,0,71,73,3,6,3,0,72,71,1,0,0,0,73,74,1,0,0,
        0,74,72,1,0,0,0,74,75,1,0,0,0,75,5,1,0,0,0,76,88,3,28,14,0,77,88,
        3,14,7,0,78,88,3,16,8,0,79,88,3,8,4,0,80,88,3,10,5,0,81,88,3,18,
        9,0,82,88,3,24,12,0,83,88,3,34,17,0,84,88,3,38,19,0,85,88,3,26,13,
        0,86,88,3,40,20,0,87,76,1,0,0,0,87,77,1,0,0,0,87,78,1,0,0,0,87,79,
        1,0,0,0,87,80,1,0,0,0,87,81,1,0,0,0,87,82,1,0,0,0,87,83,1,0,0,0,
        87,84,1,0,0,0,87,85,1,0,0,0,87,86,1,0,0,0,88,7,1,0,0,0,89,90,5,1,
        0,0,90,91,5,47,0,0,91,102,5,2,0,0,92,93,5,47,0,0,93,99,3,32,16,0,
        94,95,5,3,0,0,95,96,5,47,0,0,96,98,3,32,16,0,97,94,1,0,0,0,98,101,
        1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,103,1,0,0,0,101,99,1,0,
        0,0,102,92,1,0,0,0,102,103,1,0,0,0,103,104,1,0,0,0,104,105,5,4,0,
        0,105,9,1,0,0,0,106,109,5,46,0,0,107,109,3,12,6,0,108,106,1,0,0,
        0,108,107,1,0,0,0,109,112,1,0,0,0,110,111,5,5,0,0,111,113,5,47,0,
        0,112,110,1,0,0,0,113,114,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,
        0,115,116,1,0,0,0,116,117,5,6,0,0,117,118,3,42,21,0,118,11,1,0,0,
        0,119,124,5,46,0,0,120,121,5,7,0,0,121,122,3,42,21,0,122,123,5,8,
        0,0,123,125,1,0,0,0,124,120,1,0,0,0,125,126,1,0,0,0,126,124,1,0,
        0,0,126,127,1,0,0,0,127,13,1,0,0,0,128,129,5,46,0,0,129,133,3,32,
        16,0,130,131,5,7,0,0,131,132,5,41,0,0,132,134,5,8,0,0,133,130,1,
        0,0,0,134,135,1,0,0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,15,1,0,
        0,0,137,142,5,46,0,0,138,139,5,7,0,0,139,140,3,42,21,0,140,141,5,
        8,0,0,141,143,1,0,0,0,142,138,1,0,0,0,143,144,1,0,0,0,144,142,1,
        0,0,0,144,145,1,0,0,0,145,146,1,0,0,0,146,147,5,6,0,0,147,148,3,
        42,21,0,148,17,1,0,0,0,149,152,3,20,10,0,150,152,3,22,11,0,151,149,
        1,0,0,0,151,150,1,0,0,0,152,19,1,0,0,0,153,154,5,9,0,0,154,155,3,
        42,21,0,155,156,5,7,0,0,156,157,3,4,2,0,157,158,5,8,0,0,158,21,1,
        0,0,0,159,160,5,9,0,0,160,161,3,42,21,0,161,162,5,7,0,0,162,163,
        3,4,2,0,163,164,5,8,0,0,164,165,5,10,0,0,165,166,5,7,0,0,166,167,
        3,4,2,0,167,168,5,8,0,0,168,23,1,0,0,0,169,170,5,11,0,0,170,171,
        3,60,30,0,171,172,5,7,0,0,172,173,3,4,2,0,173,174,5,8,0,0,174,25,
        1,0,0,0,175,176,5,12,0,0,176,177,5,13,0,0,177,178,3,42,21,0,178,
        179,5,3,0,0,179,180,3,42,21,0,180,181,5,14,0,0,181,27,1,0,0,0,182,
        184,5,46,0,0,183,185,3,30,15,0,184,183,1,0,0,0,184,185,1,0,0,0,185,
        186,1,0,0,0,186,187,5,6,0,0,187,188,3,42,21,0,188,29,1,0,0,0,189,
        190,3,32,16,0,190,31,1,0,0,0,191,192,7,0,0,0,192,33,1,0,0,0,193,
        194,3,36,18,0,194,195,3,42,21,0,195,35,1,0,0,0,196,197,7,1,0,0,197,
        37,1,0,0,0,198,199,7,2,0,0,199,39,1,0,0,0,200,201,5,26,0,0,201,41,
        1,0,0,0,202,203,3,44,22,0,203,43,1,0,0,0,204,209,3,46,23,0,205,206,
        5,35,0,0,206,208,3,46,23,0,207,205,1,0,0,0,208,211,1,0,0,0,209,207,
        1,0,0,0,209,210,1,0,0,0,210,45,1,0,0,0,211,209,1,0,0,0,212,217,3,
        48,24,0,213,214,5,34,0,0,214,216,3,48,24,0,215,213,1,0,0,0,216,219,
        1,0,0,0,217,215,1,0,0,0,217,218,1,0,0,0,218,47,1,0,0,0,219,217,1,
        0,0,0,220,225,3,50,25,0,221,222,7,3,0,0,222,224,3,50,25,0,223,221,
        1,0,0,0,224,227,1,0,0,0,225,223,1,0,0,0,225,226,1,0,0,0,226,49,1,
        0,0,0,227,225,1,0,0,0,228,233,3,52,26,0,229,230,7,4,0,0,230,232,
        3,52,26,0,231,229,1,0,0,0,232,235,1,0,0,0,233,231,1,0,0,0,233,234,
        1,0,0,0,234,51,1,0,0,0,235,233,1,0,0,0,236,241,3,54,27,0,237,238,
        7,5,0,0,238,240,3,54,27,0,239,237,1,0,0,0,240,243,1,0,0,0,241,239,
        1,0,0,0,241,242,1,0,0,0,242,53,1,0,0,0,243,241,1,0,0,0,244,249,3,
        56,28,0,245,246,7,6,0,0,246,248,3,56,28,0,247,245,1,0,0,0,248,251,
        1,0,0,0,249,247,1,0,0,0,249,250,1,0,0,0,250,55,1,0,0,0,251,249,1,
        0,0,0,252,254,7,7,0,0,253,252,1,0,0,0,253,254,1,0,0,0,254,255,1,
        0,0,0,255,256,3,58,29,0,256,57,1,0,0,0,257,258,6,29,-1,0,258,290,
        3,60,30,0,259,260,5,13,0,0,260,261,3,42,21,0,261,262,5,14,0,0,262,
        290,1,0,0,0,263,264,5,13,0,0,264,265,3,32,16,0,265,266,5,14,0,0,
        266,267,3,58,29,5,267,290,1,0,0,0,268,290,5,27,0,0,269,274,5,46,
        0,0,270,271,5,7,0,0,271,272,3,42,21,0,272,273,5,8,0,0,273,275,1,
        0,0,0,274,270,1,0,0,0,275,276,1,0,0,0,276,274,1,0,0,0,276,277,1,
        0,0,0,277,290,1,0,0,0,278,279,5,2,0,0,279,284,3,42,21,0,280,281,
        5,3,0,0,281,283,3,42,21,0,282,280,1,0,0,0,283,286,1,0,0,0,284,282,
        1,0,0,0,284,285,1,0,0,0,285,287,1,0,0,0,286,284,1,0,0,0,287,288,
        5,4,0,0,288,290,1,0,0,0,289,257,1,0,0,0,289,259,1,0,0,0,289,263,
        1,0,0,0,289,268,1,0,0,0,289,269,1,0,0,0,289,278,1,0,0,0,290,296,
        1,0,0,0,291,292,10,2,0,0,292,293,5,5,0,0,293,295,5,47,0,0,294,291,
        1,0,0,0,295,298,1,0,0,0,296,294,1,0,0,0,296,297,1,0,0,0,297,59,1,
        0,0,0,298,296,1,0,0,0,299,306,5,41,0,0,300,306,5,42,0,0,301,306,
        5,43,0,0,302,306,5,44,0,0,303,306,5,45,0,0,304,306,5,46,0,0,305,
        299,1,0,0,0,305,300,1,0,0,0,305,301,1,0,0,0,305,302,1,0,0,0,305,
        303,1,0,0,0,305,304,1,0,0,0,306,61,1,0,0,0,24,68,74,87,99,102,108,
        114,126,135,144,151,184,209,217,225,233,241,249,253,276,284,289,
        296,305
    ]

class tlangParser ( Parser ):

    grammarFileName = "tlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'struct'", "'{'", "','", "'}'", "'.'", 
                     "'='", "'['", "']'", "'if'", "'else'", "'repeat'", 
                     "'goto'", "'('", "')'", "'int'", "'float'", "'double'", 
                     "'string'", "'boolean'", "'forward'", "'backward'", 
                     "'left'", "'right'", "'penup'", "'pendown'", "'pause'", 
                     "'pendown?'", "'<'", "'>'", "'=='", "'!='", "'<='", 
                     "'>='", "'&&'", "'||'", "'!'", "'+'", "'-'", "'*'", 
                     "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
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
    RULE_structDecl = 4
    RULE_fieldAssignment = 5
    RULE_arrayAccess = 6
    RULE_arrayDecl = 7
    RULE_arrayAssignment = 8
    RULE_conditional = 9
    RULE_ifConditional = 10
    RULE_ifElseConditional = 11
    RULE_loop = 12
    RULE_gotoCommand = 13
    RULE_assignment = 14
    RULE_typeAnnotation = 15
    RULE_type = 16
    RULE_moveCommand = 17
    RULE_moveOp = 18
    RULE_penCommand = 19
    RULE_pauseCommand = 20
    RULE_expr = 21
    RULE_orExpr = 22
    RULE_andExpr = 23
    RULE_equalityExpr = 24
    RULE_relationalExpr = 25
    RULE_additiveExpr = 26
    RULE_multiplicativeExpr = 27
    RULE_unaryExpr = 28
    RULE_primary = 29
    RULE_value = 30

    ruleNames =  [ "start", "instruction_list", "strict_ilist", "instruction", 
                   "structDecl", "fieldAssignment", "arrayAccess", "arrayDecl", 
                   "arrayAssignment", "conditional", "ifConditional", "ifElseConditional", 
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
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    PENCOND=27
    LT=28
    GT=29
    EQ=30
    NEQ=31
    LTE=32
    GTE=33
    AND=34
    OR=35
    NOT=36
    PLUS=37
    MINUS=38
    MUL=39
    DIV=40
    NUM=41
    FLOAT=42
    DOUBLE=43
    STRING=44
    BOOLEAN=45
    VAR=46
    NAME=47
    LINE_COMMENT=48
    BLOCK_COMMENT=49
    Whitespace=50

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

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
            self.state = 62
            self.instruction_list()
            self.state = 63
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction_list" ):
                listener.enterInstruction_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction_list" ):
                listener.exitInstruction_list(self)

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
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 70368877353474) != 0):
                self.state = 65
                self.instruction()
                self.state = 70
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStrict_ilist" ):
                listener.enterStrict_ilist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStrict_ilist" ):
                listener.exitStrict_ilist(self)

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
            self.state = 72 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 71
                self.instruction()
                self.state = 74 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 70368877353474) != 0)):
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


        def arrayDecl(self):
            return self.getTypedRuleContext(tlangParser.ArrayDeclContext,0)


        def arrayAssignment(self):
            return self.getTypedRuleContext(tlangParser.ArrayAssignmentContext,0)


        def structDecl(self):
            return self.getTypedRuleContext(tlangParser.StructDeclContext,0)


        def fieldAssignment(self):
            return self.getTypedRuleContext(tlangParser.FieldAssignmentContext,0)


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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction" ):
                return visitor.visitInstruction(self)
            else:
                return visitor.visitChildren(self)




    def instruction(self):

        localctx = tlangParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_instruction)
        try:
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.arrayDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 78
                self.arrayAssignment()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 79
                self.structDecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 80
                self.fieldAssignment()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 81
                self.conditional()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 82
                self.loop()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 83
                self.moveCommand()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 84
                self.penCommand()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 85
                self.gotoCommand()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 86
                self.pauseCommand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(tlangParser.NAME)
            else:
                return self.getToken(tlangParser.NAME, i)

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.TypeContext)
            else:
                return self.getTypedRuleContext(tlangParser.TypeContext,i)


        def getRuleIndex(self):
            return tlangParser.RULE_structDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructDecl" ):
                listener.enterStructDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructDecl" ):
                listener.exitStructDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructDecl" ):
                return visitor.visitStructDecl(self)
            else:
                return visitor.visitChildren(self)




    def structDecl(self):

        localctx = tlangParser.StructDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_structDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(tlangParser.T__0)
            self.state = 90
            self.match(tlangParser.NAME)
            self.state = 91
            self.match(tlangParser.T__1)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 92
                self.match(tlangParser.NAME)
                self.state = 93
                self.type_()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 94
                    self.match(tlangParser.T__2)
                    self.state = 95
                    self.match(tlangParser.NAME)
                    self.state = 96
                    self.type_()
                    self.state = 101
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 104
            self.match(tlangParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(tlangParser.ExprContext,0)


        def VAR(self):
            return self.getToken(tlangParser.VAR, 0)

        def arrayAccess(self):
            return self.getTypedRuleContext(tlangParser.ArrayAccessContext,0)


        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(tlangParser.NAME)
            else:
                return self.getToken(tlangParser.NAME, i)

        def getRuleIndex(self):
            return tlangParser.RULE_fieldAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldAssignment" ):
                listener.enterFieldAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldAssignment" ):
                listener.exitFieldAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldAssignment" ):
                return visitor.visitFieldAssignment(self)
            else:
                return visitor.visitChildren(self)




    def fieldAssignment(self):

        localctx = tlangParser.FieldAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_fieldAssignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 106
                self.match(tlangParser.VAR)
                pass

            elif la_ == 2:
                self.state = 107
                self.arrayAccess()
                pass


            self.state = 112 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 110
                self.match(tlangParser.T__4)
                self.state = 111
                self.match(tlangParser.NAME)
                self.state = 114 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5):
                    break

            self.state = 116
            self.match(tlangParser.T__5)
            self.state = 117
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(tlangParser.VAR, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.ExprContext)
            else:
                return self.getTypedRuleContext(tlangParser.ExprContext,i)


        def getRuleIndex(self):
            return tlangParser.RULE_arrayAccess

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayAccess" ):
                listener.enterArrayAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayAccess" ):
                listener.exitArrayAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAccess" ):
                return visitor.visitArrayAccess(self)
            else:
                return visitor.visitChildren(self)




    def arrayAccess(self):

        localctx = tlangParser.ArrayAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_arrayAccess)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(tlangParser.VAR)
            self.state = 124 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 120
                self.match(tlangParser.T__6)
                self.state = 121
                self.expr()
                self.state = 122
                self.match(tlangParser.T__7)
                self.state = 126 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==7):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(tlangParser.VAR, 0)

        def type_(self):
            return self.getTypedRuleContext(tlangParser.TypeContext,0)


        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(tlangParser.NUM)
            else:
                return self.getToken(tlangParser.NUM, i)

        def getRuleIndex(self):
            return tlangParser.RULE_arrayDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayDecl" ):
                listener.enterArrayDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayDecl" ):
                listener.exitArrayDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayDecl" ):
                return visitor.visitArrayDecl(self)
            else:
                return visitor.visitChildren(self)




    def arrayDecl(self):

        localctx = tlangParser.ArrayDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arrayDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(tlangParser.VAR)
            self.state = 129
            self.type_()
            self.state = 133 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 130
                self.match(tlangParser.T__6)
                self.state = 131
                self.match(tlangParser.NUM)
                self.state = 132
                self.match(tlangParser.T__7)
                self.state = 135 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==7):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayAssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(tlangParser.VAR, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.ExprContext)
            else:
                return self.getTypedRuleContext(tlangParser.ExprContext,i)


        def getRuleIndex(self):
            return tlangParser.RULE_arrayAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayAssignment" ):
                listener.enterArrayAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayAssignment" ):
                listener.exitArrayAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAssignment" ):
                return visitor.visitArrayAssignment(self)
            else:
                return visitor.visitChildren(self)




    def arrayAssignment(self):

        localctx = tlangParser.ArrayAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arrayAssignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(tlangParser.VAR)
            self.state = 142 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 138
                self.match(tlangParser.T__6)
                self.state = 139
                self.expr()
                self.state = 140
                self.match(tlangParser.T__7)
                self.state = 144 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==7):
                    break

            self.state = 146
            self.match(tlangParser.T__5)
            self.state = 147
            self.expr()
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = tlangParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_conditional)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.ifConditional()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfConditional" ):
                listener.enterIfConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfConditional" ):
                listener.exitIfConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfConditional" ):
                return visitor.visitIfConditional(self)
            else:
                return visitor.visitChildren(self)




    def ifConditional(self):

        localctx = tlangParser.IfConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ifConditional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(tlangParser.T__8)
            self.state = 154
            self.expr()
            self.state = 155
            self.match(tlangParser.T__6)
            self.state = 156
            self.strict_ilist()
            self.state = 157
            self.match(tlangParser.T__7)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfElseConditional" ):
                listener.enterIfElseConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfElseConditional" ):
                listener.exitIfElseConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElseConditional" ):
                return visitor.visitIfElseConditional(self)
            else:
                return visitor.visitChildren(self)




    def ifElseConditional(self):

        localctx = tlangParser.IfElseConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ifElseConditional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(tlangParser.T__8)
            self.state = 160
            self.expr()
            self.state = 161
            self.match(tlangParser.T__6)
            self.state = 162
            self.strict_ilist()
            self.state = 163
            self.match(tlangParser.T__7)
            self.state = 164
            self.match(tlangParser.T__9)
            self.state = 165
            self.match(tlangParser.T__6)
            self.state = 166
            self.strict_ilist()
            self.state = 167
            self.match(tlangParser.T__7)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = tlangParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(tlangParser.T__10)
            self.state = 170
            self.value()
            self.state = 171
            self.match(tlangParser.T__6)
            self.state = 172
            self.strict_ilist()
            self.state = 173
            self.match(tlangParser.T__7)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGotoCommand" ):
                listener.enterGotoCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGotoCommand" ):
                listener.exitGotoCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGotoCommand" ):
                return visitor.visitGotoCommand(self)
            else:
                return visitor.visitChildren(self)




    def gotoCommand(self):

        localctx = tlangParser.GotoCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_gotoCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(tlangParser.T__11)
            self.state = 176
            self.match(tlangParser.T__12)
            self.state = 177
            self.expr()
            self.state = 178
            self.match(tlangParser.T__2)
            self.state = 179
            self.expr()
            self.state = 180
            self.match(tlangParser.T__13)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = tlangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(tlangParser.VAR)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737489371136) != 0):
                self.state = 183
                self.typeAnnotation()


            self.state = 186
            self.match(tlangParser.T__5)
            self.state = 187
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeAnnotation" ):
                listener.enterTypeAnnotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeAnnotation" ):
                listener.exitTypeAnnotation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeAnnotation" ):
                return visitor.visitTypeAnnotation(self)
            else:
                return visitor.visitChildren(self)




    def typeAnnotation(self):

        localctx = tlangParser.TypeAnnotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_typeAnnotation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
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

        def NAME(self):
            return self.getToken(tlangParser.NAME, 0)

        def getRuleIndex(self):
            return tlangParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = tlangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 140737489371136) != 0)):
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoveCommand" ):
                listener.enterMoveCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoveCommand" ):
                listener.exitMoveCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoveCommand" ):
                return visitor.visitMoveCommand(self)
            else:
                return visitor.visitChildren(self)




    def moveCommand(self):

        localctx = tlangParser.MoveCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_moveCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.moveOp()
            self.state = 194
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoveOp" ):
                listener.enterMoveOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoveOp" ):
                listener.exitMoveOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoveOp" ):
                return visitor.visitMoveOp(self)
            else:
                return visitor.visitChildren(self)




    def moveOp(self):

        localctx = tlangParser.MoveOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_moveOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15728640) != 0)):
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPenCommand" ):
                listener.enterPenCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPenCommand" ):
                listener.exitPenCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPenCommand" ):
                return visitor.visitPenCommand(self)
            else:
                return visitor.visitChildren(self)




    def penCommand(self):

        localctx = tlangParser.PenCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_penCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            _la = self._input.LA(1)
            if not(_la==24 or _la==25):
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPauseCommand" ):
                listener.enterPauseCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPauseCommand" ):
                listener.exitPauseCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPauseCommand" ):
                return visitor.visitPauseCommand(self)
            else:
                return visitor.visitChildren(self)




    def pauseCommand(self):

        localctx = tlangParser.PauseCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_pauseCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(tlangParser.T__25)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = tlangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)




    def orExpr(self):

        localctx = tlangParser.OrExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_orExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.andExpr()
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 205
                self.match(tlangParser.OR)
                self.state = 206
                self.andExpr()
                self.state = 211
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)




    def andExpr(self):

        localctx = tlangParser.AndExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_andExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.equalityExpr()
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 213
                self.match(tlangParser.AND)
                self.state = 214
                self.equalityExpr()
                self.state = 219
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpr" ):
                listener.enterEqualityExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpr" ):
                listener.exitEqualityExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpr" ):
                return visitor.visitEqualityExpr(self)
            else:
                return visitor.visitChildren(self)




    def equalityExpr(self):

        localctx = tlangParser.EqualityExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_equalityExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.relationalExpr()
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30 or _la==31:
                self.state = 221
                _la = self._input.LA(1)
                if not(_la==30 or _la==31):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 222
                self.relationalExpr()
                self.state = 227
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpr" ):
                listener.enterRelationalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpr" ):
                listener.exitRelationalExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpr" ):
                return visitor.visitRelationalExpr(self)
            else:
                return visitor.visitChildren(self)




    def relationalExpr(self):

        localctx = tlangParser.RelationalExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_relationalExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.additiveExpr()
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 13690208256) != 0):
                self.state = 229
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 13690208256) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 230
                self.additiveExpr()
                self.state = 235
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpr" ):
                listener.enterAdditiveExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpr" ):
                listener.exitAdditiveExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpr" ):
                return visitor.visitAdditiveExpr(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpr(self):

        localctx = tlangParser.AdditiveExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_additiveExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.multiplicativeExpr()
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37 or _la==38:
                self.state = 237
                _la = self._input.LA(1)
                if not(_la==37 or _la==38):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 238
                self.multiplicativeExpr()
                self.state = 243
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpr" ):
                listener.enterMultiplicativeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpr" ):
                listener.exitMultiplicativeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpr" ):
                return visitor.visitMultiplicativeExpr(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpr(self):

        localctx = tlangParser.MultiplicativeExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_multiplicativeExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.unaryExpr()
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39 or _la==40:
                self.state = 245
                _la = self._input.LA(1)
                if not(_la==39 or _la==40):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 246
                self.unaryExpr()
                self.state = 251
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpr" ):
                listener.enterUnaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpr" ):
                listener.exitUnaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpr(self):

        localctx = tlangParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_unaryExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36 or _la==38:
                self.state = 252
                _la = self._input.LA(1)
                if not(_la==36 or _la==38):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 255
            self.primary(0)
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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryValue" ):
                listener.enterPrimaryValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryValue" ):
                listener.exitPrimaryValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryValue" ):
                return visitor.visitPrimaryValue(self)
            else:
                return visitor.visitChildren(self)


    class ArrayAccessExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(tlangParser.VAR, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.ExprContext)
            else:
                return self.getTypedRuleContext(tlangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayAccessExpr" ):
                listener.enterArrayAccessExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayAccessExpr" ):
                listener.exitArrayAccessExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAccessExpr" ):
                return visitor.visitArrayAccessExpr(self)
            else:
                return visitor.visitChildren(self)


    class CastExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(tlangParser.TypeContext,0)

        def primary(self):
            return self.getTypedRuleContext(tlangParser.PrimaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCastExpr" ):
                listener.enterCastExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCastExpr" ):
                listener.exitCastExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCastExpr" ):
                return visitor.visitCastExpr(self)
            else:
                return visitor.visitChildren(self)


    class FieldAccessExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary(self):
            return self.getTypedRuleContext(tlangParser.PrimaryContext,0)

        def NAME(self):
            return self.getToken(tlangParser.NAME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFieldAccessExpr" ):
                listener.enterFieldAccessExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFieldAccessExpr" ):
                listener.exitFieldAccessExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFieldAccessExpr" ):
                return visitor.visitFieldAccessExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(tlangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class StructLiteralExprContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tlangParser.ExprContext)
            else:
                return self.getTypedRuleContext(tlangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructLiteralExpr" ):
                listener.enterStructLiteralExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructLiteralExpr" ):
                listener.exitStructLiteralExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructLiteralExpr" ):
                return visitor.visitStructLiteralExpr(self)
            else:
                return visitor.visitChildren(self)


    class PenConditionContext(PrimaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tlangParser.PrimaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PENCOND(self):
            return self.getToken(tlangParser.PENCOND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPenCondition" ):
                listener.enterPenCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPenCondition" ):
                listener.exitPenCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPenCondition" ):
                return visitor.visitPenCondition(self)
            else:
                return visitor.visitChildren(self)



    def primary(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = tlangParser.PrimaryContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_primary, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                localctx = tlangParser.PrimaryValueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 258
                self.value()
                pass

            elif la_ == 2:
                localctx = tlangParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 259
                self.match(tlangParser.T__12)
                self.state = 260
                self.expr()
                self.state = 261
                self.match(tlangParser.T__13)
                pass

            elif la_ == 3:
                localctx = tlangParser.CastExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 263
                self.match(tlangParser.T__12)
                self.state = 264
                self.type_()
                self.state = 265
                self.match(tlangParser.T__13)
                self.state = 266
                self.primary(5)
                pass

            elif la_ == 4:
                localctx = tlangParser.PenConditionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 268
                self.match(tlangParser.PENCOND)
                pass

            elif la_ == 5:
                localctx = tlangParser.ArrayAccessExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 269
                self.match(tlangParser.VAR)
                self.state = 274 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 270
                        self.match(tlangParser.T__6)
                        self.state = 271
                        self.expr()
                        self.state = 272
                        self.match(tlangParser.T__7)

                    else:
                        raise NoViableAltException(self)
                    self.state = 276 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                pass

            elif la_ == 6:
                localctx = tlangParser.StructLiteralExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 278
                self.match(tlangParser.T__1)
                self.state = 279
                self.expr()
                self.state = 284
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 280
                    self.match(tlangParser.T__2)
                    self.state = 281
                    self.expr()
                    self.state = 286
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 287
                self.match(tlangParser.T__3)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 296
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = tlangParser.FieldAccessExprContext(self, tlangParser.PrimaryContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_primary)
                    self.state = 291
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 292
                    self.match(tlangParser.T__4)
                    self.state = 293
                    self.match(tlangParser.NAME) 
                self.state = 298
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringValue" ):
                listener.enterStringValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringValue" ):
                listener.exitStringValue(self)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarValue" ):
                listener.enterVarValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarValue" ):
                listener.exitVarValue(self)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatValue" ):
                listener.enterFloatValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatValue" ):
                listener.exitFloatValue(self)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanValue" ):
                listener.enterBooleanValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanValue" ):
                listener.exitBooleanValue(self)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoubleValue" ):
                listener.enterDoubleValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoubleValue" ):
                listener.exitDoubleValue(self)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumValue" ):
                listener.enterNumValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumValue" ):
                listener.exitNumValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumValue" ):
                return visitor.visitNumValue(self)
            else:
                return visitor.visitChildren(self)



    def value(self):

        localctx = tlangParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_value)
        try:
            self.state = 305
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                localctx = tlangParser.NumValueContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.match(tlangParser.NUM)
                pass
            elif token in [42]:
                localctx = tlangParser.FloatValueContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.match(tlangParser.FLOAT)
                pass
            elif token in [43]:
                localctx = tlangParser.DoubleValueContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 301
                self.match(tlangParser.DOUBLE)
                pass
            elif token in [44]:
                localctx = tlangParser.StringValueContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 302
                self.match(tlangParser.STRING)
                pass
            elif token in [45]:
                localctx = tlangParser.BooleanValueContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 303
                self.match(tlangParser.BOOLEAN)
                pass
            elif token in [46]:
                localctx = tlangParser.VarValueContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 304
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[29] = self.primary_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def primary_sempred(self, localctx:PrimaryContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




