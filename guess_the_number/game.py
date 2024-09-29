from random import randrange


def difficulty_selector(message: str) -> str:
    if not message:
        print("Select a difficulty!")
        print("HARD")
        print("MEDIUM")
        print("EASY")
    else:
        print(message)
    difficulty: str = input("Selected difficulty: ")
    # Make the result upper
    difficulty = difficulty.upper()
    return difficulty


def random_number(difficulty: str) -> int:
    min_number: int = 0
    max_number: int = 0
    match difficulty:
        case "HARD":
            max_number = 100
        case "MEDIUM":
            max_number = 66
        case "EASY":
            max_number = 33
    print(f"I thought of a number between {min_number} and {max_number} try to guess it")  # nopep8
    return randrange(min_number, max_number)


def game_loop():
    difficulty: str = ""
    message: str = ""
    # Choose the difficulty
    while True:
        difficulty = difficulty_selector(message)
        if not difficulty == "HARD" and not difficulty == "MEDIUM" and not difficulty == "EASY":
            message = "Wrong selected difficulty"
            continue
        break
    # Play the game
    tries: int = 0
    random_num: int = random_number(difficulty)
    while True:
        try:
            guess = int(input("Guess: "))
        except:
            # Input is not a number
            print("Guess a valid number")
            continue
        # guess is a valid number
        tries += 1
        # guess is less then random_num
        if guess < random_num:
            print("Think higher")
            continue
        # guess is higher then random_num
        elif guess > random_num:
            print("Think lower")
            continue
        # good guess
        elif guess == random_num:
            print(f"You found my number in {tries} tries great job!")
            break


game_loop()
