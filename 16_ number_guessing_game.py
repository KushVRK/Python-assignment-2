# Number Guessing Game
import random

best_score = None  # tracks best score across games

while True:
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    guessed = False

    print("\n--- Number Guessing Game ---")
    print("You have to guess the number which I had picked it between 1 and 100. ")
    print("You have 7 attempts to guess that number..")

    while attempts < max_attempts:
        try:
            guess = int(input("\nEnter your guessed number: "))
            attempts += 1
            remaining = max_attempts - attempts

            if guess == secret:
                print(":)  congratulation (:  it is correct")
                print(f"You guessed it in {attempts} attempts!")
                guessed = True

                # update best score if this is better
                if best_score is None or attempts < best_score:
                    best_score = attempts
                    print("New best score!🤩")
                break

            # to do your bonus work - hint if within 5
            elif abs(guess - secret) <= 5:
                if guess < secret:
                    print(f"It is soo close! a little higher. Attempts remaining: {remaining}")
                else:
                    print(f"it is soo close! a little lower. Attempts remaining: {remaining}")

            elif guess < secret:
                print(f"It is too low! Attempts remaining: {remaining}")

            else:
                print(f"It is too high! Attempts remaining: {remaining}")

        except ValueError:
            print("Please enter a valid input number.....")
            # dont count invalid input as attempt
            attempts -= 1

    if not guessed:
        print(f"\nSorry you failed to guess the number...... The number was {secret}")

    # To show best score - it also include in bonus
    if best_score is not None:
        print(f"Your's best score so far is : {best_score} attempts")

    play_again = input("\nDo you like to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing...")
        break