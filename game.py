import random

SECRET = random.randint(1, 100)

attempts = 0
while True:
    guess = int(input("Ваша догадка: "))
    attempts += 1
    if guess < SECRET:
        print("Больше")
    elif guess > SECRET:
        print("Меньше")
    else:
        print("Угадал!")
        print("Попыток:", attempts)
        break