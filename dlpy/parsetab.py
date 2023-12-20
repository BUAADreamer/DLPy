
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocLTGTLTEGTEleftPLUSMINUSleftTIMESDIVIDEAND ASSIGN BREAK COLON COMMA CONTINUE DEF DIVIDE ELSE EQ FALSE FLOAT FLOAT_TYPE GT GTE IF INT INT_TYPE LBRACK LIST_TYPE LPAREN LSQBRACK LT LTE MINUS MLP MOD NAME NEQ NONE OR PLUS PRED PRINT RBRACK RETURN RPAREN RSQBRACK SAVE SEMICOLON STRING TIMES TRAIN TRANSFORMER TRUE TUPLE_TYPE WHILEprogram : stmt_liststmt_list : stmt_list stmt\n                    | stmt\n        stmt : simple_stmt\n                | compound_stmt\n        compound_stmt : if_stmt\n                        | while_stmt\n                        | funcdef_stmt\n                        | print\n        simple_stmt : small_stmt SEMICOLON\n        small_stmt : test\n                    | flow_stmt\n                    | dl_stmt\n                    | assign_expr\n        print : PRINT LPAREN small_stmt RPAREN SEMICOLONdl_stmt : train_stmt\n                    | pred_stmt\n                    | save_stmt\n        train_stmt : TRAIN name list_expr\n        pred_stmt : PRED name STRING\n        save_stmt : SAVE name STRING\n        flow_stmt : RETURN\n                    | RETURN list_expr\n                    | BREAK\n                    | CONTINUE\n        while_stmt : WHILE test suite\n                    | WHILE test suite ELSE suite\n        if_stmt : IF test suite\n                    | IF test suite ELSE suite\n        funcdef_stmt : DEF name LPAREN list_expr RPAREN suite\n        suite : simple_stmt\n                | LBRACK stmt_list RBRACK\n        test : comparison OR test\n                | comparison AND test\n                | comparison\n        comparison : expr GT expr\n                    | expr LT expr\n                    | expr GTE expr\n                    | expr LTE expr\n                    | expr EQ expr\n                    | expr NEQ expr\n                    | expr\n        basic_type : INT_TYPE \n                        | FLOAT_TYPE\n                        | LIST_TYPE\n                        | TUPLE_TYPE\n                        | MLP\n                        | TRANSFORMER\n        assign_expr : NAME ASSIGN expr\n                | NAME COLON basic_type ASSIGN expr\n                | NAME COLON basic_type ASSIGN STRING COLON STRING\n                | NAME COLON basic_type ASSIGN list_expr COLON STRING\n        expr : expr PLUS expr\n                | expr MINUS expr\n                | expr TIMES expr\n                | expr DIVIDE expr\n                | expr MOD expr\n                | factor\n        factor : PLUS factor\n                | MINUS factor\n                | atom_expratom_expr : \n                     | atom \n                     | atom_expr LSQBRACK expr RSQBRACK\n                     | name LPAREN list_expr RPAREN\n                     atom : LPAREN list_expr RPAREN\n                | LSQBRACK list_expr RSQBRACK\n                | name\n                | number\n                | string\n                | TRUE\n                | FALSE\n                | NONE\n                | name LSQBRACK atom RSQBRACK\n        list_expr : list_expr COMMA expr\n                    | expr\n        name : NAMEnumber : INT\n                | FLOAT\n        string : STRING'
    
_lr_action_items = {'IF':([0,2,3,4,5,7,8,9,10,47,48,81,82,83,84,119,128,129,130,132,136,],[15,15,-3,-4,-5,-6,-7,-8,-9,-2,-10,-28,-31,15,-26,15,-29,-32,-27,-15,-30,]),'WHILE':([0,2,3,4,5,7,8,9,10,47,48,81,82,83,84,119,128,129,130,132,136,],[16,16,-3,-4,-5,-6,-7,-8,-9,-2,-10,-28,-31,16,-26,16,-29,-32,-27,-15,-30,]),'DEF':([0,2,3,4,5,7,8,9,10,47,48,81,82,83,84,119,128,129,130,132,136,],[17,17,-3,-4,-5,-6,-7,-8,-9,-2,-10,-28,-31,17,-26,17,-29,-32,-27,-15,-30,]),'PRINT':([0,2,3,4,5,7,8,9,10,47,48,81,82,83,84,119,128,129,130,132,136,],[20,20,-3,-4,-5,-6,-7,-8,-9,-2,-10,-28,-31,20,-26,20,-29,-32,-27,-15,-30,]),'RETURN':([0,2,3,4,5,7,8,9,10,15,16,18,21,29,30,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,57,58,59,63,64,65,66,67,68,69,70,71,72,73,77,78,81,82,83,84,89,92,93,102,103,104,105,106,107,108,109,110,111,112,117,118,119,120,122,123,127,128,129,130,131,132,136,],[22,22,-3,-4,-5,-6,-7,-8,-9,-62,-62,-68,-35,-42,-80,-62,-62,-58,-61,-63,-69,-70,-71,-72,-73,-78,-79,-2,-10,22,-77,22,22,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-59,-60,-28,-31,22,-26,-66,-33,-34,-36,-37,-38,-39,-40,-41,-53,-54,-55,-56,-57,-67,22,22,22,-65,-74,-64,-29,-32,-27,22,-15,-30,]),'BREAK':([0,2,3,4,5,7,8,9,10,15,16,18,21,29,30,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,57,58,59,63,64,65,66,67,68,69,70,71,72,73,77,78,81,82,83,84,89,92,93,102,103,104,105,106,107,108,109,110,111,112,117,118,119,120,122,123,127,128,129,130,131,132,136,],[23,23,-3,-4,-5,-6,-7,-8,-9,-62,-62,-68,-35,-42,-80,-62,-62,-58,-61,-63,-69,-70,-71,-72,-73,-78,-79,-2,-10,23,-77,23,23,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-59,-60,-28,-31,23,-26,-66,-33,-34,-36,-37,-38,-39,-40,-41,-53,-54,-55,-56,-57,-67,23,23,23,-65,-74,-64,-29,-32,-27,23,-15,-30,]),'CONTINUE':([0,2,3,4,5,7,8,9,10,15,16,18,21,29,30,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,57,58,59,63,64,65,66,67,68,69,70,71,72,73,77,78,81,82,83,84,89,92,93,102,103,104,105,106,107,108,109,110,111,112,117,118,119,120,122,123,127,128,129,130,131,132,136,],[24,24,-3,-4,-5,-6,-7,-8,-9,-62,-62,-68,-35,-42,-80,-62,-62,-58,-61,-63,-69,-70,-71,-72,-73,-78,-79,-2,-10,24,-77,24,24,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-59,-60,-28,-31,24,-26,-66,-33,-34,-36,-37,-38,-39,-40,-41,-53,-54,-55,-56,-57,-67,24,24,24,-65,-74,-64,-29,-32,-27,24,-15,-30,]),'NAME':([0,2,3,4,5,7,8,9,10,15,16,17,18,19,21,22,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,53,54,57,58,59,61,63,64,65,66,67,68,69,70,71,72,73,74,77,78,79,81,82,83,84,85,89,90,92,93,102,103,104,105,106,107,108,109,110,111,112,117,118,119,120,122,123,126,127,128,129,130,131,132,136,],[28,28,-3,-4,-5,-6,-7,-8,-9,50,50,50,-68,50,-35,50,-42,-80,50,50,50,50,50,-58,-61,-63,50,-69,-70,-71,-72,-73,-78,-79,-2,-10,28,-77,28,50,50,28,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,-59,-60,50,-28,-31,28,-26,50,-66,50,-33,-34,-36,-37,-38,-39,-40,-41,-53,-54,-55,-56,-57,-67,28,28,28,-65,-74,50,-64,-29,-32,-27,28,-15,-30,]),'TRAIN':([0,2,3,4,5,7,8,9,10,15,16,18,21,29,30,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,57,58,59,63,64,65,66,67,68,69,70,71,72,73,77,78,81,82,83,84,89,92,93,102,103,104,105,106,107,108,109,110,111,112,117,118,119,120,122,123,127,128,129,130,131,132,136,],[31,31,-3,-4,-5,-6,-7,-8,-9,-62,-62,-68,-35,-42,-80,-62,-62,-58,-61,-63,-69,-70,-71,-72,-73,-78,-79,-2,-10,31,-77,31,31,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-59,-60,-28,-31,31,-26,-66,-33,-34,-36,-37,-38,-39,-40,-41,-53,-54,-55,-56,-57,-67,31,31,31,-65,-74,-64,-29,-32,-27,31,-15,-30,]),'PRED':([0,2,3,4,5,7,8,9,10,15,16,18,21,29,30,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,57,58,59,63,64,65,66,67,68,69,70,71,72,73,77,78,81,82,83,84,89,92,93,102,103,104,105,106,107,108,109,110,111,112,117,118,119,120,122,123,127,128,129,130,131,132,136,],[32,32,-3,-4,-5,-6,-7,-8,-9,-62,-62,-68,-35,-42,-80,-62,-62,-58,-61,-63,-69,-70,-71,-72,-73,-78,-79,-2,-10,32,-77,32,32,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-59,-60,-28,-31,32,-26,-66,-33,-34,-36,-37,-38,-39,-40,-41,-53,-54,-55,-56,-57,-67,32,32,32,-65,-74,-64,-29,-32,-27,32,-15,-30,]),'SAVE':([0,2,3,4,5,7,8,9,10,15,16,18,21,29,30,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,57,58,59,63,64,65,66,67,68,69,70,71,72,73,77,78,81,82,83,84,89,92,93,102,103,104,105,106,107,108,109,110,111,112,117,118,119,120,122,123,127,128,129,130,131,132,136,],[33,33,-3,-4,-5,-6,-7,-8,-9,-62,-62,-68,-35,-42,-80,-62,-62,-58,-61,-63,-69,-70,-71,-72,-73,-78,-79,-2,-10,33,-77,33,33,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-59,-60,-28,-31,33,-26,-66,-33,-34,-36,-37,-38,-39,-40,-41,-53,-54,-55,-56,-57,-67,33,33,33,-65,-74,-64,-29,-32,-27,33,-15,-30,]),'PLUS':([0,2,3,4,5,7,8,9,10,15,16,18,19,21,22,28,29,30,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,53,56,57,58,59,61,63,64,65,66,67,68,69,70,71,72,73,74,77,78,79,81,82,83,84,85,89,90,92,93,94,102,103,104,105,106,107,108,109,110,111,112,116,117,118,119,120,122,123,124,126,127,128,129,130,131,132,133,134,136,],[34,34,-3,-4,-5,-6,-7,-8,-9,34,34,-68,34,-35,34,-77,69,-80,34,34,-58,-61,-63,34,-69,-70,-71,-72,-73,-78,-79,-2,-10,34,-77,34,34,69,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,-59,-60,34,-28,-31,34,-26,34,-66,34,-33,-34,69,69,69,69,69,69,69,-53,-54,-55,-56,69,69,-67,34,34,34,-65,-74,69,34,-64,-29,-32,-27,34,-15,69,-80,-30,]),'MINUS':([0,2,3,4,5,7,8,9,10,15,16,18,19,21,22,28,29,30,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,53,56,57,58,59,61,63,64,65,66,67,68,69,70,71,72,73,74,77,78,79,81,82,83,84,85,89,90,92,93,94,102,103,104,105,106,107,108,109,110,111,112,116,117,118,119,120,122,123,124,126,127,128,129,130,131,132,133,134,136,],[35,35,-3,-4,-5,-6,-7,-8,-9,35,35,-68,35,-35,35,-77,70,-80,35,35,-58,-61,-63,35,-69,-70,-71,-72,-73,-78,-79,-2,-10,35,-77,35,35,70,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-59,-60,35,-28,-31,35,-26,35,-66,35,-33,-34,70,70,70,70,70,70,70,-53,-54,-55,-56,70,70,-67,35,35,35,-65,-74,70,35,-64,-29,-32,-27,35,-15,70,-80,-30,]),'LSQBRACK':([0,2,3,4,5,7,8,9,10,15,16,18,19,21,22,28,29,30,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,53,54,57,58,59,61,63,64,65,66,67,68,69,70,71,72,73,74,77,78,79,81,82,83,84,85,87,89,90,92,93,102,103,104,105,106,107,108,109,110,111,112,117,118,119,120,122,123,126,127,128,129,130,131,132,134,136,],[39,39,-3,-4,-5,-6,-7,-8,-9,39,39,54,39,-35,39,-77,-42,-80,39,39,-58,79,-63,39,-69,-70,-71,-72,-73,-78,-79,-2,-10,39,-77,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-59,-60,39,-28,-31,39,-26,39,54,-66,39,-33,-34,-36,-37,-38,-39,-40,-41,-53,-54,-55,-56,-57,-67,39,39,39,-65,-74,39,-64,-29,-32,-27,39,-15,-80,-30,]),'GT':([0,2,3,4,5,7,8,9,10,15,16,18,21,28,29,30,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,57,58,59,63,64,65,66,67,68,69,70,71,72,73,77,78,81,82,83,84,89,92,93,102,103,104,105,106,107,108,109,110,111,112,117,118,119,120,122,123,127,128,129,130,131,132,136,],[-62,-62,-3,-4,-5,-6,-7,-8,-9,-62,-62,-68,-35,-77,63,-80,-62,-62,-58,-61,-63,-69,-70,-71,-72,-73,-78,-79,-2,-10,-62,-77,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-59,-60,-28,-31,-62,-26,-66,-33,-34,-36,-37,-38,-39,-40,-41,-53,-54,-55,-56,-57,-67,-62,-62,-62,-65,-74,-64,-29,-32,-27,-62,-15,-30,]),'LT':([0,2,3,4,5,7,8,9,10,15,16,18,21,28,29,30,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,57,58,59,63,64,65,66,67,68,69,70,71,72,73,77,78,81,82,83,84,89,92,93,102,103,104,105,106,107,108,109,110,111,112,117,118,119,120,122,123,127,128,129,130,131,132,136,],[-62,-62,-3,-4,-5,-6,-7,-8,-9,-62,-62,-68,-35,-77,64,-80,-62,-62,-58,-61,-63,-69,-70,-71,-72,-73,-78,-79,-2,-10,-62,-77,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-59,-60,-28,-31,-62,-26,-66,-33,-34,-36,-37,-38,-39,-40,-41,-53,-54,-55,-56,-57,-67,-62,-62,-62,-65,-74,-64,-29,-32,-27,-62,-15,-30,]),'GTE':([0,2,3,4,5,7,8,9,10,15,16,18,21,28,29,30,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,57,58,59,63,64,65,66,67,68,69,70,71,72,73,77,78,81,82,83,84,89,92,93,102,103,104,105,106,107,108,109,110,111,112,117,118,119,120,122,123,127,128,129,130,131,132,136,],[-62,-62,-3,-4,-5,-6,-7,-8,-9,-62,-62,-68,-35,-77,65,-80,-62,-62,-58,-61,-63,-69,-70,-71,-72,-73,-78,-79,-2,-10,-62,-77,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-59,-60,-28,-31,-62,-26,-66,-33,-34,-36,-37,-38,-39,-40,-41,-53,-54,-55,-56,-57,-67,-62,-62,-62,-65,-74,-64,-29,-32,-27,-62,-15,-30,]),'LTE':([0,2,3,4,5,7,8,9,10,15,16,18,21,28,29,30,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,57,58,59,63,64,65,66,67,68,69,70,71,72,73,77,78,81,82,83,84,89,92,93,102,103,104,105,106,107,108,109,110,111,112,117,118,119,120,122,123,127,128,129,130,131,132,136,],[-62,-62,-3,-4,-5,-6,-7,-8,-9,-62,-62,-68,-35,-77,66,-80,-62,-62,-58,-61,-63,-69,-70,-71,-72,-73,-78,-79,-2,-10,-62,-77,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-59,-60,-28,-31,-62,-26,-66,-33,-34,-36,-37,-38,-39,-40,-41,-53,-54,-55,-56,-57,-67,-62,-62,-62,-65,-74,-64,-29,-32,-27,-62,-15,-30,]),'EQ':([0,2,3,4,5,7,8,9,10,15,16,18,21,28,29,30,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,57,58,59,63,64,65,66,67,68,69,70,71,72,73,77,78,81,82,83,84,89,92,93,102,103,104,105,106,107,108,109,110,111,112,117,118,119,120,122,123,127,128,129,130,131,132,136,],[-62,-62,-3,-4,-5,-6,-7,-8,-9,-62,-62,-68,-35,-77,67,-80,-62,-62,-58,-61,-63,-69,-70,-71,-72,-73,-78,-79,-2,-10,-62,-77,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-59,-60,-28,-31,-62,-26,-66,-33,-34,-36,-37,-38,-39,-40,-41,-53,-54,-55,-56,-57,-67,-62,-62,-62,-65,-74,-64,-29,-32,-27,-62,-15,-30,]),'NEQ':([0,2,3,4,5,7,8,9,10,15,16,18,21,28,29,30,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,57,58,59,63,64,65,66,67,68,69,70,71,72,73,77,78,81,82,83,84,89,92,93,102,103,104,105,106,107,108,109,110,111,112,117,118,119,120,122,123,127,128,129,130,131,132,136,],[-62,-62,-3,-4,-5,-6,-7,-8,-9,-62,-62,-68,-35,-77,68,-80,-62,-62,-58,-61,-63,-69,-70,-71,-72,-73,-78,-79,-2,-10,-62,-77,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-59,-60,-28,-31,-62,-26,-66,-33,-34,-36,-37,-38,-39,-40,-41,-53,-54,-55,-56,-57,-67,-62,-62,-62,-65,-74,-64,-29,-32,-27,-62,-15,-30,]),'TIMES':([0,2,3,4,5,7,8,9,10,15,16,18,19,21,22,28,29,30,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,53,56,57,58,59,61,63,64,65,66,67,68,69,70,71,72,73,74,77,78,79,81,82,83,84,85,89,90,92,93,94,102,103,104,105,106,107,108,109,110,111,112,116,117,118,119,120,122,123,124,126,127,128,129,130,131,132,133,134,136,],[-62,-62,-3,-4,-5,-6,-7,-8,-9,-62,-62,-68,-62,-35,-62,-77,71,-80,-62,-62,-58,-61,-63,-62,-69,-70,-71,-72,-73,-78,-79,-2,-10,-62,-77,-62,-62,71,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-59,-60,-62,-28,-31,-62,-26,-62,-66,-62,-33,-34,71,71,71,71,71,71,71,71,71,-55,-56,71,71,-67,-62,-62,-62,-65,-74,71,-62,-64,-29,-32,-27,-62,-15,71,-80,-30,]),'DIVIDE':([0,2,3,4,5,7,8,9,10,15,16,18,19,21,22,28,29,30,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,53,56,57,58,59,61,63,64,65,66,67,68,69,70,71,72,73,74,77,78,79,81,82,83,84,85,89,90,92,93,94,102,103,104,105,106,107,108,109,110,111,112,116,117,118,119,120,122,123,124,126,127,128,129,130,131,132,133,134,136,],[-62,-62,-3,-4,-5,-6,-7,-8,-9,-62,-62,-68,-62,-35,-62,-77,72,-80,-62,-62,-58,-61,-63,-62,-69,-70,-71,-72,-73,-78,-79,-2,-10,-62,-77,-62,-62,72,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-59,-60,-62,-28,-31,-62,-26,-62,-66,-62,-33,-34,72,72,72,72,72,72,72,72,72,-55,-56,72,72,-67,-62,-62,-62,-65,-74,72,-62,-64,-29,-32,-27,-62,-15,72,-80,-30,]),'MOD':([0,2,3,4,5,7,8,9,10,15,16,18,19,21,22,28,29,30,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,53,56,57,58,59,61,63,64,65,66,67,68,69,70,71,72,73,74,77,78,79,81,82,83,84,85,89,90,92,93,94,102,103,104,105,106,107,108,109,110,111,112,116,117,118,119,120,122,123,124,126,127,128,129,130,131,132,133,134,136,],[-62,-62,-3,-4,-5,-6,-7,-8,-9,-62,-62,-68,-62,-35,-62,-77,73,-80,-62,-62,-58,-61,-63,-62,-69,-70,-71,-72,-73,-78,-79,-2,-10,-62,-77,-62,-62,73,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-59,-60,-62,-28,-31,-62,-26,-62,-66,-62,-33,-34,73,-36,-37,-38,-39,73,73,-53,-54,-55,-56,73,73,-67,-62,-62,-62,-65,-74,73,-62,-64,-29,-32,-27,-62,-15,73,-80,-30,]),'OR':([0,2,3,4,5,7,8,9,10,15,16,18,21,28,29,30,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,57,58,59,63,64,65,66,67,68,69,70,71,72,73,77,78,81,82,83,84,89,92,93,102,103,104,105,106,107,108,109,110,111,112,117,118,119,120,122,123,127,128,129,130,131,132,136,],[-62,-62,-3,-4,-5,-6,-7,-8,-9,-62,-62,-68,58,-77,-42,-80,-62,-62,-58,-61,-63,-69,-70,-71,-72,-73,-78,-79,-2,-10,-62,-77,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-59,-60,-28,-31,-62,-26,-66,-33,-34,-36,-37,-38,-39,-40,-41,-53,-54,-55,-56,-57,-67,-62,-62,-62,-65,-74,-64,-29,-32,-27,-62,-15,-30,]),'AND':([0,2,3,4,5,7,8,9,10,15,16,18,21,28,29,30,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,57,58,59,63,64,65,66,67,68,69,70,71,72,73,77,78,81,82,83,84,89,92,93,102,103,104,105,106,107,108,109,110,111,112,117,118,119,120,122,123,127,128,129,130,131,132,136,],[-62,-62,-3,-4,-5,-6,-7,-8,-9,-62,-62,-68,59,-77,-42,-80,-62,-62,-58,-61,-63,-69,-70,-71,-72,-73,-78,-79,-2,-10,-62,-77,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-59,-60,-28,-31,-62,-26,-66,-33,-34,-36,-37,-38,-39,-40,-41,-53,-54,-55,-56,-57,-67,-62,-62,-62,-65,-74,-64,-29,-32,-27,-62,-15,-30,]),'SEMICOLON':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,21,22,23,24,25,26,27,28,29,30,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,56,58,59,60,61,63,64,65,66,67,68,69,70,71,72,73,74,77,78,81,82,83,84,89,90,92,93,94,102,103,104,105,106,107,108,109,110,111,112,113,114,115,117,118,119,120,122,123,124,125,126,127,128,129,130,131,132,133,134,136,139,140,],[-62,-62,-3,-4,-5,48,-6,-7,-8,-9,-11,-12,-13,-14,-62,-62,-68,-35,-22,-24,-25,-16,-17,-18,-77,-42,-80,-62,-62,-58,-61,-63,-69,-70,-71,-72,-73,-78,-79,-2,-10,-62,-77,-62,-76,-62,-62,-23,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-59,-60,-28,-31,-62,-26,-66,-62,-33,-34,-49,-36,-37,-38,-39,-40,-41,-53,-54,-55,-56,-57,-19,-20,-21,-67,-62,-62,-62,-65,-74,-75,132,-62,-64,-29,-32,-27,-62,-15,-50,-80,-30,-51,-52,]),'LPAREN':([0,2,3,4,5,7,8,9,10,15,16,18,19,20,21,22,28,29,30,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,57,58,59,61,63,64,65,66,67,68,69,70,71,72,73,74,77,78,79,81,82,83,84,85,89,90,92,93,102,103,104,105,106,107,108,109,110,111,112,117,118,119,120,122,123,126,127,128,129,130,131,132,136,],[19,19,-3,-4,-5,-6,-7,-8,-9,19,19,53,19,57,-35,19,-77,-42,-80,19,19,-58,-61,-63,19,-69,-70,-71,-72,-73,-78,-79,-2,-10,19,-77,19,85,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-59,-60,19,-28,-31,19,-26,19,-66,19,-33,-34,-36,-37,-38,-39,-40,-41,-53,-54,-55,-56,-57,-67,19,19,19,-65,-74,19,-64,-29,-32,-27,19,-15,-30,]),'TRUE':([0,2,3,4,5,7,8,9,10,15,16,18,19,21,22,29,30,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,53,54,57,58,59,61,63,64,65,66,67,68,69,70,71,72,73,74,77,78,79,81,82,83,84,85,89,90,92,93,102,103,104,105,106,107,108,109,110,111,112,117,118,119,120,122,123,126,127,128,129,130,131,132,136,],[42,42,-3,-4,-5,-6,-7,-8,-9,42,42,-68,42,-35,42,-42,-80,42,42,-58,-61,-63,42,-69,-70,-71,-72,-73,-78,-79,-2,-10,42,-77,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-59,-60,42,-28,-31,42,-26,42,-66,42,-33,-34,-36,-37,-38,-39,-40,-41,-53,-54,-55,-56,-57,-67,42,42,42,-65,-74,42,-64,-29,-32,-27,42,-15,-30,]),'FALSE':([0,2,3,4,5,7,8,9,10,15,16,18,19,21,22,29,30,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,53,54,57,58,59,61,63,64,65,66,67,68,69,70,71,72,73,74,77,78,79,81,82,83,84,85,89,90,92,93,102,103,104,105,106,107,108,109,110,111,112,117,118,119,120,122,123,126,127,128,129,130,131,132,136,],[43,43,-3,-4,-5,-6,-7,-8,-9,43,43,-68,43,-35,43,-42,-80,43,43,-58,-61,-63,43,-69,-70,-71,-72,-73,-78,-79,-2,-10,43,-77,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-59,-60,43,-28,-31,43,-26,43,-66,43,-33,-34,-36,-37,-38,-39,-40,-41,-53,-54,-55,-56,-57,-67,43,43,43,-65,-74,43,-64,-29,-32,-27,43,-15,-30,]),'NONE':([0,2,3,4,5,7,8,9,10,15,16,18,19,21,22,29,30,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,53,54,57,58,59,61,63,64,65,66,67,68,69,70,71,72,73,74,77,78,79,81,82,83,84,85,89,90,92,93,102,103,104,105,106,107,108,109,110,111,112,117,118,119,120,122,123,126,127,128,129,130,131,132,136,],[44,44,-3,-4,-5,-6,-7,-8,-9,44,44,-68,44,-35,44,-42,-80,44,44,-58,-61,-63,44,-69,-70,-71,-72,-73,-78,-79,-2,-10,44,-77,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,-59,-60,44,-28,-31,44,-26,44,-66,44,-33,-34,-36,-37,-38,-39,-40,-41,-53,-54,-55,-56,-57,-67,44,44,44,-65,-74,44,-64,-29,-32,-27,44,-15,-30,]),'INT':([0,2,3,4,5,7,8,9,10,15,16,18,19,21,22,29,30,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,53,54,57,58,59,61,63,64,65,66,67,68,69,70,71,72,73,74,77,78,79,81,82,83,84,85,89,90,92,93,102,103,104,105,106,107,108,109,110,111,112,117,118,119,120,122,123,126,127,128,129,130,131,132,136,],[45,45,-3,-4,-5,-6,-7,-8,-9,45,45,-68,45,-35,45,-42,-80,45,45,-58,-61,-63,45,-69,-70,-71,-72,-73,-78,-79,-2,-10,45,-77,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-59,-60,45,-28,-31,45,-26,45,-66,45,-33,-34,-36,-37,-38,-39,-40,-41,-53,-54,-55,-56,-57,-67,45,45,45,-65,-74,45,-64,-29,-32,-27,45,-15,-30,]),'FLOAT':([0,2,3,4,5,7,8,9,10,15,16,18,19,21,22,29,30,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,53,54,57,58,59,61,63,64,65,66,67,68,69,70,71,72,73,74,77,78,79,81,82,83,84,85,89,90,92,93,102,103,104,105,106,107,108,109,110,111,112,117,118,119,120,122,123,126,127,128,129,130,131,132,136,],[46,46,-3,-4,-5,-6,-7,-8,-9,46,46,-68,46,-35,46,-42,-80,46,46,-58,-61,-63,46,-69,-70,-71,-72,-73,-78,-79,-2,-10,46,-77,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-59,-60,46,-28,-31,46,-26,46,-66,46,-33,-34,-36,-37,-38,-39,-40,-41,-53,-54,-55,-56,-57,-67,46,46,46,-65,-74,46,-64,-29,-32,-27,46,-15,-30,]),'STRING':([0,2,3,4,5,7,8,9,10,15,16,18,19,21,22,29,30,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,53,54,57,58,59,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,85,89,90,92,93,102,103,104,105,106,107,108,109,110,111,112,117,118,119,120,122,123,126,127,128,129,130,131,132,136,137,138,],[30,30,-3,-4,-5,-6,-7,-8,-9,30,30,-68,30,-35,30,-42,-80,30,30,-58,-61,-63,30,-69,-70,-71,-72,-73,-78,-79,-2,-10,30,-77,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,114,115,-59,-60,30,-28,-31,30,-26,30,-66,30,-33,-34,-36,-37,-38,-39,-40,-41,-53,-54,-55,-56,-57,-67,30,30,30,-65,-74,134,-64,-29,-32,-27,30,-15,-30,139,140,]),'$end':([1,2,3,4,5,7,8,9,10,47,48,81,82,84,128,129,130,132,136,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-2,-10,-28,-31,-26,-29,-32,-27,-15,-30,]),'RBRACK':([3,4,5,7,8,9,10,47,48,81,82,84,119,128,129,130,132,136,],[-3,-4,-5,-6,-7,-8,-9,-2,-10,-28,-31,-26,129,-29,-32,-27,-15,-30,]),'RPAREN':([11,12,13,14,18,19,21,22,23,24,25,26,27,28,29,30,34,35,36,37,38,40,41,42,43,44,45,46,50,53,55,56,57,58,59,60,61,63,64,65,66,67,68,69,70,71,72,73,74,77,78,85,86,89,90,91,92,93,94,102,103,104,105,106,107,108,109,110,111,112,113,114,115,117,121,122,123,124,126,127,133,134,139,140,],[-11,-12,-13,-14,-68,-62,-35,-22,-24,-25,-16,-17,-18,-77,-42,-80,-62,-62,-58,-61,-63,-69,-70,-71,-72,-73,-78,-79,-77,-62,89,-76,-62,-62,-62,-23,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-59,-60,-62,122,-66,-62,125,-33,-34,-49,-36,-37,-38,-39,-40,-41,-53,-54,-55,-56,-57,-19,-20,-21,-67,131,-65,-74,-75,-62,-64,-50,-80,-51,-52,]),'LBRACK':([15,16,18,21,29,30,34,35,36,37,38,40,41,42,43,44,45,46,49,50,51,58,59,63,64,65,66,67,68,69,70,71,72,73,77,78,89,92,93,102,103,104,105,106,107,108,109,110,111,112,117,118,120,122,123,127,131,],[-62,-62,-68,-35,-42,-80,-62,-62,-58,-61,-63,-69,-70,-71,-72,-73,-78,-79,83,-77,83,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-62,-59,-60,-66,-33,-34,-36,-37,-38,-39,-40,-41,-53,-54,-55,-56,-57,-67,83,83,-65,-74,-64,83,]),'COMMA':([18,19,22,30,34,35,36,37,38,39,40,41,42,43,44,45,46,50,53,55,56,60,69,70,71,72,73,74,77,78,80,85,86,89,90,108,109,110,111,112,113,117,121,122,123,124,126,127,133,134,135,],[-68,-62,-62,-80,-62,-62,-58,-61,-63,-62,-69,-70,-71,-72,-73,-78,-79,-77,-62,90,-76,90,-62,-62,-62,-62,-62,-62,-59,-60,90,-62,90,-66,-62,-53,-54,-55,-56,-57,90,-67,90,-65,-74,-75,-62,-64,-76,-80,90,]),'RSQBRACK':([18,30,34,35,36,37,38,39,40,41,42,43,44,45,46,50,56,69,70,71,72,73,77,78,79,80,87,88,89,90,108,109,110,111,112,116,117,122,123,124,127,],[-68,-80,-62,-62,-58,-61,-63,-62,-69,-70,-71,-72,-73,-78,-79,-77,-76,-62,-62,-62,-62,-62,-59,-60,-62,117,-68,123,-66,-62,-53,-54,-55,-56,-57,127,-67,-65,-74,-75,-64,]),'COLON':([18,28,30,34,35,36,37,38,40,41,42,43,44,45,46,50,69,70,71,72,73,77,78,89,90,108,109,110,111,112,117,122,123,124,126,127,133,134,135,],[-68,62,-80,-62,-62,-58,-61,-63,-69,-70,-71,-72,-73,-78,-79,-77,-62,-62,-62,-62,-62,-59,-60,-66,-62,-53,-54,-55,-56,-57,-67,-65,-74,-75,-62,-64,-76,137,138,]),'ASSIGN':([28,95,96,97,98,99,100,101,],[61,126,-43,-44,-45,-46,-47,-48,]),'ELSE':([48,81,82,84,129,],[-10,118,-31,120,-32,]),'INT_TYPE':([62,],[96,]),'FLOAT_TYPE':([62,],[97,]),'LIST_TYPE':([62,],[98,]),'TUPLE_TYPE':([62,],[99,]),'MLP':([62,],[100,]),'TRANSFORMER':([62,],[101,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'stmt_list':([0,83,],[2,119,]),'stmt':([0,2,83,119,],[3,47,3,47,]),'simple_stmt':([0,2,49,51,83,118,119,120,131,],[4,4,82,82,4,82,4,82,82,]),'compound_stmt':([0,2,83,119,],[5,5,5,5,]),'small_stmt':([0,2,49,51,57,83,118,119,120,131,],[6,6,6,6,91,6,6,6,6,6,]),'if_stmt':([0,2,83,119,],[7,7,7,7,]),'while_stmt':([0,2,83,119,],[8,8,8,8,]),'funcdef_stmt':([0,2,83,119,],[9,9,9,9,]),'print':([0,2,83,119,],[10,10,10,10,]),'test':([0,2,15,16,49,51,57,58,59,83,118,119,120,131,],[11,11,49,51,11,11,11,92,93,11,11,11,11,11,]),'flow_stmt':([0,2,49,51,57,83,118,119,120,131,],[12,12,12,12,12,12,12,12,12,12,]),'dl_stmt':([0,2,49,51,57,83,118,119,120,131,],[13,13,13,13,13,13,13,13,13,13,]),'assign_expr':([0,2,49,51,57,83,118,119,120,131,],[14,14,14,14,14,14,14,14,14,14,]),'name':([0,2,15,16,17,19,22,31,32,33,34,35,39,49,51,53,54,57,58,59,61,63,64,65,66,67,68,69,70,71,72,73,74,79,83,85,90,118,119,120,126,131,],[18,18,18,18,52,18,18,74,75,76,18,18,18,18,18,18,87,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'comparison':([0,2,15,16,49,51,57,58,59,83,118,119,120,131,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'train_stmt':([0,2,49,51,57,83,118,119,120,131,],[25,25,25,25,25,25,25,25,25,25,]),'pred_stmt':([0,2,49,51,57,83,118,119,120,131,],[26,26,26,26,26,26,26,26,26,26,]),'save_stmt':([0,2,49,51,57,83,118,119,120,131,],[27,27,27,27,27,27,27,27,27,27,]),'expr':([0,2,15,16,19,22,39,49,51,53,57,58,59,61,63,64,65,66,67,68,69,70,71,72,73,74,79,83,85,90,118,119,120,126,131,],[29,29,29,29,56,56,56,29,29,56,29,29,29,94,102,103,104,105,106,107,108,109,110,111,112,56,116,29,56,124,29,29,29,133,29,]),'factor':([0,2,15,16,19,22,34,35,39,49,51,53,57,58,59,61,63,64,65,66,67,68,69,70,71,72,73,74,79,83,85,90,118,119,120,126,131,],[36,36,36,36,36,36,77,78,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'atom_expr':([0,2,15,16,19,22,34,35,39,49,51,53,57,58,59,61,63,64,65,66,67,68,69,70,71,72,73,74,79,83,85,90,118,119,120,126,131,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'atom':([0,2,15,16,19,22,34,35,39,49,51,53,54,57,58,59,61,63,64,65,66,67,68,69,70,71,72,73,74,79,83,85,90,118,119,120,126,131,],[38,38,38,38,38,38,38,38,38,38,38,38,88,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'number':([0,2,15,16,19,22,34,35,39,49,51,53,54,57,58,59,61,63,64,65,66,67,68,69,70,71,72,73,74,79,83,85,90,118,119,120,126,131,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'string':([0,2,15,16,19,22,34,35,39,49,51,53,54,57,58,59,61,63,64,65,66,67,68,69,70,71,72,73,74,79,83,85,90,118,119,120,126,131,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'list_expr':([19,22,39,53,74,85,126,],[55,60,80,86,113,121,135,]),'suite':([49,51,118,120,131,],[81,84,128,130,136,]),'basic_type':([62,],[95,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> stmt_list','program',1,'p_program','parser.py',16),
  ('stmt_list -> stmt_list stmt','stmt_list',2,'p_stmt_list','parser.py',20),
  ('stmt_list -> stmt','stmt_list',1,'p_stmt_list','parser.py',21),
  ('stmt -> simple_stmt','stmt',1,'p_stmt','parser.py',32),
  ('stmt -> compound_stmt','stmt',1,'p_stmt','parser.py',33),
  ('compound_stmt -> if_stmt','compound_stmt',1,'p_compound_stmt','parser.py',39),
  ('compound_stmt -> while_stmt','compound_stmt',1,'p_compound_stmt','parser.py',40),
  ('compound_stmt -> funcdef_stmt','compound_stmt',1,'p_compound_stmt','parser.py',41),
  ('compound_stmt -> print','compound_stmt',1,'p_compound_stmt','parser.py',42),
  ('simple_stmt -> small_stmt SEMICOLON','simple_stmt',2,'p_simple_stmt','parser.py',48),
  ('small_stmt -> test','small_stmt',1,'p_small_stmt','parser.py',55),
  ('small_stmt -> flow_stmt','small_stmt',1,'p_small_stmt','parser.py',56),
  ('small_stmt -> dl_stmt','small_stmt',1,'p_small_stmt','parser.py',57),
  ('small_stmt -> assign_expr','small_stmt',1,'p_small_stmt','parser.py',58),
  ('print -> PRINT LPAREN small_stmt RPAREN SEMICOLON','print',5,'p_print','parser.py',63),
  ('dl_stmt -> train_stmt','dl_stmt',1,'p_dl_stmt','parser.py',67),
  ('dl_stmt -> pred_stmt','dl_stmt',1,'p_dl_stmt','parser.py',68),
  ('dl_stmt -> save_stmt','dl_stmt',1,'p_dl_stmt','parser.py',69),
  ('train_stmt -> TRAIN name list_expr','train_stmt',3,'p_train_stmt','parser.py',74),
  ('pred_stmt -> PRED name STRING','pred_stmt',3,'p_pred_stmt','parser.py',79),
  ('save_stmt -> SAVE name STRING','save_stmt',3,'p_save_stmt','parser.py',84),
  ('flow_stmt -> RETURN','flow_stmt',1,'p_flow_stmt','parser.py',90),
  ('flow_stmt -> RETURN list_expr','flow_stmt',2,'p_flow_stmt','parser.py',91),
  ('flow_stmt -> BREAK','flow_stmt',1,'p_flow_stmt','parser.py',92),
  ('flow_stmt -> CONTINUE','flow_stmt',1,'p_flow_stmt','parser.py',93),
  ('while_stmt -> WHILE test suite','while_stmt',3,'p_while_stmt','parser.py',102),
  ('while_stmt -> WHILE test suite ELSE suite','while_stmt',5,'p_while_stmt','parser.py',103),
  ('if_stmt -> IF test suite','if_stmt',3,'p_if_stmt','parser.py',112),
  ('if_stmt -> IF test suite ELSE suite','if_stmt',5,'p_if_stmt','parser.py',113),
  ('funcdef_stmt -> DEF name LPAREN list_expr RPAREN suite','funcdef_stmt',6,'p_funcdef_stmt','parser.py',121),
  ('suite -> simple_stmt','suite',1,'p_suite','parser.py',126),
  ('suite -> LBRACK stmt_list RBRACK','suite',3,'p_suite','parser.py',127),
  ('test -> comparison OR test','test',3,'p_test','parser.py',137),
  ('test -> comparison AND test','test',3,'p_test','parser.py',138),
  ('test -> comparison','test',1,'p_test','parser.py',139),
  ('comparison -> expr GT expr','comparison',3,'p_comparison','parser.py',148),
  ('comparison -> expr LT expr','comparison',3,'p_comparison','parser.py',149),
  ('comparison -> expr GTE expr','comparison',3,'p_comparison','parser.py',150),
  ('comparison -> expr LTE expr','comparison',3,'p_comparison','parser.py',151),
  ('comparison -> expr EQ expr','comparison',3,'p_comparison','parser.py',152),
  ('comparison -> expr NEQ expr','comparison',3,'p_comparison','parser.py',153),
  ('comparison -> expr','comparison',1,'p_comparison','parser.py',154),
  ('basic_type -> INT_TYPE','basic_type',1,'p_basic_type','parser.py',162),
  ('basic_type -> FLOAT_TYPE','basic_type',1,'p_basic_type','parser.py',163),
  ('basic_type -> LIST_TYPE','basic_type',1,'p_basic_type','parser.py',164),
  ('basic_type -> TUPLE_TYPE','basic_type',1,'p_basic_type','parser.py',165),
  ('basic_type -> MLP','basic_type',1,'p_basic_type','parser.py',166),
  ('basic_type -> TRANSFORMER','basic_type',1,'p_basic_type','parser.py',167),
  ('assign_expr -> NAME ASSIGN expr','assign_expr',3,'p_assign_expr','parser.py',172),
  ('assign_expr -> NAME COLON basic_type ASSIGN expr','assign_expr',5,'p_assign_expr','parser.py',173),
  ('assign_expr -> NAME COLON basic_type ASSIGN STRING COLON STRING','assign_expr',7,'p_assign_expr','parser.py',174),
  ('assign_expr -> NAME COLON basic_type ASSIGN list_expr COLON STRING','assign_expr',7,'p_assign_expr','parser.py',175),
  ('expr -> expr PLUS expr','expr',3,'p_expr','parser.py',188),
  ('expr -> expr MINUS expr','expr',3,'p_expr','parser.py',189),
  ('expr -> expr TIMES expr','expr',3,'p_expr','parser.py',190),
  ('expr -> expr DIVIDE expr','expr',3,'p_expr','parser.py',191),
  ('expr -> expr MOD expr','expr',3,'p_expr','parser.py',192),
  ('expr -> factor','expr',1,'p_expr','parser.py',193),
  ('factor -> PLUS factor','factor',2,'p_factor','parser.py',202),
  ('factor -> MINUS factor','factor',2,'p_factor','parser.py',203),
  ('factor -> atom_expr','factor',1,'p_factor','parser.py',204),
  ('atom_expr -> <empty>','atom_expr',0,'p_atom_expr','parser.py',210),
  ('atom_expr -> atom','atom_expr',1,'p_atom_expr','parser.py',211),
  ('atom_expr -> atom_expr LSQBRACK expr RSQBRACK','atom_expr',4,'p_atom_expr','parser.py',212),
  ('atom_expr -> name LPAREN list_expr RPAREN','atom_expr',4,'p_atom_expr','parser.py',213),
  ('atom -> LPAREN list_expr RPAREN','atom',3,'p_atom','parser.py',226),
  ('atom -> LSQBRACK list_expr RSQBRACK','atom',3,'p_atom','parser.py',227),
  ('atom -> name','atom',1,'p_atom','parser.py',228),
  ('atom -> number','atom',1,'p_atom','parser.py',229),
  ('atom -> string','atom',1,'p_atom','parser.py',230),
  ('atom -> TRUE','atom',1,'p_atom','parser.py',231),
  ('atom -> FALSE','atom',1,'p_atom','parser.py',232),
  ('atom -> NONE','atom',1,'p_atom','parser.py',233),
  ('atom -> name LSQBRACK atom RSQBRACK','atom',4,'p_atom','parser.py',234),
  ('list_expr -> list_expr COMMA expr','list_expr',3,'p_list_expr','parser.py',252),
  ('list_expr -> expr','list_expr',1,'p_list_expr','parser.py',253),
  ('name -> NAME','name',1,'p_name','parser.py',263),
  ('number -> INT','number',1,'p_number','parser.py',267),
  ('number -> FLOAT','number',1,'p_number','parser.py',268),
  ('string -> STRING','string',1,'p_string','parser.py',273),
]