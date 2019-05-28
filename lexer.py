import string
import re
UPPER_CASE = set(string.ascii_uppercase)

class Location:
    def __init__(self, line, col):
        self.col = col
        self.line = line


class TokenKind:
    ID = 0   # identifier
    LPAR = 1 # (
    RPAR = 2 # )
    NOT = 3  # !
    AND = 4  # /\
    OR = 5   # \/
    IMPLIES = 6  # =>
    IFF = 7  # <=>
    COMMA = 8 # ,
    ERROR = 10



class Token:
    def __init__(self, loc, kind):
        self.loc = loc
        self.kind = kind

    def __str__(self):
        return str(self.kind)


class Lexer:
    def __init__(self, text):
        self.text = text
        self.line = 1
        self.col = 1

    def tokenize(self):
        global current_match
        current_match = None
        line_tokens = []
        tokens = []
        line_start = 0
        for match in re.finditer('[A-Z]+|\\\\/|<=>|=>|/\\\\|,|!|\(|\)|\n|[^ ]', self.text):
            # print match.group()
            # print match.span()
            token = match.group()
            self.col = (match.start() + 1) - line_start
            # if token != '\n':
            #     print token + ': (' + str(self.line) + ', ' + str(self.col) + ')'
            if re.match('[A-Z]+', token):
                line_tokens.append(Token(Location(self.line, self.col), TokenKind.ID))
            elif re.match('\(', token):
                line_tokens.append(Token(Location(self.line, self.col), TokenKind.LPAR))
            elif re.match('\)', token):
                line_tokens.append(Token(Location(self.line, self.col), TokenKind.RPAR))
            elif re.match('!', token):
                line_tokens.append(Token(Location(self.line, self.col), TokenKind.NOT))
            elif re.match('\\\\/', token):
                line_tokens.append(Token(Location(self.line, self.col), TokenKind.OR))
            elif re.match('/\\\\', token):
                line_tokens.append(Token(Location(self.line, self.col), TokenKind.AND))
            elif re.match('=>', token):
                line_tokens.append(Token(Location(self.line, self.col), TokenKind.IMPLIES))
            elif re.match('<=>', token):
                line_tokens.append(Token(Location(self.line, self.col), TokenKind.IFF))
            elif re.match(',', token):
                line_tokens.append(Token(Location(self.line, self.col), TokenKind.COMMA))
            elif re.match('\n', token):
                tokens.append(line_tokens)
                line_tokens = []
                line_start = match.end()
                self.line += 1
            else:
                line_tokens.append(Token(Location(self.line, self.col), TokenKind.ERROR))
        tokens.append(line_tokens)
        return tokens
