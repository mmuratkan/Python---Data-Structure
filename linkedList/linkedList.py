class _LinkedListBase:

    class _Node:
        __slots__ = '_elem', '_prev', '_next'

        def __init__(self, elem, prev, next):
            self._elem = elem
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None,None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def _isPositionIndex(self, index):
        return index >= 0 and index < self._size;

    def _checkPositionIndex(self, index):
        if not self._isPositionIndex(index):
            raise IndexOutOfBoundsException('Index: ' + str(index) + ', List Size: ' + str(self._size))

    def _insert(self, elem, pred, succ):
        node = self._Node(elem, pred, succ)
        pred._next = node
        succ._prev = node
        self._size += 1
        return node

    def _delete(self, node):
        pred = node._prev
        succ = node._next
        pred._next = succ
        succ._prev = pred
        self._size -= 1
        element = node._elem
        node._prev = node._next = node._elem = None
        return element

    def _node(self, index):
        self._checkPositionIndex(index)
        if index < (self._size >> 1):
            x = self._header._next
            for i in range(index):
                x = x._next
            return x
        else:
            x = self._trailer._prev
            for i in range(self._size - 1, index, -1):
                x = x._prev
            return x

    def isEmpty(self):
        """This method returns true if this list contains no elements."""
        return self._size == 0


class LinkedList(_LinkedListBase):

    def __init__(self, _list=None):
        super(LinkedList, self).__init__()
        if _list is None:
            pass
        else:
            if type(_list) is list:
                self.addAll(_list)
            else:
                raise Exception('Cannot infer type arguments for')

    def add(self, elem, index = None):
        """This method appends the specified element to the end of this list,
        if position is given inserts the specified element at the specified position in this list."""
        if index is None:
            self._insert(elem, self._trailer._prev, self._trailer)
        else:
            x = self._node(index)
            x._elem = elem
        return True

    def addAll(self, arr):
        if len(arr) == 0:
            return False
        for x in arr:
            self.addLast(x)
        return True

    def addFirst(self, elem):
        """This method inserts the specified element at the beginning of this list.."""
        self._insert(elem, self._header, self._header._next)

    def addLast(self, elem):
        """This method appends the specified element to the end of this list."""
        self._insert(elem, self._trailer._prev, self._trailer)

    def clear(self):
        """This method removes all of the elements from this list."""
        x = self._header
        while self._size > 0:
            _next = x._next
            x._elem = None
            x._prev = None
            x._next = None
            x = _next
            self._size -= 1
        self._header = None
        self._trailer = None

    def indexOf(self, elem):
        """This method returns the index of the first occurrence of the specified element in this list,
        or -1 if this list does not contain the element."""
        index = 0
        if elem is not None:
            x = self._header
            while index < self._size:
                _next = x._next
                if _next._elem == elem:
                    return index
                x = _next
                index += 1
        return -1

    def contains(self, elem):
        """This method returns true if this list contains the specified element."""
        return self.indexOf(elem) != -1

    def get(self, index):
        """This method returns the element at the specified position in this list."""
        if self.isEmpty():
            raise NoSuchElementException('List is empty')
        return self._node(index)._elem

    def getFirst(self):
        """This method returns the first element in this list."""
        return self._header._next._elem

    def getLast(self):
        """This method returns the last element in this list."""
        return self._trailer._prev._elem

    def lastIndexOf(self, elem):
        """This method returns the index of the last occurrence of the specified element in this list,
        or -1 if this list does not contain the element."""
        index = self._size
        if elem is not None:
            x = self._trailer
            while index > 0:
                index -= 1
                _prev = x._prev
                if _prev._elem == elem:
                    return index
                x = _prev
        return -1

    def peek(self):
        """This method retrieves, but does not remove, the head (first element) of this list."""
        return None if self._header._next is None else self._header._next._elem

    def peekFirst(self):
        """This method retrieves, but does not remove, the first element of this list,
        or returns null if this list is empty."""
        return None if self._header._next is None else self._header._next._elem

    def peekLast(self):
        """This method retrieves, but does not remove, the last element of this list,
        or returns null if this list is empty."""
        return None if self._trailer._prev is None else self._trailer._prev._elem

    def pool(self):
        """This method retrieves and removes the head (first element) of this list."""
        return None if self.isEmpty() else self._delete(self._header._next)

    def remove(self, index = None):
        """This method retrieves and removes the last element of this list, or returns None if this list is empty."""
        if self.isEmpty():
            return None
        if index is None:
            return self._delete(self._trailer._prev)
        else:
            return self._delete(self._node(index))

    def pop(self):
        """This method pops an element from the stack represented by this list."""
        if self.isEmpty():
            raise NoSuchElementException('List is empty')
        return self._delete(self._header._next)

    def push(self, elem):
        """This method pushes an element onto the stack represented by this list."""
        self.addFirst(elem)

    def set(self, index, elem):
        """This method replaces the element at the specified position in this list with the specified element."""

        x = self._node(index)
        oldElem = x._elem
        x._elem = elem
        return oldElem

    def size(self):
        """This method returns the number of elements in this list."""
        return self.__len__()


class IndexOutOfBoundsException(Exception):
    pass


class NoSuchElementException(Exception):
    pass
