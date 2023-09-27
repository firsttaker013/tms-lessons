import random

n = random.randint(0, 101)
print(n)
while True:
    answer = input('should we break ? ')
    if answer == 'yes':
        print('gratz')
        break
    elif answer != 'yes':
        a = random.randint(0, 101)
        print(a)




