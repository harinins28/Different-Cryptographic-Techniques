import numpy as np

def hill_cipher(text, key_matrix):
    text = text.lower().replace(" ", "")
    if len(text) % 2 != 0:
        text += 'x'  # Padding with 'x' if needed

    result = ""
    for i in range(0, len(text), 2):
        pair = [ord(text[i]) - ord('a'), ord(text[i+1]) - ord('a')]
        encrypted = np.dot(key_matrix, pair) % 26
        result += ''.join(chr(num + ord('a')) for num in encrypted)

    return result

print("Hill Cipher (2x2 Matrix)")
message = input("Enter plaintext (only alphabets): ")
print("Enter 2x2 key matrix values row-wise:")
a = int(input("a11: "))
b = int(input("a12: "))
c = int(input("a21: "))
d = int(input("a22: "))
key_matrix = np.array([[a, b], [c, d]])

encoded = hill_cipher(message, key_matrix)
print("Encoded Message:", encoded)
