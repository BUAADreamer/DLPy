class Node(object):
    def accept(self, visitor, args=None):
        if args is None:
            return visitor.visit(self)
        else:
            return visitor.visit(self, args)


class Module(Node):
    def __init__(self, body):
        self.type = 'module'
        self.body = body


class StatementList(Node):
    def __init__(self):
        self.statement_list = []

    def add_statement(self, statement_list):
        self.statement_list.append(statement_list)


class Print(Node):
    def __init__(self, value):
        self.type = 'print'
        self.value = value


class While(Node):
    def __init__(self, test, body, orelse):
        self.type = 'while'
        self.test = test
        self.body = body
        self.orelse = orelse


class If(Node):
    def __init__(self, test, body, orelse):
        self.type = 'if'
        self.test = test
        self.body = body
        self.orelse = orelse


class BoolOp(Node):
    def __init__(self, op, left, right):
        self.type = 'boolop'
        self.op = op
        self.left = left
        self.right = right


class Compare(Node):
    def __init__(self, left, op, right):
        self.type = 'compare'
        self.left = left
        self.right = right
        self.op = op


class Assign(Node):
    def __init__(self, id, expression):
        self.type = 'assign'
        self.id = id
        self.expression = expression
    
class Assign_Type(Node):
    def __init__(self, id, appoint_type, expression):
        self.type = 'assign_type'
        self.id = id
        self.appoint_type = appoint_type
        self.expression = expression

class BinOp(Node):
    def __init__(self, left, op, right):
        self.type = 'binop'
        self.left = left
        self.right = right
        self.op = op


class List(Node):
    def __init__(self, values):
        self.type = 'list'
        self.values = values


class Tuple(Node):
    def __init__(self, values):
        self.type = 'tuple'
        self.values = values


class ExprList(Node):
    def __init__(self):
        self.expression_list = []

    def add_expr_list(self, expression_list):
        self.expression_list.append(expression_list)


class Const(Node):
    def __init__(self, value):
        self.type = 'const'
        self.value = value


class Name(Node):
    def __init__(self, id):
        self.type = 'name'
        self.id = id


class Number(Node):
    def __init__(self, value):
        self.type = 'number'
        self.value = value


class Str(Node):
    def __init__(self, value):
        self.type = 'str'
        self.value = value

class Break(Node):
    def __init__(self):
        self.type = 'break'

class Continue(Node):
    def __init__(self):
        self.type = 'continue'

class Index(Node):
    def __init__(self,value1,value2):
        self.type = 'index'
        self.value1 = value1
        self.value2 = value2

class Funcall(Node):
    def __init__(self,name,arguments):
        self.type = 'funcall'
        self.name = name
        self.arguments = arguments  # AST.Tuple

class Funcdef(Node):
    def __init__(self,name,arguments,body):
        self.type = 'funcdef'
        self.name = name
        self.arguments = arguments  # AST.Tuple
        self.body = body

class Return(Node):
    def __init__(self, exprs):
        self.type = 'return'
        self.exprs = exprs

class Model(Node):
    def __init__(self, model_name, model_type, model_def, data_path):
        self.type = 'model'
        self.model_name = model_name
        self.model_type = model_type
        self.model_def = model_def
        self.data_path = data_path

class Train(Node):
    def __init__(self, model_name, params):
        self.type = 'train'
        self.model_name = model_name
        self.params = params

class Pred(Node):
    def __init__(self, model_name, input):
        self.type = 'pred'
        self.model_name = model_name
        self.input = input

class Save(Node):
    def __init__(self, model_name, save_path):
        self.type = 'save'
        self.model_name = model_name
        self.save_path = save_path