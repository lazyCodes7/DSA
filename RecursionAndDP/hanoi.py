def solve_hanoi(rings, source = "A", dest = "B", inter = "C"):
    if(rings == 1):
        print("Moving ring {} from {} to {}".format(rings, source, dest))
    else:
        solve_hanoi(rings-1, source, inter, dest)
        print("Moving ring {} from {} to {}".format(rings, source, dest))
        solve_hanoi(rings-1, inter, dest, source)

num = int(input())
solve_hanoi(num)