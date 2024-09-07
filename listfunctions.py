def inputlist(ilist):
    while True:
        value = input("Enter a Value to add to the list (or type 'done' when finished):").strip()
        if value.lower() == 'done':
            break
        elif value.lower() in ilist:
            check = input ('The input value already exists in the list. do you still want to add: Type (y) for yes and (n) for no.')
            if check == 'y':
                ilist.append(value)
                print ('Item added.')
            elif check == 'n':
                print ('Item not added')
                continue
            else:
                print ('Invalid input.')
    return ilist

def printlist(plist):
    print ("The List is as follows:")
    for i in range (len(plist)):
            print (str(i+1) + '. ' + plist[i])

def list_to_str(ltslist):
    new_string=''
    for i in range (len(ltslist)):
        if i != len(ltslist) -1:
            new_string = new_string + str(ltslist[i]) + ', '
        else:
            new_string = new_string + 'and '+ str(ltslist[i]) + '.'
    return new_string



def remove_from_list(rfllist):
    if not rfllist:
        print('The list is empty')
        return
    
    printlist(rfllist)
    value = input('Choose the item name or its serial number to remove it: ').strip()
    # First, check if it's a number (for serial number)
    try:
        index = int(value) - 1  # Convert to integer and adjust for zero-based indexing
        if 0 <= index < len(rfllist):  # Check if the index is valid
            removed_item = rfllist.pop(index)  # Remove by index
            print(f"Item at position {index + 1} ('{removed_item}') has been removed.")
        else:
            print("Invalid serial number.")

    except ValueError:
        # If it's not a number, treat it as an item name
        for item in rfllist:
            if item.lower() == value.lower():  # Case-insensitive removal
                rfllist.remove(item)
                print(f"Item '{value}' removed.")
                break
        else:
            print(f"Item '{value}' not found in the list.")

def deduplication(dlist):
    unique_list=[]
    for item in dlist:
        if item not in unique_list:
            unique_list.append(item)     
    return unique_list
            
