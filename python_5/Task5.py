import random
secret = random.randint(1,20)
print('Я загадал число от 1 до 20. У тебя 5 попыток!')
attempts = 5
while attempts > 0:
    print("Введите число: ")
    number = input("")
    if int(secret) == int(number):
        print('Ты угадал! ')
        break
    elif int(secret) > int(number):
        print("Слишком мало")
    else:
        print("Слишком много")
    attempts -= 1
    print("Осталось попыток:", attempts)

