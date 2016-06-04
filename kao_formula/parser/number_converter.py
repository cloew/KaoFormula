from decimal import Decimal

def DecimalConverter(value):
    """ Convert the value to a Decimal """
    return Decimal(value)
    
def IntegerConverter(value):
    """ Convert the value to an int """
    return int(value)