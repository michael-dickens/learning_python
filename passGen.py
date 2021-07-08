import random;

upperCaseLetter = chr(random.randint(65,90))
upperCaseLetter2 = chr(random.randint(65,90))

lowerCaseLetter = chr(random.randint(97,122))
lowerCaseLetter2 = chr(random.randint(97,122))

numberChar = chr(random.randint(48,57))
numberChar2 = chr(random.randint(48,57))

specialChar =  chr(random.randint(33,64))
specialChar2 =  chr(random.randint(33,64))

unjumbledPass = upperCaseLetter + upperCaseLetter2 + lowerCaseLetter + lowerCaseLetter2 + numberChar + numberChar2 + specialChar + specialChar2
print(''.join(random.sample(unjumbledPass,len(unjumbledPass))))