# Day13

# Implement stack using arrays

## Task

As the question suggests we are supposed to implement a stack using an array which is actually pretty simple.

## Approach

Using the pop operations that we have already in the array we can easily append elements such that the last element will always be the first to go when popped as a result we maintain the constant time of operations of stack.

# **Implement Queue Using Arrays**

## Task

In this question we are supposed to implement a queue using an array.

## Approach

The approach here is simple.

First we maintain an array and push elements in the same manner as we did in stack but the only thing here we need to change is that instead of popping elements we set the index of first element that is not empty to None

so if Queue = [1,2,3,4,5]

then after dequeue [None,2,3,4,5]

and our idx will go to 2 which will make sure that we are doing dequeue in O(1) time

# **Implement Stack using Queue**

## Task

Implement a last-in-first-out (LIFO) stack using only two queues. The
 the implemented stack should support all the functions of a normal stack (`push`, `top`, `pop`, and `empty`).

Implement the `MyStack` class:

- `void push(int x)` Pushes element x to the top of the stack.
- `int pop()` Removes the element on the top of the stack and returns it.
- `int top()` Returns the element on the top of the stack.
- `boolean empty()` Returns `true` if the stack is empty, `false` otherwise.

## Approach

In this question, we will try to implement a stack by using two queues.

- Push → Normal push to queue
- Pop → First dequeue all the elements from queue1 until last element and then push to the second queue.
    - Dequeue the last element from the 1st queue and enqueue the values from 2nd queue
    

# Implement Queue using Stacks

## Task

Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a normal queue
 (`push`, `peek`, `pop`, and `empty`).

Implement the `MyQueue` class:

- `void push(int x)` Pushes element x to the back of the queue.
- `int pop()` Removes the element from the front of the queue and returns it.
- `int peek()` Returns the element at the front of the queue.
- `boolean empty()` Returns `true` if the queue is empty, `false` otherwise.

## Approach

In this question, what we will do is that by maintaining two stacks we will reach near O(1) complexity. So whenever we enqueue we just push all the elements into stack1

During dequeue,

If stack2 is empty we pop elements from stack1 and push into stack2 because of which the next time we want to pop something the first element would be at the top of the stack and hence near O(1) complexity for dequeue as well.

# Valid Parentheses

## Task

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

## Approach

For symbols like “{”, “(”, “[” push it into a stack

Now once we get a symbol like “]”, “}”, “)” then it mains an opposite sign corresponding to it must be there on top of the stack, and if not then that means it is not a valid input string.

# Next Greater Element

## Task

The **next greater element** of some element `x` in an array is the **first greater** element that is **to the right** of `x` in the same array.

You are given two **distinct 0-indexed** integer arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`.

For each `0 <= i < nums1.length`, find the index `j` such that `nums1[i] == nums2[j]` and determine the **next greater element** of `nums2[j]` in `nums2`. If there is no next greater element, then the answer for this query is `-1`.

Return *an array* `ans` *of length* `nums1.length` *such that* `ans[i]` *is the **next greater element** as described above.*

## Approach

If we want to next greater element it kinda makes sense to start at right since the rightmost element won’t have any but it could be the next greater one for someone else.

So we push it

At each step, we push these elements and for an element, we see if some element at the top of the stack is greater than it or not if yes then cool and push the current element as well, or else we keep popping from the stack until we find one and then push.

And just like that, we will get access to all the next greater ones!  

# Sort stack

## Task

Given a stack sort it.

## Approach

In this problem we have to the merge-sort ideology. The first step is to pop the stack until empty and then we take elements and compare them with the stack top.

If greater → then append

Else → pop until empty or the element to be inserted is greater.

Also popped elements are inserted in order after the element to be inserted.
