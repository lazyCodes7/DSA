def solution(x, y):
    x = set(x)
    y = set(y)
    output = list(x^y)

    return output[0]






    

x = [1, 2, 3,4,5,5]
y = [1, 2, 3, 4]

print(solution(x,y))