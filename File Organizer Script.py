import os, shutil

def get_unique_file_path(directory, file_name):
    base_name, extension = os.path.splitext(file_name)
    counter = 1
    new_file_name = file_name
    new_file_path = os.path.join(directory, new_file_name)
    
    # Keep modifying the file name until a unique one is found
    while os.path.exists(new_file_path):
        new_file_name = f"{base_name}_{counter}{extension}"
        new_file_path = os.path.join(directory, new_file_name)
        counter += 1
    
    return new_file_path

print ('This program will help you organize files inside a directory based on their extension type. The original folder structure will be removed after the following program is run. ')
folderPath = input ('Enter the folder path that you want to organize:')

for folderName, subFolders, fileNames in os.walk(folderPath,topdown= False):
    
    for fileName in fileNames:
       
        sourceFilePath = os.path.join (folderName,fileName)
        fileExtension = os.path.splitext(fileName)[1][1:]            
        extensionFolder = os.path.join(folderPath, fileExtension)
        if not os.path.exists(extensionFolder):
            os.makedirs(extensionFolder)
        copiedFilePath = get_unique_file_path(extensionFolder,fileName)
        shutil.copy(sourceFilePath,copiedFilePath)
        # shutil.move(fileName,copiedFilePath)
    
    #if folderName != folderPath and not os.listdir (folderName):
        #os.rmdir(folderName)

print ('File Organizing Completed!')
    