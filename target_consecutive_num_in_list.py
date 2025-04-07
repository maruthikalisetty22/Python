def find_three(num_lst):
    for i in range(0, len(num_lst)-1):
        if num_lst[i] == 3 and num_lst[i+1] == 3:
            print(True)
        else:
            print(False)
            
find_three([2,3,3,3])
