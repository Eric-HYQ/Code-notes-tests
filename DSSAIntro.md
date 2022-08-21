# Data structure 
What is data structure? It's a format of organizing data in a way of modifying them more convenient

### Array
Array, can put elements in it in order. String is a special type of array.

Operations:
- access by index, goes to the position according to index rather than walk over the whole road, so it's O(1)
- very bad at inserting / removing elements
  > insert one, need to shift all elements behind, requires more operations 

### Linked list
Conbined by nodes, each node contains a value and a pointer to the next node
> the last node has a null pointer

- good at inserting / removing elements, O(1)
- bad at accessing by index, have to walk over the whole road from given to target element

### Hash table
A collection of key-value pairs, each pair contains a key and a value
> the key is unique

- fast in accessing by key, removing and inserting, each O(1)

hash function turns non-int key into int type as index of array, called hash code

map hash code to value

key design 
- design a uniform distribution hash function
- use chaining or probe method to deal with key collision
- how to rehash


### stack and queue
stack LIFO, last in, first out

queue FIFO, first in , first out

### Graph & tree
good at network, dependency relationship, hierarchies

BFS

DFS

### Heaps
- get min / max, O(1)
- insert, O(logn)
- remove max / min, O(logn)
