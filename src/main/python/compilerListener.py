# Generated from d:/Users/Usuario/Documents/DHS(Calvo)/DHS2025-calvo-/src/main/python/compiler.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compilerParser import compilerParser
else:
    from compilerParser import compilerParser

# This class defines a complete listener for a parse tree produced by compilerParser.
class compilerListener(ParseTreeListener):

    # Enter a parse tree produced by compilerParser#programa.
    def enterPrograma(self, ctx:compilerParser.ProgramaContext):
        pass

    # Exit a parse tree produced by compilerParser#programa.
    def exitPrograma(self, ctx:compilerParser.ProgramaContext):
        pass


    # Enter a parse tree produced by compilerParser#instrucciones.
    def enterInstrucciones(self, ctx:compilerParser.InstruccionesContext):
        pass

    # Exit a parse tree produced by compilerParser#instrucciones.
    def exitInstrucciones(self, ctx:compilerParser.InstruccionesContext):
        pass


    # Enter a parse tree produced by compilerParser#instruccion.
    def enterInstruccion(self, ctx:compilerParser.InstruccionContext):
        pass

    # Exit a parse tree produced by compilerParser#instruccion.
    def exitInstruccion(self, ctx:compilerParser.InstruccionContext):
        pass


    # Enter a parse tree produced by compilerParser#bloque.
    def enterBloque(self, ctx:compilerParser.BloqueContext):
        pass

    # Exit a parse tree produced by compilerParser#bloque.
    def exitBloque(self, ctx:compilerParser.BloqueContext):
        pass


    # Enter a parse tree produced by compilerParser#iwhile.
    def enterIwhile(self, ctx:compilerParser.IwhileContext):
        pass

    # Exit a parse tree produced by compilerParser#iwhile.
    def exitIwhile(self, ctx:compilerParser.IwhileContext):
        pass


    # Enter a parse tree produced by compilerParser#iif.
    def enterIif(self, ctx:compilerParser.IifContext):
        pass

    # Exit a parse tree produced by compilerParser#iif.
    def exitIif(self, ctx:compilerParser.IifContext):
        pass


    # Enter a parse tree produced by compilerParser#ielse.
    def enterIelse(self, ctx:compilerParser.IelseContext):
        pass

    # Exit a parse tree produced by compilerParser#ielse.
    def exitIelse(self, ctx:compilerParser.IelseContext):
        pass


    # Enter a parse tree produced by compilerParser#ifor.
    def enterIfor(self, ctx:compilerParser.IforContext):
        pass

    # Exit a parse tree produced by compilerParser#ifor.
    def exitIfor(self, ctx:compilerParser.IforContext):
        pass


    # Enter a parse tree produced by compilerParser#asignacionFor.
    def enterAsignacionFor(self, ctx:compilerParser.AsignacionForContext):
        pass

    # Exit a parse tree produced by compilerParser#asignacionFor.
    def exitAsignacionFor(self, ctx:compilerParser.AsignacionForContext):
        pass


    # Enter a parse tree produced by compilerParser#declaracionFor.
    def enterDeclaracionFor(self, ctx:compilerParser.DeclaracionForContext):
        pass

    # Exit a parse tree produced by compilerParser#declaracionFor.
    def exitDeclaracionFor(self, ctx:compilerParser.DeclaracionForContext):
        pass


    # Enter a parse tree produced by compilerParser#declaracion.
    def enterDeclaracion(self, ctx:compilerParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by compilerParser#declaracion.
    def exitDeclaracion(self, ctx:compilerParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by compilerParser#listavar.
    def enterListavar(self, ctx:compilerParser.ListavarContext):
        pass

    # Exit a parse tree produced by compilerParser#listavar.
    def exitListavar(self, ctx:compilerParser.ListavarContext):
        pass


    # Enter a parse tree produced by compilerParser#inic.
    def enterInic(self, ctx:compilerParser.InicContext):
        pass

    # Exit a parse tree produced by compilerParser#inic.
    def exitInic(self, ctx:compilerParser.InicContext):
        pass


    # Enter a parse tree produced by compilerParser#tipo.
    def enterTipo(self, ctx:compilerParser.TipoContext):
        pass

    # Exit a parse tree produced by compilerParser#tipo.
    def exitTipo(self, ctx:compilerParser.TipoContext):
        pass


    # Enter a parse tree produced by compilerParser#asignacion.
    def enterAsignacion(self, ctx:compilerParser.AsignacionContext):
        pass

    # Exit a parse tree produced by compilerParser#asignacion.
    def exitAsignacion(self, ctx:compilerParser.AsignacionContext):
        pass


    # Enter a parse tree produced by compilerParser#opal.
    def enterOpal(self, ctx:compilerParser.OpalContext):
        pass

    # Exit a parse tree produced by compilerParser#opal.
    def exitOpal(self, ctx:compilerParser.OpalContext):
        pass


    # Enter a parse tree produced by compilerParser#exp.
    def enterExp(self, ctx:compilerParser.ExpContext):
        pass

    # Exit a parse tree produced by compilerParser#exp.
    def exitExp(self, ctx:compilerParser.ExpContext):
        pass


    # Enter a parse tree produced by compilerParser#e.
    def enterE(self, ctx:compilerParser.EContext):
        pass

    # Exit a parse tree produced by compilerParser#e.
    def exitE(self, ctx:compilerParser.EContext):
        pass


    # Enter a parse tree produced by compilerParser#term.
    def enterTerm(self, ctx:compilerParser.TermContext):
        pass

    # Exit a parse tree produced by compilerParser#term.
    def exitTerm(self, ctx:compilerParser.TermContext):
        pass


    # Enter a parse tree produced by compilerParser#t.
    def enterT(self, ctx:compilerParser.TContext):
        pass

    # Exit a parse tree produced by compilerParser#t.
    def exitT(self, ctx:compilerParser.TContext):
        pass


    # Enter a parse tree produced by compilerParser#funcion.
    def enterFuncion(self, ctx:compilerParser.FuncionContext):
        pass

    # Exit a parse tree produced by compilerParser#funcion.
    def exitFuncion(self, ctx:compilerParser.FuncionContext):
        pass


    # Enter a parse tree produced by compilerParser#parametros.
    def enterParametros(self, ctx:compilerParser.ParametrosContext):
        pass

    # Exit a parse tree produced by compilerParser#parametros.
    def exitParametros(self, ctx:compilerParser.ParametrosContext):
        pass


    # Enter a parse tree produced by compilerParser#lista_param.
    def enterLista_param(self, ctx:compilerParser.Lista_paramContext):
        pass

    # Exit a parse tree produced by compilerParser#lista_param.
    def exitLista_param(self, ctx:compilerParser.Lista_paramContext):
        pass


    # Enter a parse tree produced by compilerParser#factor.
    def enterFactor(self, ctx:compilerParser.FactorContext):
        pass

    # Exit a parse tree produced by compilerParser#factor.
    def exitFactor(self, ctx:compilerParser.FactorContext):
        pass


    # Enter a parse tree produced by compilerParser#l.
    def enterL(self, ctx:compilerParser.LContext):
        pass

    # Exit a parse tree produced by compilerParser#l.
    def exitL(self, ctx:compilerParser.LContext):
        pass


    # Enter a parse tree produced by compilerParser#returnstmt.
    def enterReturnstmt(self, ctx:compilerParser.ReturnstmtContext):
        pass

    # Exit a parse tree produced by compilerParser#returnstmt.
    def exitReturnstmt(self, ctx:compilerParser.ReturnstmtContext):
        pass



del compilerParser