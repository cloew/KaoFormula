    
class Variable:
    """ Represents a variable in a Formula """
    
    def __init__(self, name, attr=None):
        """ Initialize with the variable name """
        self.name = name
        self.attr = attr
        print(name, attr)
        
    def get_value(self, **scope):
        """ Return the proper value for the variable in the given scope """
        value = scope[self.name]
        if self.attr:
            value = getattr(value, self.attr)
        return value