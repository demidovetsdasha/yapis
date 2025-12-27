# python main.py output_dir\example4.txt

from antlr4 import *
from output_dir.DashSQLLexer import DashSQLLexer
from output_dir.DashSQLParser import DashSQLParser
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Trees import Trees
import sys
import os


class VerboseErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Синтаксическая ошибка: строка {line}, позиция {column}: {msg}")


def syntax_analyze(filename: str):
    input_stream = FileStream(filename)
    lexer = DashSQLLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(VerboseErrorListener())

    token_stream = CommonTokenStream(lexer)
    parser = DashSQLParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(VerboseErrorListener())

    tree = parser.program()
    return tree


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Укажите путь к файлу")
        sys.exit(1)
    filepath = sys.argv[1]
    if not os.path.isfile(filepath):
        print(f"Файл не найден: {filepath}")
        sys.exit(1)
    try:
        tree = syntax_analyze(filepath)
        print("OK")
        #print(tree.toStringTree(recog=None))
    except SyntaxError as e:
        print(f"ERROR: {e}")
