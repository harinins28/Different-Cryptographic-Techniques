def gronsfeld_cipher(text, key):
    result = ""
    key = [int(k) for k in key]
    key_index = 0

    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shift = key[key_index % len(key)]
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
            key_index += 1
        else:
            result += char
    return result

print("Gronsfeld Cipher")
message = input("Enter plaintext: ")
key = input("Enter numeric key (e.g., 31415): ")

encoded = gronsfeld_cipher(message, key)
print("Encoded Message:", encoded)
