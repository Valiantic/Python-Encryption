import string
import random

def atbash_cipher(text):
    # Define the alphabet and the reversed alphabet for the Atbash cipher
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    reversed_alphabet = alphabet[::-1]
    
    # Create a dictionary for Atbash cipher mapping
    atbash_dict = {alphabet[i]: reversed_alphabet[i] for i in range(len(alphabet))}
    
    # Apply the Atbash cipher
    ciphered_text = ""
    for char in text.upper():
        if char in atbash_dict:
            ciphered_text += atbash_dict[char]
        else:
            ciphered_text += char  # Keep non-alphabet characters unchanged
    
    return ciphered_text

def caesar_cipher(text, shift):
    # Define the alphabet for Caesar cipher
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Apply the Caesar cipher
    ciphered_text = ""
    for char in text.upper():
        if char in alphabet:
            # Find the new position by shifting
            new_index = (alphabet.index(char) + shift) % len(alphabet)
            ciphered_text += alphabet[new_index]
        else:
            ciphered_text += char  # Keep non-alphabet characters unchanged
    
    return ciphered_text

def substitution_cipher(text):
    # Define the alphabet
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Generate a random substitution for each letter
    shuffled_alphabet = list(alphabet)
    random.shuffle(shuffled_alphabet)
    substitution_dict = {alphabet[i]: shuffled_alphabet[i] for i in range(len(alphabet))}
    
    # Apply the substitution cipher
    ciphered_text = ""
    for char in text.upper():
        if char in substitution_dict:
            ciphered_text += substitution_dict[char]
        else:
            ciphered_text += char  # Keep non-alphabet characters unchanged
    
    return ciphered_text

def transposition_cipher(text):
    # Rail Fence Cipher: Arrange the characters in a zigzag pattern over a number of rails
    num_rails = 3  # You can change the number of rails
    rails = [''] * num_rails
    rail_index = 0
    direction = 1  # 1 for down, -1 for up

    # Place characters in rails
    for char in text:
        rails[rail_index] += char
        rail_index += direction
        if rail_index == 0 or rail_index == num_rails - 1:
            direction *= -1  # Change direction at the top and bottom rails
    
    # Combine the rails to get the ciphered text
    return ''.join(rails)

# Input from the user
while True:
    text = input("Enter a word to cipher: ")
    choice = input(
        "Choose cipher type:\n1. Atbash\n2. Caesar\n3. Substitution\n4. Transposition\n"
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
    else:
        print("Invalid choice. Please select a valid option.")
