from compilerVisitor import compilerVisitor
from compilerParser import compilerParser

class caminante(compilerVisitor):
    
    def visitPrograma(self, ctx: compilerParser.ProgramaContext):
        print("Programa procesado")
        return self.visitChildren(ctx)
    
    def visitDeclaracion(self, ctx: compilerParser.DeclaracionContext):
        print("Declaracion: " + ctx.getText())
        return self.visitChildren(ctx)
    
    def visitAsignacion(self, ctx: compilerParser.AsignacionContext):
        print("Asignacion: " + ctx.getText())
        return self.visitChildren(ctx)
    
    def visitIif(self, ctx: compilerParser.IifContext):
        print("If encontrado")
        return self.visitChildren(ctx)
    
    def visitIwhile(self, ctx: compilerParser.IwhileContext):
        print("While encontrado")
        return self.visitChildren(ctx)
    
    def visitIfor(self, ctx: compilerParser.IforContext):
        print("For encontrado")
        return self.visitChildren(ctx)
    
    def visitFuncion(self, ctx: compilerParser.FuncionContext):
        print("Funcion: " + ctx.ID().getText())
        return self.visitChildren(ctx)