# Day7

## Clone a linked list with a random pointer
![Screenshot from 2021-11-28 07-31-32](https://user-images.githubusercontent.com/53506835/143797796-3bbbf757-bb71-4035-b7e8-8336ec93fe22.png)


### Task

In this problem, we have a linked list with certain next and random pointers and our task is to create a deep copy of this list

### Approach

The approach is pretty simple we try to create a LinkedList that mimics the next pointers properly of the initial linked list

For eg

1→2→3→4→5

So we create an exact copy by of course creating node

But at the same time there is a random pointer.

For eg

1→3 signifies 1.random = 3

for these connections what we do is maintain a visited array.

so we store visited[address of 1] = address of copy of 1

### But why?

The reason we do this is that when all the old nodes are storing the address of the new nodes. When we use a copy of 1.random = visited[address of 1.random] it will actually now store a reference to the address of 3 i.e the copy one.

Since,

1.random = address of 3

and visited[address of 3] = address of copy of 3

## 3-Sum Problem
![Screenshot from 2021-11-28 07-47-05](https://user-images.githubusercontent.com/53506835/143797736-c81c8886-c3d1-456d-96dc-ec16e2c6d851.png)

### Task

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Also, the solution must not contain duplicates.

### Approach

The approach is pretty simple. What we will try is to sort the array

After sorting we will pick elements 

For example, if we have an array [1,2,-3,4,-5]

we sort it

[-5,-3,1,2,4]

Next, we pick 5 and choose our l as -3 and r as 4 and since the array is sorted we move our L and R based on the sum we get. So if sum>0 then we move R to the L and L to R for the opposite case and generate all possible pairs using this approach. 

## Trapping Rain Water
![Screenshot from 2021-11-29 06-59-19](https://user-images.githubusercontent.com/53506835/143797680-390e009f-3169-45a8-9895-b8701c028470.png)


### Task

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

### Approach

The idea is behind trapping water.

Whenever an elevation we account for is less than our max elevation it means we can store some water there. Based on this approach we try to then find the max water that can be stored from the left side and right side and this is the amount of water that can be stored

## Remove duplicates from sorted array

![Screenshot from 2021-11-29 07-04-39](https://user-images.githubusercontent.com/53506835/143797831-ffb226c6-28b5-4fea-bdbe-64dbf48dcbec.png)

### Task

Given an integer array, `nums` sorted in **non-decreasing order**, remove the duplicates **[in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** such that each unique element appears only **once**. The **relative order** of the elements should be kept the **same**.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the **first part** of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` *after placing the final result in the first* `k` *slots of* `nums`.

Do **not** allocate extra space for another array. You must do this by **modifying the input array [in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** with O(1) extra memory.

### Approach

The question might be sounding tough because sorted array to my ears is like the ultimate weapon. In this question we first try to maintain an index where we will be swapping our duplicate index

Example → [1,1,2,2,3,4,5]

taking a marked = 1

our i pointer traversing whole list

k pointer signifying first k points

- So if we current element that we visit is same as marked then we simply do i+=1
- If the current element is not the same then it means that it our next of the k element and hence we do k+=1 and then we swap it at position k
- Finally we return the no of k after whole traversal is done

## Consecutive amount of 1s in a binary array
![Screenshot from 2021-11-29 07-20-05](https://user-images.githubusercontent.com/53506835/143797875-46564817-eb0c-450b-931f-455354799307.png)

### Task

Given a binary array `nums`, return *the maximum number of consecutive* `1`*'s in the array*.

### Approach

In this approach, we will use the advantage of the fact that there can be zeroes in this array as well because of which our sum might not be the same as adding 1s till that point. So at each of these points, we will have our consecutive sum and we will just find the max consecutive amount from all these values

Example → [1,1,0,1,1,1]

Sum till index 2 if just adding 1 = 3

In reality it is 2

So our amount is 2 then we repeat this to get the max value from our array
