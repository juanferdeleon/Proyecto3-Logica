'''
        Proyecto 3
    Aplicar los conceptos de autómatas, 
    expresiones regulares y gramáticas

Creado por:

    Juan Fernando De Leon Quezada       17822
    Diego Estrada                       18XXX
    Andree Toledo                       18XXX

'''

import sys

import ply.lex as lex
import ply.yacc as yacc

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

def t_TRUE(t):
    r'\d'
    if (t.value == '1'):
        t.value = True
    return t

def t_FALSE(t):
    r'\d'
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

lexer.input("|")

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)