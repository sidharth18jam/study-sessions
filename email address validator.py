import re

inputText = input('Enter the text you want to search for Email Addresses:')

EmailAddressRegex = re.compile(r'^[a-zA-Z0-9._-%$+-]+@[a-zA-Z0-9._-%$+-]+\.[a-zA-Z0-9._%$+-]{2,}$')

emails = re.findall(EmailAddressRegex,inputText)

print(emails)