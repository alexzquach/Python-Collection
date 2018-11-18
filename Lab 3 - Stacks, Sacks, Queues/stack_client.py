"""
stack client module
"""
from stack import Stack
from typing import List


def list_stack(lst: List[object], u_stack: Stack) -> None:
    """ Adds each element of the list to the stack """
    for item in lst:
        u_stack.add(item)
    while not u_stack.is_empty():
        item = u_stack.remove()
        if type(item) == list:
            for thing in item:
                u_stack.add(thing)
        else:
            print(item)


if __name__ == '__main__':
    new_stack = Stack()
    user_s = input("Please type a string: ")
    new_stack.add(user_s)
    while user_s != 'end':
        user_s = input("Please type a string: ")
        new_stack.add(user_s)
    while not new_stack.is_empty():
        print(new_stack.remove())
