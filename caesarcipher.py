def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

choice = input("Type E for Encrypt or D for Decrypt: ").upper()

if choice == 'E':
    print("Encrypted Text:", encrypt(message, shift))
elif choice == 'D':
    print("Decrypted Text:", decrypt(message, shift))
else:
    print("Invalid choice")
    