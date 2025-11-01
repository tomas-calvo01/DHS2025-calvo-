from compilerVisitor import compilerVisitor
from compilerParser import compilerParser
class caminante(compilerVisitor):
    def visitPrograma(self, ctx:compilerParser.ProgramaContext):
        print("programa procesando")
        return (ctx)
    
    
