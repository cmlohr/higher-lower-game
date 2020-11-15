import random, math
from replit import clear
from art import logo, coder_tag, vs
from game_data import data

######Splash Screen
print(logo)
print("-------------------------------------------------------")
print(coder_tag)
if input("               Press ENTER to begin") == "":
     clear()

#######Game Def
def game():
    score = 0
    cont = True
    while cont:

#######random data setup
        choices = (random.choices(data, k=2))
        choice_a = choices[0]
        choice_b = choices[1]

# ######level setup and format
        print("|-------------------------------------------------------|")
        print(f" A:  {choice_a.get('name')}\n {choice_a.get('description')}, from {choice_a.get('country')}")
        print(vs)
        print(f" B:  {choice_b.get('name')}\n {choice_b.get('description')}, from {choice_b.get('country')}")
        print("|-------------------------------------------------------|")

# #######Choice and follower amount comparison
        a = choice_a.get('follower_count')
        b = choice_b.get('follower_count')
        set_choice = input("  Who has more followers? Type 'A' or 'B':\n  > ").lower()
        if set_choice == "a":
            choice = a
            other_choice = b
        elif set_choice == "b":
            choice = b
            other_choice = a

# #######FOLLOWER COMPARISON
        if choice > other_choice:
            score += 1
            print(f"  Correct! (^◡^ )\n  Current score: {score}")
        else:
            print(f"  Incorrect! ( ◡́.◡̀)\n  Final score: {score}")
            cont = False

######replay or quit
    if input("  Play Again: 'y'  Quit: 'n':\n  > ").lower() == "y":
        clear()
        game()
    else:
        clear()
        cont = False
game()

