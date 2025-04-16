def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char  
    return result

print("Caesar Cipher")
message = input("Enter plaintext: ")
shift = int(input("Enter the shift key: "))

encoded = caesar_cipher(message, shift)
print("Encoded Message:", encoded)
