class Stack:

    def __init__(self):
        self._data = []

    def __len__(self):
        """This method returns number of elements in the stack"""
        return len(self._data)

    def push(self, elem):
        """This method pushes an item onto the top of this stack."""
        self._data.append(elem)

    def pop(self):
        """This method removes the object at the top of this stack and returns that object as the value
        of this function."""
        if self.isEmpty():
            raise Empty('Stack is empty')
        return self._data.pop()

    def peek(self):
        """This method looks at the object at the top of this stack without removing it from the stack."""
        if self.isEmpty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def isEmpty(self):
        """This method tests if this stack is empty."""
        return len(self._data) == 0

    def search(self, elem):
        """This method returns the 1-based position where an object is on this stack."""
        for x in range(len(self._data)-1, -1, -1):
            if self._data[x] == elem:
                return len(self._data) - x
        return -1


class Empty(Exception):
    pass

