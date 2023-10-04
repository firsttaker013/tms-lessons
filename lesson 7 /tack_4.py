from functools import reduce

def my_join(words, sep):
    return reduce(lambda x, y: x + sep + y, words)

words = input('слова, разделитель\n').split()
sep = input()

print(my_join(words, sep))
