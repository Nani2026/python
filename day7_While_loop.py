'''i=1
while(i<=10):
 print("This is while loop")
 i=i+1
 '''
 
import random

game_count = 0

while True:
    game_count += 1
    random_num = random.randint(10, 20)
    count = 0

    while True:
        try:
            num = int(input("Enter a number (10-20): "))
        except ValueError:
            print("Please enter numbers only!")
            continue

        count += 1

        if num == random_num:
            print("Number matched in", count, "tries")
            play_again = input("Play again? (y/n): ")
            break
        else:
            print("Try again")

    if play_again != "y":
        break

print("You played", game_count, "games")
