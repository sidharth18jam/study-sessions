def wordCount(stringInput):
    words = stringInput.split()
    return len(words)
        
def charCount (stringInput):
    return len(stringInput)

def lineCount (stringInput):
    return stringInput.count('\n') + 1

while True:
    
    print ('This program will help you in counting the number of words, lines and characters in a text file.')
    filePath = input ('Please Enter the file path : ')

    try:
        with open (filePath, 'r') as file:
            data = file.read()

    except FileNotFoundError:
        userInput = input("The file on the given path does not exist. Do you want to try again? If yes, input 'y' and press enter, else press enter to exit.")
        if userInput.lower() != 'y':
            break
        else:
            continue
    
    except Exception:
        userInput = input(r'''The file on the given path could not be opened. 
                          Check if you have permissions or if the file is corrupted. 
                          To try again, input 'y' and press enter, else press enter to exit.''')
        if userInput.lower() != 'y':
            break
        else:
            continue
    else:
        print(f'The input file has {wordCount(data)} words, {charCount(data)} characters, {lineCount(data)} lines.')
        userInput = input("Do you want to try again? If yes, input 'y' and press enter, else press enter to quit.")
        if userInput.lower() != 'y':
            break
        else:
            continue
