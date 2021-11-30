# 1.enter 20 names in array
#bubble sort names array and print (make sure to add 'names[counter]+' before the print statmenet)
#Binary searchunlimited times ( use a if statement? find code for pressing enter)
    #if name not in list then print or display nothing
#print amount of times it looped...print[counter?]
#stop search loop by pressing enter


def main():
    name_list=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
    names=['']*20
    #might need variable for the

    print('Please enter 20 names. (Press Enter to Begin)')

    for counter in range(0,len(names)): #continues for each element in the array
        names[counter]= input(name_list[counter]+'):') #stores input in the names array as a string

    #bubble sort names to make alphabetical
    for i in range(0,len(names)-1):
        #print(names)#remove once double check it workes
        for j in range (0,len(names)-1-i):
            if names[j] > names[j+1]:
                names[j], names[j+1]= names[j+1], names[j]

    name_search=binary_search(names) #calls binary search
   # print(name_search)

def binary_search(search_names):
    #start binary search algorithm
    first=0 #initializing the variables | first element
    last=len(search_names)-1  #last element
    position=-1 #position of element
    found= False
    iterations =0 #amount of iterations until item found
    name_search= input('Enter the name you wish to search: <or ENTER to exit>')
    if name_search == '': #press enter to exit the search loop
            print('')
    else:
        while not found and first<=last: #define/calculate mid point if it is not found in first iteration
            iterations +=1 #adds/keeps track of iterations
            middle=(first+last)//2 #
            if search_names[middle] == name_search: #is the midpoint of array equal to userinput"name_search"
                found = True
                position= middle
                print('Name found: ', name_search) #if true then print name found and the name they entered
            elif search_names[middle] > name_search:
                last = middle-1 #else if the value is in lower half
            else:
                first=middle+1 #else if value in upper half
        if name_search != search_names[middle]: #if name isnt found in the array then print name not found
            print('Name not found')
        print('Position:', position) # prints position of elements
        print('Array lookups: ', iterations) #print amount of iterations of array lookups




main()
