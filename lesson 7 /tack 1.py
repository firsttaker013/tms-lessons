def map_to_tuples(letters):
    return list(map(lambda letter: (letter.upper(), letter.lower()), letters))

user_input = input('Введите буквы через пробел').upper().split()
result = map_to_tuples(user_input)
print(result)

