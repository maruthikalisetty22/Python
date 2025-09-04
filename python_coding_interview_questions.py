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
