from antlr4 import TerminalNode
from antlr4 import ErrorNode
from compilerParser import compilerParser
from compilerListener import compilerListener
from TABLA import Variable, TS, Funcion

class Escucha(compilerListener):
    def __init__(self):
        super().__init__()
        self.ts = TS.getInstance()
        self.indent = 1
        self.declaracion = 0
        self.profundidad = 0
        self.numNodos = 0
        self.hay_error_semantico = False  
        self.hay_error_sintactico = False  

    def enterPrograma(self, ctx: compilerParser.ProgramaContext):
        print("---Nuevo contexto---")

    def exitPrograma(self, ctx: compilerParser.ProgramaContext):
        ts = TS.getInstance()
        print("---Contexto finalizado---")

       
        if self.hay_error_sintactico:
            print("\n[ERROR] Se detectaron errores sintácticos. No se mostrará la tabla de símbolos.\n")
            return

        if self.hay_error_semantico:
            print("\n[ERROR] Se detectaron errores semánticos. No se mostrará la tabla de símbolos.\n")
            return

   
        print(ts)
        for i, contexto in enumerate(ts.contextos):
            for nombre, simbolo in contexto.simbolos.items():
                if isinstance(simbolo, Variable) and not simbolo.getUsado():
                    print(f"[ADVERTENCIA] Variable '{nombre}' declarada pero no usada (Contexto {i}).")
                if isinstance(simbolo, Funcion) and not simbolo.getUsado():
                    print(f"[ADVERTENCIA] Función '{nombre}' declarada pero no usada (Contexto {i}).")

  
    def exitDeclaracion(self, ctx: compilerParser.DeclaracionContext):
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
                print(f"[ERROR SEMÁNTICO] Variable '{nombre}' ya declarada en este contexto.")
                self.hay_error_semantico = True
            else:
                var = Variable(nombre, tipo)
                var.setInicializado(inicializado)
                self.ts.addSimbolo(var)
                print(f"[INFO] Declarada variable '{nombre}' tipo {tipo}, inicializada: {inicializado}")

    
    def exitAsignacion(self, ctx: compilerParser.AsignacionContext):
        nombre = ctx.ID().getText()
        simbolo = self.ts.buscarSimbolo(nombre)

        if not simbolo:
            print(f"[ERROR SEMÁNTICO] Variable '{nombre}' no declarada antes de su uso.")
            self.hay_error_semantico = True
            return

        hubo_error = False

        if ctx.opal():
            valor = ctx.opal().getText()
            simbolo_valor = self.ts.buscarSimbolo(valor)

            if simbolo_valor:
                if simbolo_valor.getTipoDato() != simbolo.getTipoDato():
                    print(f"[ERROR SEMÁNTICO] Tipos incompatibles: no se puede asignar '{simbolo_valor.getTipoDato()}' a '{simbolo.getTipoDato()}'.")
                    self.hay_error_semantico = True
                    hubo_error = True
            else:
                if valor.replace('.', '', 1).isdigit():
                    if '.' in valor and simbolo.getTipoDato() != "double":
                        print(f"[ERROR SEMÁNTICO] Tipos incompatibles: '{valor}' es double pero la variable '{nombre}' es {simbolo.getTipoDato()}.")
                        self.hay_error_semantico = True
                        hubo_error = True
                    elif '.' not in valor and simbolo.getTipoDato() != "int":
                        print(f"[ERROR SEMÁNTICO] Tipos incompatibles: '{valor}' es int pero la variable '{nombre}' es {simbolo.getTipoDato()}.")
                        self.hay_error_semantico = True
                        hubo_error = True
                elif valor.startswith('"') and valor.endswith('"'):
                    if simbolo.getTipoDato() != "string":
                        print(f"[ERROR SEMÁNTICO] Tipos incompatibles: '{valor}' es string pero la variable '{nombre}' es {simbolo.getTipoDato()}.")
                        self.hay_error_semantico = True
                        hubo_error = True

        if not hubo_error:
            simbolo.setInicializado()
            simbolo.setUsado()
            print(f"[INFO] Asignación correcta: variable '{nombre}' marcada como usada e inicializada.")

  
    def exitFactor(self, ctx: compilerParser.FactorContext):
        if ctx.ID():
            nombre = ctx.ID().getText()
            simbolo = self.ts.buscarSimbolo(nombre)

            if not simbolo:
                print(f"[ERROR SEMÁNTICO] Variable '{nombre}' no declarada antes de su uso.")
                self.hay_error_semantico = True
                return

            if not simbolo.getInicializado():
                print(f"[ERROR SEMÁNTICO] Variable '{nombre}' usada sin inicializar.")
                self.hay_error_semantico = True

            simbolo.setUsado()

   
    def exitFuncion(self, ctx: compilerParser.FuncionContext):
        tipo = ctx.tipo().getText() if ctx.tipo() else "void"
        nombre = ctx.ID().getText()

        if self.ts.buscarSimboloContexto(nombre):
            print(f"[ERROR SEMÁNTICO] Función '{nombre}' ya declarada en este contexto.")
            self.hay_error_semantico = True
        else:
            fun = Funcion(nombre, tipo, [])
            self.ts.addSimbolo(fun)

            if ctx.bloque():
                print(f"[INFO] Función '{nombre}' tipo {tipo} definida.")
            else:
                print(f"[INFO] Prototipo de función '{nombre}' tipo {tipo} declarado.")

 
    def exitCall(self, ctx: compilerParser.CallContext):
        nombre = ctx.ID().getText()
        simbolo = self.ts.buscarSimbolo(nombre)

        if not simbolo or not isinstance(simbolo, Funcion):
            print(f"[ERROR SEMÁNTICO] Llamada a función '{nombre}' no declarada.")
            self.hay_error_semantico = True
        else:
            simbolo.setUsado()
            print(f"[INFO] Llamada correcta a función '{nombre}'.")

    def visitErrorNode(self, node: ErrorNode):
        token = node.getSymbol()
        linea = token.line
        columna = token.column
        text = node.getText()
        if text == ';':
            print(f"[ERROR SINTÁCTICO] Falta de punto y coma en línea {linea}, columna {columna}")
        else: 
            if text == '(':
                print(f"[ERROR SINTÁCTICO] Falta de apertura de paréntesis en línea {linea}, columna {columna}")
           
        self.hay_error_sintactico = True