n_cases = int(input())
for i in range(n_cases):
	n_tracks = int(input())
	array = list(map(int, input().strip().split()))
	sum_array = sum(array)
	x = sum_array%n_tracks
	rem_elements = n_tracks - x
	print(x*rem_elements)


