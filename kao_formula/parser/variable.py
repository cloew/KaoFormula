    
class Variable:
    """ Represents a variable in a Formula """
    
    def __init__(self, name):
        """ Initialize with the variable name """
        self.name = name
        
    def get_value(self, **scope):
        """ Return the proper value for the variable in the given scope """
        return scope[self.name]