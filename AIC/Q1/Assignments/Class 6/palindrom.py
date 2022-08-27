# Basic global config
SEPARATOR   = '-='
REPEAT      = 8

# program title
print('\n\t'*1+SEPARATOR * REPEAT + ' Test Palindrome ' + SEPARATOR * REPEAT+ '\n'*1)

# take input
string          = input('Enter Palindromic string to test either it is palindrome or not \n-> ')
string_count    = string.__len__()

# check wether number is odd or not
if (string_count%2) == 0:
    print('Not Palindrome')
    exit()

i = 0
is_palindrom = False
for asc in string:
    if (string_count + 1) / 2 == i and string[:string_count-1]:
        is_palindrom = True
    i += 1
        
if is_palindrom:
    print('Palindrome')
else:
    print('Not Palindrome')