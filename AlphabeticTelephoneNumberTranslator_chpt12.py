######################################################
# Name:       Liéla Pressley
# File:       Practice_12.py
# Class:      CIS-1400
# Chapter:    Chapter 12
# Purpose:    Alphabetic Telephone Number Translator
#######################################################
#A, B, and C = 2
#D, E, and F = 3
#G, H, and I = 4
#J, K, and L = 5
#M, N, and O = 6
#P, Q, R, and S = 7
#T, U, and V = 8
#W, X, Y, and Z = 9
def main():
    continue_option=('') #intializing continue option
    continue_option= input(' Would you like to start phone number translation (Y or N)?  ')
    while continue_option == 'y' or continue_option == 'Y':
        # Prompt the user for some text:
        text = input('Enter the phone # you wish to translate: ')
        newstring = ''
        # Loop through the text one character at a time
        for counter in range(0, len(text)):
            char = text[counter]  # Get the single character

            # If it's a digit say so
            if char == 'A' or char == 'B' or char == 'C':
                newstring = newstring +'2'
            elif char=='D' or char=='E' or char=='F':
                newstring = newstring+'3'
            elif char == 'G' or char== 'H'or char=='I':
                newstring = newstring + '4'
            elif char == 'J' or char== 'K'or char=='L':
                newstring = newstring + '5'
            elif char == 'M' or char== 'N'or char=='O':
                newstring = newstring + '6'
            elif char == 'P' or char== 'Q'or char=='R' or char=='S':
                newstring = newstring + '7'
            elif char == 'T' or char== 'U'or char=='V':
                newstring = newstring + '8'
            elif char == 'W' or char== 'X'or char=='Y':
                newstring = newstring + '9'
            else:
                newstring= newstring+char
        print ('Translated Number: ',newstring)
        print('')
        continue_option= input('Would you like to translate another number? (y or n)  ') #continues loop until anything !=y or Y is pressed

main()
