import json

FILE_NAME = "passwords.json"

FEATURES = {
    1: "Add account",
    2: "Search account",
    3: "Delete account",
    4: "Update account",
}


def add_account(data: dict) -> None:
    """
    Add a new user account.
    """

    website, username, password = get_credentials()
    print()

    account_idx = fetch_account_index(website, username, data)

    if account_idx is not None:
        print("Account already exists with the same username!")
        return

    create_account(website, username, password, data)

    saved = save_to_JSON_file(FILE_NAME, data)

    if saved:
        print("Your account has been created successfully.")

    else:
        print("Failed to save data!")


def search_account(data: dict) -> None:
    """
    Search for existing user account.
    """

    website, username = get_website_and_username()
    print()

    account_idx = fetch_account_index(website, username, data)

    if account_idx is not None:

        for attribute, attribute_val in data[website][account_idx].items():
            print(f"{attribute.title()}: {attribute_val}")

    else:
        print("Account does not exist!")


def delete_account(data: dict) -> None:
    """
    Delete existing user account.
    """

    website, username, password = get_credentials()
    print()

    account_idx = fetch_account_index(website, username, data)

    if account_idx is not None:

        valid_password = validate_password(website, password, data, account_idx)

        if valid_password:

            data[website].pop(account_idx)

            if not data[website]:
                del data[website]

            saved = save_to_JSON_file(FILE_NAME, data)

            if saved:
                print("Your account has been deleted successfully.")

            else:
                print("Failed to save data!")

        else:
            print("Invalid password!")

    else:
        print("Account does not exist!")


def update_account(data: dict) -> None:
    """
    Update existing user account.
    """

    website, username, password = get_credentials()
    print()

    account_idx = fetch_account_index(website, username, data)

    if account_idx is not None:

        valid_password = validate_password(website, password, data, account_idx)

        if valid_password:

            new_username = input("Enter a new username: ")
            new_password = input("Enter a new password: ")
            print()

            target_account = data[website][account_idx]

            # Update attributes
            target_account["username"] = new_username
            target_account["password"] = new_password

            saved = save_to_JSON_file(FILE_NAME, data)

            if saved:
                print("Your account has been updated successfully.")

            else:
                print("Failed to save data!")

        else:
            print("Invalid password!")

    else:
        print("Account does not exist!")


def validate_password(website: str, password: str, data: dict, account_idx: int) -> bool:
    """
    Validate provided password to the actual password of the account.
    Return True if matches, else False.
    """

    target_account = data[website][account_idx]

    if target_account["password"] == password:
        return True

    return False


def save_to_JSON_file(file_name: str, data: dict) -> bool:
    """
    Save data to a JSON file.
    Return True on success, else False.
    """

    try:
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)

        return True

    except OSError:
        return False


def display_menu() -> None:
    """
    Show system features menu to the user.
    """

    for option_no, feature in FEATURES.items():
        print(f"{option_no}. {feature}")


def get_user_choice() -> int:
    """
    Take and validate user choice. Return it after validation.
    """

    while True:
        try:
            choice = int(input("Enter your choice: "))

            if choice not in FEATURES:
                print("Please enter a valid option!")
                continue

            return choice  # Return a valid choice

        except ValueError:
            print("Options must be integers!")


def get_credentials() -> tuple[str, str, str]:
    """
    Input and return user credentials.
    """

    website = input("Enter your website (e.g., Github, Google, Apple etc): ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    return website, username, password


def get_website_and_username() -> tuple[str, str]:
    """
    Input and return 'website' and 'username'.
    """

    website = input("Enter your website (e.g., Github, Google, Apple etc): ")
    username = input("Enter your username: ")

    return website, username


def load_data_from_JSON_file(file_name: str) -> dict:
    """
    Load and return existing data.
    """

    try:
        with open(file_name, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def create_account(website: str, username: str, password: str, data: dict) -> None:
    """
    Create a new user account.
    """

    new_account = {"username": username, "password": password}

    # Root dictionary modifications
    if website not in data:
        data[website] = []

    data[website].append(new_account)


def fetch_account_index(website: str, username: str, data: dict) -> int | None:
    """
    Fetch user account's index and return it.
    """

    if website in data:

        for idx, account in enumerate(data[website]):

            if account["username"] == username:
                return idx

    return None


def main() -> None:

    ACTIONS = {
        1: add_account,
        2: search_account,
        3: delete_account,
        4: update_account
    }

    data = load_data_from_JSON_file(FILE_NAME)
    display_menu()
    user_choice = get_user_choice()
    print()

    ACTIONS[user_choice](data)


if __name__ == "__main__":
    main()
