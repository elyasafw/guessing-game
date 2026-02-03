import sys
from game import play_game
from user_procedures import user_test, User_authentication, generates_user


def main():
    is_exists, user_name = user_test()

    if is_exists:
        if not User_authentication(user_name):
            print("\t\tAccess denied. Exiting...")
            sys.exit()
    else:
        generates_user(user_name)

    play_game(user_name)

    print("\n\t\tThanks for playing! Goodbye.")


if __name__ == "__main__":
    main()