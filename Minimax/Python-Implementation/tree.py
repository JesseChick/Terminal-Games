from fork import Fork

"""
This is the binary tree framework for the entire game.
"""
class MinimaxTree(object):

    """
    Tree is originally emptry (subject to change).
    """
    def __init__(self):
        self.root = None

    """
    Adds value passed as argument to the first availeble location in tree.
    """
    def add_value(self, value):
        if self.root is None: # tree is empty
            self.root = Fork(value)
        else:
            self.root.fork_of_asymmetry().split(value)
            # next_split = self.root.fork_of_asymmetry()
            # next_split.split(value)

    """
    Prints value of all branch endings in the tree.
    """
    def print_tree(self):
        self.root.print_all_below()
