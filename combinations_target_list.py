from itertools import combinations

def find_combinations_that_sum(inp_list, target):
    result = []
    for r in range(1, len(inp_list)+1):  # r = combination length
        for combo in combinations(inp_list, r):
            if sum(combo) == target:
                result.append(combo)
    return result

# Example usage
inp_list = [2, 4, 6, 1, 5]
target = 6
print(find_combinations_that_sum(inp_list, target))
