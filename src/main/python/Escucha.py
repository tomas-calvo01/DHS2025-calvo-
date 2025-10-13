from antlr4 import TerminalNode
from antlr4 import ErrorNode
from compilerParser import compilerParser
from compilerListener import compilerListener
from TABLA import Variable,Funcion,TS

class Escucha(compilerListener):
    def __init__(self):
        super().__init__()
        self.ts = TS.getInstance()
        self.indent = 1
        self.declaracion = 0
        self.profundidad = 0
        self.numNodos = 0

    def enterPrograma(self, ctx:compilerParser.ProgramaContext):
        print("Nuevo contexto")

    def exitPrograma(self, ctx:compilerParser.ProgramaContext):
        print("Contexto finalizado")
    
    def exitDeclaracion(self, ctx:compilerParser.DeclaracionContext): 
        tipo = ctx.tipo().getText()
        texto = ctx.getText()
        declaracion = texto.replace(tipo, '').replace(';', '').strip()
        partes = [p.strip() for p in declaracion.split(',')]
        for parte in partes:
            if '=' in parte:
                nombre, valor = [x.strip() for x in parte.split('=')]
                inicializado = True
            else:
                nombre = parte
                inicializado = False
            if self.ts.buscarSimboloContexto(nombre):
                print(f"Error: variable '{nombre}' ya declarada en este contexto.")
            else:
                var = Variable(nombre, tipo)
                var.setInicializado(inicializado)
                self.ts.addSimbolo(var)
                print(f"Declarada variable '{nombre}' tipo {tipo}, inicializada: {inicializado}")

    def exitAsignacion(self, ctx:compilerParser.AsignacionContext):
        nombre = ctx.ID().getText()
        simbolo = self.ts.buscarSimbolo(nombre)
        if simbolo:
            simbolo.setInicializado()
            simbolo.setUsado()
            print(f"Asignación: variable '{nombre}' marcada como usada e inicializada.")
        else:
            print(f"Error: variable '{nombre}' no definida.")


    def exitFactor(self, ctx:compilerParser.FactorContext):
        if ctx.ID():
            nombre = ctx.ID().getText()
            simbolo = self.ts.buscarSimbolo(nombre)
            if simbolo:
                simbolo.setUsado()
                print(f"Uso: variable '{nombre}' marcada como usada.")
            else:
                print(f"Error: variable '{nombre}' no definida.")

   



