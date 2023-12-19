import ply.lex as lex

reserved = {
    'if'    : 'IF',
    'else'  : 'ELSE',
    'while' : 'WHILE',
    'print' : 'PRINT'
}

tokens = [
    'ID',
    'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', # math
    'LPAREN', 'RPAREN', 'COLON', # symbols
    'EQUALS', # <- | possivelmente mudar o nome desse token
    'GREATER', 'LESS', 'GREAT_EQ', 'LESS_EQ', 'EQUAL_EQ', 'DIFF' # relation
] + list(reserved.values())

t_PLUS       = r'\+'
t_MINUS      = r'-'
t_TIMES      = r'\*'
t_DIVIDE     = r'/'
t_LPAREN     = r'\('
t_RPAREN     = r'\)'
t_EQUALS     = r'<-'
t_COLON      = r':'
t_GREATER    = r'>'
t_LESS       = r'<'
t_GREAT_EQ   = r'>='
t_LESS_EQ    = r'<='
t_EQUAL_EQ   = r'='
t_DIFF       = r'!='

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r'\#.*'
    pass

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# def t_eof(t):
#     more = input('... ')
#     if more:
#         t.lexer.input(more)
#         return t.lexer.token()
#     return None
    
lexer = lex.lex()

if __name__ ==  "__main__":
    data = '''
    a <- 2
    '''

    lexer.input(data)

    while(True):
        tok = lexer.token()
        if not tok:
            break
        print(tok)