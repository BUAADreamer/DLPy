from io import StringIO
from dlpy.lexer import Lexer
from dlpy.parser import Parser
from dlpy.interpreter import Interpreter
from dlpy.tree_printer import TreePrinter
import ply.yacc as yacc
import sys

if len(sys.argv) == 1:
    print("Usage: python3 %s filename" % __file__)
else:
    with open('{}'.format(sys.argv[1]), 'r') as content_file:
        file_input = content_file.read()
    print("====词法分析结果====")
    lexer = Lexer()
    lexer.input(file_input)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
    print("====语法分析结果====")
    parser = yacc.yacc(module=Parser)
    ast = parser.parse(file_input, lexer=Lexer())
    # print(ast)
    print("====语义分析结果====")
    original_stdout = sys.stdout
    output = StringIO()
    sys.stdout = output
    ast.accept(Interpreter())
    sys.stdout = original_stdout
    python_code = output.getvalue()
    print(python_code)
    print("====运行结果====")
    exec(python_code)