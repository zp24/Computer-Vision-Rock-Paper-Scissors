

num_list = [5, 7, 8, 9, 22, 55, 99, 100000]


from asyncore import loop
import random

print(random.choice(num_list)) #will print a random number from list

gesture = ["rock", "paper", "scissors"]


win = 0
loss = 0
draw = 0

computer_choice = random.choice(gesture)


player_continue = True

while player_continue:
    player_choice = input("Choose rock, paper, or scissors: ")
    
    if computer_choice == player_choice: 
        draw = draw + 1 #adds 1 to the overall number of draws
        print("Computer chose: ", computer_choice, "//", "Player chose: ", player_choice)
        print("It's a draw", "Wins: ", win, "Losses: ", loss, "Draws: ", draw) #shows stats
        continue
    elif computer_choice == "rock" and player_choice == "paper" or computer_choice == "scissors" and player_choice == "rock" or computer_choice == "paper" and player_choice == "scissors":
        win = win + 1 #adds 1 to the overall number of wins
        print("Computer chose: ", computer_choice, "//", "Player chose: ", player_choice)
        print("Player wins!", "Wins: ", win, "Losses: ", loss, "Draws: ", draw) #shows stats
        continue
    elif computer_choice == "paper" and player_choice == "rock" or computer_choice == "rock" and player_choice == "scissors" or computer_choice == "scissors" and player_choice == "paper":
        loss = loss + 1 #adds 1 to the overall number of losses
        print("Computer chose: ", computer_choice, "//", "Player chose: ", player_choice)
        print("Computer wins!", "Wins: ", win, " Losses: ", loss, "Draws: ", draw) #shows stats
        continue
    else:
        if player_choice == "x": #press x to quit game
            player_continue = False #breaks loop
            print("Game ended\n", "Your Stats: ", "Wins: ", win, "Losses: ", loss, "Draws: ", draw) #confirm loop has broken
        break
    
    

