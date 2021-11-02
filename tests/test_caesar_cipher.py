import pytest
from caesar_cipher import __version__
from caesar_cipher.encrypt import encrypt
from caesar_cipher.decrypt import decrypt
from caesar_cipher.crack import crack

def test_version():
    assert __version__ == '0.1.0'

def test_encrypt_shift_1():
    """
    Test the encrypt function with key equals 1.
    """
    actual = encrypt("apple", 1)
    expected = "bqqmf"
    assert actual == expected


def test_encrypt_shift_10():
    """
    Test the encrypt function with key equals 10.
    """
    actual = encrypt("apple", 10)
    expected = "kzzvo"
    assert actual == expected


def test_encrypt_shift_20():
    """
    Test the encrypt function with key equals 20.
    """
    actual = encrypt("apple", 20)
    expected = "ujjfy"
    assert actual == expected


def test_uppercase():
    """
    Test the encrypt function with key equals 10 and if it consideres the upper and lower cases in the message.
    """
    actual = encrypt("BANANA", 10)
    expected = "LKXKXK"
    assert actual == expected


def test_with_whitespace():
    """
    Test the encrypt function with key equals 1, and if it consideres whitespaces in the message.
    """
    actual = encrypt("apples and bananas", 1)
    expected = "bqqmft boe cbobobt"
    assert actual == expected


def test_with_non_alpha():
    """
    Test the encrypt function with key equals 1, and if it considres characters that are not letters.
    """
    actual = encrypt("Gimme a 1!", 1)
    expected = "Hjnnf b 1!"
    assert actual == expected


def test_round_trip():
    """
    Test the decrypt function with key equals 5.
    """
    original = "Gimme a 1!"
    shift = 5
    encrypted = encrypt(original, shift)
    actual = decrypt(encrypted, shift)
    expected = original
    assert actual == expected


def test_crack_phrase():
    """
    Test if the crack function returns the correct result.
    """
    phrase = "It was the best of times, it was the worst of times."
    encrypted = encrypt(phrase, 10)
    actual = crack(encrypted)
    expected = phrase
    assert actual == expected


def test_crack_nonsense():
    """
    Test if the crack function returns the correct result.
    """
    phrase = "Ix fhw txe fofg of ndhrl, it nad tho hndrk of allkd."
    encrypted = encrypt(phrase, 10)
    actual = crack(encrypted)
    expected = ""
    assert actual == expected