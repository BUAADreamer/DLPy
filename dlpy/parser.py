import dlpy.ast as AST
from dlpy.lexer import Lexer


class Parser(object):
    
    tokens = Lexer.tokens

    precedence = (
        ('nonassoc', 'LT', 'GT', 'LTE', 'GTE'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE')
    )

    def p_program(p):
        """program : stmt_list"""
        p[0] = AST.Module(p[1])

    def p_stmt_list(p):
        """stmt_list : stmt_list stmt
                    | stmt
        """
        if len(p) == 2:
            p[0] = AST.StatementList()
            p[0].add_statement(p[1])
        else:
            p[1].add_statement(p[2])
            p[0] = p[1]

    # stmt: simple_stmt | compound_stmt
    def p_stmt(p):
        """stmt : simple_stmt
                | compound_stmt
        """
        p[0] = p[1]

    # compound_stmt: if_stmt | while_stmt | for_stmt | try_stmt | with_stmt | funcdef | classdef | decorated | async_stmt
    def p_compound_stmt(p):
        """compound_stmt : if_stmt
                        | while_stmt
                        | funcdef_stmt
                        | print
        """
        p[0] = p[1]

    # simple_stmt: small_stmt (';' small_stmt)* [';'] NEWLINE
    def p_simple_stmt(p):
        """simple_stmt : small_stmt SEMICOLON
        """
        p[0] = p[1]

    # small_stmt: (expr_stmt | del_stmt | pass_stmt | flow_stmt |
    #             import_stmt | global_stmt | nonlocal_stmt | assert_stmt)
    def p_small_stmt(p):
        """small_stmt : test
                    | flow_stmt
                    | dl_stmt
                    | assign_expr
        """
        p[0] = p[1]

    def p_print(p):
        """print : PRINT LPAREN small_stmt RPAREN SEMICOLON"""
        p[0] = AST.Print(p[3])

    def p_dl_stmt(p):
        """dl_stmt : train_stmt
                    | pred_stmt
                    | save_stmt
                    | chat_stmt
        """
        p[0] = p[1]

    def p_train_stmt(p):
        """train_stmt : TRAIN name list_expr
        """
        p[0] = AST.Train(p[2], p[3])

    def p_pred_stmt(p):
        """pred_stmt : PRED name STRING
        """
        p[0] = AST.Pred(p[2], p[3])

    def p_save_stmt(p):
        """save_stmt : SAVE name STRING
        """
        p[0] = AST.Save(p[2], p[3])

    def p_chat_stmt(p):
        """chat_stmt : CHAT name name
        """
        p[0] = AST.Chat(p[2], p[3])

    # flow_stmt: break_stmt | continue_stmt | return_stmt | raise_stmt | yield_stmt
    def p_flow_stmt(p):
        """flow_stmt : RETURN
                    | RETURN list_expr
                    | BREAK
                    | CONTINUE
        """
        if len(p) == 2:
            p[0] = p[1]
        else :
            p[0] = AST.Return(p[2])

    # while_stmt: 'while' test ':' suite ['else' ':' suite]
    def p_while_stmt(p):
        """while_stmt : WHILE test suite
                    | WHILE test suite ELSE suite
        """
        if len(p) == 4:
            p[0] = AST.While(p[2], p[3], [])
        else:
            p[0] = AST.While(p[2], p[3], p[5])

    # if_stmt: 'if' test ':' suite ('elif' test ':' suite)* ['else' ':' suite]
    def p_if_stmt(p):
        """if_stmt : IF test suite
                    | IF test suite ELSE suite
        """
        if len(p) == 5:
            p[0] = AST.If(p[2], p[3], [])
        else:
            p[0] = AST.If(p[2], p[3], p[5])

    def p_funcdef_stmt(p):
        """funcdef_stmt : DEF name LPAREN list_expr RPAREN suite 
                        | DEF name LPAREN RPAREN suite
        """
        if len(p)==7:
            p[0] = AST.Funcdef(p[2],AST.Tuple(p[4]),p[6])
        else:
            p[0] = AST.Funcdef(p[2],None,p[5])
    
    def p_suite(p):
        """suite : simple_stmt
                | LBRACK stmt_list RBRACK
        """
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[2]

    # or_test: and_test ('or' and_test)*
    # and_test: not_test ('and' not_test)*
    def p_test(p):
        """test : comparison OR test
                | comparison AND test
                | comparison
        """
        if len(p) == 4:
            p[0] = AST.BoolOp(p[2], p[1], p[3])
        else:
            p[0] = p[1]

    # comparison: expr(comp_op expr) *
    def p_comparison(p):
        """comparison : expr GT expr
                    | expr LT expr
                    | expr GTE expr
                    | expr LTE expr
                    | expr EQ expr
                    | expr NEQ expr
                    | expr
        """
        if len(p) == 4:
            p[0] = AST.Compare(p[1], p[2], p[3])
        else:
            p[0] = p[1]

    def p_basic_type(p):
        """basic_type : INT_TYPE 
                        | FLOAT_TYPE
                        | LIST_TYPE
                        | TUPLE_TYPE
                        | MLP
                        | TRANSFORMER
        """
        p[0] = p[1]

    def p_assign_expr(p):
        """assign_expr : NAME ASSIGN expr
                | NAME COLON basic_type ASSIGN expr
                | NAME COLON basic_type ASSIGN STRING COLON STRING
                | NAME COLON basic_type ASSIGN list_expr COLON STRING
                | NAME ASSIGN SCAN LPAREN RPAREN
        """
        if p[3]=='transformer' or p[3]=='mlp':
            p[0] = AST.Model(p[1],p[3], p[5], p[7])
        elif len(p) == 4:
            p[0] = AST.Assign(p[1], p[3])
        elif len(p) == 6 and p[3]!='scan':
            p[0] = AST.Assign_Type(p[1], p[3], p[5])
        else:
            p[0] = AST.Scan(p[1])

    # arith_expr: term (('+'|'-') term)*
    # term: factor (('*'|'@'|'/'|'%'|'//') factor)*
    def p_expr(p):
        """expr : expr PLUS expr
                | expr MINUS expr
                | expr TIMES expr
                | expr DIVIDE expr
                | expr MOD expr
                | factor
        """
        if len(p) == 4:
            p[0] = AST.BinOp(p[1], p[2], p[3])
        else:
            p[0] = p[1]

    # factor: ('+'|'-'|'~') factor | power
    def p_factor(p):
        """factor : PLUS factor
                | MINUS factor
                | atom_expr"""
        if len(p) == 2:
            p[0] = p[1]

    # atom_expr: [AWAIT] atom trailer*
    def p_atom_expr(p):
        """atom_expr : atom 
                     | atom_expr LSQBRACK expr RSQBRACK
                     | name LPAREN list_expr RPAREN
                     """
        if len(p)==2:
            p[0] = p[1]
        elif p[2] == '[':
            p[0] = AST.Index(p[1],p[3])
        else:
            p[0] = AST.Funcall(p[1], AST.Tuple(p[3]))
    
    # atom: ('(' [yield_expr|testlist_comp] ')' |
    #        '[' [testlist_comp] ']' |
    #        NAME | NUMBER | STRING+ | '...' | 'None' | 'True' | 'False')
    def p_atom(p):
        """atom : LPAREN list_expr RPAREN
                | LSQBRACK list_expr RSQBRACK
                | name
                | number
                | string
                | TRUE
                | FALSE
                | NONE
                | name LSQBRACK atom RSQBRACK
        """
        if len(p) == 2:
            if isinstance(p[1], AST.Number) or isinstance(p[1], AST.Str) or isinstance(p[1], AST.Name):
                p[0] = p[1]
            else:
                p[0] = AST.Const(p[1])
        elif p[1] == '(':
            p[0] = AST.Tuple(p[2])
        elif p[1] == '[':
            p[0] = AST.List(p[2])
        elif len(p)==5:
            p[0] = AST.Index(p[1],p[3])
        else:
            p[0] = p[1]

    # testlist_comp: (test|star_expr) ( comp_for | (',' (test|star_expr))* [','] )
    def p_list_expr(p):
        """list_expr : list_expr COMMA expr
                    | expr
        """
        if len(p) == 2:
            p[0] = AST.ExprList()
            p[0].add_expr_list(p[1])
        else:
            p[1].add_expr_list(p[3])
            p[0] = p[1]

    def p_name(p):
        """name : NAME"""
        p[0] = AST.Name(p[1])

    def p_number(p):
        """number : INT
                | FLOAT
        """
        p[0] = AST.Number(p[1])

    def p_string(p):
        """string : STRING"""
        p[0] = AST.Str(p[1])

    def p_error(p):
        if p:
            print("Syntax error at {} in line {}, type {}".format(p.value, p.lineno, p.type))
        else:
            print("Syntax error at EOF")
