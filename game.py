import random
import time

# List of participants
players = ["Sonu" , "vijay" , "Parvesh"]

def spin_bottle(players):
    print("Spinning the bottle...")
    time.sleep(2)
    
    selected_player = random.choice(players)
    print(f"The bottle points to {selected_player}!")
    
    return selected_player

def ask_truth_or_dare(player):
    choice = input(f"{player}, Truth or Dare? ").strip().lower()
    
    if choice == 'truth':
        print(f"{player} chose Truth! Answer honestly!")
        # Add truth questions here
    elif choice == 'dare':
        print(f"{player} chose Dare! Be brave!")
        # Add dare tasks here
    else:
        print("Invalid choice, please choose 'Truth' or 'Dare'.")
        ask_truth_or_dare(player)

def play_game(players):
    while True:
        player = spin_bottle(players)
        ask_truth_or_dare(player)
        
        another_round = input("Do you want to play another round? (yes/no): ").strip().lower()
        if another_round != 'yes':
            break

if __name__ == "__main__":
    play_game(players)
