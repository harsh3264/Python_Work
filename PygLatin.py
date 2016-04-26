# PygLatin word
# Pyg latin means the first letter of the world will come at last of the word and it will be merged with suffix ay
original = raw_input('Enter a word:') # Ask user for a word raw_input for input from user
word = original.lower() # Convert the word into lower case to ignore the case sensetivity isssue
pyg = 'ay' # Suffix ay is used 
first = word[0] # Take the first letter of the word
new_word = word[1:len(word)] # From second letter to the last letter of the word
new_word = new_word + first + pyg # Concate all the three types in one vairable
if len(original) > 0 and original.isalpha(): # Use if condition to check if the input is empty with length and .isalpha() to check if input is only alpbhabets 
    print new_word
else:                # We can also use elif for the else if condition
    print 'empty'