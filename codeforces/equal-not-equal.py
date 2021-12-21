testcases = int(input())
for K in range(testcases):
    visited = {}
    flag = 0
    string = input()
    strlen = len(string)-1
    for i in range(len(string)):
        element = string[i]
        key = i%strlen
        if(key in visited and element!=visited[key]):
            flag = 1
            print("NO")
            break
        else:
            visited[key] = element
    #print(visited)
    if(flag == 0):
        print("YES")