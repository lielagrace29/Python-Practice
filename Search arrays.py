######################################################
# Name:       Liéla Pressley
# File:       Homework_08.py
# Class:      CIS-1400
# Chapter:    Chapter 8, pp. 301-302 in 4th edition
# Purpose:    Search arrays
#
#
#######################################################
#create constant of 10 (only allow to repeat 10 ELEMENTS IN EACH RAY)
COUNT = 10
#pritn the of all 10 entries then ask for search
#search is partial name- prints that specific element in every list

found = False  # Initialize to false


def main():
    #create three arrays : name[], phone#[], email[]
    name= [''] *COUNT
    phone=['']*COUNT
    email=['']*COUNT
   # found = False  # Initialize to false

    #get the directory data on loop until 10th entry
    for counter in range (0,COUNT):
        #get name, print information and ask for next STRCOUNTER+1= CHANGESS '# BASED OFF THE LOOP OF ENTRY'
        #NAME
        name[counter] = input('Enter name #'+ str(counter+1)+ ':  ')
        #Phone
        phone[counter] = input('Enter phone #'+ str(counter+1)+'(xxx-xxx-xxxx):  ')
        #email
        email[counter] = input('Enter email #' + str(counter+1)+':  ')
        print('')
        counter +=1
# Get the string to search for:
    search_value = str(input('Enter a name to search for : '))
    while search_value !="" :
        counter=0
        while counter < len(name):
            # If found set found to True, else increment counter:
            # print ('Counter is :', counter)
            if search_value in name[counter]:
                print(' Name             Phone#            Email')
                print('------            --------           --------')
                print(name[counter],    phone[counter],    email[counter])
            counter += 1

        search_value=str(input('Enter search value:'))


main()
