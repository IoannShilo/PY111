"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any


class PriorityQueue:
    def __init__(self):
        """
        одна очередь

        начало справа
        конец слева

        enqueue - O(N)
        dequeue - O(1)
        """
        self.queue_priority = []

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        enqueue_item = {
            "elem": elem,
            "priority": priority
        }
        if not self.queue_priority:
            self.queue_priority.append(enqueue_item)
            return None

        for index, current_item in enumerate(self.queue_priority):
            if enqueue_item["priority"] >= current_item["priority"]:
                self.queue_priority.insert(index, enqueue_item)
                break

        else:
            self.queue_priority.append(enqueue_item)

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """
        if not self.queue_priority:
            return None

        return self.queue_priority.pop()["elem"] # O(1)

    def peek(self, elem: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        return None

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.queue_priority.clear()
