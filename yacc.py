import sys
import ply.yacc as yacc

from tokrules import tokens


def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term'''
    pass
    # if p[2] == '+':
    #     p[0] = p[1] + p[3]
    # elif p[2] == '-':
    #     p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    pass
    
    # p[0] = p[1]

def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor'''    
    pass

    # if p[2] == '*':
    #     p[0] = p[1] * p[3]
    # elif p[2] == '/':
    #     p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    pass
    
    # p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    pass
    
    # p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    pass
    # p[0] = p[2]

def p_variable(p):
    'variable : ID EQUALS NUMBER'
    pass

def p_error(p):
    print('Syntax error in input!')

parser = yacc.yacc()

if __name__ == '__main__':
    fd = sys.argv[1]
    with open(fd,'r') as s:
        result = parser.parse(s.read())
        print(result)

# while True:
#     try:
#         s = input('calc > ')
#     except EOFError:
#         break
#     if not s:
#         continue
#     result = parser.parse(s)
#     print(result)