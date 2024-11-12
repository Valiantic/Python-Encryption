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

# Input from the user
text = input("Enter a word to cipher using Atbash: ")
ciphered_word = atbash_cipher(text)
print("Atbash Ciphered word:", ciphered_word)
