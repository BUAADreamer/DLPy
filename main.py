from io import StringIO
from dlpy.lexer import Lexer
from dlpy.parser import Parser
from dlpy.interpreter import Interpreter
import ply.yacc as yacc
import sys

if len(sys.argv) == 1:
    print("Usage: python3 %s filename" % __file__)
else:
    with open('{}'.format(sys.argv[1]), 'r') as content_file:
        file_input = content_file.read()

    parser = yacc.yacc(module=Parser)
    ast = parser.parse(file_input, lexer=Lexer())
    original_stdout = sys.stdout
    output = StringIO()
    sys.stdout = output
    ast.accept(Interpreter())
    sys.stdout = original_stdout
    python_code = output.getvalue()
    print(python_code)
    exec(python_code)