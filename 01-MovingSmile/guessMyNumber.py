import random
print("Guess My Number")



secret_number = random.randint(1, 100)
# print(secret_number)
counter = 0

while True:
    guess = int(input("Guess a number: "))
    counter += 1
    if guess > secret_number:
        print("Too high!")
    if guess < secret_number:
        print("Too low!")
    if guess == secret_number:
        print("Correct!!")
        break
print(f"You got it in {counter} tries!")