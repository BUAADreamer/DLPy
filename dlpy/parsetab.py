
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocLTGTLTEGTEleftPLUSMINUSleftTIMESDIVIDEAND ASSIGN BREAK CHAT COLON COMMA CONTINUE DEF DIVIDE ELSE EQ FALSE FLOAT FLOAT_TYPE GT GTE IF INT INT_TYPE LBRACK LIST_TYPE LPAREN LSQBRACK LT LTE MINUS MLP MOD NAME NEQ NONE OR PLUS PRED PRINT RBRACK RETURN RPAREN RSQBRACK SAVE SCAN SEMICOLON STRING TIMES TRAIN TRANSFORMER TRUE TUPLE_TYPE WHILEprogram : stmt_liststmt_list : stmt_list stmt\n                    | stmt\n        stmt : simple_stmt\n                | compound_stmt\n        compound_stmt : if_stmt\n                        | while_stmt\n                        | funcdef_stmt\n                        | print\n        simple_stmt : small_stmt SEMICOLON\n        small_stmt : test\n                    | flow_stmt\n                    | dl_stmt\n                    | assign_expr\n        print : PRINT LPAREN small_stmt RPAREN SEMICOLONdl_stmt : train_stmt\n                    | pred_stmt\n                    | save_stmt\n                    | chat_stmt\n        train_stmt : TRAIN name list_expr\n        pred_stmt : PRED name STRING\n        save_stmt : SAVE name STRING\n        chat_stmt : CHAT name name\n        flow_stmt : RETURN\n                    | RETURN list_expr\n                    | BREAK\n                    | CONTINUE\n        while_stmt : WHILE test suite\n                    | WHILE test suite ELSE suite\n        if_stmt : IF test suite\n                    | IF test suite ELSE suite\n        funcdef_stmt : DEF name LPAREN list_expr RPAREN suite \n                        | DEF name LPAREN RPAREN suite\n        suite : simple_stmt\n                | LBRACK stmt_list RBRACK\n        test : comparison OR test\n                | comparison AND test\n                | comparison\n        comparison : expr GT expr\n                    | expr LT expr\n                    | expr GTE expr\n                    | expr LTE expr\n                    | expr EQ expr\n                    | expr NEQ expr\n                    | expr\n        basic_type : INT_TYPE \n                        | FLOAT_TYPE\n                        | LIST_TYPE\n                        | TUPLE_TYPE\n                        | MLP\n                        | TRANSFORMER\n        assign_expr : NAME ASSIGN expr\n                | NAME COLON basic_type ASSIGN expr\n                | NAME COLON basic_type ASSIGN STRING COLON STRING\n                | NAME COLON basic_type ASSIGN list_expr COLON STRING\n                | NAME ASSIGN SCAN LPAREN RPAREN\n        expr : expr PLUS expr\n                | expr MINUS expr\n                | expr TIMES expr\n                | expr DIVIDE expr\n                | expr MOD expr\n                | factor\n        factor : PLUS factor\n                | MINUS factor\n                | atom_expratom_expr : atom \n                     | atom_expr LSQBRACK expr RSQBRACK\n                     | name LPAREN list_expr RPAREN\n                     atom : LPAREN list_expr RPAREN\n                | LSQBRACK list_expr RSQBRACK\n                | name\n                | number\n                | string\n                | TRUE\n                | FALSE\n                | NONE\n                | name LSQBRACK atom RSQBRACK\n        list_expr : list_expr COMMA expr\n                    | expr\n        name : NAMEnumber : INT\n                | FLOAT\n        string : STRING'
    
_lr_action_items = {'IF':([0,2,3,4,5,7,8,9,10,49,50,84,85,86,87,124,135,136,137,139,140,145,],[15,15,-3,-4,-5,-6,-7,-8,-9,-2,-10,-30,-34,15,-28,15,-31,-35,-29,-33,-15,-32,]),'WHILE':([0,2,3,4,5,7,8,9,10,49,50,84,85,86,87,124,135,136,137,139,140,145,],[16,16,-3,-4,-5,-6,-7,-8,-9,-2,-10,-30,-34,16,-28,16,-31,-35,-29,-33,-15,-32,]),'DEF':([0,2,3,4,5,7,8,9,10,49,50,84,85,86,87,124,135,136,137,139,140,145,],[17,17,-3,-4,-5,-6,-7,-8,-9,-2,-10,-30,-34,17,-28,17,-31,-35,-29,-33,-15,-32,]),'PRINT':([0,2,3,4,5,7,8,9,10,49,50,84,85,86,87,124,135,136,137,139,140,145,],[20,20,-3,-4,-5,-6,-7,-8,-9,-2,-10,-30,-34,20,-28,20,-31,-35,-29,-33,-15,-32,]),'RETURN':([0,2,3,4,5,7,8,9,10,18,21,30,31,38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,59,80,81,84,85,86,87,92,95,96,106,107,108,109,110,111,112,113,114,115,116,122,123,124,125,127,128,129,134,135,136,137,138,139,140,145,],[22,22,-3,-4,-5,-6,-7,-8,-9,-71,-38,-45,-83,-62,-65,-66,-72,-73,-74,-75,-76,-81,-82,-2,-10,22,-80,22,22,-63,-64,-30,-34,22,-28,-69,-36,-37,-39,-40,-41,-42,-43,-44,-57,-58,-59,-60,-61,-70,22,22,22,22,-68,-77,-67,-31,-35,-29,22,-33,-15,-32,]),'BREAK':([0,2,3,4,5,7,8,9,10,18,21,30,31,38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,59,80,81,84,85,86,87,92,95,96,106,107,108,109,110,111,112,113,114,115,116,122,123,124,125,127,128,129,134,135,136,137,138,139,140,145,],[23,23,-3,-4,-5,-6,-7,-8,-9,-71,-38,-45,-83,-62,-65,-66,-72,-73,-74,-75,-76,-81,-82,-2,-10,23,-80,23,23,-63,-64,-30,-34,23,-28,-69,-36,-37,-39,-40,-41,-42,-43,-44,-57,-58,-59,-60,-61,-70,23,23,23,23,-68,-77,-67,-31,-35,-29,23,-33,-15,-32,]),'CONTINUE':([0,2,3,4,5,7,8,9,10,18,21,30,31,38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,59,80,81,84,85,86,87,92,95,96,106,107,108,109,110,111,112,113,114,115,116,122,123,124,125,127,128,129,134,135,136,137,138,139,140,145,],[24,24,-3,-4,-5,-6,-7,-8,-9,-71,-38,-45,-83,-62,-65,-66,-72,-73,-74,-75,-76,-81,-82,-2,-10,24,-80,24,24,-63,-64,-30,-34,24,-28,-69,-36,-37,-39,-40,-41,-42,-43,-44,-57,-58,-59,-60,-61,-70,24,24,24,24,-68,-77,-67,-31,-35,-29,24,-33,-15,-32,]),'NAME':([0,2,3,4,5,7,8,9,10,15,16,17,18,19,21,22,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,59,60,61,63,65,66,67,68,69,70,71,72,73,74,75,76,79,80,81,82,84,85,86,87,88,92,93,95,96,106,107,108,109,110,111,112,113,114,115,116,122,123,124,125,127,128,129,133,134,135,136,137,138,139,140,145,],[29,29,-3,-4,-5,-6,-7,-8,-9,52,52,52,-71,52,-38,52,-45,-83,52,52,52,52,52,52,-62,-65,-66,52,-72,-73,-74,-75,-76,-81,-82,-2,-10,29,-80,29,52,52,29,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,-63,-64,52,-30,-34,29,-28,52,-69,52,-36,-37,-39,-40,-41,-42,-43,-44,-57,-58,-59,-60,-61,-70,29,29,29,29,-68,-77,52,-67,-31,-35,-29,29,-33,-15,-32,]),'TRAIN':([0,2,3,4,5,7,8,9,10,18,21,30,31,38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,59,80,81,84,85,86,87,92,95,96,106,107,108,109,110,111,112,113,114,115,116,122,123,124,125,127,128,129,134,135,136,137,138,139,140,145,],[32,32,-3,-4,-5,-6,-7,-8,-9,-71,-38,-45,-83,-62,-65,-66,-72,-73,-74,-75,-76,-81,-82,-2,-10,32,-80,32,32,-63,-64,-30,-34,32,-28,-69,-36,-37,-39,-40,-41,-42,-43,-44,-57,-58,-59,-60,-61,-70,32,32,32,32,-68,-77,-67,-31,-35,-29,32,-33,-15,-32,]),'PRED':([0,2,3,4,5,7,8,9,10,18,21,30,31,38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,59,80,81,84,85,86,87,92,95,96,106,107,108,109,110,111,112,113,114,115,116,122,123,124,125,127,128,129,134,135,136,137,138,139,140,145,],[33,33,-3,-4,-5,-6,-7,-8,-9,-71,-38,-45,-83,-62,-65,-66,-72,-73,-74,-75,-76,-81,-82,-2,-10,33,-80,33,33,-63,-64,-30,-34,33,-28,-69,-36,-37,-39,-40,-41,-42,-43,-44,-57,-58,-59,-60,-61,-70,33,33,33,33,-68,-77,-67,-31,-35,-29,33,-33,-15,-32,]),'SAVE':([0,2,3,4,5,7,8,9,10,18,21,30,31,38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,59,80,81,84,85,86,87,92,95,96,106,107,108,109,110,111,112,113,114,115,116,122,123,124,125,127,128,129,134,135,136,137,138,139,140,145,],[34,34,-3,-4,-5,-6,-7,-8,-9,-71,-38,-45,-83,-62,-65,-66,-72,-73,-74,-75,-76,-81,-82,-2,-10,34,-80,34,34,-63,-64,-30,-34,34,-28,-69,-36,-37,-39,-40,-41,-42,-43,-44,-57,-58,-59,-60,-61,-70,34,34,34,34,-68,-77,-67,-31,-35,-29,34,-33,-15,-32,]),'CHAT':([0,2,3,4,5,7,8,9,10,18,21,30,31,38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,59,80,81,84,85,86,87,92,95,96,106,107,108,109,110,111,112,113,114,115,116,122,123,124,125,127,128,129,134,135,136,137,138,139,140,145,],[35,35,-3,-4,-5,-6,-7,-8,-9,-71,-38,-45,-83,-62,-65,-66,-72,-73,-74,-75,-76,-81,-82,-2,-10,35,-80,35,35,-63,-64,-30,-34,35,-28,-69,-36,-37,-39,-40,-41,-42,-43,-44,-57,-58,-59,-60,-61,-70,35,35,35,35,-68,-77,-67,-31,-35,-29,35,-33,-15,-32,]),'PLUS':([0,2,3,4,5,7,8,9,10,15,16,18,19,21,22,29,30,31,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,58,59,60,61,63,65,66,67,68,69,70,71,72,73,74,75,76,80,81,82,84,85,86,87,88,92,93,95,96,97,106,107,108,109,110,111,112,113,114,115,116,121,122,123,124,125,127,128,129,130,133,134,135,136,137,138,139,140,142,143,145,],[36,36,-3,-4,-5,-6,-7,-8,-9,36,36,-71,36,-38,36,-80,71,-83,36,36,-62,-65,-66,36,-72,-73,-74,-75,-76,-81,-82,-2,-10,36,-80,36,36,71,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-63,-64,36,-30,-34,36,-28,36,-69,36,-36,-37,71,71,71,71,71,71,71,-57,-58,-59,-60,71,71,-70,36,36,36,36,-68,-77,71,36,-67,-31,-35,-29,36,-33,-15,71,-83,-32,]),'MINUS':([0,2,3,4,5,7,8,9,10,15,16,18,19,21,22,29,30,31,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,58,59,60,61,63,65,66,67,68,69,70,71,72,73,74,75,76,80,81,82,84,85,86,87,88,92,93,95,96,97,106,107,108,109,110,111,112,113,114,115,116,121,122,123,124,125,127,128,129,130,133,134,135,136,137,138,139,140,142,143,145,],[37,37,-3,-4,-5,-6,-7,-8,-9,37,37,-71,37,-38,37,-80,72,-83,37,37,-62,-65,-66,37,-72,-73,-74,-75,-76,-81,-82,-2,-10,37,-80,37,37,72,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-63,-64,37,-30,-34,37,-28,37,-69,37,-36,-37,72,72,72,72,72,72,72,-57,-58,-59,-60,72,72,-70,37,37,37,37,-68,-77,72,37,-67,-31,-35,-29,37,-33,-15,72,-83,-32,]),'LPAREN':([0,2,3,4,5,7,8,9,10,15,16,18,19,20,21,22,29,30,31,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,59,60,61,63,65,66,67,68,69,70,71,72,73,74,75,76,80,81,82,84,85,86,87,88,92,93,95,96,98,106,107,108,109,110,111,112,113,114,115,116,122,123,124,125,127,128,129,133,134,135,136,137,138,139,140,145,],[19,19,-3,-4,-5,-6,-7,-8,-9,19,19,55,19,59,-38,19,-80,-45,-83,19,19,-62,-65,-66,19,-72,-73,-74,-75,-76,-81,-82,-2,-10,19,-80,19,88,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-63,-64,19,-30,-34,19,-28,19,-69,19,-36,-37,132,-39,-40,-41,-42,-43,-44,-57,-58,-59,-60,-61,-70,19,19,19,19,-68,-77,19,-67,-31,-35,-29,19,-33,-15,-32,]),'LSQBRACK':([0,2,3,4,5,7,8,9,10,15,16,18,19,21,22,29,30,31,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,59,60,61,63,65,66,67,68,69,70,71,72,73,74,75,76,80,81,82,84,85,86,87,88,90,92,93,95,96,106,107,108,109,110,111,112,113,114,115,116,122,123,124,125,127,128,129,133,134,135,136,137,138,139,140,143,145,],[41,41,-3,-4,-5,-6,-7,-8,-9,41,41,56,41,-38,41,-80,-45,-83,41,41,-62,82,-66,41,-72,-73,-74,-75,-76,-81,-82,-2,-10,41,-80,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,-63,-64,41,-30,-34,41,-28,41,56,-69,41,-36,-37,-39,-40,-41,-42,-43,-44,-57,-58,-59,-60,-61,-70,41,41,41,41,-68,-77,41,-67,-31,-35,-29,41,-33,-15,-83,-32,]),'TRUE':([0,2,3,4,5,7,8,9,10,15,16,18,19,21,22,30,31,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,59,60,61,63,65,66,67,68,69,70,71,72,73,74,75,76,80,81,82,84,85,86,87,88,92,93,95,96,106,107,108,109,110,111,112,113,114,115,116,122,123,124,125,127,128,129,133,134,135,136,137,138,139,140,145,],[44,44,-3,-4,-5,-6,-7,-8,-9,44,44,-71,44,-38,44,-45,-83,44,44,-62,-65,-66,44,-72,-73,-74,-75,-76,-81,-82,-2,-10,44,-80,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,-63,-64,44,-30,-34,44,-28,44,-69,44,-36,-37,-39,-40,-41,-42,-43,-44,-57,-58,-59,-60,-61,-70,44,44,44,44,-68,-77,44,-67,-31,-35,-29,44,-33,-15,-32,]),'FALSE':([0,2,3,4,5,7,8,9,10,15,16,18,19,21,22,30,31,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,59,60,61,63,65,66,67,68,69,70,71,72,73,74,75,76,80,81,82,84,85,86,87,88,92,93,95,96,106,107,108,109,110,111,112,113,114,115,116,122,123,124,125,127,128,129,133,134,135,136,137,138,139,140,145,],[45,45,-3,-4,-5,-6,-7,-8,-9,45,45,-71,45,-38,45,-45,-83,45,45,-62,-65,-66,45,-72,-73,-74,-75,-76,-81,-82,-2,-10,45,-80,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-63,-64,45,-30,-34,45,-28,45,-69,45,-36,-37,-39,-40,-41,-42,-43,-44,-57,-58,-59,-60,-61,-70,45,45,45,45,-68,-77,45,-67,-31,-35,-29,45,-33,-15,-32,]),'NONE':([0,2,3,4,5,7,8,9,10,15,16,18,19,21,22,30,31,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,59,60,61,63,65,66,67,68,69,70,71,72,73,74,75,76,80,81,82,84,85,86,87,88,92,93,95,96,106,107,108,109,110,111,112,113,114,115,116,122,123,124,125,127,128,129,133,134,135,136,137,138,139,140,145,],[46,46,-3,-4,-5,-6,-7,-8,-9,46,46,-71,46,-38,46,-45,-83,46,46,-62,-65,-66,46,-72,-73,-74,-75,-76,-81,-82,-2,-10,46,-80,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-63,-64,46,-30,-34,46,-28,46,-69,46,-36,-37,-39,-40,-41,-42,-43,-44,-57,-58,-59,-60,-61,-70,46,46,46,46,-68,-77,46,-67,-31,-35,-29,46,-33,-15,-32,]),'INT':([0,2,3,4,5,7,8,9,10,15,16,18,19,21,22,30,31,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,59,60,61,63,65,66,67,68,69,70,71,72,73,74,75,76,80,81,82,84,85,86,87,88,92,93,95,96,106,107,108,109,110,111,112,113,114,115,116,122,123,124,125,127,128,129,133,134,135,136,137,138,139,140,145,],[47,47,-3,-4,-5,-6,-7,-8,-9,47,47,-71,47,-38,47,-45,-83,47,47,-62,-65,-66,47,-72,-73,-74,-75,-76,-81,-82,-2,-10,47,-80,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-63,-64,47,-30,-34,47,-28,47,-69,47,-36,-37,-39,-40,-41,-42,-43,-44,-57,-58,-59,-60,-61,-70,47,47,47,47,-68,-77,47,-67,-31,-35,-29,47,-33,-15,-32,]),'FLOAT':([0,2,3,4,5,7,8,9,10,15,16,18,19,21,22,30,31,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,59,60,61,63,65,66,67,68,69,70,71,72,73,74,75,76,80,81,82,84,85,86,87,88,92,93,95,96,106,107,108,109,110,111,112,113,114,115,116,122,123,124,125,127,128,129,133,134,135,136,137,138,139,140,145,],[48,48,-3,-4,-5,-6,-7,-8,-9,48,48,-71,48,-38,48,-45,-83,48,48,-62,-65,-66,48,-72,-73,-74,-75,-76,-81,-82,-2,-10,48,-80,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-63,-64,48,-30,-34,48,-28,48,-69,48,-36,-37,-39,-40,-41,-42,-43,-44,-57,-58,-59,-60,-61,-70,48,48,48,48,-68,-77,48,-67,-31,-35,-29,48,-33,-15,-32,]),'STRING':([0,2,3,4,5,7,8,9,10,15,16,18,19,21,22,30,31,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,55,56,59,60,61,63,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,81,82,84,85,86,87,88,92,93,95,96,106,107,108,109,110,111,112,113,114,115,116,122,123,124,125,127,128,129,133,134,135,136,137,138,139,140,145,146,147,],[31,31,-3,-4,-5,-6,-7,-8,-9,31,31,-71,31,-38,31,-45,-83,31,31,-62,-65,-66,31,-72,-73,-74,-75,-76,-81,-82,-2,-10,31,-80,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,118,119,-63,-64,31,-30,-34,31,-28,31,-69,31,-36,-37,-39,-40,-41,-42,-43,-44,-57,-58,-59,-60,-61,-70,31,31,31,31,-68,-77,143,-67,-31,-35,-29,31,-33,-15,-32,148,149,]),'$end':([1,2,3,4,5,7,8,9,10,49,50,84,85,87,135,136,137,139,140,145,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-2,-10,-30,-34,-28,-31,-35,-29,-33,-15,-32,]),'RBRACK':([3,4,5,7,8,9,10,49,50,84,85,87,124,135,136,137,139,140,145,],[-3,-4,-5,-6,-7,-8,-9,-2,-10,-30,-34,-28,136,-31,-35,-29,-33,-15,-32,]),'SEMICOLON':([6,11,12,13,14,18,21,22,23,24,25,26,27,28,29,30,31,38,39,40,42,43,44,45,46,47,48,52,58,62,80,81,92,95,96,97,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,122,128,129,130,131,134,141,142,143,148,149,],[50,-11,-12,-13,-14,-71,-38,-24,-26,-27,-16,-17,-18,-19,-80,-45,-83,-62,-65,-66,-72,-73,-74,-75,-76,-81,-82,-80,-79,-25,-63,-64,-69,-36,-37,-52,-39,-40,-41,-42,-43,-44,-57,-58,-59,-60,-61,-20,-21,-22,-23,-70,-68,-77,-78,140,-67,-56,-53,-83,-54,-55,]),'RPAREN':([11,12,13,14,18,21,22,23,24,25,26,27,28,29,30,31,38,39,40,42,43,44,45,46,47,48,52,57,58,62,80,81,88,89,92,94,95,96,97,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,122,126,128,129,130,132,134,141,142,143,148,149,],[-11,-12,-13,-14,-71,-38,-24,-26,-27,-16,-17,-18,-19,-80,-45,-83,-62,-65,-66,-72,-73,-74,-75,-76,-81,-82,-80,92,-79,-25,-63,-64,127,128,-69,131,-36,-37,-52,-39,-40,-41,-42,-43,-44,-57,-58,-59,-60,-61,-20,-21,-22,-23,-70,138,-68,-77,-78,141,-67,-56,-53,-83,-54,-55,]),'GT':([18,29,30,31,38,39,40,42,43,44,45,46,47,48,52,80,81,92,112,113,114,115,116,122,128,129,134,],[-71,-80,65,-83,-62,-65,-66,-72,-73,-74,-75,-76,-81,-82,-80,-63,-64,-69,-57,-58,-59,-60,-61,-70,-68,-77,-67,]),'LT':([18,29,30,31,38,39,40,42,43,44,45,46,47,48,52,80,81,92,112,113,114,115,116,122,128,129,134,],[-71,-80,66,-83,-62,-65,-66,-72,-73,-74,-75,-76,-81,-82,-80,-63,-64,-69,-57,-58,-59,-60,-61,-70,-68,-77,-67,]),'GTE':([18,29,30,31,38,39,40,42,43,44,45,46,47,48,52,80,81,92,112,113,114,115,116,122,128,129,134,],[-71,-80,67,-83,-62,-65,-66,-72,-73,-74,-75,-76,-81,-82,-80,-63,-64,-69,-57,-58,-59,-60,-61,-70,-68,-77,-67,]),'LTE':([18,29,30,31,38,39,40,42,43,44,45,46,47,48,52,80,81,92,112,113,114,115,116,122,128,129,134,],[-71,-80,68,-83,-62,-65,-66,-72,-73,-74,-75,-76,-81,-82,-80,-63,-64,-69,-57,-58,-59,-60,-61,-70,-68,-77,-67,]),'EQ':([18,29,30,31,38,39,40,42,43,44,45,46,47,48,52,80,81,92,112,113,114,115,116,122,128,129,134,],[-71,-80,69,-83,-62,-65,-66,-72,-73,-74,-75,-76,-81,-82,-80,-63,-64,-69,-57,-58,-59,-60,-61,-70,-68,-77,-67,]),'NEQ':([18,29,30,31,38,39,40,42,43,44,45,46,47,48,52,80,81,92,112,113,114,115,116,122,128,129,134,],[-71,-80,70,-83,-62,-65,-66,-72,-73,-74,-75,-76,-81,-82,-80,-63,-64,-69,-57,-58,-59,-60,-61,-70,-68,-77,-67,]),'TIMES':([18,29,30,31,38,39,40,42,43,44,45,46,47,48,52,58,80,81,92,97,106,107,108,109,110,111,112,113,114,115,116,121,122,128,129,130,134,142,143,],[-71,-80,73,-83,-62,-65,-66,-72,-73,-74,-75,-76,-81,-82,-80,73,-63,-64,-69,73,73,73,73,73,73,73,73,73,-59,-60,73,73,-70,-68,-77,73,-67,73,-83,]),'DIVIDE':([18,29,30,31,38,39,40,42,43,44,45,46,47,48,52,58,80,81,92,97,106,107,108,109,110,111,112,113,114,115,116,121,122,128,129,130,134,142,143,],[-71,-80,74,-83,-62,-65,-66,-72,-73,-74,-75,-76,-81,-82,-80,74,-63,-64,-69,74,74,74,74,74,74,74,74,74,-59,-60,74,74,-70,-68,-77,74,-67,74,-83,]),'MOD':([18,29,30,31,38,39,40,42,43,44,45,46,47,48,52,58,80,81,92,97,106,107,108,109,110,111,112,113,114,115,116,121,122,128,129,130,134,142,143,],[-71,-80,75,-83,-62,-65,-66,-72,-73,-74,-75,-76,-81,-82,-80,75,-63,-64,-69,75,75,75,75,75,75,75,-57,-58,-59,-60,75,75,-70,-68,-77,75,-67,75,-83,]),'OR':([18,21,29,30,31,38,39,40,42,43,44,45,46,47,48,52,80,81,92,106,107,108,109,110,111,112,113,114,115,116,122,128,129,134,],[-71,60,-80,-45,-83,-62,-65,-66,-72,-73,-74,-75,-76,-81,-82,-80,-63,-64,-69,-39,-40,-41,-42,-43,-44,-57,-58,-59,-60,-61,-70,-68,-77,-67,]),'AND':([18,21,29,30,31,38,39,40,42,43,44,45,46,47,48,52,80,81,92,106,107,108,109,110,111,112,113,114,115,116,122,128,129,134,],[-71,61,-80,-45,-83,-62,-65,-66,-72,-73,-74,-75,-76,-81,-82,-80,-63,-64,-69,-39,-40,-41,-42,-43,-44,-57,-58,-59,-60,-61,-70,-68,-77,-67,]),'LBRACK':([18,21,30,31,38,39,40,42,43,44,45,46,47,48,51,52,53,80,81,92,95,96,106,107,108,109,110,111,112,113,114,115,116,122,123,125,127,128,129,134,138,],[-71,-38,-45,-83,-62,-65,-66,-72,-73,-74,-75,-76,-81,-82,86,-80,86,-63,-64,-69,-36,-37,-39,-40,-41,-42,-43,-44,-57,-58,-59,-60,-61,-70,86,86,86,-68,-77,-67,86,]),'COMMA':([18,31,38,39,40,42,43,44,45,46,47,48,52,57,58,62,80,81,83,89,92,112,113,114,115,116,117,122,126,128,129,130,134,142,143,144,],[-71,-83,-62,-65,-66,-72,-73,-74,-75,-76,-81,-82,-80,93,-79,93,-63,-64,93,93,-69,-57,-58,-59,-60,-61,93,-70,93,-68,-77,-78,-67,-79,-83,93,]),'RSQBRACK':([18,31,38,39,40,42,43,44,45,46,47,48,52,58,80,81,83,90,91,92,112,113,114,115,116,121,122,128,129,130,134,],[-71,-83,-62,-65,-66,-72,-73,-74,-75,-76,-81,-82,-80,-79,-63,-64,122,-71,129,-69,-57,-58,-59,-60,-61,134,-70,-68,-77,-78,-67,]),'COLON':([18,29,31,38,39,40,42,43,44,45,46,47,48,52,80,81,92,112,113,114,115,116,122,128,129,130,134,142,143,144,],[-71,64,-83,-62,-65,-66,-72,-73,-74,-75,-76,-81,-82,-80,-63,-64,-69,-57,-58,-59,-60,-61,-70,-68,-77,-78,-67,-79,146,147,]),'ASSIGN':([29,99,100,101,102,103,104,105,],[63,133,-46,-47,-48,-49,-50,-51,]),'ELSE':([50,84,85,87,136,],[-10,123,-34,125,-35,]),'SCAN':([63,],[98,]),'INT_TYPE':([64,],[100,]),'FLOAT_TYPE':([64,],[101,]),'LIST_TYPE':([64,],[102,]),'TUPLE_TYPE':([64,],[103,]),'MLP':([64,],[104,]),'TRANSFORMER':([64,],[105,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'stmt_list':([0,86,],[2,124,]),'stmt':([0,2,86,124,],[3,49,3,49,]),'simple_stmt':([0,2,51,53,86,123,124,125,127,138,],[4,4,85,85,4,85,4,85,85,85,]),'compound_stmt':([0,2,86,124,],[5,5,5,5,]),'small_stmt':([0,2,51,53,59,86,123,124,125,127,138,],[6,6,6,6,94,6,6,6,6,6,6,]),'if_stmt':([0,2,86,124,],[7,7,7,7,]),'while_stmt':([0,2,86,124,],[8,8,8,8,]),'funcdef_stmt':([0,2,86,124,],[9,9,9,9,]),'print':([0,2,86,124,],[10,10,10,10,]),'test':([0,2,15,16,51,53,59,60,61,86,123,124,125,127,138,],[11,11,51,53,11,11,11,95,96,11,11,11,11,11,11,]),'flow_stmt':([0,2,51,53,59,86,123,124,125,127,138,],[12,12,12,12,12,12,12,12,12,12,12,]),'dl_stmt':([0,2,51,53,59,86,123,124,125,127,138,],[13,13,13,13,13,13,13,13,13,13,13,]),'assign_expr':([0,2,51,53,59,86,123,124,125,127,138,],[14,14,14,14,14,14,14,14,14,14,14,]),'name':([0,2,15,16,17,19,22,32,33,34,35,36,37,41,51,53,55,56,59,60,61,63,65,66,67,68,69,70,71,72,73,74,75,76,79,82,86,88,93,123,124,125,127,133,138,],[18,18,18,18,54,18,18,76,77,78,79,18,18,18,18,18,18,90,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,120,18,18,18,18,18,18,18,18,18,18,]),'comparison':([0,2,15,16,51,53,59,60,61,86,123,124,125,127,138,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'train_stmt':([0,2,51,53,59,86,123,124,125,127,138,],[25,25,25,25,25,25,25,25,25,25,25,]),'pred_stmt':([0,2,51,53,59,86,123,124,125,127,138,],[26,26,26,26,26,26,26,26,26,26,26,]),'save_stmt':([0,2,51,53,59,86,123,124,125,127,138,],[27,27,27,27,27,27,27,27,27,27,27,]),'chat_stmt':([0,2,51,53,59,86,123,124,125,127,138,],[28,28,28,28,28,28,28,28,28,28,28,]),'expr':([0,2,15,16,19,22,41,51,53,55,59,60,61,63,65,66,67,68,69,70,71,72,73,74,75,76,82,86,88,93,123,124,125,127,133,138,],[30,30,30,30,58,58,58,30,30,58,30,30,30,97,106,107,108,109,110,111,112,113,114,115,116,58,121,30,58,130,30,30,30,30,142,30,]),'factor':([0,2,15,16,19,22,36,37,41,51,53,55,59,60,61,63,65,66,67,68,69,70,71,72,73,74,75,76,82,86,88,93,123,124,125,127,133,138,],[38,38,38,38,38,38,80,81,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'atom_expr':([0,2,15,16,19,22,36,37,41,51,53,55,59,60,61,63,65,66,67,68,69,70,71,72,73,74,75,76,82,86,88,93,123,124,125,127,133,138,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'atom':([0,2,15,16,19,22,36,37,41,51,53,55,56,59,60,61,63,65,66,67,68,69,70,71,72,73,74,75,76,82,86,88,93,123,124,125,127,133,138,],[40,40,40,40,40,40,40,40,40,40,40,40,91,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'number':([0,2,15,16,19,22,36,37,41,51,53,55,56,59,60,61,63,65,66,67,68,69,70,71,72,73,74,75,76,82,86,88,93,123,124,125,127,133,138,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'string':([0,2,15,16,19,22,36,37,41,51,53,55,56,59,60,61,63,65,66,67,68,69,70,71,72,73,74,75,76,82,86,88,93,123,124,125,127,133,138,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'list_expr':([19,22,41,55,76,88,133,],[57,62,83,89,117,126,144,]),'suite':([51,53,123,125,127,138,],[84,87,135,137,139,145,]),'basic_type':([64,],[99,]),}

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
  ('dl_stmt -> chat_stmt','dl_stmt',1,'p_dl_stmt','parser.py',70),
  ('train_stmt -> TRAIN name list_expr','train_stmt',3,'p_train_stmt','parser.py',75),
  ('pred_stmt -> PRED name STRING','pred_stmt',3,'p_pred_stmt','parser.py',80),
  ('save_stmt -> SAVE name STRING','save_stmt',3,'p_save_stmt','parser.py',85),
  ('chat_stmt -> CHAT name name','chat_stmt',3,'p_chat_stmt','parser.py',90),
  ('flow_stmt -> RETURN','flow_stmt',1,'p_flow_stmt','parser.py',96),
  ('flow_stmt -> RETURN list_expr','flow_stmt',2,'p_flow_stmt','parser.py',97),
  ('flow_stmt -> BREAK','flow_stmt',1,'p_flow_stmt','parser.py',98),
  ('flow_stmt -> CONTINUE','flow_stmt',1,'p_flow_stmt','parser.py',99),
  ('while_stmt -> WHILE test suite','while_stmt',3,'p_while_stmt','parser.py',108),
  ('while_stmt -> WHILE test suite ELSE suite','while_stmt',5,'p_while_stmt','parser.py',109),
  ('if_stmt -> IF test suite','if_stmt',3,'p_if_stmt','parser.py',118),
  ('if_stmt -> IF test suite ELSE suite','if_stmt',5,'p_if_stmt','parser.py',119),
  ('funcdef_stmt -> DEF name LPAREN list_expr RPAREN suite','funcdef_stmt',6,'p_funcdef_stmt','parser.py',127),
  ('funcdef_stmt -> DEF name LPAREN RPAREN suite','funcdef_stmt',5,'p_funcdef_stmt','parser.py',128),
  ('suite -> simple_stmt','suite',1,'p_suite','parser.py',136),
  ('suite -> LBRACK stmt_list RBRACK','suite',3,'p_suite','parser.py',137),
  ('test -> comparison OR test','test',3,'p_test','parser.py',147),
  ('test -> comparison AND test','test',3,'p_test','parser.py',148),
  ('test -> comparison','test',1,'p_test','parser.py',149),
  ('comparison -> expr GT expr','comparison',3,'p_comparison','parser.py',158),
  ('comparison -> expr LT expr','comparison',3,'p_comparison','parser.py',159),
  ('comparison -> expr GTE expr','comparison',3,'p_comparison','parser.py',160),
  ('comparison -> expr LTE expr','comparison',3,'p_comparison','parser.py',161),
  ('comparison -> expr EQ expr','comparison',3,'p_comparison','parser.py',162),
  ('comparison -> expr NEQ expr','comparison',3,'p_comparison','parser.py',163),
  ('comparison -> expr','comparison',1,'p_comparison','parser.py',164),
  ('basic_type -> INT_TYPE','basic_type',1,'p_basic_type','parser.py',172),
  ('basic_type -> FLOAT_TYPE','basic_type',1,'p_basic_type','parser.py',173),
  ('basic_type -> LIST_TYPE','basic_type',1,'p_basic_type','parser.py',174),
  ('basic_type -> TUPLE_TYPE','basic_type',1,'p_basic_type','parser.py',175),
  ('basic_type -> MLP','basic_type',1,'p_basic_type','parser.py',176),
  ('basic_type -> TRANSFORMER','basic_type',1,'p_basic_type','parser.py',177),
  ('assign_expr -> NAME ASSIGN expr','assign_expr',3,'p_assign_expr','parser.py',182),
  ('assign_expr -> NAME COLON basic_type ASSIGN expr','assign_expr',5,'p_assign_expr','parser.py',183),
  ('assign_expr -> NAME COLON basic_type ASSIGN STRING COLON STRING','assign_expr',7,'p_assign_expr','parser.py',184),
  ('assign_expr -> NAME COLON basic_type ASSIGN list_expr COLON STRING','assign_expr',7,'p_assign_expr','parser.py',185),
  ('assign_expr -> NAME ASSIGN SCAN LPAREN RPAREN','assign_expr',5,'p_assign_expr','parser.py',186),
  ('expr -> expr PLUS expr','expr',3,'p_expr','parser.py',200),
  ('expr -> expr MINUS expr','expr',3,'p_expr','parser.py',201),
  ('expr -> expr TIMES expr','expr',3,'p_expr','parser.py',202),
  ('expr -> expr DIVIDE expr','expr',3,'p_expr','parser.py',203),
  ('expr -> expr MOD expr','expr',3,'p_expr','parser.py',204),
  ('expr -> factor','expr',1,'p_expr','parser.py',205),
  ('factor -> PLUS factor','factor',2,'p_factor','parser.py',214),
  ('factor -> MINUS factor','factor',2,'p_factor','parser.py',215),
  ('factor -> atom_expr','factor',1,'p_factor','parser.py',216),
  ('atom_expr -> atom','atom_expr',1,'p_atom_expr','parser.py',222),
  ('atom_expr -> atom_expr LSQBRACK expr RSQBRACK','atom_expr',4,'p_atom_expr','parser.py',223),
  ('atom_expr -> name LPAREN list_expr RPAREN','atom_expr',4,'p_atom_expr','parser.py',224),
  ('atom -> LPAREN list_expr RPAREN','atom',3,'p_atom','parser.py',237),
  ('atom -> LSQBRACK list_expr RSQBRACK','atom',3,'p_atom','parser.py',238),
  ('atom -> name','atom',1,'p_atom','parser.py',239),
  ('atom -> number','atom',1,'p_atom','parser.py',240),
  ('atom -> string','atom',1,'p_atom','parser.py',241),
  ('atom -> TRUE','atom',1,'p_atom','parser.py',242),
  ('atom -> FALSE','atom',1,'p_atom','parser.py',243),
  ('atom -> NONE','atom',1,'p_atom','parser.py',244),
  ('atom -> name LSQBRACK atom RSQBRACK','atom',4,'p_atom','parser.py',245),
  ('list_expr -> list_expr COMMA expr','list_expr',3,'p_list_expr','parser.py',263),
  ('list_expr -> expr','list_expr',1,'p_list_expr','parser.py',264),
  ('name -> NAME','name',1,'p_name','parser.py',274),
  ('number -> INT','number',1,'p_number','parser.py',278),
  ('number -> FLOAT','number',1,'p_number','parser.py',279),
  ('string -> STRING','string',1,'p_string','parser.py',284),
]
