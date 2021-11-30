#######################################################
#Name:        Liela Pressley
# Class:      CIS-1400
# Assignment:  Homework 4 Fall 2020
# File:       Homework_04.py
# Purpose:  Complete programming exercise 4-11 on page 170 (4th edition) of the text book. You program should display fractional units (not whole numbers).


#
#
#
#######################################################
minsec = float (60.00)
hrsec = float(3600.00)
daysec = float(86400.00)

#user input the amount of seconds to output minutes##
    #enter your pay rate to calculate the gross pay
#choose = input('would you like to convert your seconds today ?(y or n)')
    #if choose = "y":
sec = float(input('Enter the amount of seconds you worked to convert to minutes!: '))
convertmin= sec/minsec
converthr = sec/hrsec
convertday = sec/daysec
if sec >= minsec :
    print ('You have: ' , convertmin, 'minutes!')
    answer = input('would you like to convert to hours? (y or n)')
    if answer == 'y' :
        print ('You have: ' ,converthr, 'hours!')
        answer2 = input('would you like to convert to days? (y or n)')
        if answer2 == 'y':
            print ('You have:', convertday, 'days!')
            answer3= input('Do you still want your gross pay rate? y/n')
            if answer3 == 'y':
                grosshr = float(input('Enter your (hourly) pay rate:'))
                print ('Gross Pay:' ,'$',grosshr*converthr)
            else: print('Okay, bye!')

        else:
            answer3= input('Do you still want your gross pay rate? y/n')
            if answer3 == 'y':
                grosshr = float(input('Enter your (hourly) pay rate:'))
                print ('Gross Pay:' ,'$',grosshr*converthr)
            else: print('Okay, bye!')

    elif answer == 'n':
        answer2 = input('would you like to convert to days? (y or n)')
        if answer2 == 'y':
            print ('You have:', convertday, 'days!')
        else:
            answer3= input('Do you still want your gross pay rate? y/n')
            if answer3 == 'y':
                grosshr = float(input('Enter your (hourly) pay rate:'))
                print ('Gross Pay:' ,'$',grosshr*converthr)
    else:
        answer3= input('Do you still want your gross pay rate? y/n')
        if answer3 == 'y':
            grosshr = float(input('Enter your (hourly) pay rate:'))
            print ('Gross Pay:' ,'$',grosshr*converthr)
#user input amount of seconds for hours##
elif sec <= minsec:
    print('I am sorry you do not have enough seconds.')
    #enter your pay rate to calculate the gross pay
#user input amount of seconds for days##
elif sec >= daysec:
    print ('You have: ', convertday, 'days!')
    #enter your pay rate to calculate the gross pay
#elif choose == "n":
#print ("good-bye then")
