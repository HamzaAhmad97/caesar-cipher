def decrypt(msg, key):
    """
    A funciton that accepts a encrypted message and a key and returns the message decrypted by shifting its letters based on the key.

    Args:
        text (str): A general string, the encrypted message.
        key (int): The key or the amount of shift.

    Returns:
        str: The decrypted message.
    """
    letters = [chr(n) for n in range(97, 123)]
    letters_shifted = [*letters]
    decrypted_msg = ""
    for _ in range(key):
        letters_shifted.insert(0,letters_shifted.pop())
    for l in msg:
        decrypted_msg += l if not l.isalpha() else letters_shifted[letters.index(l)] if l in letters else letters_shifted[letters.index(l.lower())].upper()
    return decrypted_msg


if __name__ == "__main__":
    print(decrypt("Papc Ijgxcv", 15))