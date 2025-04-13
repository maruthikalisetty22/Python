################# Diff data types #######################

tuple_lst = tuple(range(1,6))
print(tuple_lst)

list_lst = list(range(1,6))
print(list_lst)

set_lst = set(range(1,6))
print(set_lst)

for i in range(0, len(words)):
    print(i)
    
for i in range(0, len(inp_lst)):
    print(i)

dict={}    
for i,j in enumerate(inp_lst):
    print(i)
    dict[i] = j
print(dict)

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
comma_string = " ".join(inp_lst)
print(comma_string)

#nested list count occurance
def count_target_occurrence(nested_list, target):
    count = 0
    for sublist in nested_list:
        print(sublist)
        for num in sublist:
            print(num)
            if num == target:
                count += 1
    return count

# Example nested list
nested = [[1, 2, 3], [4, 2, 2], [5, 6, 2]]

# Target to search
target = 2

# Function call
result = count_target_occurrence(nested, target)
print(f"The number {target} appears {result} times.")

#mixed list count occurance (list and int within list)
def count_occurrence(nested_list, target):
    count = 0
    for item in nested_list:
        if isinstance(item, list):
            count += item.count(target)  # If item is a list, count target inside it
        else:
            if item == target:
                count += 1
    return count

# Example usage
nested_list = [1, 2,2, [4, 2, 2], 5, 6, 2, [2,3]]
target = 2
print(f"{target} appears {count_occurrence(nested_list, target)} times.")
