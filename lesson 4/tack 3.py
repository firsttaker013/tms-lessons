import random

n = random.randint(0, 101)
print(n)
while True:
    answer = input('should we break ? ')
    if answer == 'yes':
        print('gratz')
        break
    elif answer == 'no':
        a = random.randint(0, 101)
        print(a)
    elif answer != 'no' and 'yes':
        print('ne ponimau!!!!!')








