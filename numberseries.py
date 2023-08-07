import random

def generate_random_number(start, end):
    return random.randint(start, end)

def provide_clue(actual_number, guessed_number):
    if guessed_number < actual_number:
        return "Try a larger number."
    elif guessed_number > actual_number:
        return "Try a smaller number."
    else:
        return "Congratulations! You guessed the correct number."

def main():
    start_range = 1
    end_range = 100
    actual_number = generate_random_number(start_range, end_range)
    
    score = 100
    attempts = 0
    
    while True:
        print("Current score:", score)
        guessed_number = int(input(f"Guess a number between {start_range} and {end_range}: "))
        attempts += 1
        
        if guessed_number < start_range or guessed_number > end_range:
            print("Please enter a valid number within the range.")
            continue
        
        clue = provide_clue(actual_number, guessed_number)
        print(clue)
        
        if guessed_number != actual_number:
            score -= 10
        
        if guessed_number == actual_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts with a final score of {score}.")
            break

if __name__ == "__main__":
    main()
