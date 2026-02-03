from datetime import datetime
import csv, json, sys
from operator import itemgetter


def save_game_data(player_name, user_guesses, secret_num, user_number, result):      # שמירת נתוני המשחק
    is_save = False
    while not is_save:
        save = input("\t\tYou want save game? (y/n):  ")
        if save in ["y", "n"]:
            is_save = True
        else:
            print("\t\tplease enter only y/n")
        if save == "y":
            dt = datetime.now()
            ts = dt.timestamp()
            row_to_add = [player_name, ts, user_guesses, secret_num, user_number, result]
            
            rows = []
            with open("game_files/save_games.csv", 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                header = next(reader)
                for row in reader:
                    if row and row[0] != player_name:
                        rows.append(row)
            
            rows.append(row_to_add)
            
            with open("game_files/save_games.csv", 'w', newline="", encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(rows)

    print("\t\tThe game was saved successfully.  See you later :)")


def save_players_wins(player_name, user_guesses):      # שמירת השחקן עם השיא שלו
    with open("game_files/leaderboard.json", "r+") as lb:
        new_data = json.load(lb)
        
        new_data[player_name] = user_guesses

        tuple_data = new_data.items()
        temp_data = sorted(tuple_data, key=itemgetter(1))
        new_data = dict(temp_data)

        lb.seek(0)
        lb.truncate()
        json.dump(new_data, lb, indent=4)

    rows = []
    with open("game_files/save_games.csv", 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            if row and row[0] != player_name:
                rows.append(row)
    
    with open("game_files/save_games.csv", 'w', newline="", encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)