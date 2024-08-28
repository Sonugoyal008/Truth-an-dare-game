import random
import time

# List of participants
players = ["Sonu" , "vijay" , "Parvesh"]


# List of truth questions
truth_questions = [
    "What is your biggest fear?",
    "Have you ever lied to your best friend?",
    "What is your most embarrassing moment?",
    "Who do you have a crush on?",
    "What is the last lie you told?"
]

# List of dare tasks
dare_tasks = [
    "Do 20 push-ups.",
    "Sing a song loudly.",
    "Dance like no one is watching for a minute.",
    "Call a random person and sing 'Happy Birthday'.",
    "Speak in an accent for the next 3 rounds."
]

def spin_bottle(players):
    print("Spinning the bottle...")
    time.sleep(2)
    
    selected_player = random.choice(players)
    print(f"The bottle points to {selected_player}!")
    
    return selected_player

def ask_truth_or_dare(player):
    choice = input(f"{player}, Truth or Dare? ").strip().lower()
    
    if choice == 'truth':
        question = random.choice(truth_questions)
        print(f"{player}, here is your truth question: {question}")
    elif choice == 'dare':
        dare = random.choice(dare_tasks)
        print(f"{player}, here is your dare: {dare}")
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
