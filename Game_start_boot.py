from random import randint
import csv


def start_game():
    secret_num = randint(0, 500)
    user_guesses = 0
    print(secret_num)       # !!! למחוק בהרצה סופית !!!

    with open("./guessing_record.txt", "r", encoding='utf-8') as f:
        content = f.read().strip()
        if content.isdigit():
            guessing_record = int(content)
        else:
            guessing_record = None

    print(f"\t\t\t\t< Welcome to the number guessing game >\n\n\t\t(At any time you can type 'exit' to close the game)")

    player_name = input("\t\tEnter your user name:  ")

    return secret_num, user_guesses, guessing_record, player_name


def boot_game(secret_num, user_guesses, guessing_record, player_name):
    with open("./save_games.csv", "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        data_list = list(reader)
    if len(data_list) > 1:
        while True:
            print("\t\t\t\t\t1. New game\n\t\t\t\t\t2. Continue game")
            import_game = input("\t\t\t\t\tSelect an option (1 / 2):  ")
            if import_game == "1":
                print("\n\t\t\t\t\tNew game.. Good luck :)")
                break
            elif import_game == "2":
                secret_num = int(data_list[1][2])
                importing = [int(data_list[1][1]), int(data_list[1][3]), data_list[1][4]]
                print(f"\n\t\t\t\t\tYour latest data is from: {data_list[1][0]}\n\t\t\t\t[amount of guesses: {importing[0]} | last guess: {importing[1]} | final result: {importing[2]}]")
                break
            else:
                print("\t\tPlease select only numbers 1 / 2!")
        print(f"\n\t\tThe smallest number of guesses so far: {guessing_record}\n")
    else:
        print("\n\t\t\t\t\tNew game.. Good luck :)")

    return secret_num, user_guesses, guessing_record, player_name