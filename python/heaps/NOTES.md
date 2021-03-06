# Heap

- A tree-based container type that provides O(1) access to the minimum(min-heap) or maximum(max-heap) value while satisfying the heap property

## Heap Property

- The value in the current tree node is greater than, or equal to, it's children(max-heap)
  The maximum value is the root node that's why we can always access it in O(1) time

- The value in the current tree node is lesser than, or equal to, it's children(min-heap)
  The minimum value is the root node that's why we can always access it in O(1) time

# Heap Operations

Push - adding value
Top - retrieving min or max value from the top, root node
Pop - removing min or max value from the top, root node

# Complete Tree

- A tree where every level is filled out from left-to-right before starting the next level

# Priority Queue
A queue that pops item in priority, not First-in First-out (FIFO) order