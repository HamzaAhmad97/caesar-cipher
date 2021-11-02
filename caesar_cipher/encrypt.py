def encrypt(text, key):
    """
    A funciton that accepts a message and a key and returns the message encrypted by shifting its letters based on the key.

    Args:
        text (str): A general string, the message.
        key (int): The key or the amount of shift.

    Returns:
        str: The encrypted message.
    """
    letters = [chr(n) for n in range(97, 123)]
    letters_shifted = [*letters]
    encrypted_msg = ""
    for _ in range(key):
        letters_shifted.append(letters_shifted.pop(0))
    for l in text:

        encrypted_msg += l if not l.isalpha() else letters_shifted[letters.index(l)] if l in letters else letters_shifted[letters.index(l.lower())].upper()
    return encrypted_msg


if __name__ == "__main__":
    print(encrypt("Alan Turing", 15))