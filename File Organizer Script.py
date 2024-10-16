import os, shutil

print ('This program will help you organize files inside a directory based on their extension type. The original folder structure will be removed after the following program is run. ')
folderPath = input ('Enter the folder path that you want to organize:')

for folderName, subFolders, fileName in os.walk(folderPath):
    print('')