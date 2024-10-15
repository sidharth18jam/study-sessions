import re
def strongPasswordChecker(password):
    strongPassword = re.compile(r'''
                                ^
                                (?=.*[a-z])
                                (?=.*[A-Z])
                                (?=.*\d)
                                (?=.*[!@#$%^&*()_+=-\|}]{"':;?/>.<,}])
                                .{8,}
                                $
                                ''',re.VERBOSE)
    return bool(strongPassword.match(password))


userInput = input('Enter Password to be checked for strength')

if strongPasswordChecker == True:
    print('Your password is strong.')
else:
    print('Password not strong.')

