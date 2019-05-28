import unittest
from lexer import Lexer, TokenKind
from parser import Parser


class Test(unittest.TestCase):
    def test1(self):
        text = Lexer('Q => (A \/ B)').tokenize()
        l = [token.kind for line in text for token in line]
        self.assertEqual(l, [TokenKind.ID, TokenKind.IMPLIES, TokenKind.LPAR, TokenKind.ID, TokenKind.OR, TokenKind.ID,
                             TokenKind.RPAR])

    def test2(self):
        text = Lexer('A <=> , B /\\ C').tokenize()
        l = [token.kind for line in text for token in line]
        self.assertEqual(l, [TokenKind.ID, TokenKind.IFF, TokenKind.COMMA, TokenKind.ID, TokenKind.AND, TokenKind.ID])

    def test3(self):
        text = Lexer('!(ABC),').tokenize()
        l = [token.kind for line in text for token in line]
        self.assertEqual(l, [TokenKind.NOT, TokenKind.LPAR, TokenKind.ID, TokenKind.RPAR, TokenKind.COMMA])

    def test4(self):
        text = Lexer('( P \/ Q ) , ( X => Y )').tokenize()
        l = [token.kind for line in text for token in line]
        self.assertEqual(l, [TokenKind.LPAR, TokenKind.ID, TokenKind.OR, TokenKind.ID, TokenKind.RPAR, TokenKind.COMMA,
                             TokenKind.LPAR, TokenKind.ID, TokenKind.IMPLIES, TokenKind.ID, TokenKind.RPAR])

    def test5(self):
        text = Lexer('Q').tokenize()
        l = [token for line in text for token in line]
        parse_tree = Parser().parse(l)
        # some assertion goes here
        self.assertEqual(parse_tree, ["propositions", "proposition", "atomic", "ID", "more_propositions", "epsilon"])


if __name__ == '__main__':
    unittest.main()
