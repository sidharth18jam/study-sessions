import dictionaries
newShoppingList = dictionaries.create_dict()
while True:
    userInput = input('''Choose Actions:
                       1. Ammend Shopping List. - Type 'ammend'
                       2. Display Shopping List. - Type 'print'
                       3. Mark items as Purchased - Type 'purchase'
                       4. to end the program - Type 'end' ''').strip()
    if userInput.lower() == 'end':
        break
    
    elif userInput.lower() == 'ammend':
        dictionaries.ammend(newShoppingList)
    
    elif userInput.lower() == 'print':
        dictionaries.display_dict(newShoppingList)
    
    elif userInput.lower() == 'purchase':
        dictionaries.display_dict(newShoppingList)
        print ('Typ')

