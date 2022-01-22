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

# Fill factor

- the percentage of capacity representing the maximum number of entries before the table will grow, e.g. 0.8 or 80% full before growing the size

# Growth Factor

- the multiple to increase the capacity of the hash table when the fill factor has been exceeded, e.g. 1.50, increase by half

# Finding a value in the hash table using key

- Find the index
- Use the hash function
- Module the hash of the size of the hash table to get the index
- Search entry list of entries to find one element that matches the key
