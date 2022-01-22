def stable_hash(input_string: str) -> int:
    """A stable hash function."""

    value = 0

    for character in input_string:
        value += ord(character)

    return value
