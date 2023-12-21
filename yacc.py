import sys
import ply.yacc as yacc

from tokrules import tokens

symbol_table = {}

def p_statement(p):
    '''statement : statement statement
                 | variable_declaration
                 | expression
                 | if_statement
                 | logic_expression
                 | loop_statement
                 | print_statement
                 | section_statement
                 | data_statement
    '''
    p[0] = p[1]
    pass

def p_data_statement(p):
    'data_statement : DATA ID LPAREN factor RPAREN'
    print(f'''fd = open({p[4]}, 'r')\n{p[2]} = fd.read()''')
    pass

def p_section_statement(p):
    '''section_statement : SECTION ID LPAREN factor COMMA factor RPAREN
                         | SECTION ID LPAREN RPAREN'''

    if len(p) > 5:   
        print(f'''{p[2]} = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n{p[2]}.connect(({p[4]}, {p[6]}))''')
    else:
        print(f'''{p[2]} = socket.socket(socket.AF_INET, socket.SOCK_STREAM)''')

    pass


def p_if_statement(p):
    'if_statement : IF LPAREN logic_expression RPAREN COLON statement ENDIF'

    print(f'if {p[3]}: {p[6]}')


def p_loop_statement(p):
    '''loop_statement : WHILE LPAREN logic_expression RPAREN COLON statement ENDWHILE'''
    # '''loop_statement : WHILE LPAREN logic_expression RPAREN COLON statement ENDWHILE
    #                   | FOR LPAREN variable_declaration logic_expression expression RPAREN COLON statement ENDFOR'''

    print(f'while {p[3]}: {p[6]}')

def p_print_statement(p):
    '''print_statement : PRINT LPAREN expression RPAREN
                       | PRINT LPAREN logic_expression RPAREN'''
    
    print(p[3])

def p_variable_declaration(p):
    '''variable_declaration : ID EQUALS expression'''
    
    symbol_table[p[1]] = p[3]
    print(f"{p[1]} = {p[3]}")
    
    pass

def p_logic_expression(p):
    'logic_expression : factor operation factor'
    
    p[0] = f'{p[1]} {p[2]} {p[3]}'

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
        p[0] = f'{p[1]} + {p[3]}'
    elif p[2] == '-':
        p[0] = f'{p[1]} - {p[3]}'

def p_expression_id(p):
    'expression : ID'

    # p[0] = symbol_table.get(p[1], None)
    p[0] = p[1]

def p_expression_term(p):
    'expression : term'
    
    p[0] = p[1]

def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor'''    

    if p[2] == '*':
        p[0] = f'{p[1]} * {p[3]}'
    elif p[2] == '/':
        p[0] = f'{p[1]} / {p[3]}'

def p_term_factor(p):
    'term : factor'

    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    
    p[0] = p[1]

def p_factor_string(p):
    'factor : STRING'
    p[0] = p[1]

def p_factor_db_string(p):
    'factor : DB_STRING'
    p[0] = p[1]

def p_factor_id(p):
    'factor : ID'

    p[0] = symbol_table.get(p[1], None)


def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    
    # print(f'({p[2]})')

    p[0] = f'({p[2]})'

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