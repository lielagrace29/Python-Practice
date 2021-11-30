def main():
    months= ['January', 'Febuary', 'March', 'April','May', 'June', 'July','August','September','October','November','December'] #arrays for months
    rainfall= [0]*12 #arrays for rainfall input
    total_rain=0 #initializing at 0

    for counter in range (0,len(rainfall)):
        rainfall[counter]= int(input('Enter rainfall for '+ months[counter]+ ':  '))  #user inpu tchanges month after each iteration of lopp
        #stores the input in the rainfall array as an integer
        total_rain += rainfall[counter] #goes to next element in array or creates the sum of all the different rain elements

    sortedrain= bubblesort(rainfall) #sorting time (calling the function bubblesort)
    print('- - - - - - - ')
    print('Total rainfall recorded is: ', total_rain)
    print('Highest rainfall recorded is:', sortedrain[11]) #presents the highest element which is the last element
    print('Lowest rainfall recorded is:', sortedrain[0]) #presents the lowest elements
    print('Average rainfall is:',(sum(sortedrain)/12)) #finds average might have to make it variable then print with trext






def bubblesort(organized_rain): #for loops in order to sort the rain number in numerical order from least to greatest
    for i in range(0,len(organized_rain)-1):
       # print(organized_rain)
        for j in range(0,len(organized_rain)-1-i):
            if organized_rain[j] > organized_rain[j+1]:
                organized_rain[j],organized_rain[j+1] = organized_rain[j+1], organized_rain[j]
    return organized_rain


main()
