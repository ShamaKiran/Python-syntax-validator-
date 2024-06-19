import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'NUMBER',
    'SET',
    'UNION',
    'INTERSECTION',
    'DIFFERENCE',
    'SYMMETRIC_DIFFERENCE',
    'LPAREN',
    'RPAREN',
    'COMMA',
)

t_UNION = r'\+'
t_INTERSECTION = r'&'
t_DIFFERENCE = r'-'
t_SYMMETRIC_DIFFERENCE = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_SET(t):
    r'{\d+(,\d+)*}'
    t.value = set(map(int, t.value[1:-1].split(',')))
    return t

t_ignore = ' \t'

def t_error(t):
    raise SyntaxError("Invalid Syntax")

lexer = lex.lex()

def p_expression_union(p):
    '''
    expression : expression UNION term
               | expression INTERSECTION term
               | expression DIFFERENCE term
               | expression SYMMETRIC_DIFFERENCE term
    '''
    if p[2] == '+':
        p[0] = p[1].union(p[3])
    elif p[2] == '&':
        p[0] = p[1].intersection(p[3])
    elif p[2] == '-':
        p[0] = p[1].difference(p[3])
    elif p[2] == '^':
        p[0] = p[1].symmetric_difference(p[3])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_set(p):
    'term : SET'
    p[0] = p[1]

def p_term_paren(p):
    'term : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    raise SyntaxError("Invalid Syntax")

parser = yacc.yacc()

def validate_input():
    input_string = input("Enter a set expression: ")
    try:
        result = parser.parse(input_string)
        if result is not None:
            print(f"Syntax is valid. Result: {result}")
    except SyntaxError as e:
        print(e)

validate_input()
