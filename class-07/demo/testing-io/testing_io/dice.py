from random import randint


def default_roller():
    return (randint(1, 6,), randint(1, 6,))


def play_dice(roller=default_roller):

    while True:
        print("Enter r to roll or q to quit")
        choice = input("> ")

        if choice == "q":
            print("OK, bye")
            break
        else:
            roll = roller()
            roll_str = ""
            for num in roll:
                roll_str += str(num) + " "
            print(f"*** {roll_str}***")


if __name__ == "__main__":
    play_dice()

