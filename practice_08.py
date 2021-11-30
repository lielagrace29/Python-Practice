######################################################
# Name:       Liéla Pressley
# File:       practice_08.py
# Class:      CIS-1400
# Chapter:    Chapter 7
# Purpose:      pracitice arrays by creating lottery generator
# Concepts:
#######################################################
import random


 #named constants:
NUMBER_OF_MACHINES = 7 #number of lotto MACHINES
NUMBER_OF_BALLS = 10 #number of balls in each MACHINES

 #loop that randomly generates a number for each of the 7 arrarys

def main():
    lottery_machines= ['0']*NUMBER_OF_MACHINES #reate arrays of size NUMBER_BALLS and NUMBER_OF_MACHINES
    #for ball in (random_ball):
     #   ball = random.randint (0, NUMBER_OF_BALLS)

      #  print('The lottery numbers are',random_ball)
    #create a loop to have random numbers show multiple times?
    i = 0
    while i < len(lottery_machines):
        lottery_machines[i]=random.randint (0, NUMBER_OF_BALLS)#do a random number from 1-10
        i = i+1

    x=0
    for x in range(len(lottery_machines)):
        print('Lottery numbers are:  ', str(lottery_machines(x+1))
     #printing the list using loop
main()