######################################################
#Name:        Liéla Pressley
# File:       Homework_05a.py
# Class:      CIS-1400
# Chapter:    Chapter 5
# Purpose:    Calculate Distance Using While Loop
#######################################################


mph = int(input('How fast is the train traveling? '))  # Initialize counter
hrs = int(input('How many hours has it traveled? '))
distance = mph*hrs
# Loop that prints a series of integers
print('Hours Distance')
hours =1
while hours <= hrs:
    distance = mph*hours
    print( hours,'    ',  distance)# Print the current value of the counter variable
    hours += 1       # Increment counter variable by the step amount



