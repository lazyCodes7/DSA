# Day10

# Permutation of a string.
![Screenshot from 2021-12-17 18-36-06](https://user-images.githubusercontent.com/53506835/146577929-63aeaff6-0924-4cad-92fa-d678b6d56e22.png)

## Task

Given an array `nums` of distinct integers, return *all the possible permutations*. You can return the answer in **any order**.

## Approach

For getting all the permutations of a string that is distinct we just try a recursive approach where we go through all the possible elements that we can pick. Of course, since we are supposed to pick distinct subsets we can try having a visited dict which will make sure that we pick an element only once

# N Queens
![Screenshot from 2021-12-17 18-48-36](https://user-images.githubusercontent.com/53506835/146578007-6af8a7a1-eff7-45fd-a124-176afe811968.png)

## Task

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return *all distinct solutions to the **n-queens puzzle***. You may return the answer in **any order**.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.

## Approach

We know for a fact that we can only place N Queens in N Rows

So using recursion we try to do so.

For instance, if we want to place a queen on the first row we will check in three direction

- Up
- Left
- Diagonal backward

We could check downwards or right but we are making sure to place only one in our recursion so we don’t need to check

Now, if it is possible to place that queen then we go to the next row recursively until we reach the end which means it is possible to do so!

And hence we store this configuration in our ans.

Finally, if a configuration is not possible we stop it using backtracking and undo the changes made

# Sudoku solver

![Screenshot from 2021-12-17 18-49-17](https://user-images.githubusercontent.com/53506835/146578033-b8542ae7-dd7f-4012-b6df-5eb449f9d914.png)

## Task

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy **all of the following rules**:

1. Each of the digits `1-9` must occur exactly once in each row.
2. Each of the digits `1-9` must occur exactly once in each column.
3. Each of the digits `1-9` must occur exactly once in each of the 9 `3x3` sub-boxes of the grid.

## Approach

The approach here is similar to the N-Queens problem except here we try to put numbers instead of queens and at each point check the rules we have to see if it is safe to put the number. Using backtracking we remove a number if it doesn't result in a solution and store the solution if it does.

# M-Coloring Problem

![Screenshot from 2021-12-17 19-39-39](https://user-images.githubusercontent.com/53506835/146578074-8673abb6-e29b-4800-92b0-ba8721476de4.png)

## Task

Given an undirected graph and an integer **M**. The task is to determine if the graph can be colored with at most
M colors such that no two adjacent vertices of the graph are colored
with the same color. Here coloring of a graph means the assignment of
colors to all vertices. Print 1 if it is possible to color vertices and 0 otherwise.

## Approach

The approach is to start with a node and then color it.

Next, take another node, mark with it a certain color.

If this color is different from adjacent nodes → advance more into the recursion

Else: backtrack and remove this color for this permutation

And yeah that’s it 

# Rat in a maze.
![Screenshot from 2021-12-17 19-54-05](https://user-images.githubusercontent.com/53506835/146578088-3273e26f-0bde-4667-a6ee-420d434553ae.png)

## Task

Consider a rat placed at **(0, 0)** in a square matrix of order **N * N**. It has to reach the destination at

**(N - 1, N - 1)**. Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are **'U'(up)**,**' D'(down)**,**' L' (left)**,**' R' (right)**. Value 0 at a cell in the matrix represents that it is blocked and the rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.

**Note**: 

In a path, no cell can be visited more than one time.

## Approach

The approach here is simple. I say that a lot I guess. Here we have a rat that wanna get outta the maze and so if we want to really reach the end we will try all the possible permutations and return the correct one. Of course if we a choice doesn’t result in success then we backtrack and remove that choice

# **Word Break**

![Screenshot from 2021-12-17 20-13-02](https://user-images.githubusercontent.com/53506835/146578159-0325e5b4-e426-4a0d-8bdf-263500a4c898.png)

## Task

Given an input string and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words. See following examples for more details.

## Approach

In this question, we follow a sort of MCM approach. We make variated partitions and see if those result in an answer so 

Eg:

String → ilike

Dictionary → {”i”,”like”}

Here first we separate the string as I and like and see if I is present in the dictionary. If it is then make a partition and start at L. Now at L we again make variable length partitions and see if it fits into our dictionary

So L→ No.

LI→ No

LIK → No

LIKE → Yes

Again make a partition and then do the same tasks for this recursion. Here we have reached the end of the string which signifies that our string was segmentable!

If we observe there is a chance that we might perform recursions again for substring “LI” or “LIKE” maybe hence due to this overlapping nature we try to store the results for this substring using memorization technique from DP!
