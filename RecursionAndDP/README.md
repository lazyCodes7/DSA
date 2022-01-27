This is just going to be stuff I will write related to recursion because I still kind of am not so good at it and those headaches suck when I see a recursion, backtracking, DP problems.

# Ways to really solve recursion

## IBH Method

I am not sure if that is the correct name but this is a pretty interesting way to solve a recursive problem

### H stands for hypothesis

So what does it mean?

Let’s take an example.

```python3
# A function to print numbers
def printNums(n):
'''
Here the hypothesis really is printNums(n) so based on whatever number 
we have we expect to print those numbers
'''
```

### B stands for base-case

```python3
def printNUms(n):
	if(n == 1):
		return
'''
Base case generally might be something like the smallest valid input 
that you can take or for instance the smallest invalid input. That is where your
recursion finally stops
'''. 
```

### I for induction

This is the meaty part and using this we can do a lot of stuff. It is of course related to mathematical induction.

```python3
def printNums(n):
	if(n == 1):
		return
	else:
		printNums(n-1)
		print(n)
```

For example in the first case the induction is as follows.

We already know and have printed numbers till 1...n-1 and so for printing the next number we just have to print(n)!

```python3
def printNums(n):
	if(n == 1):
		return
	else:
		print(n)
		printNums(n-1)
		
```

The induction here might be entirely different here.

Here it means we know the number n and have printed so for printing the next number we have to print(n-1) and hence we make recursive call printNums(n-1).

The mathematical induction here is weird I agree but this is what I inferred at least. 

# Recursion-Tree method

The difference between IBH method and this is that IBH is more concerned with the answer just behind it to compute the actual answer whereas in the recursion tree we might carve out the whole structure.

# Choice-Diagram.

The choice diagram is another way of solving recursive problems. Will discuss more on it later.
