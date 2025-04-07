#Return every character in a string 3 times

def paperdoll(str):
    new_str=""
    for i in str:
        new_str += i*3
    print(new_str)
    
            
str = "missisipi"
paperdoll(str)
