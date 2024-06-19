import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'NUMBER',
    'IDENTIFIER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MODULO',
    'FLOOR_DIVIDE',
    'POWER',
    'LPAREN',
    'RPAREN',
    'ILLEGAL',
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_FLOOR_DIVIDE = r'//'
t_POWER = r'\*\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ILLEGAL = r'[\^#]'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'IDENTIFIER'
    return t


t_ignore = ' \t'


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()


precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'FLOOR_DIVIDE', 'MODULO'),
    ('right', 'POWER'),
    ('nonassoc', 'UMINUS'),
)

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression FLOOR_DIVIDE expression
                  | expression MODULO expression
                  | expression POWER expression'''
    p[0] = (p[2], p[1], p[3])

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_identifier(p):
    'expression : IDENTIFIER'
    p[0] = p[1]

def p_illegal(p):
    'expression : ILLEGAL'
    p[0] = 'ILLEGAL'

def p_error(p):
    raise SyntaxError("Syntax error in input!")

parser = yacc.yacc()


def validate_input():
    input_string = input("Enter an arithmetic expression: ")
    try:
        result = parser.parse(input_string)
        if result == 'ILLEGAL':
            print("Syntax is invalid.")
        else:
            print(f"Syntax is valid.")
    except SyntaxError as e:
        print(e)


validate_input()