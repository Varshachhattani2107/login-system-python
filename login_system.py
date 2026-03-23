# Simple Login System using File Handling

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("users.txt", "a") as f:
        f.write(username + "," + password + "\n")

    print("Registration successful!\n")


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        with open("users.txt", "r") as f:
            users = f.readlines()

            for user in users:
                u, p = user.strip().split(",")

                if u == username and p == password:
                    print("Login successful!\n")
                    return

        print("Invalid username or password!\n")

    except FileNotFoundError:
        print("No users found. Please register first.\n")


def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice!\n")


if __name__ == "__main__":
    main()
