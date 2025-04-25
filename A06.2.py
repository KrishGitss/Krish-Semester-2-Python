import random

class RockPaperScissors:
    choices = ["rock", "paper", "scissors"]

    def __init__(self, rounds):
        self.rounds, self.current, self.user_wins, self.computer_wins = rounds, 0, 0, 0

    def play_round(self, user_choice):
        computer_choice = random.choice(self.choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            return "It's a tie!"
        
        if (user_choice, computer_choice) in [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")]:
            self.user_wins += 1
            return "You win this round!"
        
        self.computer_wins += 1
        return "Computer wins this round!"

    def play_game(self):
        print(f"Starting Rock-Paper-Scissors! Best of {self.rounds} rounds.")

        while self.current < self.rounds:
            user_choice = input("Enter rock, paper, or scissors: ").lower()
            if user_choice not in self.choices:
                print("Invalid choice! Try again.")
                continue
            
            self.current += 1
            print(self.play_round(user_choice))

            if self.user_wins > self.rounds // 2 or self.computer_wins > self.rounds // 2:
                break

        print(f"Final Score - You: {self.user_wins}, Computer: {self.computer_wins}")
        print("You won!" if self.user_wins > self.computer_wins else "Computer won!" if self.computer_wins > self.user_wins else "It's a tie!")

if __name__ == "__main__":
    RockPaperScissors(int(input("Enter the number of rounds: "))).play_game()