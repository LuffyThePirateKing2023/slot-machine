import random 

MAX_LINES = 3
MAX_BET = 150
MIN_BET = 1

ROWS = 3
COLS = 3

SYMBOL_COUNT = {
    "A": 2,
    "B": 4,
    "C": 8,
    "D": 6
}

SYMBOL_VALUE = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(cols, lines, bet, value):

    winnings = 0
    winning_line = []

    for line in range(lines):
        symbols = cols[0][line]
        for col in cols:
            symbol_to_check = col[line]
            if symbols != symbol_to_check:
                break
        else: 
            winnings += value(symbols) * bet
            winning_line.append(line + 1)   

    return winnings, winning_line

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _  in range(cols):
        column = []
        current_symbols = all_symbols[:]

        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i != len(columns) - 1:
                print(col[row], end=" | ")
            else:
                print(col[row], end=" ")

        print()


def deposit():
    while True:
        amount = input("what would you like to? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else :
                print("Amount should not be equal to 0")
        else :
            print("Please Enter an Amount")
    return amount

def  get_number_of_lines():
    while True:
        lines = input("Enter the line you wanna bet on ( 1 - " + str(MAX_LINES) + ")? ")       
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else :
                print("Enter a valid number of line")
        else :
            print("Please Enter a Number")
    return lines

def get_bet():
    while True:
        amount = input("what would you like bet ? $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else :
                print(f"Amount should be between ${MIN_BET} - ${MAX_BET}.")
        else :
            print("Please Enter an Amount")
    return amount

def game(balance):
    lines = get_number_of_lines()
    while True:
        if balance <= 0 :
            print(f"Your remaining balance is ${balance}. Please Deposit")  
            balance += deposit()
            print(f"Your new balance is : ${balance}")

        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough balance, your current balance is ${balance}. Please Deposit")
            balance += deposit()
            print(f"Your new balance is : ${balance}")
        else:
            break

    print(f"You are betting ${bet} on ${lines} lines. The total bets are equal to ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, SYMBOL_COUNT)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, SYMBOL_VALUE)
    print(f"You Won ${winnings}.")
    print(f"You won on line : ", * winning_lines)

    if winnings > 0:
        balance += winnings - total_bet
    else:
        balance -= total_bet

    return balance


def main():
    balance = deposit()
    while True:
        print(f"Current balance is : ${balance}")
        answer = input("Press Enter to play or q to Quit")
        if answer == "q":
            break
        balance += game(balance)
    print(f"Your balance left is : ${balance}")

main()