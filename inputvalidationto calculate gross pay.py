######################################################
# Name:       Liéla Pressley
# File:       Practice_07.py
# Class:      CIS-1400
# Chapter:    Chapter 7, pp. 272-273 in 4th edition
#             Chapter 7, pp. 270-271 in 3rd edition
# Purpose:    Input Validation to calculate gross pay
#
# Concepts:
#      o) Detect data type mismatch errors
#######################################################

def main():
    hours= get_hours()
    print('You have:', hours, 'hours')  #returned validated hour

    pay_rate= get_rate()
    print('You have:', pay_rate )

    gross_pay = pay_rate * hours

    round(gross_pay, 2)

    print('Your gross pay is:  $', gross_pay)




def get_hours():
    hrs= float(input('Please enter the number of hours worked:  '))
    while hrs < 0 or hrs > 40 :
        print('ERROR- Invalid number of hours...')
        hrs= float(input('Please enter the number of hours worked: '))
    return hrs

def get_rate():
    rate= float(input('Please enter hourly pay rate:  '))
    while rate <0 or rate > 40:
        print('ERROR- Invalid hourly pay rate...')
        rate= float(input('Please enter the number of hours worked: '))
    return rate

main()
