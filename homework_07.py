#######################################################
#Name:        Liela Pressley
# Class:      CIS-1400
# Assignment:  Homework 7 Fall 2020
# File:       Homework_07.py
# Purpose:    Calculating Speed Limit with User input validation
#######################################################


#enter a speed limit
#using that speedllimit as a variable then do a while loop using the speedlimitchart
#under the while loop restricts print the fine.
#have to set another while loop for speed limit entry restrictions (set a function)



def main():
    speedlmt = speed_limit() #assigning variable to function for speed limit
    user_speed = int(input('Please enter your speed:   ')) #assigning variable to function for speed limit
    speeding_fine = user_speed - speedlmt       #calculating the fine

    if user_speed > 200 or user_speed < speedlmt : #if the user's speed is over 200 or under the speed limit( had to incorporate this into the main function since i was running into bugs with its original place
        print('ERROR- Invalid speed entered...')
        user_speed = (input('Please enter your speed:   '))
    else:
        if speeding_fine <= 10 and speeding_fine >= 1: #after the calculations the different fines are assigned and printed
            print('Exceeded speeding limit by 1-10 MPH. $50 fine.')

        elif speeding_fine >= 11 and speeding_fine <=15:
            print('Exceeded speeding limit by 11-15 MPH. $75 fine.')

        elif speeding_fine >= 16 and speeding_fine <=20:
            print('Exceeded speeding limit by 16-20 MPH. $150 fine.')

        elif speeding_fine >=21:
            print('Exceeded speeding limit by 21+ MPH. $300 fine.')


def speed_limit():
    limit = int(input('Please enter the speed limit: ' ))

    while limit < 20 or limit >70: #restricts user input of speed limit to 20-70 mph
        print('ERROR-Please enter speed limit between 20-70 mph.')
        limit = int(input('Please enter the speed limit: ' ))
    return limit



def vehicle_speed():
    actual_speed = int(input('Please enter your speed:   '))

    while actual_speed > 200: #resticting speed enter if greater than 200 then returning it to variable
        print('ERROR- Invalid speed entered...')
        actual_speed = (input('Please enter your speed:   '))
    return actual_speed

main()
