######################################################
# Name:       Liéla Pressley
# File:       Practice_10.py
# Class:      CIS-1400
# Chapter:    Chapter 10
# Purpose:    creating menu, opening and writing a file
#######################################################


# Main procedure main menu option
def main():
    print('Select a Planet')
    print('1. Mercury')
    print('2. Venus')
    print('3. Earth')
    print('4. Mars')
    print('5. Exit the program')
    menu_selection = int(input('Please enter your selection:')) #prompting user for menu menu_selection

    #validating menu_selection
    while menu_selection < 1 or menu_selection > 5:
        print('Invalid selection, please try again...')
        menu_selection = int(input('Please enter your selection:')) #prompting user for menu menu_selection
    output_file = open('Planet_data.txt', 'a')

    #performing actual menu selection (calling the different modules)
    if menu_selection == 1:
     # This will overwrite the existing file, if it exists:

        # Write text to the file
        output_file.write('Average distance from the sun  57.9 million kilometers\n')
        output_file.write('Mass 3.31 × 10^23 kg \n')
        output_file.write('Surface temperature      –173 to 430 degrees Celsius \n')

        # Always close the file!
        output_file.close()
    elif menu_selection == 2:
    # This will overwrite the existing file, if it exists:

        # Write text to the file
        output_file.write('Average distance from the sun 108.2 million kilometers \n')
        output_file.write('Mass 4.87 × 10^24 kg \n')
        output_file.write('Surface temperature 472 degrees Celsius \n')

        # Always close the file!
        output_file.close()

    elif menu_selection == 3:
        # This will overwrite the existing file, if it exists:

        # Write text to the file
        output_file.write('Average distance from the sun 149.6 million kilometers \n')
        output_file.write('Mass 5.967 × 10^24 kg \n')
        output_file.write('Surface temperature    –50 to 50 degrees Celsius\n')

        # Always close the file!
        output_file.close()
    elif menu_selection ==4:
        # This will overwrite the existing file, if it exists:

        # Write text to the file
        output_file.write('Average distance from the sun 227.9 million kilometers \n')
        output_file.write('Mass 6.39 × 10^23 kg \n')
        output_file.write('Surface temperature   –140 to 20 degrees Celsius\n')

        # Always close the file!
        output_file.close()
    elif menu_selection ==5:
        print('')

main()