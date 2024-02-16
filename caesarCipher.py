def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)

def main():
    while True:
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value (a number between 1 and 25): "))
        if shift < 1 or shift > 25:
            print("Shift value must be between 1 and 25")
            continue
        encrypted_message = encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
        decrypted_message = decrypt(encrypted_message, shift)
        print("Decrypted message:", decrypted_message)
        
        repeat = input("Do you want to continue? (yes/no): ")
        if repeat.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
