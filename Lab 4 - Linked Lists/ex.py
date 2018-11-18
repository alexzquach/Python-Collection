""" practice on linked lists
"""
from typing import Union, Any


class LinkedListException(Exception):
    """
    A Linked list exception
    """
    pass


class LinkedListNode:
    """
    Node to be used in linked list

    === Attributes ===
    next_ - successor to this LinkedListNode
    value - data this LinkedListNode represents
    """
    next_: Union["LinkedListNode", None]
    value: object

    def __init__(self, value: object,
                 next_: Union["LinkedListNode", None]=None) -> None:
        """
        Create LinkedListNode self with data value and successor next_.
        """
        self.value, self.next_ = value, next_
        if next_ is not None:
            self.skip = self.next_.next_
        else:
            self.skip = None

    def __str__(self) -> str:
        """
        Return a user-friendly representation of this LinkedListNode.

        >>> n = LinkedListNode(5, LinkedListNode(7))
        >>> print(n)
        5 -> 7 ->|
        """
        # start with a string s to represent current node.
        s = "{} ->".format(self.value)
        # create a reference to "walk" along the list
        current_node = self.next_
        # for each subsequent node in the list, build s
        while current_node is not None:
            s += " {} ->".format(current_node.value)
            current_node = current_node.next_
        # add "|" at the end of the list
        assert current_node is None, "unexpected non_None!!!"
        s += "|"
        return s

    def __eq__(self, other: Any) -> bool:
        """
        Return whether LinkedListNode self is equivalent to other.

        @param LinkedListNode self: this LinkedListNode
        @param LinkedListNode|object other: object to compare to self.
        @rtype: bool

        >>> LinkedListNode(5).__eq__(5)
        False
        >>> n1 = LinkedListNode(5, LinkedListNode(7))
        >>> n2 = LinkedListNode(5, LinkedListNode(7, None))
        >>> n1.__eq__(n2)
        True
        """
        return type(self) == type(other) and self.next_ == other.next_ and self.value == other.value


class LinkedList:
    """
    Collection of LinkedListNodes

    === Attributes ==
    front - first node of this LinkedList
    back - last node of this LinkedList
    size - number of nodes in this LinkedList, >= 0
    """
    front: Union[LinkedListNode, None]
    back: Union[LinkedListNode, None]
    size: int

    def __init__(self) -> None:
        """
        Create an empty linked list.
        """
        self.front, self.back, self.size = None, None, 0

    def __str__(self) -> str:
        """
        Return a human-friendly string representation of
        LinkedList self.

        >>> lnk = LinkedList()
        >>> print(lnk)
        Empty!
        >>> lnk.prepend(5)
        >>> print(lnk)
        5 ->| Size: 1
        """
        # deal with the case where this list is empty
        if self.front is None:
            assert self.back is None and self.size is 0, "ooooops!"
            return "Empty!"
        else:
            # use front.__str__() if this list isn't empty
            return str(self.front) + " Size: {}".format(self.size)

    def __eq__(self, other: Any) -> bool:
        """
        Return whether LinkedList self is equivalent to
        other.

        >>> LinkedList().__eq__(None)
        False
        >>> lnk = LinkedList()
        >>> lnk.prepend(5)
        >>> lnk2 = LinkedList()
        >>> lnk2.prepend(5)
        >>> lnk.__eq__(lnk2)
        True
        >>> lnk3 = LinkedList()
        >>> lnk3.prepend(7)
        >>> lnk4 = LinkedList()
        >>> lnk4.prepend("Jimmy")
        >>> lnk3 == lnk4
        False
        """

        count = 0
        # Checks if they are both linked lists
        if type(self) == type(other):
            # Checks if both linked lists are the same size.
            # If they are not the same size, then they are not equivalent lists
            if self.size == other.size:
                # Begins walking the two linked lists
                cur_node1 = self.front
                cur_node2 = other.front
                # Keeps walking while the node from list one and the node from list
                # two are equivalent AND while we have not reached the end of the list
                while cur_node1 == cur_node2 and cur_node1 is not None and cur_node2 is not None:
                    count += 1
                    cur_node2 = cur_node2.next_
                    cur_node1 = cur_node1.next_
                # If the count equals the size of the list, that means
                # we successfully walked through the entire list
                # meaning that the two linked lists are equivalent
                if count == self.size:
                    return True
        # Returns false if anything fails
        return False

    def delete_after(self, value: object) -> None:
        """
        Remove the node following the first occurrence of value, if
        possible, otherwise leave self unchanged.
        >>> lnk2 = LinkedList()
        >>> lnk2.prepend(7)
        >>> lnk2.prepend(100)
        >>> lnk2.prepend(99)
        >>> lnk2.prepend(32)
        >>> lnk2.prepend(99)
        >>> lnk2.delete_after(99)
        >>> print(lnk2)
        99 -> 99 -> 100 -> 7 ->| Size: 4
        """

        # cur_node = self.front
        # next_node = self.front.next_
        # while next_node is not None:
        #     if cur_node.value == value:
        #         cur_node.next_ = next_node.next_
        #         self.size -= 1
        #         break
        #     cur_node = cur_node.next_
        #     next_node = next_node.next_

        # if value in self:
        #     cur_node = self.front
        #     next_node = self.front.next_
        #     while cur_node.value != value:
        #         cur_node = self.front.next_
        #         next_node = cur_node.next_
        #     cur_node.next_ = next_node.next_
        #     self.size -= 1

        if value in self:
            cur_node = self.front
            while cur_node is not None and cur_node.value != value:
                cur_node = cur_node.next_
            cur_node.next_ = cur_node.next_.next_
            self.size -= 1

    def append(self, value: object) -> None:
        """
        Insert a new LinkedListNode with value after self.back.

        >>> lnk = LinkedList()
        >>> lnk.append(5)
        >>> lnk.size
        1
        >>> print(lnk.front)
        5 ->|
        >>> lnk.append(6)
        >>> lnk.size
        2
        >>> print(lnk.front)
        5 -> 6 ->|
        """
        # create the new node
        new_node = LinkedListNode(value)
        # if the list is empty, the new node is front and back
        if self.size == 0:
            assert self.back is None and self.front is None, "ooops"
            self.front = self.back = new_node
        # if the list isn't empty, front stays the same
        else:
            # change *old* self.back.next_ first!!!!
            self.back.next_ = new_node
            self.back = new_node
        # remember to increase the size
        self.size += 1

    def prepend(self, value: object) -> None:
        """
        Insert value before LinkedList self.front.

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> str(lnk.front)
        '2 -> 1 -> 0 ->|'
        >>> lnk.size
        3
        """
        # Create new node with next_ referring to front
        new_node = LinkedListNode(value, self.front)
        # change front
        self.front = new_node
        # if the list was empty, change back
        if self.size == 0:
            self.back = new_node
        # update size
        self.size += 1

    def delete_front(self) -> None:
        """
        Delete LinkedListNode self.front from self.

        Assume self.front is not None

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> lnk.delete_front()
        >>> str(lnk.front)
        '1 -> 0 ->|'
        >>> lnk.size
        2
        >>> lnk.delete_front()
        >>> lnk.delete_front()
        >>> str(lnk.front)
        'None'
        """
        assert self.front is not None, "unexpected None!"
        # if back == front, set it to None
        if self.front == self.back:
            self.back = None
        # set front to its successor
        self.front = self.front.next_
        # decrease size
        self.size -= 1

    def __setitem__(self, index: int, value: object) -> None:
        """
        Set the value of list at position index to value. Raise IndexError
        if index >= self.size or index < -self.size
        >>> lnk = LinkedList()
        >>> lnk.prepend(5)
        >>> print(lnk)
        5 ->| Size: 1
        >>> lnk[0] = 7
        >>> print(lnk)
        7 ->| Size: 1
        >>> lnk2 = LinkedList()
        >>> lnk2.prepend(7)
        >>> lnk2.prepend(100)
        >>> lnk2.prepend(99)
        >>> lnk2.prepend(32)
        >>> lnk2[2] = 66
        >>> print(lnk2)
        32 -> 99 -> 66 -> 7 ->| Size: 4
        """
        count = 0
        if index >= self.size or index < -1 * self.size:
            raise IndexError("Index out of Linked List range!")
        # Adjusts the index if it is negative
        elif index < 0:
            index += self.size
        else:
            pass
        # Begins walking through the linked list
        cur_node = self.front
        for i in range(index):
            cur_node = cur_node.next_
        # while count < index:
        #     assert cur_node is not None, "Unexpected None!"
        #     cur_node = cur_node.next_
        #     count += 1
        cur_node.value = value

    def __add__(self, other: "LinkedList") -> "LinkedList":
        """
        Return a new list by concatenating self to other.  Leave
        both self and other unchanged.

        >>> lnk1 = LinkedList()
        >>> lnk1.prepend(5)
        >>> lnk2 = LinkedList()
        >>> lnk2.prepend(7)
        >>> lnk2.prepend(100)
        >>> lnk2.prepend(99)
        >>> lnk2.prepend(32)
        >>> print(lnk1 + lnk2)
        5 -> 32 -> 99 -> 100 -> 7 ->| Size: 5
        >>> print(lnk1)
        5 ->| Size: 1
        >>> print(lnk2)
        32 -> 99 -> 100 -> 7 ->| Size: 4
        """

        assert other.size != 0, "One of the linked lists are empty"
        # Creates the new list
        new_list = LinkedList()
        # Begins walking through the first linked list
        cur_node = self.front
        while cur_node is not None:
            new_list.append(cur_node.value)
            cur_node = cur_node.next_
        cur_node = other.front
        # Walks through the second linked list
        while cur_node is not None:
            new_list.append(cur_node.value)
            cur_node = cur_node.next_

        return new_list

    def insert_before(self, value1: object, value2: object) -> None:
        """
        Insert value1 into LinkedList self before the first occurrence
        of value2, if it exists.  Otherwise leave self unchanged.
        >>> lnk2 = LinkedList()
        >>> lnk2.prepend(7)
        >>> lnk2.prepend(100)
        >>> lnk2.prepend(99)
        >>> lnk2.prepend(32)
        >>> lnk2.insert_before(54, 100)
        >>> print(lnk2)
        32 -> 99 -> 54 -> 100 -> 7 ->| Size: 5
        """
        # Checks if the value2 is in the linked list
        if value2 in self:
            # Begins walking the list
            # previous_node = None
            # cur_node = self.front
            # while cur_node.value != value2:
            #     previous_node = cur_node
            #     cur_node = cur_node.next_
            # new_node = LinkedListNode(value1, cur_node)
            # previous_node.next_ = new_node
            # self.size += 1
            cur_node = self.front
            while cur_node.next_ is not None and cur_node.next_.value != value2:
                cur_node = cur_node.next_
            new_node = LinkedListNode(value1, cur_node.next_)
            cur_node.next_ = new_node
            self.size += 1

    def copy(self) -> "LinkedList":
        """
        Return a copy of LinkedList self.  The copy should have
        different nodes, but equivalent values, from self.

        >>> lnk = LinkedList()
        >>> lnk.prepend(5)
        >>> lnk.prepend(7)
        >>> print(lnk.copy())
        7 -> 5 ->| Size: 2
        """
        # Creates a new copy of self
        new_linked_list = LinkedList()
        cur_node = self.front
        while cur_node is not None:
            new_linked_list.append(cur_node.value)
            cur_node = cur_node.next_
        return new_linked_list

    def __len__(self) -> int:
        """
        Return the number of nodes in LinkedList self.
        >>> lnk2 = LinkedList()
        >>> lnk2.prepend(7)
        >>> lnk2.prepend(100)
        >>> lnk2.prepend(99)
        >>> lnk2.prepend(32)
        >>> len(lnk2)
        4
        """
        return self.size

    def __getitem__(self, index: int) -> object:
        """
        Return the value at LinkedList self's position index.

        >>> lnk = LinkedList()
        >>> lnk.append(1)
        >>> lnk.append(0)
        >>> lnk.__getitem__(1)
        0
        >>> lnk[-1]
        0
        """
        # deal with a negative index by adding self.size
        if (-self.size > index
                or index > self.size):
            raise IndexError("out of range!!!")
        elif index < 0:
            index += self.size
        current_node = self.front
        # walk index steps along from 0 to retrieve element
        for _ in range(index):
            assert current_node is not None, "unexpected None!!!!!"
            current_node = current_node.next_
        # return the value at position index
        return current_node.value

    def __contains__(self, value: object) -> bool:
        """
        Return whether LinkedList self contains value.

        >>> lnk = LinkedList()
        >>> lnk.append(0)
        >>> lnk.append(1)
        >>> lnk.append(2)
        >>> 2 in lnk
        True
        >>> lnk.__contains__(3)
        False
        """
        current_node = self.front
        # "walk" the linked list
        while current_node is not None:
            # if any node has a value == value, return True
            if current_node.value == value:
                return True
            current_node = current_node.next_
        # if you get to the end without finding value,
        # return False
        return False

    def concatenate(self, lnk2: "LinkedList") -> "LinkedList":
        """
        Concatenates two linked lists together and deletes the second
        linked list used to concatenate, while leaving self unchanged
        and deleting lnk2
        >>> lnk1 = LinkedList()
        >>> lnk1.prepend(5)
        >>> lnk2 = LinkedList()
        >>> lnk2.prepend(7)
        >>> lnk2.prepend(100)
        >>> lnk2.prepend(99)
        >>> lnk2.prepend(32)
        >>> print(lnk1.concatenate(lnk2))
        5 -> 32 -> 99 -> 100 -> 7 ->| Size: 5
        >>> print(lnk1)
        5 ->| Size: 1
        >>> print(lnk2)
        Empty!
        """

        assert lnk2.size != 0, "The list you are concatenating is empty!"
        new_lnk = LinkedList()
        # Walks through the first list
        cur_node = self.front
        while cur_node is not None:
            new_lnk.append(cur_node.value)
            cur_node = cur_node.next_
        # Walks through the second list
        cur_node = lnk2.front
        while cur_node is not None:
            new_lnk.append(cur_node.value)
            cur_node = cur_node.next_

        # Deletes the second linked list after concatenating
        lnk2.front = None
        lnk2.back = None
        lnk2.size = 0
        return new_lnk

    def swap(self, other: "LinkedList") -> None:
        """
        Swaps the values at every node in the linked list while keeping
        the node ID's the same

        precondition: the length of the lists must be the same, if not
        an exception is raised
        """

        if self.size != other.size:
            raise LinkedListException("The linked lists are not the same size")
        else:
            # Begins walking the two lists at the same time
            cur_node = self.front
            other_node = other.front
            # While it is not the last element of the linked list
            while cur_node is not None:
                # Swaps the values
                temp_value = cur_node.value
                cur_node.value = other_node.value
                other_node.value = temp_value
                # Moves to the next node
                cur_node = cur_node.next_
                other_node = other_node.next_

    def remove_first_double(self):
        """
        Remove second of two adjacent nodes with duplicate values.
        If there is no such node, leave self as is. No need
        to deal with subsequent adjacent duplicate values.
        @param LinkedList self: this linked list
        @rtype: None
        >>> list_ = LinkedList()
        >>> list_.append(3)
        >>> list_.append(2)
        >>> list_.append(2)
        >>> list_.append(3)
        >>> list_.append(3)
        >>> print(list_.front)
        3 -> 2 -> 2 -> 3 -> 3 ->|
        >>> list_.remove_first_double()
        >>> print(list_.front)
        3 -> 2 -> 3 -> 3 ->|
        """
        cur_node = self.front
        next_node = self.front.next_
        while next_node is not None and cur_node.value != next_node.value:
            cur_node = cur_node.next_
            next_node = next_node.next_
        cur_node.next_ = next_node.next_
        self.size -= 1

    def precursors(self, value):
        """
        Returns a tuple containing the two list nodes with the two highest
        values which are less than the method argument 'value'.
        Oparam LinkedList self : this LinkedList
        ®param int value : value to insert
        Ortype: (LinkedListNodeI None, LinkedListNodeI None)
        >>> Ink = LinkedList ()
        >>> Ink.precursors(3)
        (None, None)
        >>> a = LinkedListNode(3)
        >>> Ink.front, Ink.back, Ink.size = a, a, 1
        >>> Ink.precursors(1)
        (None, None)
        >>> b = LinkedListNode (1, a)
        >>> Ink.front, Ink.size = b, 2
        >>> prel = Ink.precursors(5)[0]
        >>> pre2 = Ink.precursors(5)[1]
        >>> prel.value, pre2.value
        (1, 3)
        """
        if self.size <= 1:
            return (None, None)
        else:
            cur_node = self.front
            if cur_node.value > value:
                return (None, None)
            elif cur_node.next_.value > value:
                return (cur_node, None)
            else:
                while cur_node.skip is not None and cur_node.skip.value < value:
                    cur_node = cur_node.next_
                return (cur_node, cur_node.next_)

    def insert(self, value, prev, cur):
        """
        Inserts a new node with value after node cur. Updates all links correctly.
        This is a method of class LinkedList.
        Sparam LinkedList self: this LinkedList
        Oparam int value : value to insert
        (Sparam LinkedListNodeI None cur: node before the one we are inserting
        @param LinkedListNodeI None prev: node before cur
        Ortype: None
        >>> Ink = LinkedList ()
        >>> Ink.insert(3, Ink.precursors(3)[0], Ink.precursors(3)[1] )
        >>> Ink.insert(0, Ink.precursors(0)[0], Ink.precursors(0)[1])
        >>> Ink. insert(2, Ink.precursors(2) [0] , Ink.precursors(2) [1] )
        >>> Ink.insert(1, Ink.precursors(1)[0], Ink.precursors(1)[1] )
        >>> print(Ink.front)
        0 -> 1 -> 2 -> 3 ->|
        >>> print (Ink.back)
        3 ->|
        >>> Ink.size
        4
        >>> print (Ink.front.next_.skip)
        3 ->|
        """
        if self.size == 0:
            self.front = self.back = LinkedListNode(value)
        else:
            if prev is None and cur is None:
                old_front = self.front
                self.front = LinkedListNode(value, old_front)
            elif cur is None:
                prev.next_ = LinkedListNode(value, prev.next_)
                prev.skip = prev.next_.next_
            else:
                cur.next_ = LinkedListNode(value, cur.next_)
        self.size += 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config="pylint.txt")
