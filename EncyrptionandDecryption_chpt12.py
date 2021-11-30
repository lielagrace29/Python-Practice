######################################################
# Name:       Liéla Pressley
# File:       Homework_12.py
# Class:      CIS-1400
# Chapter:    Chapter 12
# Purpose:    Encryption and Decryption
#######################################################


def main():
    original_abc='abcdefghijklmnopqrstuvwxyz'
    print('1.) Encrypt my Message')
    print('2.) Decrypt my Message')
    print('3.) Exit')
    menu_selection = str(input('Type 1 or 2 or 3 to Select: ')) #prompting user for menu menu_selection
    while menu_selection != '3':
        if menu_selection == '1':
            print('')
            print('Encryption')
            key= int(input('First, what is your key?  ')) #input for key to add or subtract
            new_abc = original_abc[key:26] + original_abc[0:key] #key using input
            translationtable = str.maketrans(original_abc,new_abc) #maps strings for decryption
            print('')
            text= input('Enter the text you would like to encrypt: ')
            text= text.lower()
            print('Encrypted text:  '+ text.translate(translationtable)) #prints encryption
            print('')
            print('1.) Encrypt my Message')
            print('2.) Decrypt my Message')
            print('3.) Exit')
            menu_selection = str(input('Type 1 or 2 or 3 to Select: ')) #prompting user for menu menu_selection
        elif menu_selection == '2': #decryption
            print('')
            print('Decryption')
            key= int(input('First,what is your key?  ')) #input for key to add or subtract
            new_abc = original_abc[key:26] + original_abc[0:key] #key using input
            translationtable = str.maketrans(new_abc,original_abc) #maps the strings for decryption
            print('')
            text= input('Enter the text you would like to decrypt: ')
            text= text.lower()
            print('Encrypted text:  '+ text.translate(translationtable)) #prints decryption
            print('')
            print('1.) Encrypt my Message')
            print('2.) Decrypt my Message')
            print('3.) Exit')
            menu_selection = str(input('Type 1 or 2 or 3 to Select: ')) #prompting user for menu menu_selection
main()
