# Day11

# Nth Root

## Task

Given two numbers N and A, find N-th root of A. In mathematics, Nth root of a number A is a real number that gives A, when we raise it to integer power N. These roots are used in Number Theory and other advanced branches of mathematics.

## Approach

In this problem, we are basically trying to apply binary search on answers. So the max possible root will be the number itself and the lowest might be 1 and hence through binary search we debunk one half of this range we have defined

So if we find the square root of 16

Then Range is from 1-16

And mid is 8 

so the power of 8(squared) is definitely greater than the number we have and hence we debunk 8-16 as the root and then go from 1-8. So yeah we just keep on doing this until we reach the no or have a certain precision defined.

# Matrix Median

## Task

We are given a row-wise sorted matrix of size r*c, we need to find the median of the matrix given. It is assumed that r*c is always odd.

## Approach

In this problem, we again apply the approach of binary search on answers. The answer can be between the minimum and the maximum element and hence we try to find it

First, we take mid between min and max and then check whether there are r*c/2 elements smaller than it if yes then perfection and if no

Two conditions

Maybe more elements more are there so debunk mid to max

Or the reverse so debunk min to mid and keep on doing this for each range!

# Search in Rotated Sorted Array
![Screenshot from 2021-12-17 21-08-19](https://user-images.githubusercontent.com/53506835/146577549-90c6c32b-6882-42c1-8421-d33e92145205.png)

## Task

There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly rotated** at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return *the index of* `target` *if it is in* `nums`*, or* `-1` *if it is not in* `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

## Approach

Here our approach is to basically first find the pivot and then once found we can just apply Binary search like a normal array on two subarrays.

For finding the point the point is simple. Find the point where both elements are smaller than it.

So for [4,5,6,7,0,1,2], it is 7 where both elements are smaller than it i.e 6 and 1. This is done through a binary search

So here we first take a mid and compare it with start and end. Now if the subarray is sorted, naturally the element is greater than start and less than end but that is not the case when rotated, and hence based on this intuition we try to move closer to the pivot by eliminating a certain portion at a time

# Median of Two Sorted Arrays
![Screenshot from 2021-12-17 21-20-04](https://user-images.githubusercontent.com/53506835/146577615-8140acbe-3d37-46d9-8699-e3b15742924d.png)

## Task

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

## Approach

The approach here is to take variated m+n/2 elements in a binary search fashion to get the median.

So we pick some elements and then the remaining elements from the 2nd array.

After picking if the l1≤r2 and l2≤r1 from both the left and right side of partition for both the array then that our median exists in l1 and l2

Else:

If we l1 was greater than r2 then we need to reduce our partition for the next iteration

Similarly, in the reverse case, we might want to pick more elements to match our median condition

# Kth Element in Sorted Arrays
![Screenshot from 2021-12-17 21-28-08](https://user-images.githubusercontent.com/53506835/146577658-a34911ee-65ba-47e9-a2ea-ef8eeae5d65c.png)

## Task

Given two sorted arrays **arr1** and **arr2** of size **N** and **M** respectively and an element **K**. The task is to find the element that would be at the k’th position of the final sorted array.

## Approach

This is a similar question to the median problem except here instead of finding the median we return kth element. So now the partition will consist at most k elements and rest is pretty same with few variations

# Allocate min number of pages
![Screenshot from 2021-12-17 21-35-16](https://user-images.githubusercontent.com/53506835/146577699-b17ac0f3-894c-45d9-b700-25fca07900a5.png)

## Task

Given an array of integers **A** of size **N** and an integer **B**.

College library has **N** bags,the **ith** book has **A[i]** number of pages.

You have to allocate books to **B** number of students so that the maximum number of pages allotted to a student is minimum.

`A book will be allocated to exactly one student.
Each student has to be allocated at least one book.
Allotment should be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2.`

Calculate and return that minimum possible number.

## Approach

This is again related to applying binary search on the answer so here we can have a maximum no of pages as the sum of all the pages and minimum as may be zero and through binary search, we find the solution. If the no of candidates are not fulfilled by a certain page limit then we increase the limit and if it is satisfied then we try to reduce the limit since we want to find minimum solution

# Aggressive Cows

## Task

Farmer John has built a new long barn, with N (2 <= N <= 100,000) stalls. The stalls are located along a straight line at positions x1,...,xN (0 <= xi <= 1,000,000,000).

His C (2 <= C <= N) cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, FJ wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible.  What is the largest minimum distance?

## Approach

Again, applying the principle of binary search on ans our minimum distance could vary between 0 and the distance between max and min element. So if we are able to place elements properly for a certain distance that could mean we can try for even bigger distances until we find max distance possible. Similarly, if we find a distance where it is not possible to place elements then it should hold true for elements greater than it as well and hence we try to reduce distance. Using this approach we try to find the best possible distance
