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
