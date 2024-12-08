### Explain dynamic arrays (like ArrayList) and show insertion at the end.

#### Definition

Dynamic arrays are arrays that can automatically resize and when elements are added or removed
In Python _lists_ are an implemented as dynamic arrays. They can grow and shrink in size automatically.

#### How do they work

In the beginning Python allocates them an initial chunk of memory to hold the elements.

* Resizing: As you add more elements to the list than it can hold, Python will resize the list. This resizing is
  typically
  done by allocating a larger block and copying over existing elements.
  Python usually doubles the capacity when resizing, which ensures that resizing happens less frequently, and the
  average time complexity of appending an element remains O(1).
* Amortized O(1) Time Complexity: Appending elements to Python list is typically O(1)
  , meaning it happens in constant time. However, occasionally the list runs out of space and needs to be resized, the
  time complexity for that specific append operation is O(n)

#### Limitations

While dynamic arrays (lists) in Python are very efficient for most tasks, they do have some limitations:

* Insertions and Deletions at the beginning or middle of the list can be inefficient (O(n)), because elements need to be
shifted to maintain the order.
* Memory usage: Python lists can consume more memory than the actual elements they store due to extra allocated space for
future growth.