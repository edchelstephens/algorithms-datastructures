# Associative Array (C#)

- a collection of key/value pairs where the key can only exists once in the collection

- associative array is like dictionaries in python

# Hash Table

- An associative array container that provides O(1) insert, delete and search operations

# Hash function

- a function that maps data of arbitrary size to data of a fixed size

hash function examples:

- verifying downloaded data
- storing password in a database
- hash tables key lookup

# For a function to be a suitable hash function, it has to have 3 properties

hash = f(value)

It has to be:

1. Stable

   - for a given input it will return the same result everytime

2. Uniform

   - the hash function will distribute hash values it generates uniformly across its output space.

3. Secure
   - If you have a hash result, it shouldn't be easy to determine values that would produce that result
   - A secure hashing algorithm cannot be inverted(the input derived from the output hash)

# Hash Output size

128 bits

- MD5 (message-digest algorithm)

256 bits:

- SHA 256

# Hash collision

- When multiple distinct keys would be inserted at the same hash table index

# Separate Chaining

- Collisions in a hash table are chained together into a linked list whose root node is the hash table array entry.
