import main

def test_fetch_account_index_returns_correct_index():
    data = {"github": [{"username": "example_user", "password": "exampleuser"}]}

    result = main.fetch_account_index("github", "example_user", data)

    assert result == 0

def test_fetch_account_index_returns_none_for_missing_username():
    data = {"github": [{"username": "example_user", "password": "exampleuser"}]}

    result = main.fetch_account_index("github", "example_user1", data)

    assert result is None

def test_fetch_account_index_returns_none_for_missing_website():
    data = {"github": [{"username": "example_user", "password": "exampleuser"}]}

    result = main.fetch_account_index("google", "example_user", data)

    assert result is None

def test_validate_password_returns_true_for_correct_password():
    data = {"github": [{"username": "example_user", "password": "exampleuser"}]}

    result = main.validate_password("github", "exampleuser", data, 0)

    assert result is True

def test_validate_password_returns_false_for_incorrect_password():
    data = {"github": [{"username": "example_user", "password": "exampleuser"}]}

    result = main.validate_password("github", "example_user", data, 0)

    assert result is False

def test_create_account_for_new_website():
    data = {}

    main.create_account("google", "user123", "secret", data)

    assert data == {
        "google": [{
            "username": "user123",
            "password": "secret"
        }]
    }

def test_create_account_for_existing_website():
    data = {
        "google": [{
            "username": "user123",
            "password": "secret"
        }]
    }

    main.create_account("google", "user345", "secret_no_more", data)

    assert len(data["google"]) > 1

def test_create_account_appends_correct_data():
    data = {
        "google": []
    }

    main.create_account("google", "user345", "secret_no_more", data)

    assert data["google"][0] == {
            "username": "user345",
            "password": "secret_no_more"
        }
    
def test_load_data_from_JSON_file_loads_existing_file():
    file_name = r"tests\test_data\valid_passwords.json"

    data = {
        "google": [{
            "username": "exampleuser1",
            "password": "example1user"
        }]
    }

    result = main.load_data_from_JSON_file(file_name)

    assert data == result

def test_load_data_from_JSON_file_loads_empty_file():
    file_name = r"tests\test_data\empty_passwords.json"
    
    data = {}

    result = main.load_data_from_JSON_file(file_name)

    assert data == result

def test_load_data_from_JSON_file_loads_non_existing_file():
    file_name = "does_not_exist.txt"
    
    data = {}

    result = main.load_data_from_JSON_file(file_name)

    assert data == result