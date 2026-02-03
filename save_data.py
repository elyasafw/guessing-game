from datetime import datetime
import csv, json
from operator import itemgetter


def save_game_data(user_guesses, secret_num, user_number, result):
    is_save = False
    while not is_save:
        save = input("\t\tYou want save game? (y / n):  ")
        if save == "y" or save == "n":
            is_save = True
        else:
            print("\t\tplease enter only y / n!")
        if save == "y":
            dt = datetime.now()
            ts = dt.timestamp()
            row_to_add = [ts, user_guesses, secret_num, user_number, result]
            with open("./save_games.csv", 'r+', encoding='utf-8') as file:
                header = next(csv.reader(file))
            with open("./save_games.csv", 'w', newline = "", encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerow(row_to_add)


def save_players_wins(player_name, user_guesses):   # שמירת השחקן עם השיא שלו
    with open("./leaderboard.json", "r+") as lb:
        new_data = json.load(lb)
        # הוספה או עדכון של השחקן
        new_data[player_name] = user_guesses
        # מיון של המילון:
        tuple_data = new_data.items()
        print(tuple_data)
        temp_data = sorted(tuple_data, key=itemgetter(1))
        new_data = dict(temp_data)
        # כתיבה חזרה לקובץ
        lb.seek(0)
        lb.truncate()
        json.dump(new_data, lb, indent=4)