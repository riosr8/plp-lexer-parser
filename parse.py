import sys
from lexer import Lexer
from parser import Parser, type_dict


def read_file(path):
    with open(path) as f:
        return f.read()


filename = sys.argv[-1]
input_file = open(filename)
text = read_file(filename)
res = Lexer(text).tokenize()
for line in res:
    if len(line) > 0:
        print 'Lexer: ' + str([type_dict.get(token.kind) for token in line])
        parse_res = Parser().parse(line)
        print 'Parser: ' + str(parse_res)
        print '\n'
