from .variable import Variable

class Expression:
    """ Represents an Expression """
    
    def __init__(self, left, op, right):
        """ Initialize with the op and the values to perform it with """
        self.left = left
        self.op = op
        self.right = right
        
    def __call__(self, **scope):
        """ Evaluate the Expression """
        return self.op(self.get_value(self.left, scope), self.get_value(self.right, scope))
        
    def get_value(self, parameter, scope):
        """ Return the proper value to use in the given scope """
        if isinstance(parameter, Variable):
            return parameter.get_value(**scope)
        else:
            return parameter