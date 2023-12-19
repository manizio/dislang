import sys
import ply.yacc as yacc

from tokrules import tokens

symbol_table = {}

def p_statement(p):
    '''statement : statement statement
                 | variable_declaration
                 | expression
                 | logic_expression
                 | print_statement
                 | loop_statement
                 | if_statement
    '''

    pass

def p_if_statement(p):
    'if_statement : IF LPAREN logic_expression RPAREN COLON statement'
    # FIX: statement é executado mesmo quando a condição é falsa

    if str(p[3]) == 'True':
        p[0] = p[6]

def p_loop_statement(p):
    'loop_statement : WHILE LPAREN logic_expression RPAREN COLON statement'
    
    pass
    # while p[3]:
    #     p[0] = p[6]

def p_print_statement(p):
    '''print_statement : PRINT LPAREN expression RPAREN
                       | PRINT LPAREN logic_expression RPAREN'''
    
    print(p[3])

def p_variable_declaration(p):
    'variable_declaration : ID EQUALS expression'
    symbol_table[p[1]] = p[3]
    pass

def p_logic_expression(p):
    'logic_expression : factor operation factor'
    
    # retorna True ou False
    if p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]
    elif p[2] == '=':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] !=  p[3]

def p_operation(p):
    'operation : rel_operation'
    p[0] = p[1]

def p_rel_operation(p):
    '''rel_operation : GREATER
                     | LESS
                     | GREAT_EQ
                     | LESS_EQ
                     | EQUAL_EQ
                     | DIFF'''
    p[0] = p[1]

def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term'''
    
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]

def p_expression_id(p):
    'expression : ID'
    p[0] = symbol_table.get(p[1], None)

def p_expression_term(p):
    'expression : term'
    
    p[0] = p[1]

def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor'''    

    if p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'

    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    
    p[0] = p[1]

def p_factor_id(p):
    'factor : ID'

    p[0] = symbol_table.get(p[1], None)

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    
    p[0] = p[2]

def p_error(p):

    print('Syntax error in input!')

parser = yacc.yacc()

if __name__ == '__main__':
    fd = sys.argv[1]
    with open(fd,'r') as s:
        string = s.read()
        result = parser.parse(string)
        print(result)
    
    # data = '''a <- 2 * 4
    # b <- a + 1
    # c <- a + b
    # print(a)
    # print(a < b)
    # '''

    # result = parser.parse(data)

    # print(result)
    print("=======================")
    print(symbol_table)