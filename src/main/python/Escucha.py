from antlr4 import TerminalNode
from antlr4 import ErrorNode
from antlr4.error.ErrorListener import ErrorListener
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

        self.errores_sintacticos = []
        self.errores_semanticos = []
        self.advertencias = []

    # ===================== GESTIÓN DE ERRORES =====================

    def reportar_error_sintactico(self, linea, columna, mensaje):
        error = f"[ERROR SINTÁCTICO] Línea {linea}, columna {columna}: {mensaje}"
        self.errores_sintacticos.append(error)
        self.hay_error_sintactico = True
        print(error)

    def reportar_error_semantico(self, linea, mensaje):
        error = f"[ERROR SEMÁNTICO] Línea {linea}: {mensaje}"
        self.errores_semanticos.append(error)
        self.hay_error_semantico = True
        print(error)

    def reportar_advertencia(self, linea, mensaje):
        advertencia = f"[ADVERTENCIA] Línea {linea}: {mensaje}"
        self.advertencias.append(advertencia)
        print(advertencia)

    def tiene_errores(self):
        return self.hay_error_sintactico or self.hay_error_semantico

    def generar_reporte(self):
        print("\n" + "=" * 60)
        print("               REPORTE DE ERRORES")
        print("=" * 60)

        if self.errores_sintacticos:
            print("\nERRORES SINTÁCTICOS:")
            for e in self.errores_sintacticos:
                print(" ", e)

        if self.errores_semanticos:
            print("\nERRORES SEMÁNTICOS:")
            for e in self.errores_semanticos:
                print(" ", e)

        if self.advertencias:
            print("\nADVERTENCIAS:")
            for a in self.advertencias:
                print(" ", a)

        print("=" * 60)

    # ===================== SINTAXIS =====================

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.reportar_error_sintactico(line, column, msg)

    # ===================== PROGRAMA =====================

    def enterPrograma(self, ctx: compilerParser.ProgramaContext):
        print("---Nuevo contexto---")

    def exitPrograma(self, ctx: compilerParser.ProgramaContext):
        print("---Contexto finalizado---")

        # Advertencias por símbolos no usados
        for i, contexto in enumerate(self.ts.contextos):
            for nombre, simbolo in contexto.simbolos.items():

                if isinstance(simbolo, Variable) and not simbolo.getUsado():
                    self.reportar_advertencia(
                        simbolo.getLinea(),
                        f"Variable '{nombre}' declarada pero no usada (Contexto {i})"
                    )

                if isinstance(simbolo, Funcion) and not simbolo.getUsado():
                    self.reportar_advertencia(
                        simbolo.getLinea(),
                        f"Función '{nombre}' declarada pero no usada (Contexto {i})"
                    )

        if self.tiene_errores():
            self.generar_reporte()
            print("\n[ERROR] Se detectaron errores. No se mostrará la tabla de símbolos.\n")
            return

        self.generar_reporte()
        print(self.ts)
        self.generar_archivo_tabla()

    def generar_archivo_tabla(self):
        try:
            with open("tabla_simbolos.txt", "w", encoding="utf-8") as f:
                f.write(str(self.ts))
            print("[INFO] Archivo 'tabla_simbolos.txt' generado correctamente.")
        except Exception as ex:
            print(f"[ERROR] No se pudo escribir el archivo de la tabla de símbolos: {ex}")

    # ===================== WHILE =====================

    def enterIwhile(self, ctx: compilerParser.IwhileContext):
        print("  " * self.indent + "WHILE ENTER")
        self.indent += 1
        self.ts.addContexto()

    def exitIwhile(self, ctx: compilerParser.IwhileContext):
        self.indent -= 1
        print("  " * self.indent + "WHILE EXIT")
        self.ts.delContexto()

    # ===================== IF =====================

    def enterIif(self, ctx: compilerParser.IifContext):
        print("  " * self.indent + "IF ENTER")
        self.indent += 1
        self.ts.addContexto()

    def exitIif(self, ctx: compilerParser.IifContext):
        self.indent -= 1
        print("  " * self.indent + "IF EXIT")
        self.ts.delContexto()

    # ===================== FOR =====================

    def enterIfor(self, ctx: compilerParser.IforContext):
        print("  " * self.indent + "FOR ENTER")
        self.indent += 1
        self.ts.addContexto()

    def exitIfor(self, ctx: compilerParser.IforContext):
        self.indent -= 1
        print("  " * self.indent + "FOR EXIT")
        self.ts.delContexto()
        # ===================== DECLARACIÓN =====================

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
                self.reportar_error_semantico(
                    ctx.start.line,
                    f"Variable '{nombre}' ya declarada en este contexto."
                )
            else:
                var = Variable(nombre, tipo)
                var.setLinea(ctx.start.line)

                if inicializado:
                    var.setInicializado(ctx.start.line)

                self.ts.addSimbolo(var)

                print(
                    f"[INFO] Declarada variable '{nombre}' "
                    f"tipo {tipo}, inicializada: {inicializado}"
                )

    # ===================== ASIGNACIÓN =====================

    def exitAsignacion(self, ctx: compilerParser.AsignacionContext):

        nombre = ctx.ID().getText()
        simbolo = self.ts.buscarSimbolo(nombre)

        if not simbolo:
            self.reportar_error_semantico(
                ctx.start.line,
                f"Variable '{nombre}' no declarada antes de su uso."
            )
            return

        hubo_error = False

        if ctx.opal():

            valor = ctx.opal().getText()
            simbolo_valor = self.ts.buscarSimbolo(valor)

            if simbolo_valor:

                if simbolo_valor.getTipoDato() != simbolo.getTipoDato():
                    self.reportar_error_semantico(
                        ctx.start.line,
                        f"Tipos incompatibles: no se puede asignar "
                        f"'{simbolo_valor.getTipoDato()}' "
                        f"a '{simbolo.getTipoDato()}'."
                    )
                    hubo_error = True

            else:

                if valor.replace('.', '', 1).isdigit():

                    if '.' in valor and simbolo.getTipoDato() != "double":
                        self.reportar_error_semantico(
                            ctx.start.line,
                            f"Tipos incompatibles: '{valor}' es double "
                            f"pero la variable '{nombre}' es "
                            f"{simbolo.getTipoDato()}."
                        )
                        hubo_error = True

                    elif '.' not in valor and simbolo.getTipoDato() != "int":
                        self.reportar_error_semantico(
                            ctx.start.line,
                            f"Tipos incompatibles: '{valor}' es int "
                            f"pero la variable '{nombre}' es "
                            f"{simbolo.getTipoDato()}."
                        )
                        hubo_error = True

                elif valor.startswith('"') and valor.endswith('"'):

                    if simbolo.getTipoDato() != "string":
                        self.reportar_error_semantico(
                            ctx.start.line,
                            f"Tipos incompatibles: '{valor}' es string "
                            f"pero la variable '{nombre}' es "
                            f"{simbolo.getTipoDato()}."
                        )
                        hubo_error = True

        if not hubo_error:
            simbolo.setInicializado(ctx.start.line)
            simbolo.setUsado()

            print(
                f"[INFO] Asignación correcta: variable '{nombre}' "
                f"marcada como usada e inicializada."
            )

    # ===================== FACTOR =====================

    def exitFactor(self, ctx: compilerParser.FactorContext):

        if ctx.ID() and not ctx.call():

            nombre = ctx.ID().getText()
            simbolo = self.ts.buscarSimbolo(nombre)

            if not simbolo:
                self.reportar_error_semantico(
                    ctx.start.line,
                    f"Variable '{nombre}' no declarada antes de su uso."
                )
                return

            if isinstance(simbolo, Funcion):
                self.reportar_error_semantico(
                    ctx.start.line,
                    f"'{nombre}' es una función, no se puede usar como variable."
                )
                return

            if not simbolo.getInicializado():
                self.reportar_error_semantico(
                    ctx.start.line,
                    f"Variable '{nombre}' usada sin inicializar."
                )

            simbolo.setUsado()

    # ===================== FUNCIÓN =====================

    def enterFuncion(self, ctx: compilerParser.FuncionContext):

        print("  " * self.indent + "FUNCION ENTER")
        self.indent += 1

        tipo = ctx.tipo().getText() if ctx.tipo() else "void"
        nombre = ctx.ID().getText()

        if self.ts.buscarSimboloContexto(nombre):

            self.reportar_error_semantico(
                ctx.start.line,
                f"Función '{nombre}' ya declarada en este contexto."
            )

        else:

            fun = Funcion(nombre, tipo, [])
            fun.setLinea(ctx.start.line)
            fun.setInicializado(ctx.start.line)

            self.ts.addSimbolo(fun)

            if ctx.bloque():
                print(f"[INFO] Función '{nombre}' tipo {tipo} definida.")
            else:
                print(f"[INFO] Prototipo de función '{nombre}' tipo {tipo} declarado.")

        self.ts.addContexto()

    def exitFuncion(self, ctx: compilerParser.FuncionContext):

        self.indent -= 1
        print("  " * self.indent + "FUNCION EXIT")
        self.ts.delContexto()

    # ===================== CALL =====================

    def exitCall(self, ctx: compilerParser.CallContext):

        nombre = ctx.ID().getText()
        simbolo = self.ts.buscarSimbolo(nombre)

        if not simbolo or not isinstance(simbolo, Funcion):

            self.reportar_error_semantico(
                ctx.start.line,
                f"Llamada a función '{nombre}' no declarada."
            )

        else:

            simbolo.setUsado()
            print(f"[INFO] Llamada correcta a función '{nombre}'.")