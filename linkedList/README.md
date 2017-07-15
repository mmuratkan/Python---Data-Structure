USAGE EXAMPLE:
---
```python
from linkedList import LinkedList

str1 = ['elem0', 'elem1']
str2 = ['elem2', 'elem3']
x = LinkedList(str1)
y = LinkedList()
print('y:', y.isEmpty())

for i in range(len(str2)):
    y.addFirst(str2[i])

x.addAll(str2)
print('x:', x.add('elem4'))
print('x:', x.getLast())
print('x:', x.size())
x.add('elem100', 4)
print('x:', x.getLast())
print('x:', x.lastIndexOf('elem100'))
print()

for i in range(x.size()):
    print('x', i, x.get(i))

print()
y.clear()
print(y.size())

print('x elem100:', x.indexOf('elem100'))
print('x:', x.contains('elem3'))
print('x:', x.getFirst())
x.remove(0)
x.remove()
print('x:', x.peekFirst(), x.peekLast())
print(x.pool(), x.pop())
x.push('elem150')
print('x:', x.set(0, 'elem151'), x.peek())

```
OUTPUT:
---
```python
y: True
x: True
x: elem4
x: 5
x: elem100
x: 4

x 0 elem0
x 1 elem1
x 2 elem2
x 3 elem3
x 4 elem100

0
x elem100: 4
x: True
x: elem0
x: elem1 elem3
elem1 elem2
x: elem150 elem151
```
***

Class constructors:
===
1. **LinkedList()**: This constructer constructs an empty list.
2. **LinkedList(list**): This constructs a list containing the elements of the specified list, in the order they are returned by the list iterator.

Class methods:
===
1. **add(elem)**: This method appends the specified element to the end of this list, if position is given inserts the specified element at the specified position in this list.
2. **addAll(arr**): This method inserts all of the elements in the specified collection into this list, starting at the specified position.
3. **addFirst(elem)**: This method inserts the specified element at the beginning of this list.
4. **addLast(elem)**: This method appends the specified element to the end of this list.
5. **clear()**: This method removes all of the elements from this list.
6. **indexOf(elem)**: This method returns the index of the first occurrence of the specified element in this list, or -1 if this list does not contain the element.
7. **contains(elem)**: This method returns true if this list contains the specified element.
8. **get(index)**: This method returns the element at the specified position in this list.
9. **getFirst()**: This method returns the first element in this list.
10. **getLast()**: This method returns the last element in this list.
11. **lastIndexOf(elem)**: This method returns the index of the last occurrence of the specified element in this list, or -1 if this list does not contain the element.
12. **peek()**: This method retrieves, but does not remove, the head (first element) of this list.
13. **peekFirst()**: This method retrieves, but does not remove, the first element of this list, or returns null if this list is empty.
14. **peekLast()**: This method retrieves, but does not remove, the last element of this list, or returns null if this list is empty.
15. **pool()**: This method retrieves and removes the head (first element) of this list.
16. **remove(index)**: This method retrieves and removes the last element of this list, or returns None if this list is empty, if position is given removes the element at the specified position in this list.
17. **pop()**: This method pops an element from the stack represented by this list.
18. **push(elem)**: This method pushes an element onto the stack represented by this list.
19. **set(index, elem)**: This method replaces the element at the specified position in this list with the specified element.
20. **size()**: This method returns the number of elements in this list.
21. **isEmpty()**: This method returns true if this list contains no elements.

***
