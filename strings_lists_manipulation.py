################# INPUTS #######################
words = "hello dude how are you ?"
inp_lst = ["hello", "dude", "how", "are", "you?"]

# Printing characters in the input list
for words in inp_lst:
    for char in words:
        print(char)

# converting the string into a list
out = words.split()
print(out)

#Converting the list into string
out2 = " ".join(inp_lst)
print(out2)
 
# Using for loop iterate and get index as per the length of the words from string  
for i in range(len(words)):
    print(i)
  
# Using for loop get the index and word as tuple from string          
for i,j in enumerate(words):
    print(i,j)
  
# Using for loop get the index and word as tuple from list   
for i,j in enumerate(inp_lst):
     print(i,j) 

# Reverse the list and string
print(words[::-1])
print(inp_lst[::-1])

# Lower case, upper case, capiatl case
lower_words = [word.lower() for word in inp_lst]
print(lower_words)

upper_words = [words.upper() for words in inp_lst]
print(upper_words)

capital_words = [words.capitalize() for words in inp_lst]
print(capital_words)

# Count words and character

word_count = len(inp_lst)
print(word_count)

word_count = len(words)
print(word_count)


# Find words with specific criteria

word_spec = [word for word in words if word.startswith('h')]
print(word_spec)

# Iterating thru list and finding the required word count
count = 0
start_words = []
for word in inp_lst:
    if word.startswith('h'):
        count+= 1
        start_words.append(word)
print(f"{count} is the count and {start_words} is the word")

# Iterating thru string and finding the required word count
count = 0
start_words = []
for word in words:
    if word.startswith('h'):
        count+= 1
        start_words.append(word)
print(f"{count} is the count and {start_words} is the word")

# Function to find the occurancy of given target words
def occur_func(inp_lst, target_word):
    count = 0
    found_word = ""
    for word in inp_lst:
        if word == target_word:
            count+= 1
            found_word = word
            
    print(f"This is the {target_word} and this is the target found {found_word}")
    print(count)

target_word = "hello" 
occur_func(inp_lst, target_word)


# Length of each word using map :
word_length =list(map(len, inp_lst))
print(word_length)

## Filter the words using filter :
word_filter = list(filter(lambda x: len(x) > 3, inp_lst))
print(word_filter)

# ##Convert list of strings to single string with comma separator
# comma_string = " ".join(inp_lst)
# print(comma_string)
