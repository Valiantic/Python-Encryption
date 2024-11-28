import random

# ATBASH CIPHER
def atbash_cipher(text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    reversed_alphabet = alphabet[::-1]
    atbash_dict = {alphabet[i]: reversed_alphabet[i] for i in range(len(alphabet))}
    ciphered_text = ""
    for char in text.upper():
        if char in atbash_dict:
            ciphered_text += atbash_dict[char]
        else:
            ciphered_text += char
    return ciphered_text  # Symmetric: applying again reverses the process

# CAESAR CIPHER (ENCODE)
def caesar_cipher(text, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphered_text = ""
    for char in text.upper():
        if char in alphabet:
            new_index = (alphabet.index(char) + shift) % len(alphabet)
            ciphered_text += alphabet[new_index]
        else:
            ciphered_text += char
    return ciphered_text

# CAESAR CIPHER (DECODE)
def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)  # Negative shift reverses the cipher

# ROT13 CIPHER
def rot13_cipher(text):
    return caesar_cipher(text, 13)  # ROT13 is Caesar with a shift of 13

# ROT14 CIPHER
def rot14_cipher(text):
    return caesar_cipher(text, 14)  # ROT14 is Caesar with a shift of 14

# TRANSPOSITION CIPHER
def transposition_cipher(text):
    num_rails = 3
    rails = [''] * num_rails
    rail_index = 0
    direction = 1
    for char in text:
        rails[rail_index] += char
        rail_index += direction
        if rail_index == 0 or rail_index == num_rails - 1:
            direction *= -1
    return ''.join(rails)

# KEYWORD CIPHER
def keyword_cipher(text, keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keyword = ''.join(sorted(set(keyword.upper()), key=keyword.index))  # Remove duplicates
    substitution_alphabet = keyword + ''.join([ch for ch in alphabet if ch not in keyword])
    substitution_dict = {alphabet[i]: substitution_alphabet[i] for i in range(len(alphabet))}
    ciphered_text = ""
    for char in text.upper():
        if char in substitution_dict:
            ciphered_text += substitution_dict[char]
        else:
            ciphered_text += char
    return ciphered_text

# SUBSTITUTION CIPHER
def substitution_cipher(text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shuffled_alphabet = list(alphabet)
    random.shuffle(shuffled_alphabet)
    substitution_dict = {alphabet[i]: shuffled_alphabet[i] for i in range(len(alphabet))}
    ciphered_text = ""
    for char in text.upper():
        if char in substitution_dict:
            ciphered_text += substitution_dict[char]
        else:
            ciphered_text += char
    return ciphered_text

# Input from the user
while True:
    text = input("Enter a word to cipher: ")
    choice = input(
        "Choose cipher type:\n1. Atbash\n2. Caesar (encode)\n3. Caesar (decode)\n4. ROT13\n5. ROT14\n6. Transposition\n7. Keyword\n8. Substitution\n"
    ).strip().lower()

    if choice == "1":
        ciphered_word = atbash_cipher(text)
        print("Ciphered word using Atbash (encode/decode):", ciphered_word)
    elif choice == "2":
        shift = int(input("Enter key value for Caesar cipher: "))
        ciphered_word = caesar_cipher(text, shift)
        print("Ciphered word using Caesar (encode):", ciphered_word)
    elif choice == "3":
        shift = int(input("Enter key value for Caesar cipher: "))
        deciphered_word = caesar_decipher(text, shift)
        print("Deciphered word using Caesar (decode):", deciphered_word)
    elif choice == "4":
        ciphered_word = rot13_cipher(text)
        print("Ciphered word using ROT13 (encode/decode):", ciphered_word)
    elif choice == "5":
        ciphered_word = rot14_cipher(text)
        print("Ciphered word using ROT14 (encode/decode):", ciphered_word)
    elif choice == "6":
        ciphered_word = transposition_cipher(text)
        print("Ciphered word using Transposition:", ciphered_word)
    elif choice == "7":
        keyword = input("Enter a keyword for the cipher: ")
        ciphered_word = keyword_cipher(text, keyword)
        print("Ciphered word using Keyword Cipher:", ciphered_word)
    elif choice == "8":
        ciphered_word = substitution_cipher(text)
        print("Ciphered word using Substitution:", ciphered_word)
    else:
        print("Invalid choice. Please select a valid option.")
