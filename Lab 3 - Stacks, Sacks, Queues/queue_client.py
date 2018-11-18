"""
queue client module
"""
from csc148_queue import Queue
from typing import List


def list_queue(lst: List[object], u_queue: Queue) -> None:
    """ Adds each element of the list to the stack """
    for item in lst:
        u_queue.add(item)
    while not u_queue.is_empty():
        item = u_queue.remove()
        if type(item) == list:
            for thing in item:
                u_queue.add(thing)
        else:
            print(item)


if __name__ == '__main__':
    new_queue = Queue()
    new_sum = 0
    number = int(input("Enter an integer: "))
    while number != 148:
        new_queue.add(number)
        number = int(input("Enter an integer: "))
    while not new_queue.is_empty():
        print(new_queue.remove())
        # new_sum += new_queue.remove()
    # print(new_sum)
