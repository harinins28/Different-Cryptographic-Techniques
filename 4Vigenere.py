def vigenere_cipher(text, key):
    result = ""
    key = key.lower()
    key_index = 0

    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            key_char = key[key_index % len(key)]
            shift = ord(key_char) - ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
            key_index += 1
        else:
            result += char
    return result

print("Vigenère Cipher")
message = input("Enter plaintext: ")
key = input("Enter the keyword: ")

encoded = vigenere_cipher(message, key)
print("Encoded Message:", encoded)
