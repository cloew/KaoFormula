from .identifier_converter import IdentifierConverter
from .number_converter import DecimalConverter, IntegerConverter
from kao_parser import Grammar

def Formula(value):
    print(value)
    return value

class FormulaGrammar(Grammar):
    """ Grammar to use when parsing a Formula """
    integer             = r"\d+", IntegerConverter
    decimal             = r"\d+\.\d+", DecimalConverter
    identifier          = r"[a-zA-Z]+\w*", IdentifierConverter
    formula             = r"<identifier>|<decimal>|<integer>", Formula