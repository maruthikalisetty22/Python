def capitalise(str):
    
#first approach
    first_letter = str[0]
    in_between = str[1:3]
    third_letter = str[3]
    rest = str[4:]
    
    new_word = first_letter.upper()+in_between+third_letter.upper()+rest
    print(new_word)
    print(first_letter, in_between, third_letter, rest)
    
#Second approach
     first_half = str[:3]
     second_half = str[3:]
     print(first_half.capitalize()+second_half.capitalize())
     return first_half.capitalize()+second_half.capitalize()


    

str = "hellod"        
capitalise(str)
