guestlist = []
import listfunctions
while True:
    print("""Please type one option : 
          1. To see the list - Type 'view'
          2. To add guests to list - Type 'add'.
          3. To remove guests from list - Type 'remove'.
          4. To sort the list alphabetically - Type 'sort'.
          5. To display the total number of guests invited - Type 'total'.
          6. To reverse the list - Type 'clear'.
          7. To insert guest at a specific location - Type 'specific'.
          8. To reverse the list - Type 'flip'.
          9. To end the program - Type 'done'.""")
    func = input.strip()
    
    if func.lower() == 'add':
        listfunctions.inputlist(guestlist)
    
    elif func.lower() == 'view':
        listfunctions.printlist(guestlist)
        
    elif func.lower() == 'remove':
        listfunctions.remove_from_list(guestlist)

    elif func.lower() == 'sort':
        guestlist.sort()
    
    elif func.lower() == 'total':
        print('There are ' + str(len(guestlist)) + ' guests in the List.')
    
    elif func.lower() == 'clear':
        guestlist.clear()
        print ('The guest list has been cleared.')
    
    elif func.lower() == 'specific':
        try:
            insert=int(input('Input where you want to insert the new guest:'))
            name=str(input('Enter the name of the guest:'))
            guestlist.insert(insert, name)
        except ValueError:
            print ('Invalid Input, try again.')

    elif func.lower() == 'flip':
        guestlist.reverse()

    elif func.lower() == 'done':
        break

    else:
        print('Invalid input, please try again.')