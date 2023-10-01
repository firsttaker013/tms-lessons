def get_longest_word(text):
    words = text.split()
    longest_word = max(words, key=len)
    return longest_word

result = get_longest_word("test this program ffffffffffff")
print(result)