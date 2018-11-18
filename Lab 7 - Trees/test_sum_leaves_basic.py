import unittest

from ex7 import sum_leaves
from hypothesis import given
from hypothesis.strategies import recursive
from hypothesis.strategies import integers
from hypothesis.strategies import tuples
from hypothesis.strategies import none

class BinaryTree:
    """
    A Binary Tree, i.e. arity 2.
   === Attributes ===
    @param object value: value in this node of tree
    @param BinaryTree|None left: left child
    @param BinaryTree|None right: right child
    @rtype: None
    """


    def __init__(self, data, left=None, right=None):
        """
        Create BinaryTree self with value and children left and right.
        @param BinaryTree self: this binary tree
        @param object value: value of this node
        @param BinaryTree|None left: left child
        @param BinaryTree|None right: right child
        @rtype: None
        """
        self.data, self.left, self.right = data, left, right

def tuples_to_tree(t):
    """
    Return a BinaryTree generated from t and the number of leaves.

    Precondition: t is in the form (value, left child, right child) where
                  left child and right child are either None, a value, or
                  another tuple.

    @param tuple(bool, tuple|None|int, tuple|None|int) t: The tuple to turn
                                                            into a BinaryTree
    @rtype: (BinaryTree, int)
    """
    if t is None:
        return (None, 0)

    if type(t) == int:
        return (BinaryTree(t), t)

    (left, l_count) = tuples_to_tree(t[1])
    (right, r_count) = tuples_to_tree(t[2])
    sum_leaves = l_count + r_count

    if not left and not right:
        sum_leaves = t[0]

    return (BinaryTree(t[0], left, right), sum_leaves)

class SumLeavesTests(unittest.TestCase):
    def test_returns_int(self):
        """
        Test sum_leaves to make sure it returns an int.
        """
        return_type = type(sum_leaves(BinaryTree(1)))

        self.assertEqual(return_type, int, "sum_leaves should return type " +
                         "int, but instead returned type {}.".format(
                             return_type))

    def test_none(self):
        """
        Test sum_leaves on None.
        """
        self.assertEqual(sum_leaves(None), 0, "sum_leaves on None should " +
                         "return 0.")

    def test_leaf(self):
        """
        Test sum_leaves on a leaf.
        """
        self.assertEqual(sum_leaves(BinaryTree(2)), 2, "sum_leaves should" +
                         " return the leaf's value when used on a leaf.")

    def test_one_left_child(self):
        """
        Test sum_leaves on a BinaryTree with one left child.
        """
        t = BinaryTree(1, BinaryTree(5))
        self.assertNotEqual(sum_leaves(t), 1, "sum_leaves should not " +
                            "count None or any BinaryTrees with children as" +
                            " leaf nodes.")
        self.assertNotEqual(sum_leaves(t), 6, "sum_leaves should not " +
                            "count None or any BinaryTrees with children as" +
                            " leaf nodes.")
        self.assertEqual(sum_leaves(t), 5, "sum_leaves should return the " +
                         "value of the leaf child when used on a BinaryTree " +
                         "with a single leaf child.")

    def test_one_right_child(self):
        """
        Test sum_leaves on a BinaryTree with one right child
        """
        t = BinaryTree(1, None, BinaryTree(5))
        self.assertNotEqual(sum_leaves(t), 1, "sum_leaves should not " +
                            "count None or any BinaryTrees with children as" +
                            " leaf nodes.")
        self.assertNotEqual(sum_leaves(t), 6, "sum_leaves should not " +
                            "count None or any BinaryTrees with children as" +
                            " leaf nodes.")
        self.assertEqual(sum_leaves(t), 5, "sum_leaves should return the " +
                         "value of the leaf child when used on a BinaryTree " +
                         "with a single leaf child.")

    def test_two_leaf_children(self):
        """
        Test sum_leaves on a BinaryTree with two leaf children.
        """
        t = BinaryTree(5, BinaryTree(4), BinaryTree(3))
        self.assertEqual(sum_leaves(t), 7, "sum_leaves should sum all " +
                         "of the leaves in the entire BinaryTree.")

    @given(recursive(none() | integers(min_value=0, max_value=100),
                     lambda children: tuples(integers(min_value = 0,
                                                      max_value = 100),
                                             children,
                                             children))
           )
    def test_sum_leaves(self, tuple_tree):
        """
        Test sum_leaves on a randomly generated BinaryTree.
        """
        (t, expected) = tuples_to_tree(tuple_tree)
        actual = sum_leaves(t)
        self.assertEqual(actual, expected,
                         ("test_sum_leaves on BinaryTree\n{}\nReturned {}" +
                          " instead of {}.").format(tuple_tree, actual,
                                                    expected))

if __name__ == '__main__':
    unittest.main()
