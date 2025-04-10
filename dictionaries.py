dct = {"a":100, "b":200, "c":300, "d":500}

def dict_func(dict):
    emp_lst = []
    for i in dct.values():
       emp_lst.append(i)
    print(sum(emp_lst))
    
dct = {"a":100, "b":200, "c":300, "d":500}
dict_func(dict)  
