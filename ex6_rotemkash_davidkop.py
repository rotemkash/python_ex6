"""
======================================================================
ex6
======================================================================
Writen by: Rotem kashani, ID = 209073352,   login = rotemkash
	       David Koplev, ID = 208870279 ,    login = davidkop

Question 1:
This program creates classes of shapes which inheritances from
the abstract class 'Shape'.
The class 'ShapesCollection' creates list of shapes named shape,
the shapes are sorted by its size of area. the shape with the minimum
area is at first.

Question 2:
The purpose of this program is to manage bank accounts for customers. The main goal of the program is to allow the
user to create a new bank account, perform monitoring and management operations on the account
(such as deposits and withdrawals), and receive information about the account status and transaction history.

The program utilizes the classes Person, Bank_account, and Student_account to create the corresponding instances of
 bank customers and their accounts. The program enables the creation of a regular account or a student account,
  thus providing customized functionality for each account type.

Additionally, the program can record the transaction history of the account in a file named
"history.txt" and display the history based on the user's choice.

The overall objective of the program is to enable the user to conveniently and user-friendly manage a bank
account and provide them with a simple interface for performing various banking operations.

The input of the program consists of a series of questions and actions asked  the user to manage a bank account
within the system.

The input includes the following information:
1. First name of the customer.
2. Last name of the customer.
3. Address of the customer.
4. ID number (identification number) of the customer.
5. Initial balance in the account.
6. Type of account (regular/student) of the customer.
   If it's a student account, the institution name should also be provided.

The output of the program includes messages and information printed to the user according to the actions they perform.
The output may include the following information:
- Confirmation or notification messages regarding the successful or failed execution of an action
 (e.g., successful deposit or insufficient balance for a withdrawal).
- Account details, including the account number, the customer's full name, and the current balance.
- The account's transaction history, which is updated with each action and displayed to the user based on their choice.

Additionally, the program creates a file named "history.txt" that serves as a record of the account's
transaction history. The program can display the history to the user based on their choice.

"""

# =====================Question 1=================================

import random
from abc import ABC, abstractmethod


class Shape(ABC):  # abstract class

    @abstractmethod
    def area(self):  # area of the shape
        pass

    @abstractmethod
    def perimeter(self):  # perimeter of the shape
        pass

    def __gt__(self, other):  # check if the area of the first shape is greater than the area of the second shape
        return self.area() > other.area()


# ---------------------------
class Circle(Shape):  # inherits from class 'Shape'

    def __init__(self, radius):
        super().__init__()
        if radius > 0:
            self.__radius = radius
        else:
            self.__radius = 1

    def set_radius(self, radius):  # allows setting the radius of the circle from outside the class.
        if radius > 0:
            self.__radius = radius

    def get_radius(self):  # allows accessing the radius of the circle from outside the class.
        return self.__radius

    def area(self):  # calculates the area of the circle using the formula π * radius^2.
        return 3.14 * self.__radius * self.__radius

    def perimeter(self):  # calculates the perimeter (circumference) of the circle using the formula 2 * π * radius.
        return 2 * 3.14 * self.__radius

    def __str__(self):  # overrides the default string representation of the Circle
        # class and returns a formatted string displaying the circle's radius.
        return f"Circle: radius = {self.__radius}"


# ---------------------------
class Rectangle(Shape):  # inherits from class 'Shape'

    def __init__(self, width, height):
        super().__init__()
        if width > 0:
            self.__width = width
        else:
            self.__width = 1

        if height > 0:
            self.__height = height
        else:
            self.__height = 1

    def set_width(self, width):  # allow setting the width of the rectangle from outside the class.
        if width > 0:
            self.__width = width

    def get_width(self):  # allow accessing the width of the rectangle from outside the class
        return self.__width

    def set_height(self, height):  # allow setting the height of the rectangle from outside the class.
        if height > 0:
            self.__height = height

    def get_height(self):  # allow accessing the height of the rectangle from outside the class
        return self.__height

    def area(self):  # calculates the area of the rectangle using the formula width * height.
        return self.__width * self.__height

    def perimeter(self):  # calculates the perimeter of the rectangle using the formula 2 * (width + height).
        return 2 * (self.__width + self.__height)

    def __str__(self):  # overrides the default string representation of the Rectangle class and
        # returns a formatted string displaying the rectangle's width and height.
        return f"Rectangle: width = {self.__width}, height = {self.__height}"


# ---------------------------
class Square(Rectangle):  # inherits from class 'Rectangle'

    def __init__(self, length):
        super().__init__(length, length)

    def __str__(self):  # overrides the default string representation of the Square class and returns
        # a formatted string displaying the length of the side of the square.
        return f"Square: length = {self.get_width()}"


# ---------------------------
class ShapesCollection:
    def __init__(self):
        self.shapes = []

    def __len__(self):  # returns the number of shapes in the collection using the len() function.
        return len(self.shapes)

    def __getitem__(self, index):  # enables accessing the list at a specific index using the indexing operator [].
        return self.shapes[index]

    def insert(self, shape):  # takes an object as a parameter, checks if it's of type Shape, and adds it to the
        # list in the appropriate position to keep the shapes sorted in ascending order by area.
        if isinstance(shape, Shape):
            self.shapes.append(shape)
            self.shapes.sort(key=lambda x: x.area())

    def __str__(self):  # overrides the default string representation of the ShapesCollection class and returns a
        # formatted string containing the details of all the shapes in the collection.
        result = "Shapes in collection: \n"
        for shape in self.shapes:
            result += str(shape) + "\n"
        return result

    def diff_perimeter_biggest(self):  # calculates the largest difference between the perimeters of any two
        # shapes in the collection.
        if len(self.shapes) < 2:
            return 0

        max_diff = 0
        for i in range(len(self.shapes) - 1):
            for j in range(i + 1, len(self.shapes)):
                diff = abs(self.shapes[i].perimeter() - self.shapes[j].perimeter())
                if diff > max_diff:
                    max_diff = diff

        return max_diff

    def as_area_same(self, shape):  # takes a Shape object as a parameter and returns a list containing all the shapes
        # from the collection that have the same area as the given shape.
        result = []
        if isinstance(shape, Shape):
            for shape_in_collection in self.shapes:
                if shape_in_collection.area() == shape.area():
                    result.append(shape_in_collection)
        return result

    def How_many_quadrilaterals(self):  # counts how many quadrilaterals (rectangles and squares) exist in the
        # collection.
        count = 0
        for shape in self.shapes:
            if isinstance(shape, Rectangle) or isinstance(shape, Square):
                count += 1
        return count


# =====================Question 2=================================

class Person:
    def __init__(self, first_name, last_name, address, id_number):  # Initializes a Person object with the provided
        # first_name, last_name, address, and id_number. If the input format is valid, the attributes are set
        # accordingly. Otherwise, default values are used, and an error message is printed.
        if first_name.isalpha() and last_name.isalpha() and id_number.isdigit():
            self.__first_name = first_name
            self.__last_name = last_name
            self.__id_number = id_number
        else:
            self.__first_name = "Avi"
            self.__last_name = "Cohen"
            self.__id_number = "300010000"
            print("Invalid input format. Only letters are allowed for names, and only digits are allowed for"
                  " ID number.")

        self.__address = address

    @property
    def first_name(self):  # Property getter for the private attribute __first_name.
        return self.__first_name

    @property
    def last_name(self):  # Property getter for the private attribute __last_name.
        return self.__last_name

    @property
    def address(self):  # Property getter for the private attribute __address.
        return self.__address

    @property
    def id_number(self):  # Property getter for the private attribute __id_number.
        return self.__id_number

    def new_address(self, new_address):  # Updates the __address attribute with a new address.
        self.__address = new_address

    def new_last_name(self, new_last_name):  # Updates the __last_name attribute with a new last name.
        self.__last_name = new_last_name


class Bank_account:
    def __init__(self, account_number, customer, balance):  # Initializes a Bank_account object with the provided
        # account_number, customer (a Person object), and balance.
        self.__account_number = account_number
        self.__customer = customer
        self.__balance = balance

    def __str__(self):  # Returns a string representation of the Bank_account object, including the account number,
        # full name of the customer, and balance.
        return f"Account: {self.__account_number}\nName: {self.get_full_name()}\nBalance: {self.__balance}"

    def get_account_number(self):  # Returns the account number.
        return self.__account_number

    def set_account_number(self, account_number):  # Updates the account number.
        self.__account_number = account_number

    def get_customer(self):  # Returns the customer (a Person object).
        return self.__customer

    def set_customer(self, customer):  # Updates the customer.
        self.__customer = customer

    def get_balance(self):  # Returns the account balance.
        return self.__balance

    def set_balance(self, balance):  # Updates the account balance.
        self.__balance = balance

    def deposit(self, amount):  # Deposits the specified amount into the account.
        self.__balance += amount

    def withdraw(self, amount):  # Withdraws the specified amount from the account if sufficient balance is available.
        if self.__balance >= amount:
            self.__balance -= amount
            return True
        else:
            return False


class Student_account(Bank_account):  # inherits from Bank_account
    def __init__(self, account_number, customer, balance, institution):  # Initializes a Student_account object with the
        # provided account_number, customer (a Person object), balance, and institution.
        super().__init__(account_number, customer, balance)
        self.__institution = institution

    def __str__(self):  # Returns a string representation of the Student_account object, including the account number,
        # full name of the customer, and balance.
        return f"Student Account: {self.get_account_number()}\n" \
               f"Name: {self.get_customer().first_name} {self.get_customer().last_name}\n" \
               f"Balance: {self.get_balance()}\n"


def main():  # The main function that interacts with the user. It prompts the user for input to create a bank account
    # (either a regular or student account) and performs actions based on the user's choice.
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    address = input("Enter address: ")
    id_number = input("Enter ID number: ")
    balance = float(input("Enter initial balance: "))
    account_type = input("Enter account type (regular/student): ")

    if account_type.lower() == "student":
        institution = input("Enter institution: ")
        account = Student_account(random.randint(0, 1000), Person(first_name, last_name, address, id_number),
                                  balance, institution)
    else:
        account = Bank_account(random.randint(0, 1000), Person(first_name, last_name, address, id_number), balance)

    history_file = open("history.txt", "a")
    history_file.write(f"New account, balance: {account.get_balance()}\n")
    history_file.close()

    while True:
        print("\nSelect an action:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Print account details")
        print("4. Print transaction history")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
            history_file = open("history.txt", "a")
            history_file.write(f"Deposit {amount}, balance: {account.get_balance()}\n")
            print("Deposit successful!")

        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))

            if account.withdraw(amount):
                history_file.write(f"Withdraw {amount}, balance: {account.get_balance()}\n")
                print("Withdrawal successful!")
            else:
                print("Insufficient balance!")

        elif choice == 3:
            print(account)

        elif choice == 4:
            history_file = open("history.txt", "r")
            print("Transaction History:")
            print(history_file.read())

        elif choice == 5:
            break

        else:
            print("Invalid choice. Please try again.")

    history_file.close()


def run():  # The main execution function. It provides a menu for the user to select a question to answer or
    # exit the program. When question 2 is selected, it calls the main() function.

    while True:
        print("""Select a question to answer:
                 1. Question 1
                 2. Question 2
                 0. Exit\n""")

        choice = input("Enter your choice (0-2): ")

        if choice == "1":
            # Handle question 1
            pass

        elif choice == "2":
            main()

        elif choice == "0":
            # Exit the program
            print("Exiting the program...")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    run()
