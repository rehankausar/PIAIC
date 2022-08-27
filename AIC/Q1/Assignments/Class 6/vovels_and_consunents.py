# Basic global config
SEPARATOR   = '-='
REPEAT      = 8

# program title
print('\n\t'*1+SEPARATOR * REPEAT + ' Vowels & Consonants ' + SEPARATOR * REPEAT+ '\n'*1)

# list of the vowels
vowoles = ['a','e','i','o','u']

# take paragraph from the user
paragrah = input('please enter the paragraph in which you want to check vowels and cosunents \n-> ')

result = {
    "vowels":0,
    "consonants":0
}

# count the result
for char in paragrah:
    if char in vowoles:
        result['vowels'] += 1
    else:
        result['consonants'] += 1

# printing the result
print('->proccessing...\n'*1)
print(f' vowels = {result["vowels"]}, consonants = {result["consonants"]} are in given paragraph', end='')
