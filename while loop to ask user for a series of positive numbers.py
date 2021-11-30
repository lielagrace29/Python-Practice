######################################################
# Name:      Liela Pressley
# File:       Practice_05a.py
# Class:      CIS-1400
# Chapter:    Chapter 5
# Purpose:    You must use a while loop to ask user for a series of positive numbers, stop at input of 0 to give sum of given numbers
#
#######################################################

total=0
#positiveinpt = 0 # input number is the positive integer
positiveinpt = 1#
# Repeatedly ask the user to enter a positive number
# until 0 is entered.
while positiveinpt >= 1:
    # Prompt the user to enter the positive number.
    total= int(input( 'Please enter a positive number:    '))# input number is the positive integer
    positiveinpt += 1
    if total == 0:
        print()
        print('Here is your sum: ', total)
        break


