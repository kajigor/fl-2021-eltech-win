from p_parser import build_tree
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--i")
parser.add_argument("--o")
args = parser.parse_args()
finput = args.i
foutput = args.o


try:
    inp = open(finput, 'r')
    outp = open(foutput, 'w')
    result = build_tree(inp.read())
    outp.write(str(result))
except IOError:
    print("Файл " + finput + " недоступен")
finally:
    inp.close()
    outp.close()
