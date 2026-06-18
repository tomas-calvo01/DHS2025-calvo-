from compilerVisitor import compilerVisitor
from compilerParser import compilerParser


class CodigoIntermedio(compilerVisitor):

    def __init__(self):
        self.codigo = []
        self.temp_counter = 0
        self.label_counter = 0

    # ==========================================
    # AUXILIARES
    # ==========================================

    def nuevoTemp(self):
        temp = f"t{self.temp_counter}"
        self.temp_counter += 1
        return temp

    def nuevaEtiqueta(self):
        label = f"L{self.label_counter}"
        self.label_counter += 1
        return label

    def emitir(self, instruccion):
        self.codigo.append(instruccion)

    def obtenerCodigo(self):
        return "\n".join(self.codigo)

    # ==========================================
    # PROGRAMA
    # ==========================================

    def visitPrograma(self, ctx: compilerParser.ProgramaContext):

        self.visitChildren(ctx)

        codigo = self.obtenerCodigo()

        with open("codigo_tres_direcciones.txt", "w", encoding="utf-8") as archivo:
            archivo.write(codigo)

        print("\n===== CODIGO DE TRES DIRECCIONES =====")
        print(codigo)

        return None

    # ==========================================
    # OPAL
    # ==========================================

    def visitOpal(self, ctx: compilerParser.OpalContext):
        return self.visit(ctx.relacion())

    # ==========================================
    # RELACION
    # ==========================================

    def visitRelacion(self, ctx: compilerParser.RelacionContext):

        izquierda = self.visit(ctx.exp())

        if ctx.l():
            return self.visitL_aux(ctx.l(), izquierda)

        return izquierda

    def visitL_aux(self, ctx, izquierda):

        if ctx.getChildCount() == 0:
            return izquierda

        operador = ctx.getChild(0).getText()

        derecha = self.visit(ctx.exp())

        temp = self.nuevoTemp()

        self.emitir(f"{temp} = {izquierda} {operador} {derecha}")

        if ctx.l():
            return self.visitL_aux(ctx.l(), temp)

        return temp

    # ==========================================
    # EXP
    # ==========================================

    def visitExp(self, ctx: compilerParser.ExpContext):

        izquierda = self.visit(ctx.term())

        if ctx.e():
            return self.visitE_aux(ctx.e(), izquierda)

        return izquierda

    def visitE_aux(self, ctx, izquierda):

        if ctx.getChildCount() == 0:
            return izquierda

        operador = ctx.getChild(0).getText()

        derecha = self.visit(ctx.term())

        temp = self.nuevoTemp()

        self.emitir(f"{temp} = {izquierda} {operador} {derecha}")

        if ctx.e():
            return self.visitE_aux(ctx.e(), temp)

        return temp

    # ==========================================
    # TERM
    # ==========================================

    def visitTerm(self, ctx: compilerParser.TermContext):

        izquierda = self.visit(ctx.factor())

        if ctx.t():
            return self.visitT_aux(ctx.t(), izquierda)

        return izquierda

    def visitT_aux(self, ctx, izquierda):

        if ctx.getChildCount() == 0:
            return izquierda

        operador = ctx.getChild(0).getText()

        derecha = self.visit(ctx.factor())

        temp = self.nuevoTemp()

        self.emitir(f"{temp} = {izquierda} {operador} {derecha}")

        if ctx.t():
            return self.visitT_aux(ctx.t(), temp)

        return temp

    # ==========================================
    # FACTOR
    # ==========================================

    def visitFactor(self, ctx: compilerParser.FactorContext):

        if ctx.NUMERO():
            return ctx.NUMERO().getText()

        if ctx.DECIMAL():
            return ctx.DECIMAL().getText()

        if ctx.ID():
            return ctx.ID().getText()

        if ctx.call():
            return self.visit(ctx.call())

        if ctx.exp():
            return self.visit(ctx.exp())

        return None

    # ==========================================
    # LLAMADA A FUNCION
    # ==========================================

    def visitCall(self, ctx: compilerParser.CallContext):

        nombre = ctx.ID().getText()

        if ctx.argumentos():
            self.visit(ctx.argumentos())

        temp = self.nuevoTemp()

        self.emitir(f"{temp} = call {nombre}")

        return temp

    # ==========================================
    # ARGUMENTOS
    # ==========================================

    def visitArgumentos(self, ctx: compilerParser.ArgumentosContext):

        args = []

        for child in ctx.getChildren():

            if isinstance(child, compilerParser.OpalContext):

                valor = self.visit(child)

                args.append(valor)

                self.emitir(f"param {valor}")

        return args
        # ==========================================
    # DECLARACION
    # ==========================================

    def visitDeclaracion(self, ctx: compilerParser.DeclaracionContext):

        variable = ctx.ID().getText()

        if ctx.inic().getChildCount() > 0:
            valor = self.visit(ctx.inic().opal())
            self.emitir(f"{variable} = {valor}")
        else:
            self.emitir(f"DECLARE {variable}")

        if ctx.listavar():
            self.visit(ctx.listavar())

        return None


    # ==========================================
    # LISTAVAR
    # ==========================================

    def visitListavar(self, ctx: compilerParser.ListavarContext):

        if ctx.getChildCount() == 0:
            return None

        variable = ctx.ID().getText()

        if ctx.inic().getChildCount() > 0:
            valor = self.visit(ctx.inic().opal())
            self.emitir(f"{variable} = {valor}")
        else:
            self.emitir(f"DECLARE {variable}")

        if ctx.listavar():
            self.visit(ctx.listavar())

        return None


    # ==========================================
    # ASIGNACION
    # ==========================================

    def visitAsignacion(self, ctx: compilerParser.AsignacionContext):

        primer_hijo = ctx.getChild(0).getText()

        # ++i
        if primer_hijo == "++":

            variable = ctx.ID().getText()

            temp = self.nuevoTemp()

            self.emitir(f"{temp} = {variable} + 1")
            self.emitir(f"{variable} = {temp}")

        # --i
        elif primer_hijo == "--":

            variable = ctx.ID().getText()

            temp = self.nuevoTemp()

            self.emitir(f"{temp} = {variable} - 1")
            self.emitir(f"{variable} = {temp}")

        # i++
        elif ctx.INCREMENTO():

            variable = ctx.ID().getText()

            temp = self.nuevoTemp()

            self.emitir(f"{temp} = {variable} + 1")
            self.emitir(f"{variable} = {temp}")

        # i--
        elif ctx.DECREMENTO():

            variable = ctx.ID().getText()

            temp = self.nuevoTemp()

            self.emitir(f"{temp} = {variable} - 1")
            self.emitir(f"{variable} = {temp}")

        # x = expresión
        else:

            variable = ctx.ID().getText()

            valor = self.visit(ctx.opal())

            self.emitir(f"{variable} = {valor}")

        return None
        # ==========================================
    # IF
    # ==========================================

    def visitIif(self, ctx: compilerParser.IifContext):

        etiqueta_else = self.nuevaEtiqueta()
        etiqueta_fin = self.nuevaEtiqueta()

        condicion = self.visit(ctx.opal())

        # ¿Existe else?
        tiene_else = ctx.ielse() and ctx.ielse().getChildCount() > 0

        if tiene_else:

            self.emitir(f"if not {condicion} goto {etiqueta_else}")

            # instrucción del IF
            self.visit(ctx.instruccion())

            self.emitir(f"goto {etiqueta_fin}")

            self.emitir(f"{etiqueta_else}:")

            self.visit(ctx.ielse())

            self.emitir(f"{etiqueta_fin}:")

        else:

            self.emitir(f"if not {condicion} goto {etiqueta_fin}")

            self.visit(ctx.instruccion())

            self.emitir(f"{etiqueta_fin}:")

        return None


    # ==========================================
    # ELSE
    # ==========================================

    def visitIelse(self, ctx: compilerParser.IelseContext):

        if ctx.getChildCount() > 0:
            return self.visit(ctx.instruccion())

        return None


    # ==========================================
    # WHILE
    # ==========================================

    def visitIwhile(self, ctx: compilerParser.IwhileContext):

        inicio = self.nuevaEtiqueta()
        fin = self.nuevaEtiqueta()

        self.emitir(f"{inicio}:")

        condicion = self.visit(ctx.opal())

        self.emitir(f"if not {condicion} goto {fin}")

        self.visit(ctx.instruccion())

        self.emitir(f"goto {inicio}")

        self.emitir(f"{fin}:")

        return None

    # ==========================================
    # BLOQUE
    # ==========================================

    def visitBloque(self, ctx: compilerParser.BloqueContext):

        return self.visitChildren(ctx)
    # ==========================================
    # RETURN
    # ==========================================

    def visitReturnstmt(self, ctx: compilerParser.ReturnstmtContext):

        valor = self.visit(ctx.opal())

        self.emitir(f"return {valor}")

        return None
    # ==========================================
    # FUNCION
    # ==========================================

    def visitFuncion(self, ctx: compilerParser.FuncionContext):
        nombre = ctx.ID().getText()
        self.emitir(f"FUNC {nombre}:")

        # Emitir pop por cada parámetro
        if ctx.parametros() and ctx.parametros().getChildCount() > 0:
            params = ctx.parametros()
            # El primero
            self.emitir(f"pop {params.ID().getText()}")
            # El resto via lista_param
            lista = params.lista_param()
            while lista and lista.getChildCount() > 0:
                self.emitir(f"pop {lista.ID().getText()}")
                lista = lista.lista_param()

        self.visit(ctx.bloque())
        self.emitir(f"END FUNC {nombre}")
        return None
    # ==========================================
    # FOR
    # ==========================================

    def visitIfor(self, ctx: compilerParser.IforContext):

        inicio = self.nuevaEtiqueta()
        fin = self.nuevaEtiqueta()

        # inicialización
        self.visit(ctx.forInit())

        self.emitir(f"{inicio}:")

        # condición
        condicion = self.visit(ctx.opal())

        self.emitir(f"if not {condicion} goto {fin}")

        # cuerpo del for
        self.visit(ctx.bloque())

        # incremento
        self.visit(ctx.asignacionFor())

        self.emitir(f"goto {inicio}")

        self.emitir(f"{fin}:")

        return None
    # ==========================================
    # FORINIT
    # ==========================================

    def visitForInit(self, ctx: compilerParser.ForInitContext):

        self.visitChildren(ctx)

        return None
    # ==========================================
    # ASIGNACION FOR
    # ==========================================

    def visitAsignacionFor(self, ctx: compilerParser.AsignacionForContext):

        primer_hijo = ctx.getChild(0).getText()

        # ++i
        if primer_hijo == "++":

            variable = ctx.ID().getText()

            temp = self.nuevoTemp()

            self.emitir(f"{temp} = {variable} + 1")
            self.emitir(f"{variable} = {temp}")

        # --i
        elif primer_hijo == "--":

            variable = ctx.ID().getText()

            temp = self.nuevoTemp()

            self.emitir(f"{temp} = {variable} - 1")
            self.emitir(f"{variable} = {temp}")

        # i++
        elif ctx.INCREMENTO():

            variable = ctx.ID().getText()

            temp = self.nuevoTemp()

            self.emitir(f"{temp} = {variable} + 1")
            self.emitir(f"{variable} = {temp}")

        # i--
        elif ctx.DECREMENTO():

            variable = ctx.ID().getText()

            temp = self.nuevoTemp()

            self.emitir(f"{temp} = {variable} - 1")
            self.emitir(f"{variable} = {temp}")

        # i = expresion
        else:

            variable = ctx.ID().getText()

            valor = self.visit(ctx.opal())

            self.emitir(f"{variable} = {valor}")

        return None
    # ==========================================
    # LISTA ASIGNACION FOR
    # ==========================================

    def visitListaAsignacionFor(self, ctx: compilerParser.ListaAsignacionForContext):

        for asignacion in ctx.asignacionFor():

            self.visit(asignacion)

        return None
    # ==========================================
    # LISTA VAR FOR
    # ==========================================

    def visitListaVarFor(self, ctx: compilerParser.ListaVarForContext):

        if ctx.getChildCount() == 0:
            return None

        variable = ctx.ID().getText()

        if ctx.inic().getChildCount() > 0:

            valor = self.visit(ctx.inic().opal())

            self.emitir(f"{variable} = {valor}")

        else:

            self.emitir(f"DECLARE {variable}")

        if ctx.listaVarFor():

            self.visit(ctx.listaVarFor())

        return None
