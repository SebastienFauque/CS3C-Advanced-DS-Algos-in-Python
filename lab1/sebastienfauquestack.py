"""Stack class that that allows users to add items to the top of a stack and
to remove them."""
from sebastienfauquenode import Node

class Stack:
    """Implements a Linear abstract data type known as a Stack."""
    def __init__(self, data = None):
        self.head = None

        if data:
            self.push(data)

    def push(self, data) -> None:
        """Adds a new item to the top of the stack, puts all other items
        below it."""
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def pop(self):
        """Removes and returns the top item from the stack."""
        if self.is_empty():
            return None
        popped_data = self.head.get_data()
        self.head = self.head.get_next()
        return popped_data

    def peek(self):
        """Gets the data from the top item of the stack without removing it."""
        if self.is_empty():
            return None
        return self.head.get_data()

    def is_empty(self) -> bool:
        """Checks if the stack is empty."""
        return self.head is None

    @classmethod
    def create_stack(cls):
        """Builds a stack."""
        return cls()

    def delete_stack(self) -> None:
        """Deletes the current stack."""
        self.head = None
