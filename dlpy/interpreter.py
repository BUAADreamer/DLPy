from dlpy.visit import *
import dlpy.ast as AST

from template import *


class Interpreter(object):

    def __init__(self):
        self.variables = {}
        self.layer = 0
        self.model2type = dict()
        self.importset = set()
        self.id2type = dict()

    @on('node')
    def visit(self, node):
        pass

    @when(AST.Module)
    def visit(self, node):
        node.body.accept(self)

    @when(AST.StatementList)
    def visit(self, node):
        result = []
        for statement in node.statement_list:
            print("\t"*self.layer, end="")
            if isinstance(statement,str):
                print(statement,end="")
            else:
                result.append(statement.accept(self))
            print("")
        return result

    @when(AST.Print)
    def visit(self, node):
        print("print(", end="")
        node.value.accept(self)
        print(")",end="")

    @when(AST.While)
    def visit(self, node):
        print("while ", end="")
        node.test.accept(self)
        print(":")
        self.layer += 1
        node.body.accept(self)
        self.layer -= 1
    
    @when(AST.If)
    def visit(self, node):
        print("if ", end="")
        node.test.accept(self)
        print(":")
        self.layer += 1
        node.body.accept(self)
        self.layer -= 1
        if node.orelse!=[]:
            print(self.layer*"\t",end='')
            print("else:")
            self.layer += 1
            node.orelse.accept(self)
            self.layer -= 1

    @when(AST.BoolOp)
    def visit(self, node):
        r1 = node.left.accept(self)
        print(node.op, end="")
        r2 = node.right.accept(self)

    @when(AST.Compare)
    def visit(self, node):
        r1 = node.left.accept(self)
        print(node.op, end="")
        r2 = node.right.accept(self)

    @when(AST.Assign)
    def visit(self, node):
        print(node.id, " = ", end="")
        node.expression.accept(self)
        if node.id in self.id2type:
            print("")
            print(f"assert isinstance({node.id}, {self.id2type[node.id]}), '{node.id}应当是{self.id2type[node.id]}类型'")

    @when(AST.Assign_Type)
    def visit(self, node):
        print(node.id, " = ", end="")
        node.expression.accept(self)
        print("")
        self.id2type[node.id] = node.appoint_type
        print(f"assert isinstance({node.id}, {node.appoint_type}), '{node.id}应当是{node.appoint_type}类型'")

    @when(AST.BinOp)
    def visit(self, node):
        r1 = node.left.accept(self)
        print(node.op, end="")
        r2 = node.right.accept(self)

    @when(AST.List)
    def visit(self, node):
        # print("*******",node.values,type(node.values))
        print("[", end="")
        ans = list(node.values.accept(self))
        print("]", end="")
        # print(ans, end="")
        return ans

    @when(AST.Tuple)
    def visit(self, node):
        print("(",end="")
        ans = tuple(node.values.accept(self))
        print(")",end="")
        # print(ans, end="")
        return ans

    @when(AST.ExprList)
    def visit(self, node):
        result = []
        # print("[", end="")
        N=len(node.expression_list)
        for i,expr in enumerate(node.expression_list):
            res = expr.accept(self)
            if i<N-1:
                print(",", end="")
            result.append(res)
        # print("]", end="")
        return result

    @when(AST.Funcdef)
    def visit(self,node):
        print("def ",end="")
        node.name.accept(self)
        if node.arguments is not None:
            node.arguments.accept(self)
        else:
            print('()',end='')
        print(":")
        self.layer+=1
        node.body.accept(self)
        self.layer-=1

    @when(AST.Name)
    def visit(self, node):
        print(node.id, end="")
        return node.id

    @when(AST.Const)
    def visit(self, node):
        print(node.value, end="")
        return node.value

    @when(AST.Number)
    def visit(self, node):
        print(node.value, end="")
        numStr = str(node.value)
        pos = numStr.find('.')

        if pos != -1:
            return float(node.value)
        else:
            return int(node.value)

    @when(AST.Str)
    def visit(self, node):
        print("'" + node.value + "'", end="")
        return node.value

    @when(AST.Index)
    def visit(self, node):
        node.value1.accept(self)
        print("[",end='')
        node.value2.accept(self)
        print("]",end='')

    @when(AST.Funcall)
    def visit(self, node):
        node.name.accept(self)
        node.arguments.accept(self)

    @when(AST.Return)
    def visit(self, node):
        print("return ", end="")
        node.exprs.accept(self)

    @when(AST.Model)
    def visit(self, node):
        output_str = ''
        self.model2type[node.model_name] = node.model_type
        if node.model_type == "transformer":
            if node.model_type not in self.importset:
                output_str+=transformer_import+'\n'
                self.importset.add(node.model_type)
            if isinstance(node.model_def, str):
                output_str+=transformer_def_load.format(node.model_name,node.model_def, node.data_path)+'\n'
            else:
                def_list = [x.value for x in node.model_def.expression_list]
                output_str+=transformer_def_scratch.format(node.model_name,def_list[0],def_list[1],def_list[2],node.data_path)+'\n'
        elif node.model_type == "mlp":
            if node.model_type not in self.importset:
                output_str+=mlp_import+'\n'
                self.importset.add(node.model_type)
            if isinstance(node.model_def, str):
                output_str+=mlp_def_load.format(node.model_name,node.model_def, node.data_path)+'\n'
            else:
                def_list = [x.value for x in node.model_def.expression_list]
                output_str+=mlp_def_scratch.format(node.model_name,str(def_list),node.data_path)+'\n'
        output_str = output_str.replace('\n', '\n'+'\t'*self.layer)
        print(output_str)
        
    @when(AST.Train)
    def visit(self, node):
        if node.model_name.id not in self.model2type:
            raise NotImplementedError
        model_type = self.model2type[node.model_name.id]
        param_list = [x.value for x in node.params.expression_list]
        template = eval(f'{model_type}_train')
        output_str=template.format(node.model_name.id,param_list[0],param_list[1],param_list[2])
        output_str = output_str.replace('\n', '\n'+'\t'*self.layer)
        print(output_str)

    @when(AST.Pred)
    def visit(self, node):
        if node.model_name.id not in self.model2type:
            raise NotImplementedError
        model_type = self.model2type[node.model_name.id]
        pred_input = node.input
        template = eval(f'{model_type}_pred')
        output_str = template.format(node.model_name.id, pred_input)
        output_str = output_str.replace('\n', '\n'+'\t'*self.layer)
        print(output_str)

    @when(AST.Save)
    def visit(self, node):
        if node.model_name.id not in self.model2type:
            raise NotImplementedError
        model_type = self.model2type[node.model_name.id]
        template = eval(f'{model_type}_save')
        output_str = template.format(node.model_name.id, node.save_path)
        output_str = output_str.replace('\n', '\n'+'\t'*self.layer)
        print(output_str)
        
    @when(AST.Chat)
    def visit(self, node):
        if node.model_name.id not in self.model2type:
            raise NotImplementedError
        model_type = self.model2type[node.model_name.id]
        template = eval(f'{model_type}_chat')
        output_str = 'messages = [{"role": "user", "content": ' + node.user_input.id + '}]\nresponse = ' + node.model_name.id + '.chat(tokenizer, messages)\nprint(response)'
        output_str = output_str.replace('\n', '\n'+'\t'*self.layer)
        print(output_str)
        
    @when(AST.Scan)
    def visit(self, node):
        print(node.name, " = ", end="")
        print("input()",end="")