from typing import List

def generate_squares(values: List[int]) -> List[int]:
    squares = []
    for value in values:
        squares.append(value ** 2)
    return squares


result = generate_squares(1, 3, 4)
print(result)