vowels = 'AEIOUY'

def remove_vowels(word):
    if word.isupper():
        vowels_removed = filter(lambda x: x not in vowels, word)
        return "".join(vowels_removed).upper()
    else:
        return filter(lambda x: x.lower() not in vowels, word)

user_input = input('введите буквы: ').title().split()
result = list(map(remove_vowels, user_input))
print('Результат: ', result)
