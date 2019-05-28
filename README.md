# Progamming Languages and Paradigms

## Task

#### Language for propositional language

### Implement a lexer and parser for a simple language.

Token definitions:

    ID = [A-Z]+

    LAPR = (

    RPAR = )

    NOT = !

    AND = /\

    OR = \/

    IMPLIES = ‘=>’

    IFF = ‘<=>’


Grammar:

    propositions -> proposition more-proposition

    more-proposition -> ,  propositions | epsilon

    proposition -> atomic | compound

    atomic -> 0 | 1 | ID

    compound -> atomic  connective proposition | LPAR proposition RPAR | NOT proposition

    connective ->  AND | OR | IMPLIES | IFF


 The start variable is `propositions`.



## Usage

This assignment was completed using **Python 2**.

Program execution begins in `parse.py`.
To run execute program as the following example below:

`python parse.py sample_text.txt`