def beaufort_cipher(text, key):
    result = ""
    key = key.lower()
    key_index = 0

    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            key_char = key[key_index % len(key)]
            k = ord(key_char) - ord('a')
            c = ord(char) - base
            shifted = (26 + k - c) % 26
            result += chr(shifted + base)
            key_index += 1
        else:
            result += char
    return result

print("Beaufort Cipher")
message = input("Enter plaintext: ")
key = input("Enter the keyword: ")

encoded = beaufort_cipher(message, key)
print("Encoded Message:", encoded)
