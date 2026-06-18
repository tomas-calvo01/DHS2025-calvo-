# Generated from c:/Users/tomas/OneDrive/Documents/GitHub/DHS2025-calvo-/src/main/python/compiler.g4 by ANTLR 4.13.1
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
        4,1,35,313,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,1,0,1,0,1,
        1,1,1,1,1,1,1,3,1,72,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,
        83,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,6,1,6,1,6,3,6,105,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,123,8,8,1,9,1,9,1,9,1,9,1,
        9,1,9,3,9,131,8,9,1,10,1,10,1,10,5,10,136,8,10,10,10,12,10,139,9,
        10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,152,
        8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,
        3,13,166,8,13,1,14,1,14,1,14,3,14,171,8,14,1,15,1,15,1,16,1,16,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,16,3,16,192,8,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,
        18,1,18,1,18,1,18,3,18,206,8,18,1,19,1,19,1,19,1,19,1,19,1,19,3,
        19,214,8,19,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,22,1,22,1,23,1,
        23,1,23,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,
        25,3,25,240,8,25,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,1,
        27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,258,8,27,1,28,1,28,1,28,1,
        28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,
        28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,285,8,28,1,29,1,
        29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,295,8,29,1,30,1,30,1,30,1,
        30,1,30,1,31,1,31,1,31,5,31,305,8,31,10,31,12,31,308,9,31,1,31,3,
        31,311,8,31,1,31,0,0,32,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,0,1,1,0,25,27,
        322,0,64,1,0,0,0,2,71,1,0,0,0,4,82,1,0,0,0,6,84,1,0,0,0,8,88,1,0,
        0,0,10,94,1,0,0,0,12,104,1,0,0,0,14,106,1,0,0,0,16,122,1,0,0,0,18,
        130,1,0,0,0,20,132,1,0,0,0,22,151,1,0,0,0,24,153,1,0,0,0,26,165,
        1,0,0,0,28,170,1,0,0,0,30,172,1,0,0,0,32,191,1,0,0,0,34,193,1,0,
        0,0,36,205,1,0,0,0,38,213,1,0,0,0,40,215,1,0,0,0,42,219,1,0,0,0,
        44,222,1,0,0,0,46,224,1,0,0,0,48,227,1,0,0,0,50,239,1,0,0,0,52,241,
        1,0,0,0,54,257,1,0,0,0,56,284,1,0,0,0,58,294,1,0,0,0,60,296,1,0,
        0,0,62,310,1,0,0,0,64,65,3,2,1,0,65,66,5,0,0,1,66,1,1,0,0,0,67,68,
        3,4,2,0,68,69,3,2,1,0,69,72,1,0,0,0,70,72,1,0,0,0,71,67,1,0,0,0,
        71,70,1,0,0,0,72,3,1,0,0,0,73,83,3,24,12,0,74,83,3,32,16,0,75,83,
        3,10,5,0,76,83,3,8,4,0,77,83,3,14,7,0,78,83,3,34,17,0,79,83,3,40,
        20,0,80,83,3,42,21,0,81,83,3,6,3,0,82,73,1,0,0,0,82,74,1,0,0,0,82,
        75,1,0,0,0,82,76,1,0,0,0,82,77,1,0,0,0,82,78,1,0,0,0,82,79,1,0,0,
        0,82,80,1,0,0,0,82,81,1,0,0,0,83,5,1,0,0,0,84,85,5,3,0,0,85,86,3,
        2,1,0,86,87,5,4,0,0,87,7,1,0,0,0,88,89,5,31,0,0,89,90,5,1,0,0,90,
        91,3,44,22,0,91,92,5,2,0,0,92,93,3,4,2,0,93,9,1,0,0,0,94,95,5,28,
        0,0,95,96,5,1,0,0,96,97,3,44,22,0,97,98,5,2,0,0,98,99,3,4,2,0,99,
        100,3,12,6,0,100,11,1,0,0,0,101,102,5,29,0,0,102,105,3,4,2,0,103,
        105,1,0,0,0,104,101,1,0,0,0,104,103,1,0,0,0,105,13,1,0,0,0,106,107,
        5,30,0,0,107,108,5,1,0,0,108,109,3,16,8,0,109,110,5,7,0,0,110,111,
        3,44,22,0,111,112,5,7,0,0,112,113,3,22,11,0,113,114,5,2,0,0,114,
        115,3,6,3,0,115,15,1,0,0,0,116,117,3,30,15,0,117,118,5,33,0,0,118,
        119,3,28,14,0,119,120,3,18,9,0,120,123,1,0,0,0,121,123,3,20,10,0,
        122,116,1,0,0,0,122,121,1,0,0,0,123,17,1,0,0,0,124,125,5,8,0,0,125,
        126,5,33,0,0,126,127,3,28,14,0,127,128,3,18,9,0,128,131,1,0,0,0,
        129,131,1,0,0,0,130,124,1,0,0,0,130,129,1,0,0,0,131,19,1,0,0,0,132,
        137,3,22,11,0,133,134,5,8,0,0,134,136,3,22,11,0,135,133,1,0,0,0,
        136,139,1,0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,21,1,0,0,0,139,
        137,1,0,0,0,140,141,5,33,0,0,141,142,5,9,0,0,142,152,3,44,22,0,143,
        144,5,33,0,0,144,152,5,21,0,0,145,146,5,33,0,0,146,152,5,22,0,0,
        147,148,5,21,0,0,148,152,5,33,0,0,149,150,5,22,0,0,150,152,5,33,
        0,0,151,140,1,0,0,0,151,143,1,0,0,0,151,145,1,0,0,0,151,147,1,0,
        0,0,151,149,1,0,0,0,152,23,1,0,0,0,153,154,3,30,15,0,154,155,5,33,
        0,0,155,156,3,28,14,0,156,157,3,26,13,0,157,158,5,7,0,0,158,25,1,
        0,0,0,159,160,5,8,0,0,160,161,5,33,0,0,161,162,3,28,14,0,162,163,
        3,26,13,0,163,166,1,0,0,0,164,166,1,0,0,0,165,159,1,0,0,0,165,164,
        1,0,0,0,166,27,1,0,0,0,167,168,5,9,0,0,168,171,3,44,22,0,169,171,
        1,0,0,0,170,167,1,0,0,0,170,169,1,0,0,0,171,29,1,0,0,0,172,173,7,
        0,0,0,173,31,1,0,0,0,174,175,5,33,0,0,175,176,5,9,0,0,176,177,3,
        44,22,0,177,178,5,7,0,0,178,192,1,0,0,0,179,180,5,33,0,0,180,181,
        5,21,0,0,181,192,5,7,0,0,182,183,5,33,0,0,183,184,5,22,0,0,184,192,
        5,7,0,0,185,186,5,21,0,0,186,187,5,33,0,0,187,192,5,7,0,0,188,189,
        5,22,0,0,189,190,5,33,0,0,190,192,5,7,0,0,191,174,1,0,0,0,191,179,
        1,0,0,0,191,182,1,0,0,0,191,185,1,0,0,0,191,188,1,0,0,0,192,33,1,
        0,0,0,193,194,3,30,15,0,194,195,5,33,0,0,195,196,5,1,0,0,196,197,
        3,36,18,0,197,198,5,2,0,0,198,199,3,6,3,0,199,35,1,0,0,0,200,201,
        3,30,15,0,201,202,5,33,0,0,202,203,3,38,19,0,203,206,1,0,0,0,204,
        206,1,0,0,0,205,200,1,0,0,0,205,204,1,0,0,0,206,37,1,0,0,0,207,208,
        5,8,0,0,208,209,3,30,15,0,209,210,5,33,0,0,210,211,3,38,19,0,211,
        214,1,0,0,0,212,214,1,0,0,0,213,207,1,0,0,0,213,212,1,0,0,0,214,
        39,1,0,0,0,215,216,5,32,0,0,216,217,3,44,22,0,217,218,5,7,0,0,218,
        41,1,0,0,0,219,220,3,60,30,0,220,221,5,7,0,0,221,43,1,0,0,0,222,
        223,3,46,23,0,223,45,1,0,0,0,224,225,3,48,24,0,225,226,3,56,28,0,
        226,47,1,0,0,0,227,228,3,52,26,0,228,229,3,50,25,0,229,49,1,0,0,
        0,230,231,5,10,0,0,231,232,3,52,26,0,232,233,3,50,25,0,233,240,1,
        0,0,0,234,235,5,11,0,0,235,236,3,52,26,0,236,237,3,50,25,0,237,240,
        1,0,0,0,238,240,1,0,0,0,239,230,1,0,0,0,239,234,1,0,0,0,239,238,
        1,0,0,0,240,51,1,0,0,0,241,242,3,58,29,0,242,243,3,54,27,0,243,53,
        1,0,0,0,244,245,5,12,0,0,245,246,3,58,29,0,246,247,3,54,27,0,247,
        258,1,0,0,0,248,249,5,13,0,0,249,250,3,58,29,0,250,251,3,54,27,0,
        251,258,1,0,0,0,252,253,5,14,0,0,253,254,3,58,29,0,254,255,3,54,
        27,0,255,258,1,0,0,0,256,258,1,0,0,0,257,244,1,0,0,0,257,248,1,0,
        0,0,257,252,1,0,0,0,257,256,1,0,0,0,258,55,1,0,0,0,259,260,5,19,
        0,0,260,261,3,48,24,0,261,262,3,56,28,0,262,285,1,0,0,0,263,264,
        5,20,0,0,264,265,3,48,24,0,265,266,3,56,28,0,266,285,1,0,0,0,267,
        268,5,15,0,0,268,269,3,48,24,0,269,270,3,56,28,0,270,285,1,0,0,0,
        271,272,5,16,0,0,272,273,3,48,24,0,273,274,3,56,28,0,274,285,1,0,
        0,0,275,276,5,17,0,0,276,277,3,48,24,0,277,278,3,56,28,0,278,285,
        1,0,0,0,279,280,5,18,0,0,280,281,3,48,24,0,281,282,3,56,28,0,282,
        285,1,0,0,0,283,285,1,0,0,0,284,259,1,0,0,0,284,263,1,0,0,0,284,
        267,1,0,0,0,284,271,1,0,0,0,284,275,1,0,0,0,284,279,1,0,0,0,284,
        283,1,0,0,0,285,57,1,0,0,0,286,287,5,1,0,0,287,288,3,48,24,0,288,
        289,5,2,0,0,289,295,1,0,0,0,290,295,5,24,0,0,291,295,5,23,0,0,292,
        295,3,60,30,0,293,295,5,33,0,0,294,286,1,0,0,0,294,290,1,0,0,0,294,
        291,1,0,0,0,294,292,1,0,0,0,294,293,1,0,0,0,295,59,1,0,0,0,296,297,
        5,33,0,0,297,298,5,1,0,0,298,299,3,62,31,0,299,300,5,2,0,0,300,61,
        1,0,0,0,301,306,3,44,22,0,302,303,5,8,0,0,303,305,3,44,22,0,304,
        302,1,0,0,0,305,308,1,0,0,0,306,304,1,0,0,0,306,307,1,0,0,0,307,
        311,1,0,0,0,308,306,1,0,0,0,309,311,1,0,0,0,310,301,1,0,0,0,310,
        309,1,0,0,0,311,63,1,0,0,0,18,71,82,104,122,130,137,151,165,170,
        191,205,213,239,257,284,294,306,310
    ]

class compilerParser ( Parser ):

    grammarFileName = "compiler.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "';'", "','", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'<='", "'>='", "'=='", "'!='", "'<'", "'>'", "'++'", 
                     "'--'", "<INVALID>", "<INVALID>", "'int'", "'double'", 
                     "'float'", "'if'", "'else'", "'for'", "'while'", "'return'" ]

    symbolicNames = [ "<INVALID>", "PA", "PC", "LLA", "LLC", "CA", "CC", 
                      "PYC", "COMA", "ASIG", "SUMA", "RESTA", "MULT", "DIV", 
                      "MOD", "MENOREQ", "MAYOREQ", "EQUAL", "NEQUAL", "MENOR", 
                      "MAYOR", "INCREMENTO", "DECREMENTO", "DECIMAL", "NUMERO", 
                      "INT", "DOUBLE", "FLOAT", "IF", "ELSE", "FOR", "WHILE", 
                      "RETURN", "ID", "WS", "OTRO" ]

    RULE_programa = 0
    RULE_instrucciones = 1
    RULE_instruccion = 2
    RULE_bloque = 3
    RULE_iwhile = 4
    RULE_iif = 5
    RULE_ielse = 6
    RULE_ifor = 7
    RULE_forInit = 8
    RULE_listaVarFor = 9
    RULE_listaAsignacionFor = 10
    RULE_asignacionFor = 11
    RULE_declaracion = 12
    RULE_listavar = 13
    RULE_inic = 14
    RULE_tipo = 15
    RULE_asignacion = 16
    RULE_funcion = 17
    RULE_parametros = 18
    RULE_lista_param = 19
    RULE_returnstmt = 20
    RULE_llamada = 21
    RULE_opal = 22
    RULE_relacion = 23
    RULE_exp = 24
    RULE_e = 25
    RULE_term = 26
    RULE_t = 27
    RULE_l = 28
    RULE_factor = 29
    RULE_call = 30
    RULE_argumentos = 31

    ruleNames =  [ "programa", "instrucciones", "instruccion", "bloque", 
                   "iwhile", "iif", "ielse", "ifor", "forInit", "listaVarFor", 
                   "listaAsignacionFor", "asignacionFor", "declaracion", 
                   "listavar", "inic", "tipo", "asignacion", "funcion", 
                   "parametros", "lista_param", "returnstmt", "llamada", 
                   "opal", "relacion", "exp", "e", "term", "t", "l", "factor", 
                   "call", "argumentos" ]

    EOF = Token.EOF
    PA=1
    PC=2
    LLA=3
    LLC=4
    CA=5
    CC=6
    PYC=7
    COMA=8
    ASIG=9
    SUMA=10
    RESTA=11
    MULT=12
    DIV=13
    MOD=14
    MENOREQ=15
    MAYOREQ=16
    EQUAL=17
    NEQUAL=18
    MENOR=19
    MAYOR=20
    INCREMENTO=21
    DECREMENTO=22
    DECIMAL=23
    NUMERO=24
    INT=25
    DOUBLE=26
    FLOAT=27
    IF=28
    ELSE=29
    FOR=30
    WHILE=31
    RETURN=32
    ID=33
    WS=34
    OTRO=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instrucciones(self):
            return self.getTypedRuleContext(compilerParser.InstruccionesContext,0)


        def EOF(self):
            return self.getToken(compilerParser.EOF, 0)

        def getRuleIndex(self):
            return compilerParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = compilerParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.instrucciones()
            self.state = 65
            self.match(compilerParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion(self):
            return self.getTypedRuleContext(compilerParser.InstruccionContext,0)


        def instrucciones(self):
            return self.getTypedRuleContext(compilerParser.InstruccionesContext,0)


        def getRuleIndex(self):
            return compilerParser.RULE_instrucciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucciones" ):
                listener.enterInstrucciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucciones" ):
                listener.exitInstrucciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrucciones" ):
                return visitor.visitInstrucciones(self)
            else:
                return visitor.visitChildren(self)




    def instrucciones(self):

        localctx = compilerParser.InstruccionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instrucciones)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 21, 22, 25, 26, 27, 28, 30, 31, 32, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.instruccion()
                self.state = 68
                self.instrucciones()
                pass
            elif token in [-1, 4]:
                self.enterOuterAlt(localctx, 2)

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


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(compilerParser.DeclaracionContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(compilerParser.AsignacionContext,0)


        def iif(self):
            return self.getTypedRuleContext(compilerParser.IifContext,0)


        def iwhile(self):
            return self.getTypedRuleContext(compilerParser.IwhileContext,0)


        def ifor(self):
            return self.getTypedRuleContext(compilerParser.IforContext,0)


        def funcion(self):
            return self.getTypedRuleContext(compilerParser.FuncionContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(compilerParser.ReturnstmtContext,0)


        def llamada(self):
            return self.getTypedRuleContext(compilerParser.LlamadaContext,0)


        def bloque(self):
            return self.getTypedRuleContext(compilerParser.BloqueContext,0)


        def getRuleIndex(self):
            return compilerParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = compilerParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instruccion)
        try:
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.declaracion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.asignacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self.iif()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 76
                self.iwhile()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 77
                self.ifor()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 78
                self.funcion()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 79
                self.returnstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 80
                self.llamada()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 81
                self.bloque()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLA(self):
            return self.getToken(compilerParser.LLA, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(compilerParser.InstruccionesContext,0)


        def LLC(self):
            return self.getToken(compilerParser.LLC, 0)

        def getRuleIndex(self):
            return compilerParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = compilerParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(compilerParser.LLA)
            self.state = 85
            self.instrucciones()
            self.state = 86
            self.match(compilerParser.LLC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IwhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(compilerParser.WHILE, 0)

        def PA(self):
            return self.getToken(compilerParser.PA, 0)

        def opal(self):
            return self.getTypedRuleContext(compilerParser.OpalContext,0)


        def PC(self):
            return self.getToken(compilerParser.PC, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compilerParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compilerParser.RULE_iwhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIwhile" ):
                listener.enterIwhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIwhile" ):
                listener.exitIwhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIwhile" ):
                return visitor.visitIwhile(self)
            else:
                return visitor.visitChildren(self)




    def iwhile(self):

        localctx = compilerParser.IwhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_iwhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(compilerParser.WHILE)
            self.state = 89
            self.match(compilerParser.PA)
            self.state = 90
            self.opal()
            self.state = 91
            self.match(compilerParser.PC)
            self.state = 92
            self.instruccion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(compilerParser.IF, 0)

        def PA(self):
            return self.getToken(compilerParser.PA, 0)

        def opal(self):
            return self.getTypedRuleContext(compilerParser.OpalContext,0)


        def PC(self):
            return self.getToken(compilerParser.PC, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compilerParser.InstruccionContext,0)


        def ielse(self):
            return self.getTypedRuleContext(compilerParser.IelseContext,0)


        def getRuleIndex(self):
            return compilerParser.RULE_iif

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIif" ):
                listener.enterIif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIif" ):
                listener.exitIif(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIif" ):
                return visitor.visitIif(self)
            else:
                return visitor.visitChildren(self)




    def iif(self):

        localctx = compilerParser.IifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_iif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(compilerParser.IF)
            self.state = 95
            self.match(compilerParser.PA)
            self.state = 96
            self.opal()
            self.state = 97
            self.match(compilerParser.PC)
            self.state = 98
            self.instruccion()
            self.state = 99
            self.ielse()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IelseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(compilerParser.ELSE, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compilerParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compilerParser.RULE_ielse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIelse" ):
                listener.enterIelse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIelse" ):
                listener.exitIelse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIelse" ):
                return visitor.visitIelse(self)
            else:
                return visitor.visitChildren(self)




    def ielse(self):

        localctx = compilerParser.IelseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ielse)
        try:
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.match(compilerParser.ELSE)
                self.state = 102
                self.instruccion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IforContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(compilerParser.FOR, 0)

        def PA(self):
            return self.getToken(compilerParser.PA, 0)

        def forInit(self):
            return self.getTypedRuleContext(compilerParser.ForInitContext,0)


        def PYC(self, i:int=None):
            if i is None:
                return self.getTokens(compilerParser.PYC)
            else:
                return self.getToken(compilerParser.PYC, i)

        def opal(self):
            return self.getTypedRuleContext(compilerParser.OpalContext,0)


        def asignacionFor(self):
            return self.getTypedRuleContext(compilerParser.AsignacionForContext,0)


        def PC(self):
            return self.getToken(compilerParser.PC, 0)

        def bloque(self):
            return self.getTypedRuleContext(compilerParser.BloqueContext,0)


        def getRuleIndex(self):
            return compilerParser.RULE_ifor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfor" ):
                listener.enterIfor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfor" ):
                listener.exitIfor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfor" ):
                return visitor.visitIfor(self)
            else:
                return visitor.visitChildren(self)




    def ifor(self):

        localctx = compilerParser.IforContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(compilerParser.FOR)
            self.state = 107
            self.match(compilerParser.PA)
            self.state = 108
            self.forInit()
            self.state = 109
            self.match(compilerParser.PYC)
            self.state = 110
            self.opal()
            self.state = 111
            self.match(compilerParser.PYC)
            self.state = 112
            self.asignacionFor()
            self.state = 113
            self.match(compilerParser.PC)
            self.state = 114
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(compilerParser.TipoContext,0)


        def ID(self):
            return self.getToken(compilerParser.ID, 0)

        def inic(self):
            return self.getTypedRuleContext(compilerParser.InicContext,0)


        def listaVarFor(self):
            return self.getTypedRuleContext(compilerParser.ListaVarForContext,0)


        def listaAsignacionFor(self):
            return self.getTypedRuleContext(compilerParser.ListaAsignacionForContext,0)


        def getRuleIndex(self):
            return compilerParser.RULE_forInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInit" ):
                listener.enterForInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInit" ):
                listener.exitForInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInit" ):
                return visitor.visitForInit(self)
            else:
                return visitor.visitChildren(self)




    def forInit(self):

        localctx = compilerParser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_forInit)
        try:
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25, 26, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.tipo()
                self.state = 117
                self.match(compilerParser.ID)
                self.state = 118
                self.inic()
                self.state = 119
                self.listaVarFor()
                pass
            elif token in [21, 22, 33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.listaAsignacionFor()
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


    class ListaVarForContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compilerParser.COMA, 0)

        def ID(self):
            return self.getToken(compilerParser.ID, 0)

        def inic(self):
            return self.getTypedRuleContext(compilerParser.InicContext,0)


        def listaVarFor(self):
            return self.getTypedRuleContext(compilerParser.ListaVarForContext,0)


        def getRuleIndex(self):
            return compilerParser.RULE_listaVarFor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaVarFor" ):
                listener.enterListaVarFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaVarFor" ):
                listener.exitListaVarFor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaVarFor" ):
                return visitor.visitListaVarFor(self)
            else:
                return visitor.visitChildren(self)




    def listaVarFor(self):

        localctx = compilerParser.ListaVarForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_listaVarFor)
        try:
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.match(compilerParser.COMA)
                self.state = 125
                self.match(compilerParser.ID)
                self.state = 126
                self.inic()
                self.state = 127
                self.listaVarFor()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)

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


    class ListaAsignacionForContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacionFor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compilerParser.AsignacionForContext)
            else:
                return self.getTypedRuleContext(compilerParser.AsignacionForContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(compilerParser.COMA)
            else:
                return self.getToken(compilerParser.COMA, i)

        def getRuleIndex(self):
            return compilerParser.RULE_listaAsignacionFor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaAsignacionFor" ):
                listener.enterListaAsignacionFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaAsignacionFor" ):
                listener.exitListaAsignacionFor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaAsignacionFor" ):
                return visitor.visitListaAsignacionFor(self)
            else:
                return visitor.visitChildren(self)




    def listaAsignacionFor(self):

        localctx = compilerParser.ListaAsignacionForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_listaAsignacionFor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.asignacionFor()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 133
                self.match(compilerParser.COMA)
                self.state = 134
                self.asignacionFor()
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionForContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compilerParser.ID, 0)

        def ASIG(self):
            return self.getToken(compilerParser.ASIG, 0)

        def opal(self):
            return self.getTypedRuleContext(compilerParser.OpalContext,0)


        def INCREMENTO(self):
            return self.getToken(compilerParser.INCREMENTO, 0)

        def DECREMENTO(self):
            return self.getToken(compilerParser.DECREMENTO, 0)

        def getRuleIndex(self):
            return compilerParser.RULE_asignacionFor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacionFor" ):
                listener.enterAsignacionFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacionFor" ):
                listener.exitAsignacionFor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacionFor" ):
                return visitor.visitAsignacionFor(self)
            else:
                return visitor.visitChildren(self)




    def asignacionFor(self):

        localctx = compilerParser.AsignacionForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_asignacionFor)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.match(compilerParser.ID)
                self.state = 141
                self.match(compilerParser.ASIG)
                self.state = 142
                self.opal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.match(compilerParser.ID)
                self.state = 144
                self.match(compilerParser.INCREMENTO)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 145
                self.match(compilerParser.ID)
                self.state = 146
                self.match(compilerParser.DECREMENTO)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 147
                self.match(compilerParser.INCREMENTO)
                self.state = 148
                self.match(compilerParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 149
                self.match(compilerParser.DECREMENTO)
                self.state = 150
                self.match(compilerParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(compilerParser.TipoContext,0)


        def ID(self):
            return self.getToken(compilerParser.ID, 0)

        def inic(self):
            return self.getTypedRuleContext(compilerParser.InicContext,0)


        def listavar(self):
            return self.getTypedRuleContext(compilerParser.ListavarContext,0)


        def PYC(self):
            return self.getToken(compilerParser.PYC, 0)

        def getRuleIndex(self):
            return compilerParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = compilerParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.tipo()
            self.state = 154
            self.match(compilerParser.ID)
            self.state = 155
            self.inic()
            self.state = 156
            self.listavar()
            self.state = 157
            self.match(compilerParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListavarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compilerParser.COMA, 0)

        def ID(self):
            return self.getToken(compilerParser.ID, 0)

        def inic(self):
            return self.getTypedRuleContext(compilerParser.InicContext,0)


        def listavar(self):
            return self.getTypedRuleContext(compilerParser.ListavarContext,0)


        def getRuleIndex(self):
            return compilerParser.RULE_listavar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListavar" ):
                listener.enterListavar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListavar" ):
                listener.exitListavar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListavar" ):
                return visitor.visitListavar(self)
            else:
                return visitor.visitChildren(self)




    def listavar(self):

        localctx = compilerParser.ListavarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_listavar)
        try:
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.match(compilerParser.COMA)
                self.state = 160
                self.match(compilerParser.ID)
                self.state = 161
                self.inic()
                self.state = 162
                self.listavar()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)

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


    class InicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASIG(self):
            return self.getToken(compilerParser.ASIG, 0)

        def opal(self):
            return self.getTypedRuleContext(compilerParser.OpalContext,0)


        def getRuleIndex(self):
            return compilerParser.RULE_inic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInic" ):
                listener.enterInic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInic" ):
                listener.exitInic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInic" ):
                return visitor.visitInic(self)
            else:
                return visitor.visitChildren(self)




    def inic(self):

        localctx = compilerParser.InicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_inic)
        try:
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.match(compilerParser.ASIG)
                self.state = 168
                self.opal()
                pass
            elif token in [7, 8]:
                self.enterOuterAlt(localctx, 2)

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


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(compilerParser.INT, 0)

        def DOUBLE(self):
            return self.getToken(compilerParser.DOUBLE, 0)

        def FLOAT(self):
            return self.getToken(compilerParser.FLOAT, 0)

        def getRuleIndex(self):
            return compilerParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = compilerParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 234881024) != 0)):
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


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compilerParser.ID, 0)

        def ASIG(self):
            return self.getToken(compilerParser.ASIG, 0)

        def opal(self):
            return self.getTypedRuleContext(compilerParser.OpalContext,0)


        def PYC(self):
            return self.getToken(compilerParser.PYC, 0)

        def INCREMENTO(self):
            return self.getToken(compilerParser.INCREMENTO, 0)

        def DECREMENTO(self):
            return self.getToken(compilerParser.DECREMENTO, 0)

        def getRuleIndex(self):
            return compilerParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = compilerParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_asignacion)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.match(compilerParser.ID)
                self.state = 175
                self.match(compilerParser.ASIG)
                self.state = 176
                self.opal()
                self.state = 177
                self.match(compilerParser.PYC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.match(compilerParser.ID)
                self.state = 180
                self.match(compilerParser.INCREMENTO)
                self.state = 181
                self.match(compilerParser.PYC)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 182
                self.match(compilerParser.ID)
                self.state = 183
                self.match(compilerParser.DECREMENTO)
                self.state = 184
                self.match(compilerParser.PYC)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 185
                self.match(compilerParser.INCREMENTO)
                self.state = 186
                self.match(compilerParser.ID)
                self.state = 187
                self.match(compilerParser.PYC)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 188
                self.match(compilerParser.DECREMENTO)
                self.state = 189
                self.match(compilerParser.ID)
                self.state = 190
                self.match(compilerParser.PYC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(compilerParser.TipoContext,0)


        def ID(self):
            return self.getToken(compilerParser.ID, 0)

        def PA(self):
            return self.getToken(compilerParser.PA, 0)

        def parametros(self):
            return self.getTypedRuleContext(compilerParser.ParametrosContext,0)


        def PC(self):
            return self.getToken(compilerParser.PC, 0)

        def bloque(self):
            return self.getTypedRuleContext(compilerParser.BloqueContext,0)


        def getRuleIndex(self):
            return compilerParser.RULE_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion" ):
                listener.enterFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion" ):
                listener.exitFuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncion" ):
                return visitor.visitFuncion(self)
            else:
                return visitor.visitChildren(self)




    def funcion(self):

        localctx = compilerParser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_funcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.tipo()
            self.state = 194
            self.match(compilerParser.ID)
            self.state = 195
            self.match(compilerParser.PA)
            self.state = 196
            self.parametros()
            self.state = 197
            self.match(compilerParser.PC)
            self.state = 198
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(compilerParser.TipoContext,0)


        def ID(self):
            return self.getToken(compilerParser.ID, 0)

        def lista_param(self):
            return self.getTypedRuleContext(compilerParser.Lista_paramContext,0)


        def getRuleIndex(self):
            return compilerParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametros" ):
                return visitor.visitParametros(self)
            else:
                return visitor.visitChildren(self)




    def parametros(self):

        localctx = compilerParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_parametros)
        try:
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25, 26, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.tipo()
                self.state = 201
                self.match(compilerParser.ID)
                self.state = 202
                self.lista_param()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)

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


    class Lista_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compilerParser.COMA, 0)

        def tipo(self):
            return self.getTypedRuleContext(compilerParser.TipoContext,0)


        def ID(self):
            return self.getToken(compilerParser.ID, 0)

        def lista_param(self):
            return self.getTypedRuleContext(compilerParser.Lista_paramContext,0)


        def getRuleIndex(self):
            return compilerParser.RULE_lista_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_param" ):
                listener.enterLista_param(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_param" ):
                listener.exitLista_param(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista_param" ):
                return visitor.visitLista_param(self)
            else:
                return visitor.visitChildren(self)




    def lista_param(self):

        localctx = compilerParser.Lista_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_lista_param)
        try:
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.match(compilerParser.COMA)
                self.state = 208
                self.tipo()
                self.state = 209
                self.match(compilerParser.ID)
                self.state = 210
                self.lista_param()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)

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


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(compilerParser.RETURN, 0)

        def opal(self):
            return self.getTypedRuleContext(compilerParser.OpalContext,0)


        def PYC(self):
            return self.getToken(compilerParser.PYC, 0)

        def getRuleIndex(self):
            return compilerParser.RULE_returnstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnstmt" ):
                listener.enterReturnstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnstmt" ):
                listener.exitReturnstmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = compilerParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_returnstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(compilerParser.RETURN)
            self.state = 216
            self.opal()
            self.state = 217
            self.match(compilerParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlamadaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call(self):
            return self.getTypedRuleContext(compilerParser.CallContext,0)


        def PYC(self):
            return self.getToken(compilerParser.PYC, 0)

        def getRuleIndex(self):
            return compilerParser.RULE_llamada

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamada" ):
                listener.enterLlamada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamada" ):
                listener.exitLlamada(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamada" ):
                return visitor.visitLlamada(self)
            else:
                return visitor.visitChildren(self)




    def llamada(self):

        localctx = compilerParser.LlamadaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_llamada)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.call()
            self.state = 220
            self.match(compilerParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relacion(self):
            return self.getTypedRuleContext(compilerParser.RelacionContext,0)


        def getRuleIndex(self):
            return compilerParser.RULE_opal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpal" ):
                listener.enterOpal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpal" ):
                listener.exitOpal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpal" ):
                return visitor.visitOpal(self)
            else:
                return visitor.visitChildren(self)




    def opal(self):

        localctx = compilerParser.OpalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_opal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.relacion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(compilerParser.ExpContext,0)


        def l(self):
            return self.getTypedRuleContext(compilerParser.LContext,0)


        def getRuleIndex(self):
            return compilerParser.RULE_relacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelacion" ):
                listener.enterRelacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelacion" ):
                listener.exitRelacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelacion" ):
                return visitor.visitRelacion(self)
            else:
                return visitor.visitChildren(self)




    def relacion(self):

        localctx = compilerParser.RelacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_relacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.exp()
            self.state = 225
            self.l()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(compilerParser.TermContext,0)


        def e(self):
            return self.getTypedRuleContext(compilerParser.EContext,0)


        def getRuleIndex(self):
            return compilerParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = compilerParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.term()
            self.state = 228
            self.e()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUMA(self):
            return self.getToken(compilerParser.SUMA, 0)

        def term(self):
            return self.getTypedRuleContext(compilerParser.TermContext,0)


        def e(self):
            return self.getTypedRuleContext(compilerParser.EContext,0)


        def RESTA(self):
            return self.getToken(compilerParser.RESTA, 0)

        def getRuleIndex(self):
            return compilerParser.RULE_e

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterE" ):
                listener.enterE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitE" ):
                listener.exitE(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitE" ):
                return visitor.visitE(self)
            else:
                return visitor.visitChildren(self)




    def e(self):

        localctx = compilerParser.EContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_e)
        try:
            self.state = 239
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.match(compilerParser.SUMA)
                self.state = 231
                self.term()
                self.state = 232
                self.e()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.match(compilerParser.RESTA)
                self.state = 235
                self.term()
                self.state = 236
                self.e()
                pass
            elif token in [2, 7, 8, 15, 16, 17, 18, 19, 20]:
                self.enterOuterAlt(localctx, 3)

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


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(compilerParser.FactorContext,0)


        def t(self):
            return self.getTypedRuleContext(compilerParser.TContext,0)


        def getRuleIndex(self):
            return compilerParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = compilerParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.factor()
            self.state = 242
            self.t()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULT(self):
            return self.getToken(compilerParser.MULT, 0)

        def factor(self):
            return self.getTypedRuleContext(compilerParser.FactorContext,0)


        def t(self):
            return self.getTypedRuleContext(compilerParser.TContext,0)


        def DIV(self):
            return self.getToken(compilerParser.DIV, 0)

        def MOD(self):
            return self.getToken(compilerParser.MOD, 0)

        def getRuleIndex(self):
            return compilerParser.RULE_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT" ):
                listener.enterT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT" ):
                listener.exitT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT" ):
                return visitor.visitT(self)
            else:
                return visitor.visitChildren(self)




    def t(self):

        localctx = compilerParser.TContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_t)
        try:
            self.state = 257
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                self.match(compilerParser.MULT)
                self.state = 245
                self.factor()
                self.state = 246
                self.t()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.match(compilerParser.DIV)
                self.state = 249
                self.factor()
                self.state = 250
                self.t()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 252
                self.match(compilerParser.MOD)
                self.state = 253
                self.factor()
                self.state = 254
                self.t()
                pass
            elif token in [2, 7, 8, 10, 11, 15, 16, 17, 18, 19, 20]:
                self.enterOuterAlt(localctx, 4)

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


    class LContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MENOR(self):
            return self.getToken(compilerParser.MENOR, 0)

        def exp(self):
            return self.getTypedRuleContext(compilerParser.ExpContext,0)


        def l(self):
            return self.getTypedRuleContext(compilerParser.LContext,0)


        def MAYOR(self):
            return self.getToken(compilerParser.MAYOR, 0)

        def MENOREQ(self):
            return self.getToken(compilerParser.MENOREQ, 0)

        def MAYOREQ(self):
            return self.getToken(compilerParser.MAYOREQ, 0)

        def EQUAL(self):
            return self.getToken(compilerParser.EQUAL, 0)

        def NEQUAL(self):
            return self.getToken(compilerParser.NEQUAL, 0)

        def getRuleIndex(self):
            return compilerParser.RULE_l

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterL" ):
                listener.enterL(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitL" ):
                listener.exitL(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitL" ):
                return visitor.visitL(self)
            else:
                return visitor.visitChildren(self)




    def l(self):

        localctx = compilerParser.LContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_l)
        try:
            self.state = 284
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.match(compilerParser.MENOR)
                self.state = 260
                self.exp()
                self.state = 261
                self.l()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.match(compilerParser.MAYOR)
                self.state = 264
                self.exp()
                self.state = 265
                self.l()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 267
                self.match(compilerParser.MENOREQ)
                self.state = 268
                self.exp()
                self.state = 269
                self.l()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 271
                self.match(compilerParser.MAYOREQ)
                self.state = 272
                self.exp()
                self.state = 273
                self.l()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 5)
                self.state = 275
                self.match(compilerParser.EQUAL)
                self.state = 276
                self.exp()
                self.state = 277
                self.l()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 6)
                self.state = 279
                self.match(compilerParser.NEQUAL)
                self.state = 280
                self.exp()
                self.state = 281
                self.l()
                pass
            elif token in [2, 7, 8]:
                self.enterOuterAlt(localctx, 7)

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


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PA(self):
            return self.getToken(compilerParser.PA, 0)

        def exp(self):
            return self.getTypedRuleContext(compilerParser.ExpContext,0)


        def PC(self):
            return self.getToken(compilerParser.PC, 0)

        def NUMERO(self):
            return self.getToken(compilerParser.NUMERO, 0)

        def DECIMAL(self):
            return self.getToken(compilerParser.DECIMAL, 0)

        def call(self):
            return self.getTypedRuleContext(compilerParser.CallContext,0)


        def ID(self):
            return self.getToken(compilerParser.ID, 0)

        def getRuleIndex(self):
            return compilerParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = compilerParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_factor)
        try:
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.match(compilerParser.PA)
                self.state = 287
                self.exp()
                self.state = 288
                self.match(compilerParser.PC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.match(compilerParser.NUMERO)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 291
                self.match(compilerParser.DECIMAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 292
                self.call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 293
                self.match(compilerParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compilerParser.ID, 0)

        def PA(self):
            return self.getToken(compilerParser.PA, 0)

        def argumentos(self):
            return self.getTypedRuleContext(compilerParser.ArgumentosContext,0)


        def PC(self):
            return self.getToken(compilerParser.PC, 0)

        def getRuleIndex(self):
            return compilerParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = compilerParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(compilerParser.ID)
            self.state = 297
            self.match(compilerParser.PA)
            self.state = 298
            self.argumentos()
            self.state = 299
            self.match(compilerParser.PC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compilerParser.OpalContext)
            else:
                return self.getTypedRuleContext(compilerParser.OpalContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(compilerParser.COMA)
            else:
                return self.getToken(compilerParser.COMA, i)

        def getRuleIndex(self):
            return compilerParser.RULE_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos" ):
                listener.enterArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos" ):
                listener.exitArgumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentos" ):
                return visitor.visitArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def argumentos(self):

        localctx = compilerParser.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_argumentos)
        self._la = 0 # Token type
        try:
            self.state = 310
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 23, 24, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.opal()
                self.state = 306
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 302
                    self.match(compilerParser.COMA)
                    self.state = 303
                    self.opal()
                    self.state = 308
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)

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





