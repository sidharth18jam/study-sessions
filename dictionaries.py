def create_dict():
    dict = {}  # Create an empty dictionary
    while True:
        key = input("Enter key (or type 'exit' to stop): ")  # Ask for the key
        if key.lower() == 'exit':
            break  # Exit the loop if the user types 'exit'
        
        value = input(f"Enter value for {key}: ")  # Ask for the value
        dict[key] = value  # Store the key-value pair in the dictionary
        
    return dict  # Return the final dictionary

def display_dict(dict):
    total = 0
    print('Items in the dictionary:')
    for k,v in dict.items():
        print (str(v) +' ' + k)
        total = total + int (v)
    print('Total number of items:' + str(total))

def add_to_dict(dict,added_items):
    for i in added_items:
        if i in dict.keys():
            dict[i] = int(dict[i])+1
        else:
            dict[i] = 1
    return dict

def ammend(dict):
    print('''Choose one of the options:
          1. To Add keys - Type 'add'
          2. To Remove a key - Type 'remove'
          3. To Change a preexisting key - Type 'change'
          4. To Change the value for a preexisting key - Type 'changeval' ''')
    
    input1 = input().strip()
    
    if input1.lower() == 'add':
        
        input2=input('Add new Key.').strip()
        
        if input2 in dict.keys():
            
            print(f'''{input2} already exists in the dictionary with value {dict[input2]}.
                  Do you still want to add it? Type 'y' if yes, or 'n' for no. ''')
            
            input3 = input().strip()
            
            if input3 == 'y':
                
                print(f'''What do you want to do with {input2}'s current value? 
                      1. Completely change it?
                      2. Add a specific amount to it?
                      2. Decrease a specific amount from it? 
                      Choose 1,2 or 3.''')
                input4 = input().strip()
                
                if input4 == '1':
                    input5 = input(f'Enter the new value for {input2}.')
                    dict[input2] = input5
                    print (f'The new value for key {input2} is {input5}')

                elif input4 == '2':
                    try:
                        input6 = input(f'''The current key of {input2} is {dict[input2]}.
                                   How much more do you want to add?''')
                        dict[input2] = int(dict[input2]) + input6
                        print(f'The new value of {input2} is {dict[input2]}')
                    except ValueError:
                        print('Error: The value must be a number.')

                elif input4 == '3':
                    try:
                        input7 = input(f'''The current key of {input2} is {dict[input2]}.
                                   How much more do you want to subtract?''')
                        dict[input2] = int(dict[input2]) - int (input7)
                        print(f'The new value of {input2} is {dict[input2]}')
                    except ValueError:
                        print('Error: The value must be a number.')

                else:
                    print('Wrong Input.')
            
            elif input3=='n':
                print('Okay, you are not adding.')

            else:
                print('Wrong Input.')

        else:
            while True:
                key = input("Enter key (or type 'exit' to stop): ").strip()  # Ask for the key
                if key.lower() == 'exit':
                    break  # Exit the loop if the user types 'exit'
        
                value = input(f"Enter value for {key}: ")  # Ask for the value
                dict[key] = value  # Store the key-value pair in the dictionary

    elif input1.lower() == 'remove':
        input8 = input('Enter the key you want to remove').strip()
        
        if input8.lower() in dict.keys():
            arbval = dict.pop (input8)
            print (f'The {input8} key removed from the dictionary.')

        else:
            print ('Entered key not found in the Dictionary.')

    elif input1.lower() == 'change':
        print ('Keys in the Dictionary:')
        i=1
        for k in dict.items():
            print (str(i)+'. ' + k)
            i+= 1
        input9 = input('Enter the key or serial number of the key you want to change:')
        
        if input9.isdigit():
            serialNo = int(input9)
            if 1<= serialNo <=len(dict):
                selectedKey = list(dict.keys())[serialNo-1]
            else:
                print ('Invalid input.')
                selectedKey = None

        else:
            if input9 in dict.keys():
                selectedKey = input9
            else:
                print('Key not present.')
                selectedKey = None

        if selectedKey:
            print (f'You selected {selectedKey} to ammend.')
            newKey = input(f'Enter new Key for {selectedKey}')
            if selectedKey in dict:
                dict[newKey] = dict.pop(selectedKey)
        print (f'The ammended dictionary is: \n{dict}')
    
    elif input1.lower() == 'changeval':
        print('Items in the dictionary:')
        i =1
        for k,v in dict.items():
            print (f'{i}. {k} - {str(v)}')
            i+= 1
        input10 = input('Enter the key or serial number of the key whose value you want to change:')

        if input10.isdigit():
            serialNo = int(input9)
            if 1<= serialNo <=len(dict):
                selectedKey1 = list(dict.keys())[serialNo-1]
            else:
                print ('Invalid input.')
                selectedKey1 = None

        else:
            if input10 in dict.keys():
                selectedKey1 = input9
            else:
                print('Key not present.')
                selectedKey1 = None

        if selectedKey1:
            print (f"You selected {selectedKey1}'s  value to ammend.")
            newVal = input(f'Enter new value for {selectedKey1}')
            dict[selectedKey1] = newVal
        print (f'The ammended dictionary is: \n{dict}')

    else:
        print('Invalid Input.')




# Example usage
my_dict = create_dict()
display_dict(my_dict)
dragon_loot=['gold coin', 'dagger', 'gold coin', 'ruby', 'gold coin']
inv = add_to_dict(my_dict,dragon_loot)
display_dict(inv)
