def commaCode(list):
    cCode = ''
    for i in range(len(list)-1):
        cCode = cCode +  list[i] + ', '
    cCode = cCode + 'and ' + list[len(list)-1]
    return cCode

l1 = ['cat', 'bat', 'rat', 'elephant','apples', 'bananas', 'tofu', 'cats']
cCode = commaCode(l1)
print(cCode)