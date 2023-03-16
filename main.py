import time
from code_logo import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
]

print(logo)

reset = True

while reset:
    decrypt_encrypt = input("\nEnter 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()
    text = input("Enter your message: ").lower()
    shift = int(input("Enter the shift number: "))

    # modify if number shift exceeds 45
    shift = shift % 26


    def caesar(code=decrypt_encrypt, text_to_decode=text, shift_to_decode=shift):
        # Function to decrypt or encrypt message
        message = ""
        if code == "decrypt":
            shift_to_decode = (0 - shift_to_decode)

        for item in text_to_decode:
            if item in alphabet:
                position = alphabet.index(item)
                new_position = position + shift_to_decode
                message += alphabet[new_position]
            else:
                message += item
        print(message)

    # Calling keyword arguments
    caesar(code=decrypt_encrypt, text_to_decode=text, shift_to_decode=shift)

    # Ask if still want to continue
    again = input("\nWanna continue? Type 'Y', 'N' to Exit. ").lower()
    if again == "n":
        reset = False

time.sleep(10)

# # THIS IS THE OLD CODE##
# function for encrypting
# def encrypt(text_to_decode=text, shift_to_decode=shift):
#     encrypt_word = ""
#     for item in text_to_decode:
#         position = alphabet.index(item) + shift_to_decode
#         encrypt_word += alphabet[position]
#     print(encrypt_word)
#
# function for decrypting
# def decrypt(text_to_decode=text, shift_to_decode=shift):
#     decrypt_word = ""
#     for item in text_to_decode:
#         position = alphabet.index(item) - shift_to_decode
#         decrypt_word += alphabet[position]
#     print(decrypt_word)

# calling the functions
# if decrypt_encrypt == "encrypt":
#     encrypt(text_to_decode=text, shift_to_decode=shift)
# else:
#     decrypt(text_to_decode=text, shift_to_decode=shift)


