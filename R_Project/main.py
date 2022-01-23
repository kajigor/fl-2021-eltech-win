from rParser import build_tree
import argparse
import sys

argumentParser = argparse.ArgumentParser()
argumentParser.add_argument("--input")
argumentParser.add_argument("--output")
args = argumentParser.parse_args()
fileInput = ""
fileInput = args.input
fileOutput = args.output


try:
    input = open(fileInput, 'r')
    output = open(fileOutput, 'w')
    result = build_tree(input.read())
    output.write(str(result))
except IOError:
    print("Файл " + fileInput + " недоступен")
finally:
    input.close()
    output.close()