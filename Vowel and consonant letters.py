#VOWEL AND CONSONANT LETTERS

"""Writing a code that prints out the number of vowels and consonants in a sentence or statement."""

statement = input('Write a statement: ')

new_statement = ''

#remove the space in the statement and get statement without space 

for char in statement:
    if char == ' ':
        continue
    else:
        new_statement += char #new_statement = new_statement + char

#get a vowel list 
        
vowels = ['a', 'e', 'i', 'o', 'u']

#set initializer

vowel_count = 0
consonant_count  = 0

#iterate through new_statement and check if the characters are in vowel_list or not

for char in new_statement:
    if char not in vowels:
        consonant_count += 1
    else:
        vowel_count += 1

print(f'The total number of vowels in the statement  is {vowel_count}')    
print(f'The total number of consonants in the statement  is {consonant_count}')            
    
