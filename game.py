import random

print("🎮 Welcome to Number Guessing Game")
print("Guess a number between 1 and 10")

# Computer random number generate karega
secret_number = random.randint(1, 10)

attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print("🎉 Correct!")
        print("You guessed in", attempts, "attempt(s)")
        break

    elif guess > secret_number:
        print("📈 Too High! Try again")

    else:
        print("📉 Too Low! Try again")