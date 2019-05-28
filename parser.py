from lexer import Location, Token
import sys


type_dict = {
    0: 'ID',
    1: 'LPAR',
    2: 'RPAR',
    3: 'NOT',
    4: 'AND',
    5: 'OR',
    6: 'IMPLIES',
    7: 'IFF',
    8: 'COMMA',
    9: 'epsilon',
    10: 'ERROR'
}


class Parser:
    def __init__(self):
        self.loc = Location(0, 0)
        self.lookahead = None
        self.tokens_list = []
        self.tree = []
        self.error = None

    def parse(self, tokenList):
        lastToken = tokenList[-1]
        tokenList.append(Token(Location(lastToken.loc.line, lastToken.loc.col + 1), 9))
        self.tokens_list = tokenList
        self.lookahead = self.tokens_list.pop(0)
        self.loc = self.lookahead.loc
        self.propositions()
        if self.error != None:
            return self.error
        else:
            return self.tree

    def match(self, token):
        if token == self.lookahead.kind:
            self.tree.append(type_dict.get(token, None))
            # self.currentIndex += 1
            if len(self.tokens_list) > 0:
                self.lookahead = self.tokens_list.pop(0)
                self.loc = self.lookahead.loc
        else:
            self.error = 'Syntax Error on line ' + str(self.loc.line) + ', column ' + str(self.loc.col)

    def propositions(self):
        self.tree.append(sys._getframe().f_code.co_name)
        self.proposition()
        self.more_propositions()

    def more_propositions(self):
        self.tree.append(sys._getframe().f_code.co_name)
        if self.lookahead.kind == 8:
            self.match(8)
            self.propositions()
        elif self.lookahead.kind == 9:
            self.tree.append(type_dict.get(9, None))
        else:
            self.error = 'Syntax Error on line ' + str(self.loc.line) + ', column ' + str(self.loc.col)

    def proposition(self):
        self.tree.append(sys._getframe().f_code.co_name)
        next_token = self.peek_next()
        if self.lookahead.kind == 0 and next_token and next_token.kind in [4, 5, 6, 7]:
            self.compound()
        elif self.lookahead.kind in [1, 3]:
            self.compound()
        else:
            self.atomic()
        # elif self.lookahead.kind == 0:
        #     self.atomic()
        # else:
        #     self.error = 'Syntax Error on line ' + str(self.loc.line) + ', column ' + str(self.loc.col)
        #     return

    def atomic(self):
        self.tree.append(sys._getframe().f_code.co_name)
        self.match(0)

    def compound(self):
        self.tree.append(sys._getframe().f_code.co_name)
        if self.lookahead.kind == 0:
            self.atomic()
            self.connective()
            self.proposition()
        elif self.lookahead.kind == 1:
            self.match(1)
            self.proposition()
            self.match(2)
        elif self.lookahead.kind == 3:
            self.match(3)
            self.proposition()

    def connective(self):
        self.tree.append(sys._getframe().f_code.co_name)
        if self.lookahead.kind == 4:
            self.match(4)
        elif self.lookahead.kind == 5:
            self.match(5)
        elif self.lookahead.kind == 6:
            self.match(6)
        elif self.lookahead.kind == 7:
            self.match(7)

    def peek_next(self):
        if len(self.tokens_list) > 0:
            # print 'next: ' + str(next(iter(self.tokens_list)))
            return next(iter(self.tokens_list))
