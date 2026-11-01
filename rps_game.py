#Rock defeats Scissors.
#Scissors defeats Paper.
#Paper defeats Rock.
#If both players choose the same option, the round ends in a draw.
import random

print("Welcome to Rock, Paper, Scissors!")


while True:
    print("R.Rock")
    print("P.Paper")
    print("S.Scissors")
    print("Q.Quit")

    choice = input("Enter your choice (r, p, s, or q to quit): ").lower()

    if choice == 'q':
        print("Thanks for playing! Goodbye!")
        break
    elif choice not in ['r', 'p', 's']:
        print("Invalid choice. Please enter r, p, or s.")
    else:
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"Computer chose: {computer_choice}")

        if choice == computer_choice:
            print("It's a draw!")
        elif (choice == 'r' and computer_choice == 'scissors') or \
             (choice == 's' and computer_choice == 'paper') or \
             (choice == 'p' and computer_choice == 'rock'):
            print("You win!")
        else:
            print("Computer wins!")
