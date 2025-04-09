def spygame(num_lst):
    for i in range(len(num_lst)):
        for j in range(i+1, len(num_lst)):
            for k in range(j+1, len(num_lst)):
                if num_lst[i] == 0 and  num_lst[j] == 0 and  num_lst[k]== 7 :
                    print(f"Num list {i}, {j}, {k} and he is james bond")
    else:
        print("He is not bond")
                    
num_lst = [7,1,2,3,4,5, 0,0]                    
spygame(num_lst)

####### Second approach ################

def spygame(num_lst):
    code = [0,0,7, 'x']
    
    for num in num_lst:
        if num in code:
            code.pop(0)
    
    return len(code) == 1

num_lst = [0,1,2,3,4,5,0,7]                    
output = spygame(num_lst)
print(output)
