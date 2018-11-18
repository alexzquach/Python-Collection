""" Tree class and functions.
"""
from csc148_queue import Queue
from typing import Any, Callable, List


class Tree:
    """
    A bare-bones Tree ADT that identifies the root with the entire tree.
    """

    def __init__(self, value=None, children=None) -> None:
        """
        Create Tree self with content value and 0 or more children
        """
        self.value = value
        # copy children if not None
        self.children = children[:] if children is not None else []

    def __repr__(self) -> str:
        """
        Return representation of Tree (self) as string that
        can be evaluated into an equivalent Tree.

        >>> t1 = Tree(5)
        >>> t1
        Tree(5)
        >>> t2 = Tree(7, [t1])
        >>> t2
        Tree(7, [Tree(5)])
        """
        # Our __repr__ is recursive, because it can also be called
        # via repr...!
        return ('Tree({}, {})'.format(repr(self.value), repr(self.children))
                if self.children
                else 'Tree({})'.format(repr(self.value)))

    def __eq__(self, other: Any) -> bool:
        """
        Return whether this Tree is equivalent to other.
        >>> t1 = Tree(5)
        >>> t2 = Tree(5, [])
        >>> t1 == t2
        True
        >>> t3 = Tree(5, [t1])
        >>> t2 == t3
        False
        """
        return (type(self) is type(other) and
                self.value == other.value and
                self.children == other.children)

    def __str__(self, indent=0) -> str:
        """
        Produce a user-friendly string representation of Tree self,
        indenting each level as a visual clue.

        >>> t = Tree(17)
        >>> print(t)
        17
        >>> t1 = Tree(19, [t, Tree(23)])
        >>> print(t1)
        19
           17
           23
        >>> t3 = Tree(29, [Tree(31), t1])
        >>> print(t3)
        29
           31
           19
              17
              23
        """
        root_str = indent * " " + str(self.value)
        return '\n'.join([root_str] +
                         [c.__str__(indent + 3) for c in self.children])


def list_internal(t: Tree) -> list:
    """
    Return list of values in internal nodes of t.

    >>> t = Tree(0)
    >>> list_internal(t)
    []
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> L = list_internal(t)
    >>> L.sort()
    >>> L
    [0, 1, 2]
    """
    # Checks if the starting tree has no children
    if t.children == []:
        return []
    else:
        return gather_lists([list_internal(x) for x in t.children]) + [t.value]


def count_internal(t: Tree) -> int:
    """
    Return number of internal nodes of t.

    >>> t = Tree(0)
    >>> count_internal(t)
    0
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> count_internal(t)
    3
    """
    # Base case if the tree has no internal nodes
    if t.children == []:
        return 0
    else:
        # Adds one to the list every time since there are
        # children
        return sum([count_internal(x) for x in t.children] + [1])


def count_leaves(t: Tree) -> int:
    """
    Return the number of leaves in Tree t.

    >>> t = Tree(7)
    >>> count_leaves(t)
    1
    >>> t = descendants_from_list(Tree(7), [0, 1, 3, 5, 7, 9, 11, 13], 3)
    >>> count_leaves(t)
    6
    >>> t2 = Tree(0)
    >>> count_leaves(t2)
    1
    >>> t2 = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
    >>> count_leaves(t2)
    7
    """
    # Returns 1 everytime the tree has no children
    # If the tree has no children, then it is a leaf
    if t.children == []:
        return 1
    else:
        return sum([count_leaves(x) for x in t.children])


def sum_internal(t: Tree) -> int:
    """
    Return sum of the internal (non-leaf) nodes of t.

    Assume all nodes have integer values.

    >>> t = Tree(0)
    >>> sum_internal(t)
    0
    >>> t = descendants_from_list(Tree(1), [2, 3, 4, 5, 6, 7, 8, 9], 3)
    >>> sum_internal(t)
    6
    """
    # Base case if it has no children, it is not a node
    if t.children == []:
        return 0
    else:
        return sum([sum_internal(x) for x in t.children]) + t.value


def sum_leaves(t: Tree) -> int:
    """
    Return sum of the leaves of t.
    >>> t = Tree(0)
    >>> sum_leaves(t)
    0
    >>> t = descendants_from_list(Tree(1), [2, 3, 4, 5, 6, 7, 8, 9], 3)
    >>> sum_leaves(t)
    39
    """
    # Base case if it has no children, it is a leaf
    if t.children == []:
        return t.value
    else:
        return sum([sum_leaves(x) for x in t.children])


def arity(t: Tree) -> int:
    """
    Return the maximum branching factor (arity) of Tree t.

    >>> t = Tree(23)
    >>> arity(t)
    0
    >>> tn2 = Tree(2, [Tree(4), Tree(4.5), Tree(5), Tree(5.75)])
    >>> tn3 = Tree(3, [Tree(6), Tree(7)])
    >>> tn1 = Tree(1, [tn2, tn3])
    >>> arity(tn1)
    4
    """
    # Base case if it has no children, it is a leaf so
    # there are no more branches
    if t.children == []:
        return 0
    else:
        # Comparing everything
        return max([len(x.children) for x in t.children] + [arity(x) for x in t.children])


def contains_test_passer(t: Tree, test: Callable[[Any], bool]) -> bool:
    """
    Return whether t contains a value that test(value) returns True for.

    >>> t = descendants_from_list(Tree(0), [1, 7, 3, 4.5, 5, 9, 7.5, 8.5], 4)
    >>> def greater_than_nine(n): return n > 9
    >>> contains_test_passer(t, greater_than_nine)
    False
    >>> def even(n): return n % 2 == 0
    >>> contains_test_passer(t, even)
    True
    >>> t = Tree(3)
    >>> def is_3(n): return n == 3
    >>> contains_test_passer(t, is_3)
    True
    """
    # Base case if the value satisfies the test,
    # then we return true
    if t.children == []:
        return test(t.value)
    else:
        return any([contains_test_passer(x, test) for x in t.children] + [test(t.value)])
    # This also works!
    # return test(t.value) or any([contains_test_passer(x, test) for x in t.children])


def list_if(t: Tree, p: Callable[[Any], bool]) -> list:
    """
    Return a list of values in Tree t that satisfy predicate p(value).

    Assume p is defined on all of t's values.

    >>> def p(v): return v > 4
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> list_ = list_if(t, p)
    >>> set(list_) == {5, 6, 7, 8}
    True
    >>> def p(v): return v % 2 == 0
    >>> list_ = list_if(t, p)
    >>> set(list_) == {0, 2, 4, 6, 8}
    True
    """
    # If there is only one leaf
    if t.children == []:
        # If the leaf satisfies the predicate, return the leaf value
        if p(t.value):
            return [t.value]
        else:
            return []
    # If the tree has children
    else:
        # Checks the node value
        if p(t.value):
            # If the node value satisfies the predicate and it has children,
            # add the node
            # value to the list and continue through the children
            return gather_lists([list_if(x, p) for x in t.children]) + [t.value]
        else:
            # If the node value does not satisfy the predicate
            # and it does have children, add
            # the empty list and continue through the children
            return gather_lists([list_if(x, p) for x in t.children]) + []


# helper function that may be useful in the functions
# above
def gather_lists(list_: List[list]) -> list:
    """
    Concatenate all the sublists of L and return the result.

    >>> gather_lists([[1, 2], [3, 4, 5]])
    [1, 2, 3, 4, 5]
    >>> gather_lists([[6, 7], [8], [9, 10, 11]])
    [6, 7, 8, 9, 10, 11]
    """
    new_list = []
    for l in list_:
        new_list += l
    return new_list
    # equivalent to...
    # return sum([list_ for list_ in list_], [])


# helpful helper function
def descendants_from_list(t: Tree, list_: list, branching: int) -> Tree:
    """
    Populate Tree t's descendants from list_, filling them
    in in level order, with up to arity children per node.
    Then return t.

    >>> descendants_from_list(Tree(0), [1, 2, 3, 4], 2)
    Tree(0, [Tree(1, [Tree(3), Tree(4)]), Tree(2)])
    """
    q = Queue()
    q.add(t)
    list_ = list_.copy()
    while not q.is_empty():  # unlikely to happen
        new_t = q.remove()
        new_t: Tree
        for _ in range(0, branching):
            if len(list_) == 0:
                return t  # our work here is done
            else:
                new_t_child = Tree(list_.pop(0))
                new_t.children.append(new_t_child)
                q.add(new_t_child)
    return t


def height(t: Tree) -> int:
    """
    Return 1 + length of longest path of t.

    @param Tree t: tree to find height of
    @rtype: int

    >>> t = Tree(13)
    >>> height(t)
    1
    >>> tn2 = Tree(2, [Tree(4), Tree(4.5), Tree(5)])
    >>> tn3 = Tree(3, [Tree(6), Tree(7)])
    >>> tn1 = Tree(1, [tn2, tn3])
    >>> height(tn1)
    3
    """
    if t.children == []:
        return 1
    else:
        return max([height(x) for x in t.children]) + 1


if __name__ == '__main__':
    import python_ta
    python_ta.check_all()
    import doctest
    doctest.testmod()
