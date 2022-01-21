# Tree

- A datastructure where nodes have a 1:N parent-child relationship

- begins at the root
- branches expand out
- leaves are outer boundary

## Properties

- 0 or 1 parent node
  every node in a tree, except for the root has exactly one parent

- 0-N child nodes(binary, trinary, k-ary)
  every part of the tree spawns zero or more children.
  A branch may have hundreds of leaves or none at all

- degree of the tree is the number of children the node has

- leaf nodes have no children

- one data item per node

- edges connect nodes

- internal nodes are the nodes neither the root nor the leaf nodes, nodes which have children that is not the root node

- degree of a tree is max children of a node in the tree

- Height counts edges

- Height of a node is the maximum number of edges between the node and a leaf
- In general, when we refer to the height of the node, we are referring to the maximum height through all of it's children

- Level counts the edges to root
- it is 1 + the number of edges between that node and the root

# Binary Tree

- A tree with nodes with at most two children
- A binary tree is recursively defined
  every node in the tree can itself be thought of as the root node of a smaller, distinct tree

# Binary Search Tree

- A binary tree where nodes with lesser values are placed to the left of the root, and nodes with equal or greater values are placed to the right

- The smallest value is in the left most node(left most leaf) and the greatest value is in the right most node(the right most leaf)

> > Complexities

- Insertion:
  average - O(log n)
  worst case - O(n)

- A binary search tree can be a balanced tree where insertion is O(log n)
  or imbalanced, only on the left side or right side, therefore insertion is O(n)

> > Traversal Operations

- Visit the left child
- Visit the right child
- Process the current value

## Pre-order Traversal

- The node is visited before it's children
- Process the current value
- Visit the left child
- Visit the right child

- Pre order is useful on copying an entire tree structure

## In-order Traversal

- The left child is visited before the node, then the right child

## Post-order Traversal

- The left and right children are visited before the node
