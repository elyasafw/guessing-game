from random import randint
import csv


def start_game():
    secret_num = randint(0, 500)
    user_guesses = 0

    with open("game_files/guessing_record.txt", "r", encoding='utf-8') as file:
        content = file.read().strip()
        if content.isdigit():
            guessing_record = int(content)
        else:
            guessing_record = None

    print(f"\n\t< Welcome to the number guessing game >\n(At any time you can type 'exit' to close & save the game)\n")

    return secret_num, user_guesses, guessing_record


def boot_game(secret_num, user_guesses, guessing_record, player_name):
    user_data = None
    with open("game_files/save_games.csv", "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0] == player_name:
                user_data = row
                break

    if user_data:
        while True:
            print("\t\t1. New game\n\t\t2. Continue game")
            import_game = input("\t\tSelect an option (1 / 2):  ")
            if import_game == "1":
                print("\n\t\tNew game..  Good luck :)")
                break
            elif import_game == "2":
                secret_num = int(user_data[3])
                user_guesses = int(user_data[2])
                importing = [int(user_data[2]), int(user_data[4]), user_data[5]]
                print(f"\n\tYour latest data is from: {user_data[1]}\n[amount of guesses: {user_guesses} | last guess: {importing[1]} | final result: {importing[2]}]")
                break
            else:
                print("\t\tPlease select only numbers 1 / 2!")
    else:
        print("\n\t\tNew game..  Good luck :)")

    return secret_num, user_guesses, guessing_record, player_name