import random

# Unit 1

countOfMoney = int(input('Введите количество монеток: '))
money = []

emblems = 0
tails = 0

for i in range(0, countOfMoney):
    currentMeaning = random.randint(0, 1)
    if currentMeaning == 0:
        tails += 1
    else:
        emblems += 1

if emblems > tails:
    print(f'нужно первернуть {tails} монет.')
else:
    print(f'Нужно перевернуть {emblems} монет.')

# Unit 2

firstDigit = int(input('Петя загадывает первое число: '))
secondDigit = int(input('Петя загадывает второе число: '))

sumOfDigits = firstDigit + secondDigit
productOfDigits = firstDigit * secondDigit

for i in range(1001):
    for j in range(1001):
        if i + j == sumOfDigits and i * j == productOfDigits:
            print(f'Катя говорит, что загаданные числа: {i} и {j}')