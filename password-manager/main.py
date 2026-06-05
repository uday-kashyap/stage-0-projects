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
    Take and validate user input. Return it after validation.
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
    Input and return user credentials.
    '''

    website = input("Enter your website (e.g., Github, Google, Apple etc): ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    return website, username, password


def get_website_and_username():
    '''
    Input and return 'website' and 'username'.
    '''

    website = input("Enter your website (e.g., Github, Google, Apple etc): ")
    username = input("Enter your username: ")

    return website, username


def load_data():
    '''
    Load and return existing data.
    '''
    
    try:
        with open("passwords.json", "r") as file:
            return json.load(file)
        
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    

def account_exists(website, username, data):
    '''
    Check for the pre-existing account with the same username and website name.
    '''

    if website in data:
        
        for account in data[website]:

            if account["username"] == username:
                return True
    
    return False


def save_account(website, username, password, data):
    '''
    Create new user account and store their credentials.
    '''

    if website not in data:
        data[website] = []

    data[website].append({
        "username": username,
        "password": password
    })

    with open("passwords.json", "w") as file:
        json.dump(data, file, indent=4)
    
    print("Your account has been created successfully.")


def fetch_account(website, username, data):
    '''
    Fetch user account and return it.
    '''

    if not account_exists(website, username, data):
        return {}
    
    for account in data[website]:

        if account["username"] == username:
            return account


def main():

    data = load_data()
    display_menu()
    user_input = get_user_input()
    print()

    if user_input == 1:

        website, username, password = get_credentials()
        print()

        if account_exists(website, username, data):
            print("Account already exists with the same username!")
            return
        
        save_account(website, username, password, data)
    
    elif user_input == 2:
        
        website, username = get_website_and_username()
        print()
        account_data = fetch_account(website, username, data)

        if not account_data:
            print("Account does not exist!")
            return
        
        for entry in account_data:
            print(f"{entry.title()}: {account_data[entry]}")     


if __name__ == '__main__':
    main()