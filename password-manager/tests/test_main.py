import main
import json
import pytest

@pytest.fixture
def sample_account_data():
    return {"github": [{"username": "example_user", "password": "exampleuser"}]}

def test_fetch_account_index_returns_correct_index(sample_account_data):
    result = main.fetch_account_index("github", "example_user", sample_account_data)

    assert result == 0

def test_fetch_account_index_returns_none_for_missing_username(sample_account_data):
    result = main.fetch_account_index("github", "example_user1", sample_account_data)

    assert result is None

def test_fetch_account_index_returns_none_for_missing_website(sample_account_data):
    result = main.fetch_account_index("google", "example_user", sample_account_data)

    assert result is None

def test_validate_password_returns_true_for_correct_password(sample_account_data):
    result = main.validate_password("github", "exampleuser", sample_account_data, 0)

    assert result is True

def test_validate_password_returns_false_for_incorrect_password(sample_account_data):
    result = main.validate_password("github", "example_user", sample_account_data, 0)

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

def test_create_account_for_existing_website(sample_account_data):
    data = sample_account_data
    main.create_account("github", "user345", "secret_no_more", data)

    assert len(data["github"]) > 1

def test_create_account_appends_correct_data():
    data = {
        "google": []
    }
    main.create_account("google", "user345", "secret_no_more", data)

    assert data["google"][0] == {
            "username": "user345",
            "password": "secret_no_more"
        }
    
def test_load_data_from_JSON_file_loads_existing_file(tmp_path, sample_account_data):
    file_path = tmp_path / "valid_passwords.json"
    expected = sample_account_data
    file_path.write_text(json.dumps(expected))
    result = main.load_data_from_JSON_file(file_path)

    assert result == expected

def test_load_data_from_JSON_file_loads_empty_file(tmp_path):
    file_path = tmp_path / "empty_password.json"
    file_path.write_text(json.dumps({}))
    result = main.load_data_from_JSON_file(file_path)

    assert result == {}

def test_load_data_from_JSON_file_loads_non_existing_file(tmp_path):
    file_path = tmp_path / "does_not_exist.txt"
    result = main.load_data_from_JSON_file(file_path)

    assert result == {}

def test_save_to_JSON_file_saves_data_to_a_missing_file(tmp_path, sample_account_data):
    file_path = tmp_path / "saved_passwords.json"

    # Check for the missing file
    assert not file_path.exists()

    saved = main.save_to_JSON_file(file_path, sample_account_data)

    # Check for the file created through the helper method
    assert file_path.exists()

    assert saved is True

    # Verify the exact provided data
    with open(file_path, "r") as file:
        loaded_data = json.load(file)
        
    assert loaded_data == sample_account_data
