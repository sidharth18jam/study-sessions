import sys
def collatz (number):
    if number%2 == 0:
        print (number//2)
        return (number//2)
    else :
        print(3 * number + 1)
        return int(3 * number + 1)

print ('Enter a number:')    
try:
    inumber = int(input())
except ValueError:
    print ('Invalid Input, Enter integer')
    sys.exit
onumber = collatz(inumber)
while onumber!=1:
    onumber=collatz(onumber)

