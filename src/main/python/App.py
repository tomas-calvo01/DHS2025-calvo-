import sys
from antlr4 import *
from compilerLexer import compilerLexer
from compilerParser import compilerParser
from Escucha import Escucha
from CodigoIntermedio import CodigoIntermedio


def main(argv):

    archivo = "input/programa.txt"

    if len(argv) > 1:
        archivo = argv[1]

    input_stream = FileStream(archivo, encoding="utf-8")

    lexer = compilerLexer(input_stream)
    stream = CommonTokenStream(lexer)

    parser = compilerParser(stream)

    esc = Escucha()

    parser.removeErrorListeners()
    parser.addErrorListener(esc)

    tree = parser.programa()

    # Recorrer el árbol con el listener (análisis semántico)
    walker = ParseTreeWalker()
    walker.walk(esc, tree)

    # SOLO generar código intermedio si NO hubo errores
    if not esc.tiene_errores():
        generador = CodigoIntermedio()
        generador.visit(tree)
    else:
        print("\n[INFO] No se generó código intermedio debido a errores detectados.")


if __name__ == '__main__':
    main(sys.argv)