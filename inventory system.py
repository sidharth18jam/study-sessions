inventory = []
import listfunctions
while True:
    print("""Please type one option : 
          1.  To see the list - Type 'view'
          2.  To add items to list - Type 'add'.
          3.  To remove items from list - Type 'remove'.
          4.  To sort the list alphabetically - Type 'sort'.
          5.  To display the total number of items - Type 'total'.
          6.  To delete the list - Type 'clear'.
          7.  To insert item at a specific location - Type 'specific'.
          8.  To reverse the list - Type 'flip'.
          9.  To count the occurence of an item - Type 'count'.
          10. To search if an item exists in the inventory - Type 'search'.
          11. To end the program - Type 'done'.""")
    
    func = input().strip()
    
    if func.lower() == 'add':
        listfunctions.inputlist(inventory)
    
    elif func.lower() == 'view':
        listfunctions.printlist(inventory)
        
    elif func.lower() == 'remove':
        listfunctions.remove_from_list(inventory)

    elif func.lower() == 'sort':
        inventory.sort()
    
    elif func.lower() == 'total':
        print('There are ' + str(len(inventory)) + ' items in the List.')
    
    elif func.lower() == 'clear':
        inventory.clear()
        print ('The inventory has been cleared.')
    
    elif func.lower() == 'specific':
        try:
            insert=int(input('Input where you want to insert the new item:'))
            name=str(input('Enter the name of the item:'))
            inventory.insert(insert, name)
        except ValueError:
            print ('Invalid Input, try again.')

    elif func.lower() == 'flip':
        inventory.reverse()
    
    elif func.lower() == 'search':
        searched = str(input('Enter the item you want to search:').strip())
        if searched in inventory:
            print(f"The item you searched for is present in the list at {inventory.index(searched)} postion.")
        else:
            print ('Item not found.')

    elif func.lower() == 'count':
        count = str(input ('Enter the item whose count you want to know').strip())
        if count in inventory:
            print (f"The item you searched for is present {inventory.count(count)} number of times in the list.")
        else :
            print('Item not found in the list.')



    elif func.lower() == 'done':
        break

    else:
        print('Invalid input, please try again.')