"""Node class that can be used in abstract data types such as a linked list."""
from typing import Any


class Node:
    """Implementation of a Linked List node."""
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def set_data(self, data: Any) -> bool:
        """Assigns data to a node."""
        if data is not None:
            self.data = data
            return True
        return False

    def set_next(self, next_node) -> bool:
        """Set the next node."""
        if isinstance(next_node, Node):
            self.next = next_node
            return True
        return False

    def get_data(self):
        """Gets the current node's data.'"""
        return self.data

    def get_next(self):
        """Gets the next node of the LL."""
        return self.next

    def has_next(self):
        """Assert this node points to another node."""
        return self.next is not None




