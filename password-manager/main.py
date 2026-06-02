import json

# Input Credentials
website = input("Enter your website (e.g., Github, Google, Apple etc): ")
username = input("Enter your username: ")
password = input("Enter your password: ")

# Load data
with open("passwords.json", "r") as file:
    data = json.load(file)

    # Handle existing data
    if (website in data) and (data[website]["username"] == username):
        print("Account already exists with the same username!")
        exit()

# Store data
data = {
    website: {
        "username": username,
        "password": password
    }
}

# Save data
with open("passwords.json", "w") as file:
    json.dump(data, file, indent=4)
    
print("Your credentials have been saved successfully.")