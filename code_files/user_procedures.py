import hashlib, csv, sys

def user_test():
    user_name = input("\n\t\tEnter your user-name:  ").strip()
    with open("game_files/users.csv", "r", encoding='utf-8') as file:
        users_list = file.readlines()
        for line in users_list:
            existing_user = line.split(",")[0].strip()
            if existing_user == user_name:
                return True, user_name
        return False, user_name


def generates_user(user_name):
    choice = input(f"\t\tUser '{user_name}' not found.. Would you like to create a new user? (y/n):  ").lower().strip()
    if choice == 'y':
        user_pass = input("\t\tEnter your password to register:  ")
        hash_encryption = hashlib.md5(user_pass.encode()).hexdigest()
        with open("game_files/users.csv", "a", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([user_name, hash_encryption])
        print(f"\t\tUser {user_name} registered successfully!")
        return True
    else:
        print("\t\tExiting game..  Goodbye!")
        sys.exit()


def User_authentication(user_name):
    user_pass = input("\t\tEnter your password to login:  ")
    input_hash = hashlib.md5(user_pass.encode()).hexdigest()
    with open("game_files/users.csv", "r", encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == user_name and row[1] == input_hash:
                print("\t\tLogin Successful!")
                return True
    print("\t\tWrong password..  Goodbye!")
    return False