import sys
import ply.yacc as yacc

from tokrules import tokens

symbol_table = {}

def p_statement(p):
    '''statement : statement statement
                 | variable_declaration
                 | expression
                 | print_statement
    '''
    pass

def p_print_statement(p):
    'print_statement : PRINT expression'
    print(p[2])

def p_variable_declaration(p):
    'variable_declaration : ID EQUALS expression'
    symbol_table[p[1]] = p[3]
    pass

def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term'''
    pass
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

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    
    p[0] = p[2]

def p_error(p):

    print('Syntax error in input!')

parser = yacc.yacc()

if __name__ == '__main__':
    # fd = sys.argv[1]
    # with open(fd,'r') as s:
    #     string = s.read()
    #     result = parser.parse(string)
    #     print(result)

    # FIX: declaração de variável c <- a + b não funciona
    
    data = '''a <- 2 * 4
    b <- a + 1
    print a
    print b
    '''

    result = parser.parse(data)

    print(result)
    print(symbol_table)