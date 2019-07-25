StudentList = []

program = True

while program:
    print('''***********************************
            1. add
            2. read
            3. update
            4. delete
            5. exit
***********************************''')
    print('\nPlease enter a number? ')
    ans = int(input())
    if ans == "":
        print('Please enter a valid number')
    

    if ans == 1:
        print('please add a name. ')
        x = input()
        StudentList.append(x)
        print('Added Sucessful. ')

        if x == "":
            print('Please add a name. ')
            
        
        continue

    if ans == 2:
        print('Here your List/s. ')
        print(StudentList)
        continue

    if ans == 3:
        print('Select valid index you want to change.')
        x = int(input())
        print(StudentList[x] + 'is selected, now enter the name. ')
        i = input()
        StudentList[x] = i
        print('Updated Sucessful. ')
        continue

    if ans == 4:
        print('Enter the name you want to delete.')
        x = input()
        StudentList.remove(x)
        print('Deleted Sucessful. ')
        continue

    if ans == 5:
        print('Areou want to exit? Y/N? ')
        x = input()

        if x == "y":
            print('Goodbye. SEE YOU SOON! ')
            running = False

        else:
            continue
    
    break
        
    
            
