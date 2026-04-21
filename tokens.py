from dataclasses import dataclass
from enum import Enum


class TokenType(Enum):
    # single symbols
    LEFT_PAREN = "("
    RIGHT_PAREN = ")"
    LEFT_BRACE = "["
    RIGHT_BRACE = "]"
    COMMA = ","
    SEMICOLON = ";"

    # operators
    PLUS = "+"
    MINUS = "−"
    STAR = "*"
    SLASH = "/"
    EQUAL = "="
    EQUAL_EQUAL = "=="
    NOT_EQUAL = "!="
    LESS = "<"
    LESS_EQUAL = "<="
    GREATER = ">"
    GREATER_EQUAL = ">="

    # literals
    IDENTIFIER = "indentifier"
    NUMBER = "number"
    STRING = "string"

    # keywords
    INT = "int"
    FLOAT = "float"
    BOOL = "bool"
    TYPE_STRING = "type_string"
    IF = "if"
    ELSE = "else"
    WHILE = "while"
    FUNC = "func"
    RETURN = "return"
    TRUE = "true"
    FALSE = "false"

    # end of file
    EOF = "eof"


@dataclass
class Token:
    type: TokenType
    value: str
    line: int
    column: int


KEYWORDS = {
    "int": TokenType.INT,
    "float": TokenType.FLOAT,
    "bool": TokenType.BOOL,
    "string": TokenType.TYPE_STRING,
    "if": TokenType.IF,
    "else": TokenType.ELSE,
    "while": TokenType.WHILE,
    "func": TokenType.FUNC,
    "return": TokenType.RETURN,
    "true": TokenType.TRUE,
    "false": TokenType.FALSE,
}
