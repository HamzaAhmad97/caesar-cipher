import nltk
import re
from caesar_cipher.decrypt import decrypt
#from decrypt import decrypt

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

from nltk.corpus import words, names

word_list = words.words()
name_list = [name.lower() for name in names.words()]

all_words = word_list + name_list

text = "Ix fhw txe fofg of ndhrl, it nad tho hndrk of allkd."

def crack(text):
    """
    A function that accepts a string or a message that is encrypted, and tried to decrypt the message without knowing the key.

    Args:
        text (str): The encrypted message.

    Returns:
        str: The decrypted message or and empty string if the message does not seem to be in real English.
    """
    results = []
    top = (0,"")
    for k in range(1,27):
        results.append(decrypt(text, k))
    for k,result in enumerate(results, start= 1):
        known = 0
        num_of_words = len(result.split(' '))
        for word in re.findall(r'[a-zA-Z]+', result):
            known += 1 if word.lower() in all_words else 0
        percentage = known / num_of_words * 100
        top= (percentage,result) if percentage >= top[0] and percentage >= 50 else top
    return top[1] 

if __name__ == "__main__":
    print(crack(text))