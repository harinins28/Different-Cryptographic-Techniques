def get_key_order(key):
    key = key.upper()
    key_order = {}
    current = 1
    for char in sorted(set(key)):
        indexes = [i for i, c in enumerate(key) if c == char]
        for i in indexes:
            key_order[i] = current
        current += 1
    return [key_order[i] for i in range(len(key))]

def myszkowski_encrypt(plaintext, key):
    key = key.upper().replace(" ", "")
    plaintext = plaintext.replace(" ", "").upper()
    
    col_count = len(key)
    row_count = -(-len(plaintext) // col_count)  # ceiling division

    # Fill grid row-wise
    grid = [['' for _ in range(col_count)] for _ in range(row_count)]
    idx = 0
    for r in range(row_count):
        for c in range(col_count):
            if idx < len(plaintext):
                grid[r][c] = plaintext[idx]
                idx += 1
            else:
                grid[r][c] = 'X'  # padding

    # Get key order mapping
    order = get_key_order(key)

    # Collect columns based on repeating order
    result = ''
    unique_levels = sorted(set(order))
    for num in unique_levels:
        indices = [i for i, v in enumerate(order) if v == num]
        for col in indices:
            for row in grid:
                result += row[col]
    return result

print("Myszkowski Cipher")
message = input("Enter plaintext: ")
key = input("Enter keyword (with possible repeated letters): ")

cipher = myszkowski_encrypt(message, key)
print("Encoded Message:", cipher)
