import os, re

folderInput = input ('Enter the path of the folder you want to search:')
regexInput = input ('Enter the regex you want to search:')

pattern = re.compile(regexInput)

for fileName in os.listdir(folderInput):
    if fileName.endswith('.txt'):
        filePath = os.path.join(folderInput,fileName)

    with open(filePath, 'r') as file:
        text = file.read()
        matches = pattern.findall(text)

    if matches:
        print(f'The matches found in {fileName} are:')
        for i in matches:
            print (i)
    else:
        print(f'No matches found in file {fileName}')
