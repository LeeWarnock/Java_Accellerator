#Import Modules
import random
import time

#create choices and directions
choose = ["y","n"]
directions = ["forward", "backward", "left", "right"]

#random.choice definition

#random.randint definition


#print line function with sleep
def print_line():
    print(narration)
    time.sleep(1)

#intro function
def introduction():

#define surface

#define Mirage

#define Martian Temple

#define reactor

#define asphyxiation

#define play again
def restart_game():
    restart = input("GAME OVER./nWould you like to play again? (y/n)")
    if restart == "y":
        print_line("You close your eyes as a slight dizziness washes over you. A sensation of falling jolts you awake and you open your eyes to find yourself sitting at the controls of your shuttle. Was it all a dream?")
        start_game()
    elif restart == "n":
        print_line("You close your eyes as you accept your fate. With each breath the air in your suit becomes more acrid. As your consciousness slips away a wave of euphoric understanding washes over you, and your essence becomes one with the universe.")

#start the game function
def start_game():
start_game()