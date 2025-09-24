# Generated from d:/Users/Usuario/Documents/DHS(Calvo)/DHS2025-calvo-/src/main/python/compiler.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .compilerParser import compilerParser
else:
    from compilerParser import compilerParser

# This class defines a complete generic visitor for a parse tree produced by compilerParser.

class compilerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compilerParser#programa.
    def visitPrograma(self, ctx:compilerParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compilerParser#instrucciones.
    def visitInstrucciones(self, ctx:compilerParser.InstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compilerParser#instruccion.
    def visitInstruccion(self, ctx:compilerParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compilerParser#bloque.
    def visitBloque(self, ctx:compilerParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compilerParser#iwhile.
    def visitIwhile(self, ctx:compilerParser.IwhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compilerParser#iif.
    def visitIif(self, ctx:compilerParser.IifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compilerParser#ielse.
    def visitIelse(self, ctx:compilerParser.IelseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compilerParser#ifor.
    def visitIfor(self, ctx:compilerParser.IforContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compilerParser#asignacionFor.
    def visitAsignacionFor(self, ctx:compilerParser.AsignacionForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compilerParser#declaracionFor.
    def visitDeclaracionFor(self, ctx:compilerParser.DeclaracionForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compilerParser#declaracion.
    def visitDeclaracion(self, ctx:compilerParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compilerParser#listavar.
    def visitListavar(self, ctx:compilerParser.ListavarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compilerParser#inic.
    def visitInic(self, ctx:compilerParser.InicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compilerParser#tipo.
    def visitTipo(self, ctx:compilerParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compilerParser#asignacion.
    def visitAsignacion(self, ctx:compilerParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compilerParser#opal.
    def visitOpal(self, ctx:compilerParser.OpalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compilerParser#exp.
    def visitExp(self, ctx:compilerParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compilerParser#e.
    def visitE(self, ctx:compilerParser.EContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compilerParser#term.
    def visitTerm(self, ctx:compilerParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compilerParser#t.
    def visitT(self, ctx:compilerParser.TContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compilerParser#funcion.
    def visitFuncion(self, ctx:compilerParser.FuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compilerParser#parametros.
    def visitParametros(self, ctx:compilerParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compilerParser#lista_param.
    def visitLista_param(self, ctx:compilerParser.Lista_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compilerParser#factor.
    def visitFactor(self, ctx:compilerParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compilerParser#l.
    def visitL(self, ctx:compilerParser.LContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compilerParser#returnstmt.
    def visitReturnstmt(self, ctx:compilerParser.ReturnstmtContext):
        return self.visitChildren(ctx)



del compilerParser