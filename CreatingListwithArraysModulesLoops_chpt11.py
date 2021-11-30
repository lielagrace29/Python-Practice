######################################################
# Name:       Liéla Pressley
# File:       Homework_11.py
# Class:      CIS-1400
# Chapter:    Chapter 11
# Purpose:    Creating List with Menu, adding, removal etc using arrays and modules and loops
#######################################################
# Main procedure main menu option
def main():
    menu_selection = ('') #initialize in for while loop to continue procedure
    shopping_list=[]

    while menu_selection !='Q':
        print('')
        print('How would you like to edit your shopping list?  ')
        print('A - Add Option')
        print('R - Remove option')
        print('S - Sort List')
        print('P - Print List')
        print('Q - Quit')
        menu_selection = str(input('Type a Letter to Select: ')) #prompting user for menu menu_selection

        #validating menu_selection
        while menu_selection != 'A' and menu_selection != 'a' and menu_selection !='R' and menu_selection !='r' and menu_selection !='S' and menu_selection !='s' and menu_selection !='p' and menu_selection !='P' and menu_selection !='Q' and menu_selection !='q'  :
            print('Invalid selection, please try again...')
            print('')
            menu_selection = input('Please enter your selection:') #prompting user for menu_selection

        #menu options
        if menu_selection == 'A' or  menu_selection =='a': #adding element
            new_item = input('What would you like to add to your list?  ')
            shopping_list.append(new_item)
            print('')
            print('This is the list after adding:')
            for counter in range (0,len(shopping_list)):
                print('Item #'+str(counter+1)+ ':' +shopping_list[counter])

        if menu_selection == 'R'  or menu_selection == 'r': #deleting element
            delete_item = int(input('What item would you like to delete?'))
            del shopping_list[delete_item-1]
            print('')
            print('This is the list after deletion:  ')
            for counter in range (0,len(shopping_list)):
                print('Item #'+str(counter+1)+ ':' +shopping_list[counter])

        elif menu_selection == 'S' or menu_selection == 's': #sorting array
            for i in range (0, len(shopping_list) - 1):
               # print(shopping_list)
                for j in range (0, len(shopping_list) - 1 - i):
                     if shopping_list [j] > shopping_list [j+1]:
                        shopping_list [j], shopping_list[j+1] = shopping_list[j+1], shopping_list [j]
            print('')
            print('Here is your sorted list')
            for counter in range (0,len(shopping_list)):
                print('Item #'+str(counter+1)+ ':' +shopping_list[counter])

        elif menu_selection == 'P' or menu_selection =='p': #print list
            print('')
            print('Your list:')
            for counter in range (0,len(shopping_list)):
                print('Item #'+str(counter+1)+ ':' +shopping_list[counter])

        elif menu_selection == 'Q' or menu_selection =='q': #quit program
            menu_selection='Q'


main()