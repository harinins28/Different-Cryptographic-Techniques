def running_key_cipher(text, key):
    result = ""
    key = key.lower()
    key_index = 0

    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shift = ord(key[key_index]) - ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
            key_index += 1
        else:
            result += char
    return result

print("Running Key Cipher")
message = input("Enter plaintext: ")
key = input("Enter running key (must be at least as long as message): ")

if len(key) < len([c for c in message if c.isalpha()]):
    print("Error: Key must be at least as long as the message (excluding spaces/punctuation).")
else:
    encoded = running_key_cipher(message, key)
    print("Encoded Message:", encoded)
