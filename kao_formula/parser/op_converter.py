import operator

OpToMethod = {'+':operator.add}

def OpConverter(value):
    """ Convert the given Operation into the actual operator function """
    return OpToMethod[value]