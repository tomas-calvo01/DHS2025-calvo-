import sys
from antlr4 import *
from compilerLexer import compilerLexer
from compilerParser import compilerParser
from Escucha import Escucha

def main(argv):
    archivo = "input/programa.txt"
    if len(argv) > 1 :
        archivo = argv[1]
    input = FileStream(archivo)
    lexer = compilerLexer(input)
    stream = CommonTokenStream(lexer)
    parser = compilerParser(stream)
    esc =Escucha()
    parser.addParseListener(esc)
    tree = parser.programa()
    print(esc)
    #print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)