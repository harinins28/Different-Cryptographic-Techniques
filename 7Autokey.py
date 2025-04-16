def autokey_cipher(text, key):
    result = ""
    key = key.lower()
    extended_key = key + text.lower()
    key_index = 0

    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shift = ord(extended_key[key_index]) - ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
            key_index += 1
        else:
            result += char
    return result

print("Autokey Cipher")
message = input("Enter plaintext: ")
key = input("Enter the initial keyword: ")

encoded = autokey_cipher(message, key)
print("Encoded Message:", encoded)
