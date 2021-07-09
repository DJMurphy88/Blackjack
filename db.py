import sys
FILENAME = "money.txt"

def exit_program():
    print("Terminating program.")
    sys.exit()

def save_money(money):
    try:
        with open(FILENAME, "w", newline="") as file:
            file.write(str(money))
    except OSError as e:
        print(type(e), e)
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()

def load_money():
    try:
        money = []
        with open(FILENAME) as file:
            money = file.read()
        return money
    except FileNotFoundError as e:
        print("Could not find " + FILENAME + " file.")
        exit_program()
        return money
    except Exception as e:
        print(type(e), e)
        exit_program()