import copy
def computePermutaions(input_string, i, visited_map, return_list, temp_list):
    if(i == len(input_string)):
        subset = copy.deepcopy(temp_list)
        return_list.append("".join(subset))
    else:
        for j in range(len(input_string)):
            if(visited_map[input_string[j]] == False):
                temp_list.append(input_string[j])
                visited_map[input_string[j]] = True
                computePermutaions(input_string, i+1, visited_map, return_list, temp_list)
                temp_list.pop()
                visited_map[input_string[j]] = False
    return return_list
            
testcases = int(input())
for x in range(testcases):
    input_str = input()
    input_list = list(input_str)
    visited_map = {}
    for k in range(len(input_list)):
        visited_map[input_list[k]] = False
    res = computePermutaions(input_list, 0, visited_map, [], [])
    res.sort()
    for string in res:
        print(string, end = " ")
    print("")