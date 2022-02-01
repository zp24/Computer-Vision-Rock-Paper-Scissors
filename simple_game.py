

num_list = [5, 7, 8, 9, 22, 55, 99, 100000]


import random

print(random.choice(num_list)) #will print a random number from list

#num = input("Pick a number ")

#if __name__ =='__main__': #implies module is being run standalone by the user

gesture = ["rock", "paper", "scissors"]

#r = gesture["rock"]

#p = gesture["paper"]

#s = gesture["scissors"]

#pw = p > r

#pl = s > r

win = 0
loss = 0
computer_choice = random.choice(gesture)

player_choice = input("Choose rock, paper, or scissors: ")
print("Computer chose: ", computer_choice, "Player chose: ", player_choice)
while True:
    if computer_choice == player_choice:
        print("It's a draw")
        #print("try again?")
        #new_game = input("yes or no")
                
    elif computer_choice == "rock" and player_choice == "paper" or computer_choice == "scissors" and player_choice == "rock" or computer_choice == "paper" and player_choice == "scissors":
        win = win + 1
        print("Player wins!", "Wins:", win)
    else:
        loss = loss + 1
        print("Computer wins!", " Losses: ", loss)
    break


