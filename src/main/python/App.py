import sys
from antlr4 import *
from compilerLexer import compilerLexer
from compilerParser import compilerParser
from Escucha import Escucha
from CodigoIntermedio import CodigoIntermedio
from optimizador import Optimizador


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

    walker = ParseTreeWalker()
    walker.walk(esc, tree)

    if not esc.tiene_errores():

        # Generar TAC
        generador = CodigoIntermedio()
        generador.visit(tree)

        # Optimizar TAC
        codigo_original = generador.codigo[:]
        opt = Optimizador(generador.codigo)
        codigo_optimizado = opt.optimizar()

        # Reporte de optimización
        opt.imprimir_reporte(codigo_original, codigo_optimizado)

        # Guardar TAC optimizado
        with open("codigo_tres_direcciones.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(codigo_optimizado))

        print("\n===== CODIGO OPTIMIZADO =====")
        print("\n".join(codigo_optimizado))

    else:
        print("\n[INFO] No se generó código intermedio debido a errores detectados.")


if __name__ == '__main__':
    main(sys.argv)