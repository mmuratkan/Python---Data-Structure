USAGE EXAMPLE:
---
```python
from stack import Stack

x = Stack()
print(x.search('c'))
x.push('a')
x.push('b')
x.push('c')
x.push('c')
print()
print(x.search('c'))
print(x.peek())
print(x.pop())
print(x.isEmpty())

```
OUTPUT:
---
```python
-1

1
c
c
False

```
***

Class constructors:
===
1. **Stack()**: This constructor creates an empty stack.

Class methods:
===
1. **pop()**: This method removes the object at the top of this stack and returns that object as the value of this function.
2. **peek()**: This method looks at the object at the top of this stack without removing it from the stack.
3. **isEmpty()**: This method tests if this stack is empty.
4. **search(elem)**: This method returns the 1-based position where an object is on this stack.

***