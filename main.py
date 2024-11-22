import string
import random

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
    return ciphered_text

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

def keyword_cipher(text, keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Create a substitution alphabet using the keyword
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

def vigenere_cipher(text, keyword, encrypt=True):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keyword = keyword.upper()
    text = text.upper()
    
    ciphered_text = ""
    keyword_index = 0

    for char in text:
        if char in alphabet:
            shift = alphabet.index(keyword[keyword_index])
            if not encrypt:
                shift = -shift  # Decrypt by reversing the shift
            
            new_index = (alphabet.index(char) + shift) % len(alphabet)
            ciphered_text += alphabet[new_index]

            keyword_index = (keyword_index + 1) % len(keyword)
        else:
            ciphered_text += char  # Non-alphabet characters remain unchanged
    
    return ciphered_text

# Input from the user
while True:
    text = input("Enter a word to cipher: ")
    choice = input(
        "Choose cipher type:\n1. Atbash\n2. Caesar\n3. Substitution\n4. Transposition\n5. Keyword\n6. Vigenère\n"
    ).strip().lower()

    if choice == "1":
        ciphered_word = atbash_cipher(text)
        print("Ciphered word using Atbash:", ciphered_word)
    elif choice == "2":
        shift = int(input("Enter key value for Caesar cipher: "))
        ciphered_word = caesar_cipher(text, shift)
        print("Ciphered word using Caesar:", ciphered_word)
    elif choice == "3":
        ciphered_word = substitution_cipher(text)
        print("Ciphered word using Substitution:", ciphered_word)
    elif choice == "4":
        ciphered_word = transposition_cipher(text)
        print("Ciphered word using Transposition:", ciphered_word)
    elif choice == "5":
        keyword = input("Enter a keyword for the cipher: ")
        ciphered_word = keyword_cipher(text, keyword)
        print("Ciphered word using Keyword Cipher:", ciphered_word)
        
    elif choice == "6":
        keyword = input("Enter a keyword for the Vigenère Cipher: ")
        operation = input("Encrypt or Decrypt? (E/D): ").strip().lower()
        if operation == "e":
            ciphered_word = vigenere_cipher(text, keyword, encrypt=True)
            print("Ciphered word using Vigenère Cipher (Encrypt):", ciphered_word)
        elif operation == "d":
            ciphered_word = vigenere_cipher(text, keyword, encrypt=False)
            print("Ciphered word using Vigenère Cipher (Decrypt):", ciphered_word)
        else:
            print("Invalid operation.")
    else:
        print("Invalid choice. Please select a valid option.")
