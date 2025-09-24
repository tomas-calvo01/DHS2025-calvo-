import sys
from antlr4 import *
from compiladorLexer import compiladorLexer
# from compiladorParser import compiladorParse


def main(argv):
    archivo = "input/entrada.txt"
    if len(argv) > 1 :
        archivo = argv[1]
    input = FileStream(archivo)
    lexer = compiladorLexer(input)
    stream = CommonTokenStream(lexer)
    parser = compiladorParser(stream)
    tree = parser.programa()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)