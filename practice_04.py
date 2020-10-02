#######################################################
#Name:        Liela Pressley
# Class:      CIS-1400
# Assignment:  Practice 4 Fall 2020
# File:       Program_04.py
# Purpose:    prompt user for change inputs, calculate inputs into exact change, display output
#
# Concepts:
#      o) If-Then statement
#      o) Flowchart Figure 4-7, p. 130
#      o) Dim shortcut - more than one variable on a single line
#      o) Boolean operators (result in True or False)
#      o) > vs >=
#      o) == in pseudocode
#      o) !=
#
# NOTE: Modified version of Program_02_10.py - copy and then modify
#
#######################################################


# Get penny total in cents
pnny = float(input('Enter the amount of pennies you have: '))
# Get nickel total in cents
nckl = float(input('Enter the amount of nickels you have: ')*5)
# Get dime total in cents
dime = float(input('Enter the amount of dimes you have: ')*10)
# Get quarter total in cents
qrtr = float(input('Enter the amount of quarters you have: ')*25)

# Calculate the cent total
centtotal = (pnny + nckl + dime + qrtr)

# If the cent total is = 100 print ""
# If cent total > 100 print " #Wow you must have a heavy coin purse

if centtotal == 100:
    print('Awesome you have exactly a dollar!')
elif centtotal < 100:
    print('Hold up! You have less than a dollar, try again next time!')
else :
    print('Wow you must have a heavy coin purse. You have more than a dollar!')
