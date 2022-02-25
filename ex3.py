import random

AI_num = random.randrange(0, 20)
print(AI_num)

player_guess = int(input("Guess what the number could be: "))

while player_guess != AI_num:
    if player_guess < AI_num:
        print("your number is smaller than the number")
        player_guess = int(input("Guess what the number could be: "))
    elif player_guess > AI_num:
        print("your number is bigger than the number")
        player_guess = int(input("Guess what the number could be: "))
    if player_guess == AI_num:
        print("You got it right!!")
        want_play = input("Want to play again (y/n)")

        if want_play == "y":
            AI_num = random.randrange(0, 20)