import random

def main():

    game_over = False
    player_score = 0
    computer_score = 0

    while not game_over:
        while True:
            player_choice = input("Rock, Paper, or Scissors? ")
            if player_choice in ["Rock", "Paper", "Scissors"]:
                break
            print("Invalid input. Please try again.")

        computer_choice = random.choice(["Rock", "Paper", "Scissors"])

        if player_choice == computer_choice:
            print("It's a tie!")
        elif player_choice == "Rock" and computer_choice == "Scissors":
            print("You win!")
            player_score += 1
        elif player_choice == "Paper" and computer_choice == "Rock":
            print("You win!")
            player_score += 1
        elif player_choice == "Scissors" and computer_choice == "Paper":
            print("You win!")
            player_score += 1
        else:
            print("You lose!")
            computer_score += 1

        print(f"Player: {player_score} | Computer: {computer_score}")
        if player_score == 3 or computer_score == 3:
            game_over = True
        # ask player if they want to play again
        play_again = input("Do you want to play again? (yes/no) ")

         # end the game if player says no
        if play_again.lower() != "yes":
            break

main()