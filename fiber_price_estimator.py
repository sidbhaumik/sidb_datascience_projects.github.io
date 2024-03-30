"""
 Program Details:


 Purpose: Create a program which can perform the below list of tasks for the user-
           - Retrieve the number of feet of fiber optic cable to be installed.
           - Calculate the installation cost of fiber optic cable.
           - Print a receipt which includes company name, number of feet of fiber to be installed,
             the calculated cost, and total cost in a legible format.
 Author: Siddhartha Bhaumik
 Initial Release Date: 12/9/2021
------------------------------------------
 Version Control Log:

 Version#:1
 Change Details: Initial Release
 Date of Change: 12/9/2021
 Author: Siddhartha Bhaumik
 Change Approved by: N/A
 Production Release: N/A

 Version#:2
 Change Details: Added Discount logic for bulk purchase of fiberOptics cable
                 - Less than 100 feet cable, charged at $0.87 per foot
                 - More than 100 feet cable, charged at $0.80 per foot
                 - More than 250 feet cable, charged at $0.70 per foot
                 - More than 500 feet cable, charged at $0.50 per foot
 Date of Change: 12/18/2021
 Author: Siddhartha Bhaumik
 Change Approved by: N/A
 Production Release: N/A

 Version#:3
  Change Details: Added function call on top of Version#2 program
  Date of Change: 01/07/2022
  Author: Siddhartha Bhaumik
  Change Approved by: N/A
  Production Release: N/A
"""
# Welcome Greetings
print('Welcome To The Home Of FiberOptics\n')

# Get user's company name
# Convert to upper case for Display Purpose
company_name = (input('Please provide the company name:')).upper()

# Retrieve the length of fiber optic cable to be installed from the user.
no_of_feet = float(input('Please provide the number of feet of fiber optic cable:'))

# Standard Installation cost per feet
base_install_cost = 0.87


# function to get the installation cost based on number of feets of fibre cable needed
def install_rate():
    if no_of_feet >= 500:
        install_cost = 0.50
    elif no_of_feet >= 250:
        install_cost = 0.70
    elif no_of_feet >= 100:
        install_cost = 0.80
    else:
        install_cost = base_install_cost
    return float(install_cost)


# Total cost calculation based on installation cost and no. of feet for Fiber Cable
def total_cost(feet, price):
    return print('Total Cost: $', format((feet * price), '.2f'))


# Print receipt with multiple info for the user
print('\nReceipt')
print('=======')
print('Company Name:', company_name)
print('Length Of Fiber Optics Cable:', no_of_feet, 'feet')
print('Standard Installation Cost Per Feet: $', base_install_cost)
print('Applied Installation Cost Per Foot: $', (format(install_rate(), '.2f')))
total_cost(no_of_feet, install_rate())

print('\nPlease Visit Again')
