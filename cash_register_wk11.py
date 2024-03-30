"""
Program Details:

Course: DSC 510
Version#:1: Week 10, Programming Assignment 11.1

Requirements:
Your program must have a welcome message for the user.
Your program must have one class called CashRegister.
Your program will have an instance method called addItem which takes one parameter for price. The method should also keep track of the number of items in your cart.
Your program should have two getter methods.
getTotal – returns totalPrice
getCount – returns the itemCount of the cart
Your program must have a properly defined main function and a call to main.
Your program must create an instance of the CashRegister class within your main function.
Your program should have a loop in main which allows the user to continue to add items to the cart until they request to quit.
Your program should print the total number of items in the cart.
Your program should print the total $ amount of the cart.
The output should be formatted as currency. Be sure to investigate the locale class. You will need to call locale.setlocale and locale.currency.

Author: Siddhartha Bhaumik
Initial Release Date: 02/26/2022
"""

import locale

print("Welcome to Simple Cash Register Program.\n")


class CashRegister:
    def __init__(self):
        self.total = 0.0
        self.items = 0

    def add_item(self, price):
        self.total = self.total + price
        self.items += 1

    def get_total(self):
        locale.setlocale(locale.LC_ALL, 'en_US')
        return locale.currency(self.total)

    def get_count(self):
        return self.items


def main():
    """The main function calls the CashRegister class,
      allows the user to continue to add items to the cart until they request to quit """
    register = CashRegister()

    while True:
        try:
            price = input("Please enter your item value or enter 'Quit' to exit: ").strip().strip('$').lower()
            if price == 'quit':
                print(f'\nYou have {register.get_count()} items in your cart, Total price: {register.get_total()}.\n')
                print('Thank you!! Please visit again!!')
                break
            else:
                price = float(price)
                register.add_item(price)
        except ValueError:
            print("Please enter a valid numeric item value or 'Quit' to exit!!")
            continue


if __name__ == "__main__":
    main()
