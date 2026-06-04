import json


FEATURES = {
        1: "Add account",
        2: "Search account"
    }


def display_menu():
    '''
    Show system features menu to the user.
    '''

    for option_no, feature in FEATURES.items():
        print(f"{option_no}. {feature}")


def get_user_input():
    '''
    Take and validate user input.
    '''

    while True:
        try:
            choice = int(input("Enter your choice: "))

            if choice not in FEATURES:
                print("Please enter a valid option!")
                continue

            return choice # Return a valid choice
        
        except ValueError:
            print("Options must be integers!")


def get_credentials():
    '''
    Input user credentials.
    '''

    website = input("Enter your website (e.g., Github, Google, Apple etc): ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    return website, username, password


def load_data():
    '''
    Load existing data.
    '''
    
    try:
        with open("passwords.json", "r") as file:
            return json.load(file)
        
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    

def is_account_duplicate(website, username, data):
    '''
    Check for the pre-existing account with the same username and website name.
    '''

    if website in data:
        
        for credentials in data[website]:

            if credentials["username"] == username:
                return True
    
    return False


def save_data(website, username, password, data):
    '''
    Store and save the user credentials.
    '''

    if website not in data:
        data[website] = []

    data[website].append({
        "username": username,
        "password": password
    })

    with open("passwords.json", "w") as file:
        json.dump(data, file, indent=4)
    
    print("Your credentials have been saved successfully.")


def main():

    data = load_data()
    display_menu()
    user_input = get_user_input()

    if user_input == 1:

        website, username, password = get_credentials()
        account_exists = is_account_duplicate(website, username, data)

        if account_exists:
            print("Account already exists with the same username!")
            return
        
        save_data(website, username, password, data)
    
    elif user_input == 2:
        print("Coming Soon!")


if __name__ == '__main__':
    main()