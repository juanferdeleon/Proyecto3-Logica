'''
        Proyecto 3
    Aplicar los conceptos de autómatas, 
    expresiones regulares y gramáticas

Creado por:

    Juan Fernando De Leon Quezada       17822
    Diego Estrada                       18XXX
    Andree Toledo                       18439

'''

import sys

import ply.lex as lex
import ply.yacc as yacc

from graph import generate_graph

tokens = [
    'VARIABLE',
    'NOT',
    'AND',
    'OR',
    'CONDITIONAL',
    'BICONDITIONAL',
    'PUNCTUATION_OPEN',
    'PUNCTUATION_CLOSE',
    'TRUE',
    'FALSE',
    'EQUALS'
]

t_NOT = r'\~'
t_AND = r'\^'
t_OR = r'\|'
t_CONDITIONAL = r'\=>'
t_BICONDITIONAL = r'\<=>'
t_PUNCTUATION_OPEN = r'\('
t_PUNCTUATION_CLOSE = r'\)'
t_EQUALS = r'\='

t_ignore = r' '

precedence = (
    ('left', 'BICONDITIONAL'),
    ('left', 'CONDITIONAL'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'NOT'),
    ('left', 'PUNCTUATION_OPEN')
)

def t_TRUE(t):
    r'[1]'
    if (t.value == '1'):
        t.value = True
    return t

def t_FALSE(t):
    r'[0]'
    if (t.value == '0'):
        t.value = False
    return t

def t_VARIABLE(t):
    r"[pqrstuvwxyz]"
    t.type = 'VARIABLE'
    return t

def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)

lexer = lex.lex()

def p_error(p):
    print("SYNTAX ERROR.")

def p_calc(p):
    '''
    clac : expression
         | var_assign
         | empty
    '''
    print("Tupla", p[1])
    print(run(p[1]))

def p_var_assign(p):
    '''
    var_assign : VARIABLE EQUALS expression
    '''

    p[0] = ('=', p[1], p[3])

def p_expression(p):
    '''
    expression : expression AND expression
               | expression OR expression
               | expression CONDITIONAL expression
               | expression BICONDITIONAL expression 
    '''

    p[0] = (p[2], p[1], p[3])

def p_expression_not(p):
    '''
    expression : NOT TRUE
               | NOT FALSE
               | NOT expression
    '''

    p[0] = (p[1], p[2])

def p_expression_parenthesis(p):
    '''
    expression : PUNCTUATION_OPEN expression PUNCTUATION_CLOSE
    '''

    p[0] = (p[2])    

def p_expression_var(p):
    '''
    expression : VARIABLE
    '''

    p[0] = ('var', p[1])

def p_expression_true_false(p):
    '''
    expression : TRUE
               | FALSE
    '''

    p[0] = p[1]

def p_empty(p):
    '''
    empty : 
    '''

    p[0] = None

parser = yacc.yacc()
env = {}

def run(p):
    if type(p) == tuple:
       
        global env
        
        if p[0] == '=>':
            p_1 = run(p[1])
            p_2 = run(p[2])
            
            if p_1 == True and p_2 == False:
                return False
            
            return True
        elif p[0] == '<=>':
            p_1 = run(p[1])
            p_2 = run(p[2])
            
            if p_1 == p_2:
                return True
            
            return False
        elif p[0] == '^':
            return (run(p[1]) and run(p[2]))
        elif p[0] == '|':
            return (run(p[1]) or run(p[2]))
        elif p[0] == '~':
            return not run(p[1])
        elif p[0] == '=':
            env[p[1]] = run(p[2])
        elif p[0] == 'var':
            if p[1] not in env:
                return 'Undeclared variable.'
            else:
                return env[p[1]]
    else:
        return p

while True:
    try: 
        s = input('>> ')
    except EOFError:
        break

    parser.parse(s)