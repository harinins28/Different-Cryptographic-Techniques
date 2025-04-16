def rail_fence_cipher(text, rails):
    fence = ['' for _ in range(rails)]
    rail = 0
    direction = 1  # 1: moving down, -1: moving up

    for char in text:
        fence[rail] += char
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1  # change direction

    return ''.join(fence)

print("Rail Fence Cipher")
message = input("Enter plaintext: ")
rails = int(input("Enter number of rails: "))

encoded = rail_fence_cipher(message, rails)
print("Encoded Message:", encoded)
