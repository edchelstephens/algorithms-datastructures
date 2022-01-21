# Challenge 1

- Implement BinarySearchTree constructor, given a list of items, the first item being the root, construct a binary search tree out of it

# Challenge 2

- Implement remove method of binary search tree and keeping the tree in tact

Scenarios:

- leaf node
  - just unlink from parent
- node with 1 child
  - moved the child node to the node position to be deleted, "promote" the child node in replacement of it's to be deleted parent node
- node with 2 left and right children
  - take the left-most child of the deleted node's right child and promote it in place of the to be deleted node
