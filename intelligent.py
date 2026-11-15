# Intelligent Number Guessing Agent

low = 1
high = 100

print("Think of a number between 1 and 100.")
print("Give feedback: H = Higher, L = Lower, C = Correct")

while low <= high:

    guess = (low + high) // 2

    print("\nMy Guess is:", guess)

    feedback = input("Enter feedback (H/L/C): ").upper()

    if feedback == 'H':
        low = guess + 1

    elif feedback == 'L':
        high = guess - 1

    elif feedback == 'C':
        print("Correct! Number guessed successfully.")
        break

    else:
        print("Invalid feedback! Try again.")

else:
    print("Invalid feedback or inconsistent answers!")