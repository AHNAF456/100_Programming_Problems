import random
lowest_num=1
answer = random.randint(lowest_num,highest_num)
guesses=0
is_running = True
highest_num=1000
while is_running:
    guess=input("Enter your guess: ")
    guesses += 1
    if guess.isalpha():
        print("INVALID GUESS")
        print(f"Please enter a number between {lowest_num} and {highest_num}")
    elif int(guess)<lowest_num or int(guess)>highest_num:
        print("Your guess is out of range")
        print(f"Please enter a number between {lowest_num} and {highest_num}")
    elif int(guess) < int(answer):
        print("Too low")
    elif int(guess) > int(answer):
        print("Too high")
    else:
        print("Correct")
        is_running = False
print(f"The correct answer is {answer}")
print(f"You took {guesses} guesses")