from lexer import tokens
from node import Node
import ply.yacc as yacc
import sys

error_count = 0

precedence = (
    ('right', 'PCONJ'),
    ('right', 'PDISJ')
)

def p_code_empty(p):
    '''code :'''
    p[0] = None


def p_code_notempty(p):
    '''code : str code'''
    p[0] = p[1].add_parts([p[2]])


def p_str_target(p):
    '''str : PTARGET target PEND'''
    p[0] = Node('target', [p[2]])


def p_str_attitude(p):
    '''str : attitude PEND'''
    p[0] = Node('attitude', [p[1]])


def p_attitude_moreThanHead(p):
    '''attitude : head PSEP target'''
    p[0] = p[1].add_parts([p[3]])


def p_attitude_headOnly(p):
    '''attitude : head'''
    p[0] = p[1]


def p_head(p):
    '''head : PIDENT arg'''
    p[0] = Node(p[1] + '\nhead', [p[2]])


def p_arg_empty(p):
    '''arg :'''
    p[0] = None


def p_arg_notempty(p):
    '''arg : elem arg'''
    p[0] = Node('arg', [p[1].add_parts([p[2]])])


def p_elem_head(p):
    '''elem : POPEN head PCLOSE
            | head'''
    if len(p) > 2:
        p[0] = p[2]
    else:
        p[0] = p[1]


def p_elem_var(p):
    '''elem : PVAR'''
    p[0] = Node('var', [p[1]])


def p_target(p):
    '''target : targetBody'''
    p[0] = Node('target', [p[1]])


def p_targetBody_head(p):
    '''targetBody : head'''
    p[0] = p[1]


def p_targetBody_conj(p):
    '''targetBody : targetBody PCONJ targetBody'''
    p[0] = Node('conj', [p[1].add_parts([p[3]])])


def p_targetBody_disj(p):
    '''targetBody : targetBody PDISJ targetBody'''
    p[0] = Node('disj', [p[1].add_parts([p[3]])])


def p_targetBody_parentheses(p):
    '''targetBody : POPEN targetBody PCLOSE'''
    p[0] = p[1]


def p_error(p):
    global error_count
    print("Unexpected token: " + str(p.value) + " at line " + str(p.lexer.lineno) + " position " + str(p.lexer.lexpos))
    error_count += 1


parser = yacc.yacc()


def build_tree(code):
    res = parser.parse(code)
    if error_count > 0:
        sys.exit()
    return res