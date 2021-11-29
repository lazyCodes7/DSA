## N-meetings in one room
![Screenshot from 2021-11-29 07-47-36](https://user-images.githubusercontent.com/53506835/143801233-c90f8f02-068e-49f6-b49f-ba421e14e419.png)

### Task

There is **one** meeting room in a firm. There are **N** meetings in the form of **(start[i], end[i])** where **start[i]** is start time of meeting **i** and **end[i]** is finish time of meeting **i.**
What is the **maximum** number of meetings that can be 
accommodated in the meeting room when only one meeting can be held in 
the meeting room at a particular time?

**Note:** Start time of one chosen meeting can't be equal to the end time of the other chosen meeting.

### Approach

The approach we will carry out here is a greedy one. Since we want to maximize the no of meetings it makes sense the sort the array according to end time and hence we do so. At each point, we take the meeting with the least end time and increment the no of meetings and once we reach the limit we return this value

## Minimum Platforms
![Screenshot from 2021-11-29 07-54-59](https://user-images.githubusercontent.com/53506835/143801284-31c58ee1-7f59-4947-b621-de07633d8ef9.png)

### Task

Given arrival and departure times of all trains that reach a railway station. Find the minimum number of platforms required for the railway station so that no train is kept 
waiting.

### Approach

To get the minimum platforms we sort both the arrival and departure times

Now let's start with an arrival time if it is lesser than departure time then we need another platform else we don't. Yeah, that's how simple it is. We just have to repeat this for the whole array and we get minimum platforms

## Job Sequencing Problem  
![Screenshot from 2021-11-29 08-00-59](https://user-images.githubusercontent.com/53506835/143801311-df3a99c5-e14d-4146-b98b-8cc82ad90396.png)


### Task

Given a set of **N** jobs where each **jobi** has a deadline and profit associated with it. Each job takes ***1***
 unit of time to complete and only one job can be scheduled at a time. 
We earn the profit if and only if the job is completed by its deadline. 
The task is to find the number of jobs done and the **maximum profit**.

**Note:** Jobs will be given in the form (Jobid, Deadline, Profit) associated with that Job.

### Approach

The approach here is to be lazy. The jobs which have a later deadline we do it last and once that is a priority we do it first

So we sort our job sequence w.r.t deadline in reverse. Next, we maintain a visited array from 1 to max deadline+1. At each time we take an element and check if its deadline is filled or not if yes then we go to the deadline before it until we hit an empty slot. If the following doesn't happen then we have already filled the max jobs possible

## Fractional Knapsack 
![Screenshot from 2021-11-29 08-07-26](https://user-images.githubusercontent.com/53506835/143801362-eca925ce-ad9d-4718-bb6b-0f3ae01511b4.png)


### Task

Given *weights* and *values* of **N i**tems, we need to put these items in a knapsack of capacity **W** to get the *maximum* total value in the knapsack.

**Note:**

Unlike 0/1 knapsack, you are allowed to break the item.

### Approach

Since we are trying to maximize our profit here. What we will try to do is sort the array in reverse w.r.t profit/weight ratio and then select those weights first and then when there is only some weight left less than our current item we just pick the percentage possible

## Minimum number of coins that make a given value

### Task

Given a value V, if we want to make a change for V cents, and we have an infinite supply of each of C = { C1, C2, .., Cm} valued coins, what is the minimum number of coins to make the change? If it’s not possible to make a change, print -1.

### Approach

In this task, we will try to recursively pick coins, and once the target is zero while backtracking we set the min coins value. 

Seems easy but there is a problem. The solution is exponential.

So we use memorization to make our recursion smart. In this problem, I said we recursively pick coins. So at each point, we would have certain changes and this change might overlap so what we do with memoization is that we store these values so we don't have to do the computations again!
