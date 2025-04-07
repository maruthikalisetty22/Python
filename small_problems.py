#Return every character in a string 3 times
def paperdoll(str):
    new_str=""
    for i in str:
        new_str += i*3
    print(new_str)
    
            
str = "missisipi"
paperdoll(str)

#Reverse given string
def masteryoda(str):
    word_list = str.split()
    reverse_list = word_list[::-1]
    reverse_list = " ".join(reverse_list)
    print(reverse_list)
  
str = "Hello how are you"   
masteryoda(str)

#Absolute function 
def abs_func(n):
    return (abs(100-n) <= 10) or (abs(200-n) <= 10)
    
output = abs_func(950)
print(output)
