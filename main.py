

db_username = "abdulloh"
db_passcode = "1234"

username = input("Username: ")
password = input("password: ")


while True:
    if db_username == username and db_passcode == password:
        print("Togri!")
        break
    print("Username or password notori")

    username = print("Username: ")
    password = print("passcode: ")