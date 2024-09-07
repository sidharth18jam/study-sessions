import dictionaries
newShoppingList = dictionaries.create_dict()
purchasedList={}
while True:
    userInput = input('''Choose Actions:
                       1. Ammend Shopping List. - Type 'ammend'
                       2. Display Shopping List. - Type 'print'
                       3. Mark items as Purchased - Type 'purchase'
                       4. To end the program - Type 'end' 
                       5. To view purchased list - Type 'purchasedlist' ''').strip()
                        
    if userInput.lower() == 'end':
        break
    
    elif userInput.lower() == 'ammend':
        dictionaries.ammend(newShoppingList)
    
    elif userInput.lower() == 'print':
        dictionaries.display_dict(newShoppingList)
    
    elif userInput.lower() == 'purchase':
        while True:
            dictionaries.display_dict(newShoppingList)
            input1 = input('''Choose the item or its index that you have purchased. or type 'end' to end.''')
            
            if input1.lower() == 'end':
                break 
            
            elif input1.isdigit():
                serialNo = int(input1)
                if 1<= serialNo <=len(newShoppingList):
                    selectedKey = list(newShoppingList.keys())[serialNo-1]
                else:
                    print ('Invalid input.')
                    selectedKey = None

            else:
                if input1 in newShoppingList.keys():
                    selectedKey = input1
                else:
                    print('Key not present.')
                    selectedKey = None

            if selectedKey:
                print (f'You selected {selectedKey} to be put in purchased list.')
                if selectedKey in newShoppingList:
                    purchasedList[selectedKey] = newShoppingList.pop(selectedKey)
            print (f'The ammended dictionary is: \n{newShoppingList}')

    elif userInput.lower() == 'purchasedlist':
        print ('The purchased list is as follows:')
        dictionaries.display_dict(purchasedList)

    else :
        print('Invalid Input')


