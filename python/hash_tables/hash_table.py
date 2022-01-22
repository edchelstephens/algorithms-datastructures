from typing import Any

class HashTableEntry:
    """A hash table entry for separate chaining collisions."""

    def __init__(self, key:str, value:Any, next:object) -> None:
        self.key = key
        self.value = value
        self.next = next

class HashTable:
    """A hash table data structure."""

    pass
