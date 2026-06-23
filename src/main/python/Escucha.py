
from antlr4 import TerminalNode
from antlr4 import ErrorNode
from antlr4.error.ErrorListener import ErrorListener
from compilerParser import compilerParser
from compilerListener import compilerListener
from TABLA import Variable, TS, Funcion
 
 
class Escucha(compilerListener, ErrorListener):
    def __init__(self):
        super().__init__()
        self.ts = TS.getInstance()
        self.indent = 1
        self.hay_error_semantico = False
        self.hay_error_sintactico = False
        self.errores_sintacticos = []
        self.errores_semanticos = []
        self.advertencias = []
        self.pila_tipos = []
        self.tipo_actual = None
    def _pop_tipo(self):
        if self.pila_tipos:
            return self.pila_tipos.pop()
        return "int"
 
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
 
    # ===================== AUXILIAR: COMBINAR TIPOS =====================
 
    def combinar_aritmetico(self, izq, der):
        if "double" in (izq, der):
            return "double"
        if "float" in (izq, der):
            return "float"
        return "int"
 
    def tipo_compatible(self, tipo_origen, tipo_destino):
        if tipo_origen == tipo_destino:
            return True
        if tipo_origen == "int" and tipo_destino in ("double", "float"):
            return True
        return False
 
    # ===================== PROGRAMA =====================
 
    def enterPrograma(self, ctx: compilerParser.ProgramaContext):
        print("---Nuevo contexto---")
 
    def exitPrograma(self, ctx: compilerParser.ProgramaContext):
        print("---Contexto finalizado---")
 
        if self.pila_tipos and not self.hay_error_sintactico:
            print(
                f"[ALERTA INTERNA] La pila de tipos no quedó vacía: {self.pila_tipos}. "
                f"Hay un push sin pop en algún exit() — revisar Escucha.py."
            )
 
        # Advertencias por símbolos no usados
        for i, contexto in enumerate(self.ts.todosLosContextos()):
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
        # La condición (opal) ya dejó su tipo en la pila al exitarse;
        # como nadie más la usa, se descarta aquí mismo.
        self._pop_tipo()
        self.indent -= 1
        print("  " * self.indent + "WHILE EXIT")
        self.ts.delContexto()
 
    # ===================== IF =====================
 
    def enterIif(self, ctx: compilerParser.IifContext):
        print("  " * self.indent + "IF ENTER")
        self.indent += 1
        self.ts.addContexto()
 
    def exitIif(self, ctx: compilerParser.IifContext):
        self._pop_tipo()  # se descarta el tipo de la condición
        self.indent -= 1
        print("  " * self.indent + "IF EXIT")
        self.ts.delContexto()
 
    # ===================== FOR =====================
 
    def enterIfor(self, ctx: compilerParser.IforContext):
        print("  " * self.indent + "FOR ENTER")
        self.indent += 1
        self.ts.addContexto()
 
    def exitIfor(self, ctx: compilerParser.IforContext):
        self._pop_tipo()  # se descarta el tipo de la condición
        self.indent -= 1
        print("  " * self.indent + "FOR EXIT")
        self.ts.delContexto()
 
    # ===================== DECLARACIÓN =====================
 
    def enterDeclaracion(self, ctx: compilerParser.DeclaracionContext):
        # Guardamos el tipo de ESTA declaración para que listavar (las
        # variables que vienen después de la coma: "int x, y, z;") lo
        # pueda usar sin tener que trepar el árbol con parentCtx.
        self.tipo_actual = ctx.tipo().getText()
 
    def exitDeclaracion(self, ctx: compilerParser.DeclaracionContext):
        tipo = ctx.tipo().getText()
        nombre = ctx.ID().getText()
 
        tiene_init = ctx.inic().getChildCount() > 0
 
        # Si hubo "= opal", su tipo ya está en la pila: SIEMPRE hay que
        # sacarlo (haya o no error de doble declaración más abajo) para
        # no desbalancear la pila para las instrucciones siguientes.
        tipo_valor = self._pop_tipo() if tiene_init else None
 
        if self.ts.buscarSimboloContexto(nombre):
            self.reportar_error_semantico(
                ctx.start.line,
                f"Variable '{nombre}' ya declarada en este contexto."
            )
            return
 
        var = Variable(nombre, tipo)
        var.setLinea(ctx.start.line)
 
        if tiene_init:
            if not self.tipo_compatible(tipo_valor, tipo):
                self.reportar_error_semantico(
                    ctx.start.line,
                    f"Tipos incompatibles: no se puede inicializar '{nombre}' "
                    f"(tipo '{tipo}') con un valor de tipo '{tipo_valor}'."
                )
            else:
                var.setInicializado(ctx.start.line)
 
        self.ts.addSimbolo(var)
        print(f"[INFO] Declarada variable '{nombre}' tipo {tipo}, inicializada: {var.getInicializado()}")
 
    # ===================== LISTAVAR =====================
 
    def exitListavar(self, ctx: compilerParser.ListavarContext):
        if ctx.getChildCount() == 0:
            return
 
        tiene_init = ctx.inic().getChildCount() > 0
        tipo_valor = self._pop_tipo() if tiene_init else None
 
        tipo = self.tipo_actual
        nombre = ctx.ID().getText()
 
        if self.ts.buscarSimboloContexto(nombre):
            self.reportar_error_semantico(
                ctx.start.line,
                f"Variable '{nombre}' ya declarada en este contexto."
            )
            return
 
        var = Variable(nombre, tipo)
        var.setLinea(ctx.start.line)
 
        if tiene_init:
            if not self.tipo_compatible(tipo_valor, tipo):
                self.reportar_error_semantico(
                    ctx.start.line,
                    f"Tipos incompatibles: no se puede inicializar '{nombre}' "
                    f"(tipo '{tipo}') con un valor de tipo '{tipo_valor}'."
                )
            else:
                var.setInicializado(ctx.start.line)
 
        self.ts.addSimbolo(var)
        print(f"[INFO] Declarada variable '{nombre}' tipo {tipo}, inicializada: {var.getInicializado()}")
 
    # ===================== ASIGNACIÓN =====================
 
    def exitAsignacion(self, ctx: compilerParser.AsignacionContext):
 
        nombre = ctx.ID().getText()
        simbolo = self.ts.buscarSimbolo(nombre)
 
        # ID ASIG opal -> hay un valor en la pila que viene de 'opal'.
        # ID++ / ID-- / ++ID / --ID -> no pasan por 'opal', no hay nada
        # que sacar de la pila.
        tipo_valor = None
        if ctx.opal() is not None:
            tipo_valor = self._pop_tipo()
 
        if not simbolo:
            self.reportar_error_semantico(
                ctx.start.line,
                f"Variable '{nombre}' no declarada antes de su uso."
            )
            return
 
        if tipo_valor is not None and not self.tipo_compatible(tipo_valor, simbolo.getTipoDato()):
            self.reportar_error_semantico(
                ctx.start.line,
                f"Tipos incompatibles: no se puede asignar "
                f"'{tipo_valor}' a '{simbolo.getTipoDato()}'."
            )
            return
 
        simbolo.setInicializado(ctx.start.line)
        simbolo.setUsado()
        print(f"[INFO] Asignación correcta: variable '{nombre}' marcada como usada e inicializada.")
 
    # ===================== EXPRESIONES: FACTOR =====================
    #
    # Esta es la pieza que el profesor señaló: antes, en exitAsignacion,
    # se llamaba a ctx.opal().getText() y se reparseaba el string a mano
    # con .replace() e isdigit(). Eso no usa el árbol de ANTLR para nada;
    # es indistinguible de tomar el código fuente y analizarlo con
    # expresiones regulares por afuera del compilador.
    #
    # Ahora cada NODO HOJA de una expresión (un número, un decimal, un
    # ID, una llamada) empuja su tipo a la pila en el momento en que se
    # lo visita. El tipo de cualquier expresión completa termina
    # disponible en la pila exactamente cuando el nodo que la contiene
    # (asignación, declaración, return, argumento...) la necesita.
 
    def exitFactor(self, ctx: compilerParser.FactorContext):
 
        if ctx.NUMERO():
            self.pila_tipos.append("int")
            return
 
        if ctx.DECIMAL():
            self.pila_tipos.append("double")
            return
 
        if ctx.call():
            # exitCall ya empujó el tipo de retorno de la función.
            # Este factor no agrega ni saca nada, solo "pasa" el valor.
            return
 
        if ctx.ID():
            nombre = ctx.ID().getText()
            simbolo = self.ts.buscarSimbolo(nombre)
 
            if not simbolo:
                self.reportar_error_semantico(
                    ctx.start.line,
                    f"Variable '{nombre}' no declarada antes de su uso."
                )
                self.pila_tipos.append("int")  # tipo "de error" para no romper la pila
                return
 
            if isinstance(simbolo, Funcion):
                self.reportar_error_semantico(
                    ctx.start.line,
                    f"'{nombre}' es una función, no se puede usar como variable."
                )
                self.pila_tipos.append("int")
                return
 
            if not simbolo.getInicializado():
                self.reportar_error_semantico(
                    ctx.start.line,
                    f"Variable '{nombre}' usada sin inicializar."
                )
 
            simbolo.setUsado()
            self.pila_tipos.append(simbolo.getTipoDato())
            return
 
        # PA opal PC   -> el tipo ya está en la pila (lo dejó 'opal')
        # RESTA factor -> el tipo ya está en la pila (lo dejó el factor interno)
        # En ambos casos no hay que tocar la pila.
 
    # ===================== EXPRESIONES: TERM / EXP (aritmética) =====
 
    def exitT(self, ctx: compilerParser.TContext):
        # t : MULT factor t | DIV factor t | MOD factor t | (vacío)
        if ctx.getChildCount() == 0:
            return
        der = self._pop_tipo()
        izq = self._pop_tipo()
        self.pila_tipos.append(self.combinar_aritmetico(izq, der))
 
    def exitE(self, ctx: compilerParser.EContext):
        # e : SUMA term e | RESTA term e | (vacío)
        if ctx.getChildCount() == 0:
            return
        der = self._pop_tipo()
        izq = self._pop_tipo()
        self.pila_tipos.append(self.combinar_aritmetico(izq, der))
 
    # term y exp no necesitan exit propio: el valor que dejan sus hijos
    # (factor+t, o term+e) ya queda como el único valor en la pila.
 
    # ===================== EXPRESIONES: RELACION / LOGICOS ==========
 
    def exitRelacion(self, ctx: compilerParser.RelacionContext):
        # relacion : exp | exp (< > <= >= == !=) exp
        if ctx.exp(1) is None:
            return  # sin comparación, el valor de "exp" ya está en la pila
 
        der = self._pop_tipo()
        izq = self._pop_tipo()
        # El resultado de comparar es booleano (en C, 0/1 como int),
        # independientemente de los tipos comparados.
        self.pila_tipos.append("int")
 
    def exitCon(self, ctx: compilerParser.ConContext):
        # con : AND relacion con | (vacío)
        if ctx.getChildCount() == 0:
            return
        der = self._pop_tipo()
        izq = self._pop_tipo()
        self.pila_tipos.append("int")
 
    def exitDis(self, ctx: compilerParser.DisContext):
        # dis : OR conjuncion dis | (vacío)
        if ctx.getChildCount() == 0:
            return
        der = self._pop_tipo()
        izq = self._pop_tipo()
        self.pila_tipos.append("int")
 
    # conjuncion, disyuncion y opal no necesitan exit propio: son pura
    # delegación, el valor que dejan sus hijos ya es el valor final.
 
    # ===================== FUNCIÓN =====================
 
    def enterFuncion(self, ctx: compilerParser.FuncionContext):
        print("  " * self.indent + "FUNCION ENTER")
        self.indent += 1
 
        tipo = ctx.tipo().getText()
        nombre = ctx.ID().getText()
 
        if self.ts.buscarSimboloContexto(nombre):
            self.reportar_error_semantico(
                ctx.start.line,
                f"Función '{nombre}' ya declarada en este contexto."
            )
        else:
            # Armar lista de parámetros ANTES de crear la Funcion
            parametros = []
            if ctx.parametros() and ctx.parametros().getChildCount() > 0:
                params = ctx.parametros()
                parametros.append((params.tipo().getText(), params.ID().getText()))
                lista = params.lista_param()
                while lista and lista.getChildCount() > 0:
                    parametros.append((lista.tipo().getText(), lista.ID().getText()))
                    lista = lista.lista_param()
 
            # Crear la función con los parámetros reales
            fun = Funcion(nombre, tipo, parametros)
            fun.setLinea(ctx.start.line)
            fun.setInicializado(ctx.start.line)
            self.ts.addSimbolo(fun)
            print(f"[INFO] Función '{nombre}' tipo {tipo} definida con {len(parametros)} parámetro(s).")
 
        # Abrir scope hijo para el cuerpo de la función
        self.ts.addContexto()
 
        # Registrar parámetros en el scope hijo como variables
        if ctx.parametros() and ctx.parametros().getChildCount() > 0:
            params = ctx.parametros()
            tipo_param = params.tipo().getText()
            nombre_param = params.ID().getText()
            var = Variable(nombre_param, tipo_param)
            var.setLinea(ctx.start.line)
            var.setInicializado(ctx.start.line)
            self.ts.addSimbolo(var)
            print(f"[INFO] Parámetro '{nombre_param}' tipo {tipo_param} registrado.")
 
            lista = params.lista_param()
            while lista and lista.getChildCount() > 0:
                tipo_param = lista.tipo().getText()
                nombre_param = lista.ID().getText()
                var = Variable(nombre_param, tipo_param)
                var.setLinea(ctx.start.line)
                var.setInicializado(ctx.start.line)
                self.ts.addSimbolo(var)
                print(f"[INFO] Parámetro '{nombre_param}' tipo {tipo_param} registrado.")
                lista = lista.lista_param()
 
    def exitFuncion(self, ctx: compilerParser.FuncionContext):
        self.indent -= 1
        nombre = ctx.ID().getText() if ctx.ID() else "?"
        tipo = ctx.tipo().getText() if ctx.tipo() else "void"
        print("  " * self.indent + f"FUNCION EXIT: {nombre}() -> {tipo}")
        self.ts.delContexto()
 
    # ===================== RETURN =====================
 
    def exitReturnstmt(self, ctx: compilerParser.ReturnstmtContext):
        # return opal ;  -> hay un valor en la pila, se descarta acá
        # return ;       -> no hay nada que sacar
        if ctx.opal() is not None:
            self._pop_tipo()
 
    # ===================== LLAMADA COMO INSTRUCCIÓN =====================
 
    def exitLlamada(self, ctx: compilerParser.LlamadaContext):
        # 'call' ya empujó el tipo de retorno. Como acá se usa como
        # instrucción suelta (sin asignar el resultado a nada), hay que
        # descartarlo para no dejar la pila desbalanceada.
        self._pop_tipo()
 
    # ===================== CALL =====================
 
    def exitCall(self, ctx: compilerParser.CallContext):
        nombre = ctx.ID().getText()
        simbolo = self.ts.buscarSimbolo(nombre)
 
        n_args = 0
        if ctx.argumentos() is not None:
            n_args = len(ctx.argumentos().opal())
 
        # Cada argumento (cada 'opal' de argumentos) ya dejó su tipo en
        # la pila, en orden. Los sacamos todos (síempre, haya o no
        # error) y los volvemos a poner en el orden original.
        tipos_args = [self._pop_tipo() for _ in range(n_args)]
        tipos_args.reverse()
 
        if not simbolo or not isinstance(simbolo, Funcion):
            self.reportar_error_semantico(
                ctx.start.line,
                f"Llamada a función '{nombre}' no declarada."
            )
            self.pila_tipos.append("int")  # valor de error, para no desbalancear la pila
            return
 
        simbolo.setUsado()
        params_esperados = simbolo.getListaArgs()
 
        if len(tipos_args) != len(params_esperados):
            self.reportar_error_semantico(
                ctx.start.line,
                f"Función '{nombre}' espera {len(params_esperados)} argumento(s) "
                f"pero se pasaron {len(tipos_args)}."
            )
        else:
            for i, (tipo_arg, (tipo_esperado, nombre_param)) in enumerate(zip(tipos_args, params_esperados)):
                if not self.tipo_compatible(tipo_arg, tipo_esperado):
                    self.reportar_error_semantico(
                        ctx.start.line,
                        f"Argumento {i+1} de '{nombre}': se esperaba '{tipo_esperado}' "
                        f"pero se pasó '{tipo_arg}'."
                    )
 
        # El resultado de la llamada es el tipo de retorno de la función;
        # queda en la pila para quien lo use (un factor, una asignación...).
        self.pila_tipos.append(simbolo.getTipoDato())
        print(f"[INFO] Llamada a función '{nombre}' procesada.")
 
    # ===================== FOR INIT =====================
 
    def enterForInit(self, ctx: compilerParser.ForInitContext):
        # Igual que enterDeclaracion: si esta forma de forInit es una
        # declaración ("int i = 0, j = 0"), guardamos el tipo ANTES de
        # bajar a listaVarFor, que lo va a necesitar en su propio exit.
        if ctx.tipo():
            self.tipo_actual = ctx.tipo().getText()
 
    def exitForInit(self, ctx: compilerParser.ForInitContext):
        # Si es declaración (int j = 0): mismo tratamiento que exitDeclaracion
        if ctx.tipo():
            tipo = ctx.tipo().getText()
            nombre = ctx.ID().getText()
 
            tiene_init = ctx.inic().getChildCount() > 0
            tipo_valor = self._pop_tipo() if tiene_init else None
 
            if self.ts.buscarSimboloContexto(nombre):
                self.reportar_error_semantico(
                    ctx.start.line,
                    f"Variable '{nombre}' ya declarada en este contexto."
                )
                return
 
            var = Variable(nombre, tipo)
            var.setLinea(ctx.start.line)
 
            if tiene_init:
                if not self.tipo_compatible(tipo_valor, tipo):
                    self.reportar_error_semantico(
                        ctx.start.line,
                        f"Tipos incompatibles: no se puede inicializar '{nombre}' "
                        f"(tipo '{tipo}') con un valor de tipo '{tipo_valor}'."
                    )
                else:
                    var.setInicializado(ctx.start.line)
 
            self.ts.addSimbolo(var)
            print(f"[INFO] Declarada variable '{nombre}' tipo {tipo} en for, inicializada: {var.getInicializado()}")
 
        # Si es 'listaAsignacionFor' (for (i=0; ...)), cada asignacionFor
        # ya se valida sola en exitAsignacionFor; no hace falta nada más aquí.
 
    # ===================== LISTA VAR FOR =====================
 
    def exitListaVarFor(self, ctx: compilerParser.ListaVarForContext):
        # COMA ID inic listaVarFor | (vacío)
        if ctx.getChildCount() == 0:
            return
 
        tiene_init = ctx.inic().getChildCount() > 0
        tipo_valor = self._pop_tipo() if tiene_init else None
 
        tipo = self.tipo_actual
        nombre = ctx.ID().getText()
 
        if self.ts.buscarSimboloContexto(nombre):
            self.reportar_error_semantico(
                ctx.start.line,
                f"Variable '{nombre}' ya declarada en este contexto."
            )
            return
 
        var = Variable(nombre, tipo)
        var.setLinea(ctx.start.line)
 
        if tiene_init:
            if not self.tipo_compatible(tipo_valor, tipo):
                self.reportar_error_semantico(
                    ctx.start.line,
                    f"Tipos incompatibles: no se puede inicializar '{nombre}' "
                    f"(tipo '{tipo}') con un valor de tipo '{tipo_valor}'."
                )
            else:
                var.setInicializado(ctx.start.line)
 
        self.ts.addSimbolo(var)
        print(f"[INFO] Declarada variable '{nombre}' tipo {tipo} en for, inicializada: {var.getInicializado()}")
 
    # ===================== ASIGNACION FOR (incremento del for) ======
 
    def exitAsignacionFor(self, ctx: compilerParser.AsignacionForContext):
        # ID ASIG opal   -> hay valor en la pila, validar y sacar
        # ID++ / ID-- / ++ID / --ID -> no pasan por opal, nada que sacar
        if ctx.opal() is None:
            return
 
        nombre = ctx.ID().getText()
        simbolo = self.ts.buscarSimbolo(nombre)
        tipo_valor = self._pop_tipo()
 
        if not simbolo:
            self.reportar_error_semantico(
                ctx.start.line,
                f"Variable '{nombre}' no declarada antes de su uso."
            )
            return
 
        if not self.tipo_compatible(tipo_valor, simbolo.getTipoDato()):
            self.reportar_error_semantico(
                ctx.start.line,
                f"Tipos incompatibles en el for: no se puede asignar "
                f"'{tipo_valor}' a '{simbolo.getTipoDato()}'."
            )
            return
 
        simbolo.setInicializado(ctx.start.line)
        simbolo.setUsado()