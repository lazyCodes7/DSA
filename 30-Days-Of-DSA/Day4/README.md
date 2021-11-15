# Day4

## 2 sum Problem

Simple frequency array approach where you can store the values in a dict. 

## 4 sum Problem

The approach is a bit different here.

- Firstly, sort the array that we have
- then use two loops to iterate in a pair (i,j) fashion
- Take two values L and R which will start at i+1 and n-1 resp
- Since the array is sorted we will compute the sum of these values and use a 2 pointer approach to move L and R accordingly

## Longest Common Sequence

The intuition behind this is pretty simple

Let's take for instance the numbers 99,100,101,102

So in our algorithm whenever we get a number such as 100, 101, 102 we know there is one number before it so we don't do anything but when we finally get 99 we will loop over all these values to get our longest sequence.

This is possible by using a freq arr

## Longest subarray with sum 0

The approach here is that whenever we get zero the sum before it is bound to repeat so at each point we store the sum with the index and when that sum repeats at a certain index because of zero-sum we know that is the length of our subarray. On the other hand, there are conditions where the sum == 0 could occur for the length of the subarray before any non-zero-sum so we simply do the position we are at + 1 for the length!

## Longest Substring without repeat

In this approach, we maintain two pointers l and r, and at each point, we store in a frequency mapping the index at which a char was visited. Whenever we get a repeated character we accordingly increase our l to get the new substring without repeat

Also at each point, we keep on updating the max length for our substring and finally return the max length that was found
