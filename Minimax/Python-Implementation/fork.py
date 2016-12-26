"""
An instance of this class is the fork of two branches of a binary tree to be implemented
in a minimax tree.
"""
class Fork(object):

    """
    Each branch is bare. Value assigned by argument.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # def get_value(self): return self.value
    # def get_left(self): return self.left
    # def get_right(self): return self.right

    """
    This function will recurse the branches of the fork denoted by "self" and print its
    value if both its branches are bare.
    """
    def print_all_below(self):
        if self.value != -1: print "%s" % (self.value),
        if self.left is not None: self.left.print_all_below()
        if self.right is not None: self.right.print_all_below()

    """
    This function compares the length of the leftmost and rightmost branches of self.
    Returns true if the lengths are the same (the fork is symmetrical).
    """
    def _is_peak(self):
        return self._length_of_leftmost_fork() == self._length_of_rightmost_branch()

    """
    Returns number of leftmost forks beneath self.
    """
    def _length_of_leftmost_fork(self):
        if self.left is None:
            return 0
        else:
            return 1 + self.left._length_of_leftmost_fork()

    """
    Returns number of rightmost forks beneath self.
    """
    def _length_of_rightmost_branch(self):
        if self.right is None:
            return 0
        else:
            return 1 + self.right._length_of_rightmost_branch()


    """
    Returns the fork leftmost of self.
    """
    def _leftmost_fork(self):
        if self.left is None:
            return self
        else:
            return self.left._leftmost_fork()

    """
    This function returns the first fork wheren a new value can be added.
    """
    def fork_of_asymmetry(self):
        if self._is_peak(): # tree is symmetrical: start new row
            return self._leftmost_fork()
        else:
            if self.left._is_peak():
                if self.right._is_peak():
                    return self.right._leftmost_fork()
                else:
                    return self.right.fork_of_asymmetry()
            else:
                return self.left.fork_of_asymmetry()

    """
    This function splits the first available branch and adds the new value to it.
    """
    def split(self, value):
        # if not self._bare_branches(): print "error in split"
        self.left = Fork(self.value)
        self.right = Fork(value)
        self.value = -1 # tag that branches are not bare

    # def _bare_branches(self):
    #     """
    #     Returns true if both left and right branches are null (none).
    #     """
    #     return self.left is None and self.right is None
    #
    # def _both_branches_active(self):
    #     """
    #     Returns true if both branches are active.
    #     """
    #     return self.left is not None and self.right is not None
