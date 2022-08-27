# Basic global config
SEPARATOR   = '-='
REPEAT      = 8
# program title
print('\n\t'*1+SEPARATOR * REPEAT + ' Paragraph Information ' + SEPARATOR * REPEAT+ '\n'*1)
# this is the programe which take string and count characters in a string

# taking input
string_to_check = input('Enter paragraph to check its length \n-> ')

# now testing string have how many characters
paragraph_length    = 0
words_length        = 0
characters_length   = 0
spaces   = 0

# calculating paragpraph and letters
for character in string_to_check:
    paragraph_length += 1
    if(character.isspace()):
        spaces += 1
    else:
        characters_length += 1
        
# counting words
words_length = len(string_to_check.strip().split(" "))
        
# print out the length
print(f' length of the paragraph = {paragraph_length} \n words = {words_length} \n letters = {characters_length} \n spaces = {spaces}')