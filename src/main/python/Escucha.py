from antlr4 import TerminalNode
from antlr4 import ErrorNode
from compilerParser import compilerParser
from compilerListener import compilerListener
class Escucha(compilerListener):
    indent = 1
    declaracion = 0
    profundidad = 0
    numNodos = 0

    def enterPrograma(self, ctx:compilerParser.ProgramaContext):
        print("Comienza el parsing")

    def exitPrograma(self, ctx:compilerParser.ProgramaContext):
        print("Fin del parsing")

    def enterIwhile(self, ctx:compilerParser.IwhileContext):
        print("  "*self.indent + "Comienza while")
        self.indent += 1

    def exitIwhile(self, ctx:compilerParser.IwhileContext):
        self.indent -= 1
        print("  "*self.indent + "Fin while")

    def enterDeclaracion(self, ctx:compilerParser.DeclaracionContext):
        self.declaracion += 1
        print("Declaracion ENTER -> |" + ctx.getText() + "|")
        print("  -- Cant. hijos = " + str(ctx.getChildCount()))
    
    def exitDeclaracion(self, ctx:compilerParser.DeclaracionContext):
        print("Declaracion EXIT  -> |" + ctx.getText() + "|")
        print("  -- Cant. hijos = " + str(ctx.getChildCount()))
    
    def enterListavar(self, ctx:compilerParser.ListavarContext):
        self.profundidad += 1

    def exitListavar(self, ctx:compilerParser.ListavarContext):
        print("  -- ListaVar(%d) Cant. hijos  = %d" % (self.profundidad, ctx.getChildCount()))
        self.profundidad -= 1
        if ctx.getChildCount() == 4 :
            print("      hoja ID --> |%s|" % ctx.getChild(1).getText())

    # def visitTerminal(self, node: TerminalNode):
    #     print(" ---> Token: " + node.getText())
        # self.numTokens += 1
    
    def visitErrorNode(self, node: ErrorNode):
        print(" ---> ERROR")
        
    def enterEveryRule(self, ctx):
        self.numNodos += 1
    
    def __str__(self):
        return "Se hicieron " + str(self.declaracion) + " declaraciones\n" + \
                "Se visitaron " + str(self.numNodos) + " nodos"