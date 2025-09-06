################################################## PYTHON CODING INTERVIEW QUESTIONS ###########################################


### 1. Reverse a string.
##Approach -1 
def reverse_string(str):
    return str[::-1]
    
a = reverse_string("hello")
print(a)


##Approach-2
def reverse_string(str):
    emp_str = ""
    for i in str:
        emp_str= i + emp_str
    return emp_str

a = reverse_string("hello")
print(a)


##Approach 3
str = "hello"
print("".join(reversed(str)))

##Approach-4 (Recursive function)

def recursive_reverse(str):
    if len(str) == 0:
        return str
    return recursive_reverse(str[1:]) + str[0]

a = recursive_reverse("hello")
print(a)



### 2.Palyndrome or not
#Method-1
def palyndrome(str):
    if str.replace(" ", "") == str[::-1].replace(" ", ""):
        print("Yes")
    else:
        print("no")
        
palyndrome("nurses run")


#Method-2 
def palyndrome(str):
    return "True" if str == str[::-1] else "False"

a = palyndrome("nursesrun")
print(a)
    
        
#Method-3                                    
def is_palyndorm_recursive(str):
    if len(str) <= 1:
        return True
    if str[0] != str[-1]:
        return False
    return is_palyndorm_recursive(str[1:-1])    
  
a = is_palyndorm_recursive("nursesrun")
print(a)


### 3. Vowels and constraints

#Approach -1 
def check_oc(str):
    vowels = "AEIOUaeiou"
    vowel_list = []
    vowel_count = 0
    for i in str:
        if i in vowels:
            vowel_list.append(i)
            vowel_count+= 1
    
    if vowel_count > 1:
        return vowel_list, vowel_count
    else:
            return "no vowels"

a = check_oc("Are you there")
print(a)


#Approach -2 
def check_vowels(str):
    vowels = "AEIOUaeiou"
    vowel_list = [char for char in str if char in vowels]
    return (vowel_list, len(vowel_list)) if vowel_list else "no vowels"

print(check_vowels("Are you there"))  # (['A', 'e', 'o', 'u', 'e', 'e'], 6)
print(check_vowels("xyz")) 

##Approach - 3 {using dictionary}

def check_oc(s):
    vowels = "AEIOUaeiou"
    counts = {v: s.count(v) for v in vowels if v in s}
    return counts if counts else "no vowels"

print(check_oc("Are you there"))
print(check_oc("xyz"))


########################## String to list, list to string, string to dict, list to dict conversion ###############################

def word_split(s):
   s_list = s.split() #Convert string to list
   s_string = " ".join(s_list) #Convert the list to string
   s_string_dict = {x: s_string.count(x) for x in s_string} #Count occurance of letters in the string
   s_list_dict = {x: s_list.count(x) for x in s_list} #Count occurance of letters in the list
   return s_list,s_string, s_string_dict, s_list_dict

var = word_split("hello how are you you")
print(var)


##Find given no occurance and append in a list

def find_given_no(lst):
    inp_num = int(input("Enter the no : "))
    count=0
    emp_list = []
    for i in lst:
        if i == inp_num:
            count+= 1
            emp_list.append(i)
    print(count, emp_list)

find_given_no(lst)  

#####Move the zeros to the end of the list without changing the order

lst = [1, 0, 0, 3, 4, 5, 12]

#Approach-1 with creating new list and append
def move_zeroes(lst):
    non_zeroes = [x for x in lst if x!= 0]
    zeros = [0] * (len(lst) - len(non_zeroes))
    return non_zeroes + zeros
    
a = move_zeroes(lst)
print(a)

#Approach - 2 , In place (using pointers)
def move_zeroes(lst):
    post = 0
    emp_list = []
    for i in range(len(lst)):
        if lst[i]!= 0:
            lst[post], lst[i] = lst[i], lst[post]
            post+= 1
    return lst
    
a = move_zeroes(lst)
print(a)
