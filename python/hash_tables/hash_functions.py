from string import ascii_letters

def stable_hash(alphabet_string:str) -> int:
    """A stable hash function."""

    lowercase_input = alphabet_string.lower()
    table = { letter: i+1 for i, letter in enumerate(ascii_letters)}

    value = 0

    for character in lowercase_input:
        value += table[character]

    return value