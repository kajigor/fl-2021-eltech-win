import ply.lex as lex

tokens = (
    'RVAR', 'RIDENT', 'ROPEN', 'RCLOSE', 'RSPLIT', 'REND', 'RCONJ', 'RDISJ', 'RTARGET'
)

precedence = (
    ('right', 'RCONJ'),
    ('right', 'RDISJ')
)


t_RVAR = r'[A-Z]\w*'
t_RIDENT = r'[a-z]\w*'
t_ROPEN = r'\('
t_RCLOSE = r'\)'
t_RSPLIT = r'\:\-'
t_REND = r'\.'
t_RCONJ = r'\,'
t_RDISJ = r'\;'
t_RTARGET = r'\?'


t_ignore = ' '


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("\033[31m Error! Unexpected character: " + str(t.value[0]) + ". Line " + str(t.lexer.lineno) + ", Position " + str(t.lexer.lexpos) + "\033[0m")
    t.lexer.skip(1)


lexer = lex.lex()