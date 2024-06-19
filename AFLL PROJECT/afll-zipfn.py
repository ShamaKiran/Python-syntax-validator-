import os
import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'ZIP',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'NAME',
)

def t_ZIP(t):
    r'zip'
    return t

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_ignore = ' \t'  


def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()


def p_expression_zip(p):
    'expression : ZIP LPAREN elements RPAREN'
    p[0] = f'{p[1]}{p[2]}{p[3]}{p[4]}'

def p_lists_single(p):
    'lists : list'
    p[0] = [p[1]]

def p_lists_multiple(p):
    'lists : lists COMMA list'
    p[0] = p[1] + [p[3]]

def p_list(p):
    'list : LPAREN elements RPAREN'
    p[0] = f'{p[1]}{p[2]}{p[3]}'

def p_elements_single(p):
    'elements : NAME'
    p[0] = f'{p[1]}'

def p_elements_multiple(p):
    'elements : elements COMMA NAME'
    p[0] = f'{p[1]}{p[2]}{p[3]}'

def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}'")
    else:
        print("Syntax error: Unexpected end of input")

output_directory = 'C:/Users/Shama Kiran/afll_project_output'  

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

parser = yacc.yacc(outputdir=output_directory)


def validate_input():
    input_string = input("Enter a zip function: ")
    lexer.input(input_string)
    for token in lexer:
        pass  

    try:
        result = parser.parse(input_string)
        if result is not None:
            print(f"Syntax is valid.")
    except:
        pass  


validate_input()

























