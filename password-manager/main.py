import json


FEATURES = {
        1: "Add account",
        2: "Search account",
        3: "Delete account"
    }


def add_account(data: dict) -> None:
    '''
    FEATURE: Add user account.
    '''

    website, username, password = get_credentials()
    print()

    account_already_exists = account_exists(website, username, data)
    
    if account_already_exists:
        print("Account already exists with the same username!")
        return
        
    save_account(website, username, password, data)
    print("Your account has been created successfully.")


def search_account(data: dict) -> None:
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


def delete_account(data: dict) -> None:
    '''
    FEATURE: Delete user account.
    '''

    # Status mapping
    statuses = {

        "success": "Your account has been deleted successfully.",
        "invalid_password": "Invalid password!",
        "account_not_found": "Account does not exist!"
    }

    website, username, password = get_credentials()
    print()
    
    status = remove_account(website, username, password, data)
    print(statuses[status])


def display_menu() -> None:
    '''
    Show system features menu to the user.
    '''

    for option_no, feature in FEATURES.items():
        print(f"{option_no}. {feature}")


def get_user_choice() -> int:
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


def get_credentials() -> tuple[str, str, str]:
    '''
    Input and return user credentials.
    '''

    website = input("Enter your website (e.g., Github, Google, Apple etc): ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    return website, username, password


def get_website_and_username() -> tuple[str, str]:
    '''
    Input and return 'website' and 'username'.
    '''

    website = input("Enter your website (e.g., Github, Google, Apple etc): ")
    username = input("Enter your username: ")

    return website, username


def load_data() -> dict:
    '''
    Load and return existing data.
    '''
    
    try:
        with open("passwords.json", "r") as file:
            return json.load(file)
        
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    

def account_exists(website: str, username: str, data: dict) -> bool:
    '''
    Check for the pre-existing account with the same username and website name.
    Return True if found, else False.
    '''

    if website in data:
        
        for account in data[website]:

            if account["username"] == username:
                return True
    
    return False


def save_account(website: str, username: str, password: str, data: dict) -> None:
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


def fetch_account(website: str, username: str, data: dict) -> dict:
    '''
    Fetch user account and return it.
    '''

    if website in data:
    
        for account in data[website]:

            if account["username"] == username:
                return account
        
    return {}
        
        
def remove_account(website: str, username: str, password: str, data: dict) -> str:
    '''
    Remove existing user account.
    Return operation status.
    '''
    
    if website in data:

        for idx, account in enumerate(data[website]):

            if account["username"] == username:

                if account["password"] == password:

                    data[website].pop(idx)

                    if not data[website]:
                        del data[website]

                    with open("passwords.json", "w") as file:
                        json.dump(data, file, indent=4)
                    
                    return "success"
                
                else:
                    return "invalid_password" 
        
    return "account_not_found"


def main() -> None:

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