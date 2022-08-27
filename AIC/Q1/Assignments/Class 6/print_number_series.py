# Basic global config
SEPARATOR   = '-='
REPEAT      = 8

# program title
print('\n\t'*1+SEPARATOR * REPEAT + ' Print Number Of Series ' + SEPARATOR * REPEAT+ '\n'*1)

# validate always come number only
def takeNumber():
    try:
        number = int(input('Enter Number Between 1 to 9 : \n-> '))
    except ValueError as e:
        print('\n\t'*1+SEPARATOR * REPEAT + ' Enter a valid number ' + SEPARATOR * REPEAT+ '\n'*1)
        return takeNumber()

    if number <= 0 or number >= 9:
        print('Not a Valid number')
        return takeNumber()
    return number

# take input
count = takeNumber()

# triangle in Ascending format
for row in range(count, 0, -1):
    print('# ', end =" ")
    for column in range(row):
        print(f' {column+1}', end= " ")
    print('\n')
    

# triangle in Desending format
for row in range(count, 0, -1):
    print('# ', end =" ")
    column = row
    while column > 0:
        print(f' {column}', end= " ")
        column -= 1
    print('\n')