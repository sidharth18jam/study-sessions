
placeHolders = ['ADVERB','NOUN','ADJECTIVE','VERB']

madText = open('/Users/sid/Documents/Madlibs.txt')

for placeHolder in placeHolders:

    while placeHolder in madText:
        replacedText=input(f'Enter a {placeHolder}:')
        madText = madText.replace(placeHolder,replacedText,1)

print('The completed Madlib:\n')
print (madText)