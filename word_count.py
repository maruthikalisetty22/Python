#Find count of given word

def count_frequency():
    str = input("Give your string here: ")
    input_target_word = input("Give your target word: ")
    
    count = 0
    final_list  = []
    
    for i in str:
        if i == input_target_word.lower():
            count+= 1
            final_list.append(i)
    print(f"This is the count of target word : {count} and here is the list: {final_list}")
            
        
count_frequency()
