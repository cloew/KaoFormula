from .expression import Expression
from .variable import Variable
from .number_converter import DecimalConverter, IntegerConverter
from .op_converter import OpConverter
from kao_parser import Grammar

def Formula(expr):
    return expr

class FormulaGrammar(Grammar):
    """ Grammar to use when parsing a Formula """
    integer             = r"\d+", IntegerConverter
    decimal             = r"\d+\.\d+", DecimalConverter
    number              = r"<decimal>|<integer>"
    variable            = r"[a-zA-Z]+\w*", Variable
    op                  = r"\+", OpConverter
    primitive           = r"<variable>|<number>"
    expr                = r"<primitive>\s*<op>\s*<primitive>", Expression
    formula             = r"\s*<expr>\s*", Formula