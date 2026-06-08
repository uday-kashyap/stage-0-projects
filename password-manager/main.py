import json


FEATURES = {
        1: "Add account",
        2: "Search account",
        3: "Delete account"
    }


def add_account(data):
    '''
    FEATURE: Add user account.
    '''

    website, username, password = get_credentials()
    print()

    if account_exists(website, username, data):
        print("Account already exists with the same username!")
        return
        
    save_account(website, username, password, data)
    print("Your account has been created successfully.")


def search_account(data):
    '''
    FEATURE: Search user account.
    '''

    website, username = get_website_and_username()
    print()
    
    account_data = fetch_account(website, username, data)
        
    if account_data:

        for entry in account_data:
            print(f"{entry.title()}: {account_data[entry]}")

    else:
        print("Account does not exist!")


def delete_account(data):
    '''
    FEATURE: Delete user account.
    '''

    website, username = get_website_and_username()
    print()
    
    removed = remove_account(website, username, data)

    if removed:
        print("Your account has been deleted successfully.")

    else:
        print("Account does not exist!")


def display_menu():
    '''
    Show system features menu to the user.
    '''

    for option_no, feature in FEATURES.items():
        print(f"{option_no}. {feature}")


def get_user_choice():
    '''
    Take and validate user choice. Return it after validation.
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
    Return True if found, else False.
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


def fetch_account(website, username, data):
    '''
    Fetch user account and return it.
    '''

    if website in data:
    
        for account in data[website]:

            if account["username"] == username:
                return account
        
    return {}
        
        
def remove_account(website, username, data):
    '''
    Remove existing user account.
    Return True on success, else False.
    '''
    
    if website not in data:
        return False

    for idx, account in enumerate(data[website]):

        if account["username"] == username:
            data[website].pop(idx)

            if data[website] == []:
                del data[website]

            with open("passwords.json", "w") as file:
                json.dump(data, file, indent=4)
            
            return True
        
    return False


def main():

    data = load_data()
    display_menu()
    user_input = get_user_choice()
    print()

    if user_input == 1:
        add_account(data)

    elif user_input == 2:
        search_account(data)

    elif user_input == 3:
        delete_account(data)


if __name__ == '__main__':
    main()