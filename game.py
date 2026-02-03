from Game_start_boot import start_game, boot_game
from check_win import check_win
from save_data import save_game_data, save_players_wins


# תחילת משחק
def play_game():
    secret_num, user_guesses, guessing_record, player_name = start_game()
    secret_num, user_guesses, guessing_record, player_name = boot_game(secret_num, user_guesses, guessing_record, player_name)
    won = False
    while not won:
        user_number = input("\n\t\tGuess your number (0-500):  ")
        if user_number == "exit":
            save_game_data(user_guesses, secret_num, temp_user_number, result)
            break
        try:
            user_number = int(user_number)
            temp_user_number = user_number
            if 0 > user_number or user_number > 500:
                print("\t\tJust guess a number between 0-500.")
                continue
        except ValueError:
                print("\t\tPlease enter a valid number.")
                continue

        user_guesses += 1
        won, result = check_win(player_name, user_number, secret_num, guessing_record, user_guesses)

        if won:
            save_players_wins(player_name, user_guesses)
            break
        save_game_data(user_guesses, secret_num,user_number, result)