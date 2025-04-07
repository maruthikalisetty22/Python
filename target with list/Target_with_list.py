def find_pairs_with_sum(inp_lst, target):
    result = []
    for i in range(len(inp_lst)):
        for j in range(i+1, len(inp_lst)):
            if inp_lst[i] + inp_lst[j] == target:
                result.append((inp_lst[i], inp_lst[j]))
    return result

# Example usage:
inp_list = [2, 4, 6, 1, 5]
target = 6
print(find_pairs_with_sum(inp_list, target))
