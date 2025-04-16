def affine_cipher(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            x = ord(char) - base
            encrypted = (a * x + b) % 26
            result += chr(encrypted + base)
        else:
            result += char
    return result

print("Affine Cipher")
message = input("Enter plaintext: ")
a = int(input("Enter key 'a' (within 26): "))
b = int(input("Enter key 'b': "))

encoded = affine_cipher(message, a, b)
print("Encoded Message:", encoded)
