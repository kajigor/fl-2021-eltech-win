import ply.lex as lex

tokens = (
    'PVAR', 'PIDENT', 'POPEN', 'PCLOSE', 'PSEP', 'PEND', 'PCONJ', 'PDISJ', 'PTARGET'
)

precedence = (
    ('right', 'PCONJ'),
    ('right', 'PDISJ')
)


t_PVAR = r'[A-Z]\w*'
t_PIDENT = r'[a-z]\w*'
t_POPEN = r'\('
t_PCLOSE = r'\)'
t_PSEP = r'\:\-'
t_PEND = r'\.'
t_PCONJ = r'\,'
t_PDISJ = r'\;'
t_PTARGET = r'\?'


t_ignore = ' '


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character " + str(t.value[0]) + " at line " + str(t.lexer.lineno) + "position" + str(t.lexer.lexpos))
    t.lexer.skip(1)


lexer = lex.lex()

