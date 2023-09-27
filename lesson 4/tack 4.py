import random

n = random.randint(0, 25)
while True:
    x = int(input('random: '))
    if x == n:
        print('gratz')
        break
    elif x < n:
        print('bolwe')
    elif x > n:
        print('menwe')




