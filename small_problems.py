#Return every character in a string 3 times
def paperdoll(str):
    new_str=""
    for i in str:
        new_str += i*3
    print(new_str)
                
str = "missisipi"
paperdoll(str)


#Reverse a given string
def masteryoda(str):
    word_list = str.split()
    reverse_list = word_list[::-1]
    reverse_list = " ".join(reverse_list)
    print(reverse_list)
  
str = "Hello how are you"   
masteryoda(str)


#Give required number as ouput abs function
def abs_func(n):
    return (abs(100-n) <= 10) or (abs(200-n) <= 10)
    
output = abs_func(950)
print(output)


#Common letters between the strings
def common_letters(str1, str2):
    s1 = set(str1) 
    s2 = set(str2)
    common_letters = s1 & s2
    print(common_letters)
    
str1 = "hello"
str2= "hiddo"
common_letters(str1, str2)



#String to list conversion
def str_list_conversion(inp_str):
    str_inp = inp_str.split()
    print(str_inp)
    
inp_str = "Hello dude how are you"
str_list_conversion(inp_str)

#Splicer
def splicer(word_list):
    for word in word_list:
        if len(word) % 2 == 0:
            print("Even")
        else:
            print(word[:4])  # print first 4 letters of the current word

words = ["Hello", "Dude", "how", "are", "you"]
splicer(words)


#### Check if given number is in the range of low and high

def check_range(num, low, high):
    if num in range(low, high+1):
        print(f"Yes {num} is in the range b/w {low} & {high}")
    else:
        print(f"No {num} is not in the range b/w {low} & {high}")

check_range(5, 4, 4)


#### Return bolean

def check_range(num, low, high):
    if num in range(low, high+1):
        return True
    else:
        return False
        
output = check_range(5, 4, 6)
print(output)

# Calculate no of upper case and low case words in a given string

def up_low(s):
    upper_count = 0
    lower_count = 0
    upper_list = []
    lower_list = []

    for i in s:
        if i.isupper():
            upper_count += 1
            upper_list.append(i)
        elif i.islower():
            lower_count += 1
            lower_list.append(i)

    print(f"This is upper count: {upper_count}")
    print(f"This is lower count: {lower_count}")
    print(f"Uppercase letters: {upper_list}")
    print(f"Lowercase letters: {lower_list}")

#### Check if given number is in the range of low and high

def check_range(num, low, high):
    if num in range(low, high+1):
        print(f"Yes {num} is in the range b/w {low} & {high}")
    else:
        print(f"No {num} is not in the range b/w {low} & {high}")

check_range(5, 4, 4)


#### Return bolean

def check_range(num, low, high):
    if num in range(low, high+1):
        return True
    else:
        return False
        
output = check_range(5, 4, 6)
print(output)

## Calculate no of upper case and low case words in a given string

def up_low(s):
    upper_count = 0
    lower_count = 0
    upper_list = []
    lower_list = []

    for i in s:
        if i.isupper():
            upper_count += 1
            upper_list.append(i)
        elif i.islower():
            lower_count += 1
            lower_list.append(i)

    print(f"This is upper count: {upper_count}")
    print(f"This is lower count: {lower_count}")
    print(f"Uppercase letters: {upper_list}")
    print(f"Lowercase letters: {lower_list}")

## Example usage
s = "Hello dude How are you doing, Is everything Going good?"
up_low(s)


## Return unique number in the list

def unq_lst(num_lst):
    final_lst = list(set(num_lst))
    print(final_lst)
    
num_lst = [1,1,1,1,2,2,2,2,3,3,3,3,4,5,6,6,6]
unq_lst(num_lst)

# Multiply all number in a list

def multiply_numbers(nos):
    output = 1
    for i in nos:
        output *= i
    print(output)


nos = [1, 2, 3, 4, -5]
multiply_numbers(nos)  # Output: 120

#Check a gven string is palyndorme or not:

def palyndrome(s):
    if s.replace(" ", "") == s[::-1].replace(" ", ""):
        print(True)
    else:
        print(False)
        
s = "nurses run"
palyndrome(s)

# Example usage
s = "Hello dude How are you doing, Is everything Going good?"
up_low(s)
