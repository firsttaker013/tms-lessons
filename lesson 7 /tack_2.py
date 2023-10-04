def remove_vowels(letters):
    return list(filter(lambda letter: letter not in "aeiou", letters))

user_input = input("Введите маленькие латинские буквы: ")
result = remove_vowels(user_input.split())
print("Результат: ", result)



