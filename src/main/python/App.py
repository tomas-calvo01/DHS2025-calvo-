import sys
from antlr4 import *
from compilerLexer import compilerLexer
from compilerParser import compilerParser
from Escucha import Escucha
from compilerVisitor import compilerVisitor
from caminante import caminante
def main(argv):
    archivo = "input/programa.txt"
    if len(argv) > 1 :
        archivo = argv[1]
    input = FileStream(archivo)
    lexer = compilerLexer(input)
    stream = CommonTokenStream(lexer)
    parser = compilerParser(stream)
    esc =Escucha()
    parser.removeErrorListeners()  
    parser.addErrorListener(esc) 
    parser.addParseListener(esc)
    tree = parser.programa()
    #visitante=caminante()
    #visitante.visitPrograma(tree)
    #print(esc)
    #print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)