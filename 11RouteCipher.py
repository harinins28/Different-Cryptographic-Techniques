import math

def fill_grid(text, rows, cols):
    text = text.replace(" ", "").upper()
    padded_text = text.ljust(rows * cols, 'X')
    grid = []
    index = 0
    for r in range(rows):
        grid.append([padded_text[index + c] for c in range(cols)])
        index += cols
    return grid

def spiral_clockwise_inward(grid):
    result = []
    top, bottom = 0, len(grid) - 1
    left, right = 0, len(grid[0]) - 1

    while top <= bottom and left <= right:
        for i in range(top, bottom + 1):
            result.append(grid[i][right])
        right -= 1

        for i in range(right, left - 1, -1):
            result.append(grid[bottom][i])
        bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(grid[i][left])
            left += 1

        if top <= bottom:
            for i in range(left, right + 1):
                result.append(grid[top][i])
            top += 1

    return ''.join(result)

def spiral_anticlockwise_inward(grid):
    result = []
    top, bottom = 0, len(grid) - 1
    left, right = 0, len(grid[0]) - 1

    while top <= bottom and left <= right:
        for i in range(top, bottom + 1):
            result.append(grid[i][left])
        left += 1

        for i in range(left, right + 1):
            result.append(grid[bottom][i])
        bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(grid[i][right])
            right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(grid[top][i])
            top += 1

    return ''.join(result)

print("Custom Route Cipher")
message = input("Enter plaintext: ")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
route_key = input("Enter route key (clockwise-inward / anticlockwise-inward): ").strip().lower()

grid = fill_grid(message, rows, cols)

if route_key == "clockwise-inward":
    cipher = spiral_clockwise_inward(grid)
elif route_key == "anticlockwise-inward":
    cipher = spiral_anticlockwise_inward(grid)
else:
    print("Unsupported route key.")
    cipher = ""

if cipher:
    print("Encoded Message:", cipher)
