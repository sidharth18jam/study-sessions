import re
inputText = input('Enter the text you want to search for urls:')

urlParser=re.compile(r'^(https?|ftp|file|mailto):\/\/([\S]+)(:[\d]+)?(\/[\S]+)*(\?[\S]+)*(#[\S]+)*')

urls = re.findall(urlParser,inputText)
print (urls)