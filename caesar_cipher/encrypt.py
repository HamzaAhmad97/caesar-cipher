def encrypt(text, key):
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