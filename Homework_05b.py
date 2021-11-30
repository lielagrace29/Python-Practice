######################################################
# Name:       Liéla Pressley
# File:       Homework_05b.py
# Class:      CIS-1400
# Chapter:    Chapter 5
# Purpose:    For Loop to Find Factorial
#######################################################

total= 1
num = int(input('enter a number for factorial: ')) #user input 
print (num, '! =', end = " ") #number!=   
for x in range (1, num+1): #for loop  (add 1 to user input so it displays from 1- that specific number)
    print (x, 'x', end = " ", ) #prints equation
    total= total*x #the multiplicaiton part

print('=', total) #prints answer




