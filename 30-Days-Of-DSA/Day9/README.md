# Day9
## Subset sums

![Screenshot from 2021-11-29 08-29-55](https://user-images.githubusercontent.com/53506835/143974127-dc659330-85e7-49bc-b4a6-1f16cf57a052.png)

### Task

Given a list **arr** of **N** integers, print sums of all subsets in it.

### Approach

For generating all the possible subsets we will take a simple approach of either picking an element or not. If we pick an element then we add it to the sum else we don't. In the base case we simply just add this sum to a list

## Subsets II
![Screenshot from 2021-11-29 08-46-44](https://user-images.githubusercontent.com/53506835/143974162-7d4b3664-6111-4ff7-933c-ea3bffb06bcf.png)

### Task

Given an integer array `nums` that may contain duplicates, return *all possible subsets (the power set)*.

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

### Approach

In this problem, there is a stress on the solution not containing duplicate subsets. But it is bound to happen so we sort the array first and at each recursion call, we will skip the indexes that are the same so as to escape this. If not sorting, frozenset can be used but it won't work out that well for each case

Coming to the solution after sorting, at each step we will maintain a temporary list that will have some elements in it and then after that, we make a choice of picking that element and adding it to the temp_list at the same time we create a deepcopy of that list and add it to our final ans. After the recursion call is complete for the element we just picked we remove it from the temp list to make another choice to generate more subsets

## Combination sum 1
![Screenshot from 2021-11-29 08-55-10](https://user-images.githubusercontent.com/53506835/143974191-5340232f-5d1d-47b8-99e9-df334d0f33d1.png)

### Task.

Given an array of **distinct** integers `candidates` and a target integer `target`, return *a list of all **unique combinations** of* `candidates` *where the chosen numbers sum to* `target`*.* You may return the combinations in **any order**.

The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is **guaranteed** that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input

### Approach

In this approach, we have basically two choices either to pick the element or not. Using this approach we recursively try to find the subsets that give us our answers. We maintain a temp_list with some elements and if it results in the target then we finally append it to the answer else we discard it

## Combination Sum2

![Screenshot from 2021-11-30 07-17-55](https://user-images.githubusercontent.com/53506835/143974209-2e11c069-c4ef-42d3-b047-47b460abd09f.png)

### Task

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note:** The solution set must not contain duplicate combinations.

### Approach

The approach is pretty similar but the only thing we need to keep in mind is that we can only pick an element once here and not an infinite amount of times so once we decide to pick an element then we have to go to the next element

## Palindrome Partitioning
![Screenshot from 2021-11-30 07-20-57](https://user-images.githubusercontent.com/53506835/143974237-77e31866-f7d4-4340-b8b9-700c56b43a63.png)


### Task

Given a string `s`, partition `s` such that every substring of the partition is a **palindrome**. Return all possible palindrome partitioning of `s`.

A **palindrome** string is a string that reads the same backward as forward.

### Approach

The approach here is similar to MCM approach in solving these problems

What we do is that we have a certain I and J and a k that iterates between these values and then we apply a function to get our answers

In this case, our k will be the partition index and I and j would be the end and the start of the strings usually and we recursively keep on doing this. Here the function possible would be one to check if a partition is a palindrome or not

## Permutation Sequence

![Screenshot from 2021-11-30 07-44-32](https://user-images.githubusercontent.com/53506835/143974255-3a69c349-9a64-402b-a6a5-54b6a16cdc93.png)

### Task

The set `[1, 2, 3, ..., n]` contains a total of `n!` unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for `n = 3`:

1. `"123"`
2. `"132"`
3. `"213"`
4. `"231"`
5. `"312"`
6. `"321"`

Given `n` and `k`, return the `kth` permutation sequence.

### Approach

In this problem, what we really need is the kth sequence so instead of generating everything we just need to generate the one we want. For instance, if we observe the initial task we can see each number has a certain no of intervals.

Numbers starting with 1 are repeated two times and starting with 2 also two times so based on our k we can recursively generate these numbers to find the matching number that we want and return it finally!
