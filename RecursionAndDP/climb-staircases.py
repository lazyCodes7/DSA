def solveSteps(target, ans = 0, memo = {}):
    #print(target)
    if(target in memo.keys()):
        return ans + memo[target]
    if(target == 0):
        return True
    else:
        ans = 0
        for i in range(1,4):
            if(target>=i):
                result = solveSteps(target-i, ans, memo)
                if(isinstance(result, bool)):
                    ans+=1
                else:
                    ans = result
        memo[target] = ans
        return ans
testcases = int(input())
for j in range(testcases):
    height = int(input())
    #print(height)
    print(solveSteps(height, 0, {}))