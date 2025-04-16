def atbash_cipher(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr(219 - ord(char))  # 219 = ord('a') + ord('z')
            else:
                result += chr(155 - ord(char))  # 155 = ord('A') + ord('Z')
        else:
            result += char  # Non-alphabetical characters are left unchanged
    return result

print("Atbash Cipher")
message = input("Enter the plaintext: ")
output = atbash_cipher(message)

print("Result:", output)
