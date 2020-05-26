# Justin Chang
# May 19, 2020
# This is a program that simulates asking the user to create an account or just login
import csv


def create_account(username, password, security_question, security_answer):
    user_info = [username, password, security_question, security_answer]
    myfile = open("users.csv", "a")
    enter_info = csv.writer(myfile)
    enter_info.writerow(user_info)
    myfile.close()


def login(username, password):
    # Read the csv file to see if the user and password are in it.
    myfile = open("users.csv", "r")
    user_reader = list(csv.reader(myfile))
    myfile.close()

    found = False
    row_count = 0
    while not found:
        if user_reader[row_count][0] == username and user_reader[row_count][1] == password:
            return True

        elif row_count == len(user_reader)-1:
            return False

        else:
            row_count += 1


def find_account(username):
    myfile = open("users.csv", "r")
    user_reader = list(csv.reader(myfile))
    myfile.close()

    # Find the user in the database:
    found = False
    row_count = 0
    while not found:
        if user_reader[row_count][0] == username:
            return user_reader[row_count]
        elif row_count == len(user_reader)-1:
            return False
        else:
            row_count += 1


def main():
    print("Welcome!")

    action = input("Press 1 to login \nPress 2 to create an account \nPress 3 if you forgot your password")

    # For login
    if action == "1":
        again = True
        while again:
            user = input("Enter username: ")
            pw = input("Enter password: ")
            if login(user, pw):
                print("Successful login!")
                again = False
            else:
                go_again = input("User not found in database. Try again? (y/n)")
                if go_again != "y":
                    again = False

    # To create account
    if action == "2":
        user = input("Enter username: ")
        pw = input("Enter password: ")
        sq = input("Enter a security question: ")
        sa = input("Enter the answer to the security question: ")
        create_account(user, pw, sq, sa)
        print("Account created!")

    # If password is forgotten
    if action == "3":
        user = input("Enter your username: ")
        if find_account(user):
            info = find_account(user)
            print("Please answer the following question:")
            user_answer = input(info[2])
            if user_answer == info[3]:
                print("Your password is " + info[1])
        else:
            print("Username not found in database.")


main()

