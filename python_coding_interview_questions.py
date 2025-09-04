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
