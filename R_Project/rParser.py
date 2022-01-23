from lexer import tokens
from node import Node
import ply.yacc as yacc
import sys

error_count = 0

precedence = (
    ('right', 'RCONJ'),
    ('right', 'RDISJ')
)

def p_code(p):
    '''code :
            | str code'''
    if(len(p) == 1):
        p[0] = None
    elif(len(p) == 3):
        p[0] = p[1].add_parts([p[2]])
        #print([p[2]])
    else:
        print("ERR p_code")


def p_str(p):
    '''str : RTARGET target REND
            | attitude REND'''
    if(len(p) == 4):
         p[0] = Node('target', [p[2]])
    elif(len(p) == 3):
        p[0] = Node('attitude', [p[1]])
    else: print("ERR p_str")



def p_attitude(p):
    '''attitude : head RSPLIT target
                | head'''
    if(len(p) == 2):
        p[0] = p[1]
    elif (len(p) == 4):
        p[0] = p[1].add_parts([p[3]])
    else:
        print("ERR p_attitude")



def p_head(p):
    '''head : RIDENT arg'''
    p[0] = Node(p[1] + '\nhead', [p[2]])


def p_arg(p):
    '''arg :
            | elem arg'''
    if (len(p) == 1):
        p[0] = None
    elif(len(p) == 3):
        p[0] = Node('arg', [p[1].add_parts([p[2]])])
    else:print("ERR p_arg")


def p_elem_head(p):
    '''elem : ROPEN head RCLOSE
            | head'''
    if len(p) == 4:
        p[0] = p[2]
    elif len(p) == 2:
        p[0] = p[1]
    else:
        print("ERR p_elem")


def p_elem_var(p):
    '''elem : RVAR'''
    p[0] = Node('per', [p[1]]) # var == per


def p_target(p):
    '''target : targetBody'''
    p[0] = Node('target', [p[1]])


def p_targetBody_head(p):
    '''targetBody : head
                    | targetBody RCONJ targetBody
                    | targetBody RDISJ targetBody'''
    if(len(p) == 2):
        p[0] = p[1]
    elif(p[2] == ','):
        p[0] = Node('conj', [p[1].add_parts([p[3]])])
    elif(p[2] == ';'):
        p[0] = Node('disj', [p[1].add_parts([p[3]])])
    else:
        print("ERR p_targetBody")


def p_targetBody_breakets(p):
    '''targetBody : ROPEN targetBody RCLOSE'''
    p[0] = p[1]


def p_error(p):
    global error_count
    print("Error! Unexpected token: " + str(p.value) + " at line " + str(p.lexer.lineno) + " position " + str(p.lexer.lexpos))
    error_count += 1


parser = yacc.yacc()


def build_tree(code):
    res = parser.parse(code)
    if error_count > 0:
        sys.exit()
    return res