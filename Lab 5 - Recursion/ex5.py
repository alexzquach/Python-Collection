""" recursion exercises with nested lists
"""
from typing import List, Union, Callable, Any


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
        return max(max([max_length(x) for x in obj]), len(obj))


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
    elif len(obj) > n:
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


if __name__ == '__main__':
    import doctest
    doctest.testmod()
