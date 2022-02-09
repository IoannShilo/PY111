"""
My little Queue
"""
from typing import Any

# append() -> O(1)
# pop(-1) -> O(1)
# insert() -> O(N)
# del 0(N)

class Queue:
    def __init__(self):
        self.queue = []  # начало очереди слева, конец справа

    def enqueue(self, elem: Any) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        self.queue.append(elem)

    def dequeue(self) -> Any:  # O(N)
        """
        Return element from the beginning of the queue. Should return None if no elements.

        :return: dequeued element
        """
        if not self.queue:
            return None

        else:
            print(self.queue[0])
            self.queue.pop(0)
            return self.queue

    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        if not 0 <= ind <= len(self.queue) - 1:
            raise IndexError()

        else:
            return self.queue[ind]

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        return self.queue.clear()


if __name__ == '__main__':
    qu = Queue()
    qu.enqueue(1)
    qu.enqueue(2)
    qu.enqueue(3)

    qu.dequeue()
    print(qu.queue)
    qu.dequeue()
    print(qu.queue)