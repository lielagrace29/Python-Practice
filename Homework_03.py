######################################################
# Name:       Liéla Pressley
# File:       Homework_03.py
# Class:      CIS-1400
# Chapter:    Chapter 3, (version of program 3-5 on pp. 98-99 in 4th edition)
# Purpose:    Parameters,Modules to calculate BMI
#

#######################################################

# BMI = lbs/in^2   *703
# Main procedure

def main():

    print('\n**  Enter the following information for your BMI  **\n')  # Display author's name

    # Prompt user for a lbs, feet converted to inches and inches:
    ('Enter a number and I will display')
    lbs = int(input('Pounds: '))
    ft_inch = int(input('Feet: '))*12  #convert feet to inches
    inches = int(input('Inches : ') ) # extra inches
    total_inch = ft_inch + inches # total inches

    display_bmi(total_inch,lbs)  # Display BMI


# Calculates BMI and displays it
def display_bmi(total_inches,pounds):
    hgt = total_inches*total_inches #squaring inches
    bmi = (pounds/hgt)*703
    print ('Your BMI is:  ', bmi)  #output bmi


# Call the main procedure
main()
