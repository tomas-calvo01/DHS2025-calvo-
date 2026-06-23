class ID:
    def __init__(self, nombre, tipoDato):
        self.nombre = nombre
        self.tipoDato = tipoDato
        self.inicializado = False
        self.usado = False
        self.linea = 0

    def getNombre(self):
        return self.nombre

    def getTipoDato(self):
        return self.tipoDato

    def setInicializado(self, linea=0):
        self.inicializado = True
        if linea > 0:
            self.linea = linea

    def getInicializado(self):
        return self.inicializado

    def setUsado(self):
        self.usado = True

    def getUsado(self):
        return self.usado

    def getLinea(self):
        return self.linea

    def setLinea(self, linea):
        self.linea = linea


class Variable(ID):
    def __init__(self, nombre, tipoDato):
        super().__init__(nombre, tipoDato)


class Funcion(ID):
    def __init__(self, nombre, tipoDato, args=None):
        super().__init__(nombre, tipoDato)
        self.args = args if args else []
        self.tiene_cuerpo = False        

    def getListaArgs(self):
        return self.args

    def setTieneCuerpo(self):          
        self.tiene_cuerpo = True

    def getTieneCuerpo(self):            
        return self.tiene_cuerpo


class Contexto:
    def __init__(self):
        self.simbolos = {}

    def addSimbolo(self, id):
        self.simbolos[id.getNombre()] = id

    def buscarSimbolo(self, nombre):
        return self.simbolos.get(nombre, None)

    def __str__(self):
        if not self.simbolos:
            return "  (vacío)\n"
        return "".join([f"  {nombre}: {sim.tipoDato}\n" for nombre, sim in self.simbolos.items()])


class TS:
    _instancia = None

    def __init__(self):
        self.contextos = [Contexto()]
        self.contextos_cerrados = []

    @staticmethod
    def getInstance():
        if TS._instancia is None:
            TS._instancia = TS()
        return TS._instancia

    def addContexto(self):
        self.contextos.append(Contexto())

    def delContexto(self):
        if len(self.contextos) > 1:
            contexto = self.contextos.pop()
            self.contextos_cerrados.append(contexto)
    def todosLosContextos(self):
       return self.contextos + self.contextos_cerrados

    def addSimbolo(self, id):
        # Verifica si ya existe en el contexto ACTUAL -> doble declaración
        if id.getNombre() in self.contextos[-1].simbolos:
            return False
        self.contextos[-1].addSimbolo(id)
        return True

    def buscarSimbolo(self, nombre):
        for contexto in reversed(self.contextos):
            simbolo = contexto.buscarSimbolo(nombre)
            if simbolo:
                return simbolo
        return None

    def buscarSimboloContexto(self, nombre):
        return self.contextos[-1].buscarSimbolo(nombre)

    def __str__(self):
        resultado = "\nTabla de Simbolos:\n"
        for i, contexto in enumerate(self.todosLosContextos()):
            resultado += f"--- Contexto {i} ---\n"
            resultado += str(contexto)
        return resultado