# בדיקת ניצחונות והכוונת השחקן
def check_win(player_name, user_number, secret_num, guessing_record, user_guesses):
        if user_number == secret_num:   # יש ניצחון
            result = "Equal!"
            print(f"\t\t{result} {player_name} You won in {user_guesses} guesses.")

# בדיקת שבירת שיא ניצחונות
            if guessing_record == None:
                print(f"\t\tWell done {player_name}! You broke the previous record for guesses ({guessing_record}).")
                with open("./guessing_record.txt", "w") as f:
                    f.write(str(user_guesses))
            elif user_guesses < int(guessing_record):
                print(f"\t\tWell done {player_name}! You broke the previous record for guesses ({guessing_record}).")
                with open("./guessing_record.txt", "w") as f:
                    f.write(str(user_guesses))
            else:
                print(f"\t\tThe record of guesses is: {guessing_record}, You failed to break the record.. Good luck next time :)")
            return True, result

# אין ניצחון
        elif user_number < secret_num:
            result = "Too low!"
            print(f"\t\t{result}")
        else:
            result = "Too high!"
            print(f"\t\t{result}")

        print(f"\t\tTry again.. Number of guesses so far: {user_guesses}")
        return False, result