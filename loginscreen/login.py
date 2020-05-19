# Justin Chang
# May 19, 2020
# This is a program that simulates asking the user to create an account or just login
import csv


class User:
    """
    Class that offers the user to login or to create a new account
    """

    def __init__ (self):
        self.username = ""
        self.password = ""
        self.security_question = ""
        self.security_answer = ""

    def create_account(self, username, password, security_question, security_answer):
        self.username = username
        self.password = password
        self.security_question = security_question
        self.security_answer = security_answer

        user_info = [self.username, self.password, self.security_question, self.security_answer]
        myfile = open("users.csv", "w")
        enter_info = csv.writer(myfile)
        enter_info.writerow(user_info)

    def login(self):
        pass

    def ask_security_question(self):
        pass


person1 = User()
username = input("Enter username: ")
password = input("Enter password: ")
security_question = input("Enter security question: ")
security_answer = input("Enter answer to security quesetion: ")

person1.create_account(username, password, security_question, security_answer)
