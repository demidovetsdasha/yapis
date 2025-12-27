# main_semantic.py

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from output_dir.DashSQLLexer import DashSQLLexer
from output_dir.DashSQLParser import DashSQLParser
from semantic_analyzer import analyze_semantics
import sys
import os

class MyErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []
    
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"line {line}:{column} {msg}")
    
    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass
    
    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass
    
    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass

def semantic_analyze(filename: str):
    try:
        input_stream = FileStream(filename, encoding='utf-8')
    except:
        try:
            input_stream = FileStream(filename, encoding='cp1251')
        except:
            try:
                input_stream = FileStream(filename, encoding='latin-1')
            except:
                print(f"Ошибка чтения файла: {filename}")
                return None
    
    lexer = DashSQLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = DashSQLParser(token_stream)
    
    error_listener = MyErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    
    tree = parser.program()
    
    if error_listener.errors:
        for error in error_listener.errors:
            print(error)
        return None
    
    errors = analyze_semantics(tree)
    
    return errors

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Укажите путь к файлу")
        sys.exit(1)
    
    filepath = sys.argv[1]
    if not os.path.isfile(filepath):
        print(f"Файл не найден: {filepath}")
        sys.exit(1)
    
    try:
        errors = semantic_analyze(filepath)
        
        if errors is None:
            sys.exit(1)
        
        if errors:
            print("Найдены семантические ошибки:")
            for error in errors:
                print(f"  • {error}")
            sys.exit(1)
        else:
            print("Семантических ошибок не найдено.")
            print("OK")
            
    except Exception as e:
        print(f"Ошибка при анализе: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)