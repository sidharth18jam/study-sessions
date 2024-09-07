shopping_list=[]
import listfunctions
while True:
    print("""Please type one option : 
          1. To see the list - Type 'view'
          2. To add items to cart - Type 'add'.
          3. To delete items from cart - Type 'delete'.
          4. To sort the cart - Type 'sort'.
          5. To display the total number of items in the cart - Type 'total'.
          6. To clear the cart - Type 'clear'.
          7. To end the program - Type 'done'.""")
    
    func=input().strip()
    
    if func.lower() == 'add':
        listfunctions.inputlist(shopping_list)
    
    elif func.lower() == 'view':
        listfunctions.printlist(shopping_list)
        
    elif func.lower() == 'delete':
        listfunctions.remove_from_list(shopping_list)

    elif func.lower() == 'sort':
        shopping_list.sort()
    
    elif func.lower() == 'total':
        print('There are ' + str(len(shopping_list)) + ' items in the List.')
    
    elif func.lower() == 'clear':
        shopping_list.clear()
        print ('The shopping cart has been cleared.')
    
    elif func.lower() == 'done':
        break

    else:
        print('Invalid input, please try again.')

