import ply.lex as lex
import ply.yacc as yacc


tokens = (
    'AT',
    'IDENTIFIER',
    'LPAREN',
    'RPAREN',
    'NEWLINE',
    'COLON',
    'INDENT',
    'DEDENT',
    'DEF',
    'STRING',
    'COMMA',
)


t_AT = r'@'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_COLON = r':'
t_COMMA = r','

def t_STRING(t):
    r'(\'[^\']*\'|\"[^\"]*\")'
    t.value = t.value[1:-1]  
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

def t_INDENT(t):
    r'\n[ \t]*'
    t.lexer.lineno += 1
    t.lexer.begin('INDENT')
    return t

def t_DEDENT(t):
    r'\n[ \t]*\n'
    t.lexer.lineno += 1
    t.lexer.begin('INITIAL')
    return t

def t_INITIAL_INDENT(t):
    r'^[ \t]+'
    t.lexer.lineno += 1
    return t


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()


def p_decorator(p):
    '''
    decorator : AT IDENTIFIER arguments NEWLINE
              | AT IDENTIFIER NEWLINE
    '''
    pass  

def p_arguments(p):
    '''
    arguments : LPAREN arg_values RPAREN
              | LPAREN RPAREN
    '''
    pass

def p_arg_values(p):
    '''
    arg_values : arg_value
               | arg_values COMMA arg_value
    '''
    pass

def p_arg_value(p):
    '''
    arg_value : IDENTIFIER
              | STRING
    '''
    pass

def p_function_def(p):
    '''
    function_def : decorator DEF IDENTIFIER LPAREN RPAREN COLON NEWLINE INDENT DEDENT
    '''
    pass  

def p_error(p):
    if p:
        print(f"Syntax error near '{p.value}' at line {p.lineno}")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()

def validate_decorator_syntax(input_string):
    parser.parse(input_string, lexer=lexer)

# Example usage
print("Enter a Python decorator function definition (Enter 'done' on a new line to finish input):")
user_input = []
while True:
    line = input()
    if line.strip().lower() == 'done':  
        break  
    if line.strip():
        user_input.append(line)

input_string = '\n'.join(user_input)
validate_decorator_syntax(input_string)



