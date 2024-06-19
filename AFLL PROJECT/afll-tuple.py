import ply.lex as lex
import ply.yacc as yacc


tokens = (
    'LPAREN',
    'RPAREN',
    'COMMA',
    'NUMBER',
    'STRING',  
    'PLUS',
    'LEN',
)


t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_NUMBER = r'\d+(\.\d+)?'  # Match integers or floats
t_STRING = r'("[^"]*"|\'[^\']*\')' 
t_PLUS = r'\+'
t_LEN = r'len'

t_ignore = ' \t'

syntax_valid_flag = True  


def t_error(t):
    global syntax_valid_flag
    syntax_valid_flag = False
    t.lexer.skip(1)

lexer = lex.lex()


def p_tuple(p):
    '''
    tuple : LPAREN elements RPAREN
          | tuple PLUS tuple
          | LEN LPAREN tuple RPAREN
    '''
    if len(p) == 4:  
        p[0] = p[2]
    elif p[1] == 'len':  
        p[0] = (len(p[3]),)
    else:  # tuple + tuple
        p[0] = p[1] + p[3]

def p_elements_single(p):
    'elements : element'
    p[0] = (p[1],)

def p_elements_multiple(p):
    'elements : elements COMMA element'
    p[0] = p[1] + (p[3],)

def p_element_number(p):
    'element : NUMBER'
    p[0] = float(p[1]) if '.' in p[1] else int(p[1])

def p_element_string(p):
    'element : STRING'
    p[0] = eval(p[1])  

def p_error(p):
    global syntax_valid_flag
    syntax_valid_flag = False

parser = yacc.yacc()

def validate_input(input_string):
    global syntax_valid_flag
    syntax_valid_flag = True

    result = parser.parse(input_string, lexer=lexer)

    if syntax_valid_flag:
        print(f"Syntax is valid. ")
    else:
        print(f"Syntax is invalid. Input: {input_string}")


user_input = input("Enter a tuple, tuple operation, or len(tuple): ")
validate_input(user_input)
