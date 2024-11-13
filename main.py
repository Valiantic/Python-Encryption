# ATBASH

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

# CAESAR

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

# Input from the user
text = input("Enter a word to cipher: ")
choice = input("Choose cipher type (Atbash/Caesar): ").strip().lower()

if choice == "atbash":
    ciphered_word = atbash_cipher(text)
    print("Ciphered word using Atbash:", ciphered_word)
elif choice == "caesar":
    shift = int(input("Enter shift amount for Caesar cipher: "))
    ciphered_word = caesar_cipher(text, shift)
    print("Ciphered word using Caesar:", ciphered_word)
else:
    print("Invalid choice. Please select either 'Atbash' or 'Caesar'.")
