from typing import List, Union, Callable, Any
from csc148_queue import Queue

# ------ LIST FUNCTIONS COLLECTION ------


def gather_lists(list_: List[List[object]]) -> List[object]:
    """
    Return the concatenation of the sublists of list_.

    >>> list_ = [[1, 2], [3, 4]]
    >>> gather_lists(list_)
    [1, 2, 3, 4]
    """
    # special form of sum for "adding" lists
    return sum(list_, [])


def sum_list(list_: Union[List[int], int]):
    """
    Return the sum of all ints in L.
    >>> sum_list([1, [2, 3], [4, 5, [6, 7], 8]])
    36
    >>> sum([])
    0
    """
    if isinstance(list_, list):
        return sum([sum_list(x) for x in list_])
    else:
        return list_


def list_all(obj: Union[list, object]) -> list:
    """
    Return a list of all non-list elements in obj or obj's sublists, if obj
    is a list.  Otherwise, return a list containing obj.

    >>> obj = 17
    >>> list_all(obj)
    [17]
    >>> obj = [1, 2, 3, 4]
    >>> list_all(obj)
    [1, 2, 3, 4]
    >>> obj = [[1, 2, [3, 4], 5], 6]
    >>> all([x in list_all(obj) for x in [1, 2, 3, 4, 5, 6]])
    True
    >>> all ([x in [1, 2, 3, 4, 5, 6] for x in list_all(obj)])
    True
    """
    if isinstance(obj, list):
        return gather_lists([list_all(x) for x in obj])
        # return sum([list_all(x) for x in obj], [])
    return [obj]


def max_length(obj: Union[list, object]) -> int:
    """
    Return the maximum length of obj or any of its sublists, if obj is a list.
    otherwise return 0.

    >>> max_length(17)
    0
    >>> max_length([1, 2, 3, 17])
    4
    >>> max_length([[1, 2, 3, 3], 4, [4, 5]])
    4
    """
    if not isinstance(obj, list):
        return 0
    else:
        return max([max_length(x) for x in obj] + [len(obj)])#max(max([max_length(x) for x in obj]), len(obj))


def list_over(obj: Union[list, str], n: int) -> List[object]:
    """
    Return a list of strings of length greater than n in obj,
    or sublists of obj, if obj is a list.
    If obj is a string of length greater than n, return a list
    containing obj.  Otherwise return an empty list.

    >>> list_over("five", 3)
    ['five']
    >>> list_over("five", 4)
    []
    >>> list_over(["one", "two", "three", "four"], 3)
    ['three', 'four']
    """
    if isinstance(obj, list):
        return gather_lists([list_over(x, n) for x in obj])
        # return sum([list_over(x, n) for x in obj], [])
    else:
        if len(obj) > n:
            return [obj]
        else:
            return []


def list_even(obj: Union[list, int]) -> List[object]:
    """
    Return a list of all even integers in obj,
    or sublists of obj, if obj is a list.  If obj is an even
    integer, return a list containing obj.  Otherwise return
    en empty list.

    >>> list_even(3)
    []
    >>> list_even(16)
    [16]
    >>> list_even([1, 2, 3, 4, 5])
    [2, 4]
    >>> list_even([1, 2, [3, 4], 5])
    [2, 4]
    >>> list_even([1, [2, [3, 4]], 5])
    [2, 4]
    """
    if isinstance(obj, list):
        return gather_lists([list_even(x) for x in obj])
        # return sum([list_even(x) for x in obj], [])
    elif obj % 2 == 0:
        return [obj]
    else:
        return []


def count_even(obj: Union[list, int]) -> int:
    """
    Return the number of even numbers in obj or sublists of obj
    if obj is a list.  Otherwise, if obj is a number, return 1
    if it is an even number and 0 if it is an odd number.

    >>> count_even(3)
    0
    >>> count_even(16)
    1
    >>> count_even([1, 2, [3, 4], 5])
    2
    """
    if isinstance(obj, list):
        return sum([count_even(x) for x in obj])
    else:
        if obj % 2 == 0:
            return 1
        else:
            return 0


def count_all(obj: Union[list, object]) -> int:
    """
    Return the number of elements in obj or sublists of obj if obj is a list.
    Otherwise, if obj is a non-list return 1.

    >>> count_all(17)
    1
    >>> count_all([17, 17, 5])
    3
    >>> count_all([17, [17, 5], 3])
    4
    """
    if isinstance(obj, list):
        return sum([count_all(x) for x in obj])
    else:
        return 1


def count_above(obj: Union[list, int], n: int) -> int:
    """
    Return tally of numbers in obj, and sublists of obj, that are over n, if
    obj is a list.  Otherwise, if obj is a number over n, return 1.  Otherwise
    return 0.

    >>> count_above(17, 19)
    0
    >>> count_above(19, 17)
    1
    >>> count_above([17, 18, 19, 20], 18)
    2
    >>> count_above([17, 18, [19, 20]], 18)
    2
    """
    if isinstance(obj, list):
        return sum([count_above(x, n) for x in obj])
    elif obj > n:
        return 1
    else:
        return 0


def depth(obj: Union[list, int]) -> int:
    """
    Return 0 if obj is a non-list, or 1 + maximum
    depth of elements of obj, a possibly nested
    list of objects. Or 1 if obj == []

    Assume obj has finite nesting depth

    @param list[object]|object obj: possibly nested list of objects
    @rtype: int

    >>> depth(3)
    0
    >>> depth([])
    1
    >>> depth([[], [[]]])
    3
    >>> depth([1, 2, 3])
    1
    >>> depth([1, [2, 3], 4])
    2
    """
    if obj == []:
        return 1
    elif isinstance(obj, list):
        return 1 + max([depth(x) for x in obj])
    else:
        return 0


def rec_max(obj: Union[list, int]) -> int:
    """
    Return obj if it's an int, or the maximum int in obj,
    a possibly nested list of numbers.

    Assume: obj is an int or non-empty list with finite nesting depth,
    and obj doesn't contain any empty lists

    @param int|list[int|list[...]] obj: possibly nested list of int
    @rtype: int

    >>> rec_max([17, 21, 0])
    21
    >>> rec_max([17, [21, 24], 0])
    24
    >>> rec_max(31)
    31
    """
    if obj == []:
        return 0
    elif isinstance(obj, list):
        return max([rec_max(x) for x in obj])
    else:
        return obj


def concat_strings(string_list: Union[list, str]) -> str:
    """
    Concatenate all the strings in possibly-nested string_list.

    @param list[str]|str string_list:
    @rtype: str

    >>> concat_strings("brown")
    'brown'
    >>> concat_strings(["now", "brown"])
    'nowbrown'
    >>> concat_strings(["how", ["now", "brown"], "cow"])
    'hownowbrowncow'
    >>> concat_strings(["one", ["two", ["three", ["four", "five"], "six"]]])
    'onetwothreefourfivesix'
    >>> concat_strings([])
    ''
    """
    if isinstance(string_list, list):
        return "".join([concat_strings(x) for x in string_list])
    else:
        return string_list


def nested_contains(list_: list, value: object) -> object:
    """
    Return whether list_, or any nested sub-list of list_ contains value.

    @param list list_: list to search
    @param object value: non-list value to search for
    @rtype: bool

    >>> list_ = ["how", ["now", "brown"], 1]
    >>> nested_contains(list_, "brown")
    True
    >>> nested_contains([], 5)
    False
    >>> nested_contains([5], 5)
    True
    >>> nested_contains([100, [17, 23, [1, 11, 10], 5, 7], 0, 9], 1)
    True
    >>> nested_contains([100, [17, 23, [1, 11, 10], 5, 7], 0, 9], 69)
    False
    """
    # check out Python built-in any
    if isinstance(list_, list):
        return any([nested_contains(x, value) for x in list_])
    else:
        return list_ == value


def nested_count(list_: list) -> int:
    """
    Return the number of non-list elements of list_ or its nested sub-lists.

    @param list list_: possibly nested list to count elements of
    @rtype: int

    >>> list_ = ["how", ["now", "brown"], "cow"]
    >>> nested_count(list_)
    4
    >>> nested_count([100, [17, 23, [1, 11, 10], 5, 7], 0, 9])
    10
    """
    # functional if helps here
    if isinstance(list_, list):
        return sum([nested_count(x) for x in list_])
    else:
        return 1


def list_level(obj: List[Any], d: int) -> List:
    """

    Return the non-list elements at a particular level.

    @param list obj: possibly nested list
    @param int d: The level to print out
    @rtype: List

    >>> list_ = [1, [2, [3, 4], 5], 2]
    >>> list_level(list_, 2)
    [2, 5]
    >>> list_level(list_, 3)
    [3, 4]
    """
    if d < 1:
        return []
    elif d == 1:
        return [x for x in obj if not isinstance(x, list)]
    else:
        return sum([list_level(x, d - 1) for x in obj if isinstance(x, list)], [])


def list_levels(obj: List[Any]) -> List:
    """

    Return the non-list elements at all levels as a list.

    @param list obj: possibly nested list
    @rtype: List

    >>> list_ = [1, [2, [3, 4], 5], 2]
    >>> list_levels(list_)
    [[1, 2], [2, 5], [3, 4]]
    """

    return [list_level(obj, d) for d in range(1, depth(obj) + 1)]


def contains_satisfier(list_, predicate: Callable[[object], bool]):
    """
    Return whether possibly-nested list_ contains a non-list element
    that satisfies (returns True for) predicate.
    @param list list_: list to check for predicate satisfiers
    @param (object)->bool predicate: boolean function
    @rtype: bool
    >>> list_ = [5, [6, [7, 8]], 3]
    >>> def p(n): return n > 7
    >>> contains_satisfier(list_, p)
    True
    >>> def p(n): return n > 10
    >>> contains_satisfier(list_, p)
    False
    """
    if not isinstance(list_, list):
        return predicate(list_)
    else:
        return any([contains_satisfier(a, predicate) for a in list_])


# ------ TREE FUNCTIONS ------

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


def count(t: Tree) -> int:
    """
    Return the number of nodes in Tree t.

    >>> t = Tree(17)
    >>> count(t)
    1
    >>> t4 = descendants_from_list(Tree(17), [0, 2, 4, 6, 8, 10, 11], 4)
    >>> count(t4)
    8
    """
    if t.children == []:
        return 1
    else:
        return 1 + sum([count(child) for child in t.children])


def list_all_tree(t: Tree) -> list:
    """
    Return list of values in t.

    >>> t = Tree(0)
    >>> list_all_tree(t)
    [0]
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> list_ = list_all_tree(t)
    >>> list_
    [0, 1, 4, 5, 6, 2, 7, 8, 3]
    >>> list_.sort()
    >>> list_
    [0, 1, 2, 3, 4, 5, 6, 7, 8]
    """
    # implicit base case when len(t.children) == 0
    if t.children == []:
        return [t.value]
    else:
        return sum([list_all_tree(child) for child in t.children], []) + [t.value]

    # if t.children != []:
    #     return [t.value] + sum([list_all_tree(child) for child in t.children], [])
    # else:
    #     return [t.value]


def list_leaves(t: Tree) -> list:
    """
    Return list of values in leaves of t.
    >>> t = Tree(0)
    >>> list_leaves(t)
    [0]
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> list_ = list_leaves(t)
    >>> list_.sort() # so list_ is predictable to compare
    >>> list_
    [3, 4, 5, 6, 7, 8]
    """
    if t.children == []:
        return [t.value]
    else:
        return sum([list_leaves(child) for child in t.children if child is not None], [])


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
        return sum([count_internal(x) for x in t.children]) + 1


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
        return sum([sum_internal(x) for x in t.children] + [t.value])


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
    return max([len(t.children)] + [arity(x) for x in t.children])


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


def count_if(t: Tree, p: Callable[[object], bool]) -> int:
    """
    Return number of values in Tree t that satisfy predicate p(value).
    Assume predicate p is defined on t’s values
    >>> def p(v): return v > 4
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> count_if(t, p)
    4
    >>> def p(v): return v % 2 == 0
    >>> count_if(t, p)
    5
    """
    if t.children == []:
        if p(t.value):
            return 1
        return 0
    else:
        if p(t.value):
            return 1 + sum([count_if(child, p) for child in t.children])
        else:
            return sum([count_if(child, p) for child in t.children])


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
            return gather_lists([list_if(x, p) for x in t.children])


def list_below(t: Tree, n: int) -> list:
    """
    Return list of values in t from nodes with paths no longer
    than n from root.

    >>> t = Tree(0)
    >>> list_below(t, 0)
    [0]
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> L = list_below(t, 1)
    >>> L.sort()
    >>> L
    [0, 1, 2, 3]
    """
    if n == 0:
        return [t.value]
    else:
        return [t.value] + sum([list_below(child, n-1) for child in t.children], [])


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


def preorder_visit(t: Tree, act: Callable[[Tree], Any]) -> None:
    """
    Visit each node of Tree t in preorder, and act on the nodes as they are visited

    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7], 3)
    >>> def act(node): print(node.value)
    >>> preorder_visit(t, act)
    0
    1
    4
    5
    6
    2
    7
    3
    """
    # act on t, then visit t's children in preorder
    act(t)
    # Visit
    for child in t.children:
        preorder_visit(child, act)


def post_order_visit(t: Tree, act: Callable[[Tree], Any]) -> None:
    """
    Visit each node of Tree t in preorder, and act on the nodes as they are visited

    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7], 3)
    >>> def act(node): print(node.value)
    >>> post_order_visit(t, act)
    4
    5
    6
    1
    7
    2
    3
    0
    """
    # Visit t's children then act on t
    for child in t.children:
        post_order_visit(child, act)
    # Act on t
    act(t)


def levelorder_visit(t: Tree, act: Callable[[Tree], Any]) -> None:
    """
    Visit each node of Tree t in levelorder, and act on the nodes as they are visited

    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7], 3)
    >>> def act(node): print(node.value)
    >>> levelorder_visit(t, act)
    0
    1
    2
    3
    4
    5
    6
    7
    """
    t: Tree

    # Adds the tree to the queue
    to_act = Queue()
    to_act.add(t)
    # While the queue is not empty
    while not to_act.is_empty():
        # Acts on the node
        t = to_act.remove()
        act(t)
        # Adds the children to the queue
        for child in t.children:
            to_act.add(child)
def levelorder_visit(t: Tree, act: Callable[[Tree], Any]) -> None:
    """
    Visit each node of Tree t in levelorder, and act on the nodes as they are visited

    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7], 3)
    >>> def act(node): print(node.value)
    >>> levelorder_visit(t, act)
    0
    1
    2
    3
    4
    5
    6
    7
    """
    t: Tree

    # Adds the tree to the queue
    to_act = Queue()
    to_act.add(t)
    # While the queue is not empty
    while not to_act.is_empty():
        # Acts on the node
        t = to_act.remove()
        act(t)
        # Adds the children to the queue
        for child in t.children:
            to_act.add(child)

def levelorder_visit2(t: Tree, act: Callable[[Tree], Any]) -> None:
    """
    Visit each node of Tree t in levelorder, and act on the nodes as they are visited

    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7], 3)
    >>> def act(node): print(node.value)
    >>> levelorder_visit2(t, act)
    0
    1
    2
    3
    4
    5
    6
    7
    """
    level_to_visit = 0
    visited = 1
    while visited > 0:
        visited = visit_level(t, act, level_to_visit)
        level_to_visit += 1


def visit_level(t: Tree, act: Callable[[Tree], Any], n: int) -> int:
    """
    Visit every node in Tree t at level n, return the number of nodes visited

    Assume n is non-negative
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7], 3)
    >>> def act(node): print(node.value)
    >>> visit_level(t, act, 1)
    1
    2
    3
    3
    """
    if n == 0:
        act(t)
        return 1
    else:
        return sum([visit_level(child, act, n - 1) for child in t.children])


def two_count(t: Tree) -> int:
    """Return number of times 2 occurs as a value in any node of t.
    precondition - t is a non-empty tree with number values
    >>> tn2 = Tree(2, [Tree(4), Tree(4.5), Tree(2), Tree(5.75)])
    >>> tn3 = Tree(3, [Tree(6), Tree(2)])
    >>> tn1 = Tree(1, [tn2, tn3])
    >>> two_count(tn1)
    3
    """
    if t.children == []:
        if t.value == 2:
            return 1
        return 0
    else:
        if t.value == 2:
            return 1 + sum([two_count(child) for child in t.children])
        return sum([two_count(child) for child in t.children])

# ------ BINARY TREE CLASSES -------


class BTNode:
    """Binary Tree node.

    data - data this node represents
    left - left child
    right - right child
    """
    data: object
    left: Union["BTNode", None]
    right: Union["BTNode", None]

    def __init__(self, data: object,
                 left: Union["BTNode", None]=None,
                 right: Union["BTNode", None]=None) -> None:
        """
        Create BTNode (self) with data and children left and right.

        An empty BTNode is represented by None.

        """
        self.data, self.left, self.right = data, left, right

    def __eq__(self, other: Any) -> bool:
        """
        Return whether BTNode (self) is equivalent to other.

        >>> BTNode(7).__eq__('seven')
        False
        >>> b1 = BTNode(7, BTNode(5))
        >>> b1.__eq__(BTNode(7, BTNode(5), None))
        True
        """
        return (type(self) == type(other) and
                self.data == other.data and
                (self.left, self.right) == (other.left, other.right))

    def __repr__(self) -> str:
        """
        Represent BTNode (self) as a string that can be evaluated to
        produce an equivalent BTNode.

        >>> BTNode(1, BTNode(2), BTNode(3))
        BTNode(1, BTNode(2, None, None), BTNode(3, None, None))
        """
        return 'BTNode({}, {}, {})'.format(self.data,
                                           repr(self.left),
                                           repr(self.right))

    def __str__(self, indent: str="") -> str:
        """
        Return a user-friendly string representing BTNode (self) inorder.
        Indent by indent.

        >>> b = BTNode(1, BTNode(2, BTNode(3)), BTNode(4))
        >>> print(b)
            4
        1
            2
                3
        <BLANKLINE>
        """
        right_tree = self.right.__str__(indent + '    ') if self.right else ''
        left_tree = self.left.__str__(indent + '    ') if self.left else ''
        return right_tree + '{}{}\n'.format(indent, str(self.data)) + left_tree

    def __contains__(self: Union["BTNode", None], data: object) -> bool:
        """ (BTNode, object) -> value

        Return whether tree rooted at node contains value.

        >>> BTNode.__contains__(None, 5)
        False
        >>> t = BTNode(5, BTNode(7), BTNode(9))
        >>> t.__contains__(7)
        True
        >>> 9 in t
        True
        >>> 11 in t
        False
        """
        if self is None:
            return False
        else:
            return (self.data == data
                    # call with BTNode in case self.left, self.right are None
                    or BTNode.__contains__(self.left, data)
                    or BTNode.__contains__(self.right, data))


def list_longest_path(node: Union[BTNode, None]) -> list:
    """ List the data in a longest path of node.

    >>> list_longest_path(None)
    []
    >>> list_longest_path(BTNode(5))
    [5]
    >>> b1 = BTNode(7)
    >>> b2 = BTNode(3, BTNode(2), None)
    >>> b3 = BTNode(5, b2, b1)
    >>> list_longest_path(b3)
    [5, 3, 2]
    >>> b4 = BTNode(1, BTNode(2, BTNode(4)), BTNode(3))
    >>> list_longest_path(b4)
    [1, 2, 4]
    """

    if node is None:
        return []
    # Determines if the node is a leaf
    left = list_longest_path(node.left)
    right = list_longest_path(node.right)
    if len(left) > len(right):
        return [node.data] + left
    return [node.data] + right


def list_between(node: Union[BTNode, None], start: object, end: object) -> list:
    """
    Return a Python list of all data in the binary search tree
    rooted at node that are between start and end (inclusive).

    A binary search tree t is a BTNode where all nodes in the subtree
    rooted at t.left are less than t.data, and all nodes in the subtree
    rooted at t.right are more than t.data

    Avoid visiting nodes with values less than start or greater than end.

    >>> b_left = BTNode(4, BTNode(2), BTNode(6))
    >>> b_right = BTNode(12, BTNode(10), BTNode(14))
    >>> b = BTNode(8, b_left, b_right)
    >>> list_between(None, 3, 13)
    []
    >>> list_between(b, 2, 3)
    [2]
    >>> L = list_between(b, 3, 11)
    >>> L.sort()
    >>> L
    [4, 6, 8, 10]
    """
    # Base case
    if node is None:
        return []
    else:
        # If the data is out of range, return the right node because
        # we know it is a binary search tree
        if node.data < start:
            return list_between(node.right, start, end)
        # If the data is out of range, return the left because we know
        # it is a binary search tree
        elif node.data > end:
            return list_between(node.left, start, end)
        # Else, if it is in the range append the data and return
        # the left and the right
        else:
            # return list_between(node.left, start, end) + [node.data] + list_between(node.right, start, end)
            return [node.data] + sum([list_between(node.left, start, end), list_between(node.right, start, end)], [])


def count_shallower(t: Union[BTNode, None], n: int) -> int:
    """ Return the number of nodes in tree rooted at t with
    depth less than n.

    >>> t = BTNode(0, BTNode(1, BTNode(2)), BTNode(3))
    >>> count_shallower(t, 2)
    3
    """
    if t is None or n == 0:
        return 0
    else:
        return 1 + sum([count_shallower(t.left, n - 1), count_shallower(t.right, n - 1)])


def concatenate_leaves(t: Union[BTNode, None]) -> str:
    """
    Return the string values in the Tree rooted at t concatenated from left to right.
    Assume all leaves have string value.

    >>> t1 = BTNode("one")
    >>> t2 = BTNode("two")
    >>> t3 = BTNode("three", t1, t2)
    >>> concatenate_leaves(t1)
    'one'
    >>> concatenate_leaves(t3)
    'onetwo'
    """
    t.data: str
    if t is None:
        return ""
    elif t.left is None and t.right is None:
        return t.data
    else:
        return "".join([concatenate_leaves(t.left), concatenate_leaves(t.right)])


def count_leaves_b(t: Union[BTNode, None]) -> int:
    """
    Return the number of leaves in BinaryTree t.

    >>> t1 = BTNode(1)
    >>> t2 = BTNode(2)
    >>> t3 = BTNode(3, t1, t2)
    >>> count_leaves_b(None)
    0
    >>> count_leaves_b(t3)
    2
    """
    if t is None:
        return 0
    # If it does not have a right or left, it is a leaf
    elif t.left is None and t.right is None:
        return 1
    else:
        return sum([count_leaves_b(t.left), count_leaves_b(t.right)])


def sum_leaves_b(t: Union[BTNode, None]) -> int:
    """
    Return the sum of the values in the leaves of BinaryTree t.  Return
    0 if t is empty.
    Assume all leaves have integer value.

    >>> t1 = BTNode(1)
    >>> t2 = BTNode(2)
    >>> t3 = BTNode(3, t1, t2)
    >>> sum_leaves_b(t2)
    2
    >>> sum_leaves_b(t3)
    3
    """
    t.data: int

    if t is None:
        return 0
    # If it does not have a right or left, it is a leaf
    elif t.left is None and t.right is None:
        return t.data
    else:
        return sum([sum_leaves_b(t.left), sum_leaves_b(t.right)])


def sum_internal_b(t: Union[BTNode, None]) -> int:
    """
    Return the sum of the values in the internal nodes of BinaryTree t.  Return
    0 if t is empty.
    Assume all internal nodes have integer value.

    >>> t1 = BTNode(1)
    >>> t2 = BTNode(2)
    >>> t3 = BTNode(3, t1, t2)
    >>> sum_internal_b(t2)
    0
    >>> sum_internal_b(t3)
    3
    """
    t.data: int

    # If the binary tree is empty
    if t is None:
        return 0
    # If it has a left or right, it is an internal node, so return
    # the value of the internal node + the sum of its left or right
    elif t.left is not None or t.right is not None:
        return t.data + sum([sum_internal_b(t.left), sum_internal_b(t.right)])
    # Handles if the tree has a node and just a node
    else:
        return 0


def evaluate(b: "BTNode") -> float:
    """
    Evaluate the expression rooted at b.  If b is a leaf,
    return its float value.  Otherwise, evaluate b.left and
    b.right and combine them with b.value.

    Assume:  -- b is a non-empty binary tree
             -- interior nodes contain value in {"+", "-", "*", "/"}
             -- interior nodes always have two children
             -- leaves contain float value

     @param BinaryTree b: binary tree representing arithmetic expression
     @rtype: float

    >>> b = BTNode(3.0)
    >>> evaluate(b)
    3.0
    >>> b = BTNode("*", BTNode(3.0), BTNode(4.0))
    >>> evaluate(b)
    12.0
    """
    b.data: Union[str, float]
    if b.left is None and b.right is None:
        return b.data
    else:
        return eval(str(evaluate(b.left))
                    + b.data
                    + str(evaluate(b.right)))


def parenthesize(b: "BTNode") -> str:
    """
        Evaluate the expression rooted at b.  If b is a leaf,
        return its float value.  Otherwise, evaluate b.left and
        b.right and combine them with b.value.

        Assume:  -- b is a non-empty binary tree
                 -- interior nodes contain value in {"+", "-", "*", "/"}
                 -- interior nodes always have two children
                 -- leaves contain float value

         @param BinaryTree b: binary tree representing arithmetic expression
         @rtype: float

    >>> b = BTNode(3.0)
    >>> print(parenthesize(b))
    3.0
    >>> b = BTNode("*", BTNode(3.0), BTNode(4.0))
    >>> parenthesize(b)
    '(3.0) * (4.0)'
    """

    if b.left is None:
        return str(b.data)
    else:
        return "({}) {} ({})".format(parenthesize(b.left), b.data, parenthesize(b.right))


def height_b(node: "BTNode") -> int:
    """
    Returns the height of the tree

    >>> t = BinaryTree(5, BinaryTree(7), None)
    >>> height_b(t)
    2
    """

    if node is None:
        return 0
    else:
        return 1 + max(height_b(node.left), height_b(node.right))


def find(node: Union["BTNode", None], data: object) -> Union["BTNode", None]:
    """
    Return a BTnode containing data, or else None


    >>> find(None, 5) is None
    True
    >>> find(BTNode(5, BTNode(7), BTNode(9)), 7)
    BTNode(7, None, None)
    """

    if node is None:
        pass  # return None, python style requires this
    else:
        find_left_result = find(node.left, data)
        if node.data == data:
            return node
        elif find_left_result is not None:
            return find_left_result
        elif find(node.right, data) is not None:
            return find(node.right, data)
        else:
            return None


def inorder(root: Union["BTNode, None"], visit) -> None:
    """
    Visit the left subtree inorder
    Visit the node itself
    Visit the right subtree inorder

    >>> b = BTNode("A", BTNode("C"), BTNode("D"))
    >>> def f(node): print(node.data)
    >>> inorder(b, f)
    C
    A
    D
    >>> b2 = BTNode(1, BTNode(2, BTNode(3), BTNode(5)), BTNode(4, BTNode(6), BTNode(7)))
    >>> inorder(b2, f)
    3
    2
    5
    1
    6
    4
    7
    """
    if root is None:
        pass
    else:
        inorder(root.left, visit)
        visit(root)
        inorder(root.right, visit)


def preorder_visit_b(root: Union[BTNode, None], visit) -> None:
    """
    Visit the tree in preorder

    >>> b = BTNode("A", BTNode("C"), BTNode("D"))
    >>> def f(node): print(node.data)
    >>> preorder_visit_b(b, f)
    A
    C
    D
    >>> b2 = BTNode(1, BTNode(2, BTNode(4, BTNode(6)), BTNode(5)), BTNode(3, BTNode(7), BTNode(8, BTNode(9))))
    >>> preorder_visit_b(b2, f)
    1
    2
    4
    6
    5
    3
    7
    8
    9
    """

    if root is None:
        pass
    else:
        visit(root)
        preorder_visit_b(root.left, visit)
        preorder_visit_b(root.right, visit)


def postorder_visit(root: Union[BTNode, None], visit) -> None:
    """
    Visit the tree in postorder

    >>> b = BTNode("A", BTNode("C"), BTNode("D"))
    >>> def f(node): print(node.data)
    >>> postorder_visit(b, f)
    C
    D
    A
    >>> b2 = BTNode(1, BTNode(2, BTNode(4, BTNode(6)), BTNode(5)), BTNode(3, BTNode(7), BTNode(8, BTNode(9))))
    >>> postorder_visit(b2, f)
    6
    4
    5
    2
    7
    9
    8
    3
    1
    """

    if root is None:
        pass
    else:
        postorder_visit(root.left, visit)
        postorder_visit(root.right, visit)
        visit(root)


def level_order_visit(root: Union[BTNode, None], visit: Callable[["BTNode"], Any]) -> None:
    """
    Visit the tree in level order

    >>> b = BTNode("A", BTNode("C", BTNode("B")), BTNode("D"))
    >>> def f(node): print(node.data)
    >>> level_order_visit(b, f)
    A
    C
    D
    B
    >>> b2 = BTNode(1, BTNode(2, BTNode(4, BTNode(6)), BTNode(5)), BTNode(3, BTNode(7), BTNode(8, BTNode(9))))
    >>> level_order_visit(b2, f)
    1
    2
    3
    4
    5
    7
    8
    6
    9
    """
    node: BTNode

    if root is None:
        pass
    else:
        q = Queue()
        q.add(root)
        while not q.is_empty():
            node = q.remove()
            visit(node)
            if node.left is not None:
                q.add(node.left)
            if node.right is not None:
                q.add(node.right)


def string_to(t: Union[BTNode, None], d: int) -> str:
    """
    >>> t = BTNode("a", BTNode("b"), BTNode("c"))
    >>> string_to(t, 0)
    'a'
    >>> string_to(t, 1)
    'bc'
    >>> string_to(t, 3)
    ''
    """
    t.data: str

    if t is None:
        return ''
    else:
        if d < 0:
            return ''
        elif d == 0:
            return t.data
        else:
            return "".join([string_to(t.left, d - 1), string_to(t.right, d - 1)])


def prune(t, predicate) -> Union[Tree, None]:
    """ Return a new tree with the same values as t, except it prunes (omits) all paths of t that start
    with nodes where predicate(node.value) == False. If predicate(t.value) == False, then prune
    returns None.
    Assume that all values in t are ints, and that predicate always takes an int and returns a bool.
    Oparam Tree t: tree to prune
    ®param function[int, bool] predicate: predicate on t's values.
    Qrtype: Tree I None
    >>> tl = Tree(6, [Tree(8) , Tree(9)])
    >>> t2 = Tree(4, [Tree(11), Tree(10)])
    >>> t3 = Tree(7, [Tree(3), Tree(12)])
    >>> t = Tree(5, [tl, t2, t3] )
    >>> t3_pruned = Tree (7, [Tree(12)])
    >>> def predicate (v) : return v > 4
    >>> pruned = prune(t, predicate)
    >>> pruned == Tree(5, [tl, t3_pruned])
    True
    """

    if t.children == []:
        if predicate(t.value):
            return Tree(t.value)
        return None
    else:
        if predicate(t.value):
            children = [prune(x, predicate) for x in t.children]
            return Tree(t.value, [x for x in children if x is not None])
        return None

class BSTree:
    """ A simple binary search tree ADT """
    def __init__(self, data, left=None, right=None):
        """
        Create BSTree self with content data, left child left,
        and right child right.
        @param BSTree self: this binary search tree
        Qparam object data: data contained in this tree
        Oparam BSTree left: left child of this tree
        Sparam BSTree right: right child of this tree
        Ortype: None
        """
        self.data, self.left, self.right = data, left, right


def find_left_streak(t) :
    """ Return the parent node of the shallowest left streak in t,
    or None if there is no left streak.
    Qparam BSTree t : the root of the whole tree
    ©rtype: BSTreeI None
    >>> left = BSTree(4, (BSTree(3, BSTree(2, BSTree(1, BSTree(0))))))
    >>> t = BSTree(5, left, BSTree(6))
    >>> find_left_streak(t).data
    5
    >>> t.left.right = BSTree(4.5)
    >>> find_left_streak(t).data
    4
    """
    streak_parent = t
    while streak_parent.left is not None:
        node = streak_parent.left
        if (node.left is not None and node.right is None) and \
        (node.left.left is not None and node.left.right is None):
            return streak_parent
        streak_parent = node
    # if the end of the loop is reached, there is no left streak - return None


def fix_left_streaks(t):
    """ Modify t by fixing all left streaks.
    Qparam BSTree t: the tree to fix
    Ortype: None
    >>> left = BSTree(4, (BSTree(3, BSTree(2, BSTree(1, BSTree(0))))))
    >>> t = BSTree(5, left, BSTree(6))
    >>> t.left.right is None
    True
    >>> t.left.left.right is None
    True
    >>> fix_left_streaks(t)
    >>> t.left.right.data == 4
    True
    >>> t.left.left.right.data == 2
    True
    """
    left_streak_parent = find_left_streak(t)
    if left_streak_parent is None:
        pass
    else:
        left_streak_child = left_streak_parent.left
        left_streak_parent.left = left_streak_child.left
        left_streak_parent.left.right = left_streak_child
        fix_left_streaks(left_streak_parent.left)

def pathlength_sets(t) :
    """
    Replace the value of each node in Tree t by a se t containing al l
    path lengths from tha t node t o any leaf. A path's length is the
    number of edges i t contains.
    Oparam Tree t : tre e to record path lengths in
    Qrtype : None
    >>> t = Tree (5)
    >>> pathlength_sets(t)
    >>> print(t)
    {0}
    >>> t . children . append(Tree(17) )
    >>> t.children.append(Tree(13, [Tree(11)]))
    >>> pathlength_sets(t)
    >>> print(t)
    """
    if t.children == []:
        t.value = set([0])
    else:
        t.value = set()
        for x in t.children:
            pathlength_sets(x)
            t.value = t.value.union(x.value)
        t.value = {x + 1 for x in t.value}

def swap_even(t, d=0):
    """
    Swap lef t and righ t children of nodes at even depth.
    Recall tha t the root has depth 0, its children have depth 1,
    grandchildren have depth 2, and so on.
    ®param BinaryTree t : tre e to carry out swapping on.
    ®param in t depth: distanc e from the root
    ®rtype: None
    >>> bl = BTNode(1, BTNode(2, BTNode(3)))
    >>> b4 = BTNode(4, BTNode(5), bl)
    >>> print(b4)
    >>> swap_even(b4)
    >>> print(b4)
    """
    if t is None or (t.left is None and t.right is None):
        pass
    else:
        if d % 2 == 0:
            t.left, t.right = t.right, t.left
        swap_even(t.left, d + 1)
        swap_even(t.right, d + 1)

