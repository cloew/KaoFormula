
class Expression:
    """ Represents an Expression """
    
    def __init__(self, left, op, right):
        """ Initialize with the op and the values to perform it with """
        self.left = left
        self.op = op
        self.right = right
        
    def __call__(self):
        """ Evaluate the Expression """
        return self.op(self.left, self.right)