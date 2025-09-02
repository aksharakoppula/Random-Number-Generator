import random
computer_guess=random.randint(1,100)
print(computer_guess)
user_guess=int(input("Guess\n"))
print(user_guess)
while user_guess != computer_guess:
    user_guess=int(input("Guess\n"))
    if user_guess != computer_guess:
        print("Wrong guess49\n")
    else:
        print("Right guess\n")