# Reverse Words in a String
![Screenshot from 2022-01-24 08-33-22](https://user-images.githubusercontent.com/53506835/150717940-d9857728-f83d-4698-a6e3-d82713329e41.png)

## Task

Given an input string `s`, reverse the order of the **words**.

A **word** is defined as a sequence of non-space characters. The **words** in `s` will be separated by at least one space.

Return *a string of the words in reverse order concatenated by a single space.*

**Note** that `s` may contain leading or trailing 
spaces or multiple spaces between two words. The returned string should 
only have a single space separating the words. Do not include any extra 
spaces.

## Approach

In this problem we just strip the leading and trailing whitespace using builtin functions and then split based on whitespace and reverse this list and then join them together!

# Longest Palindromic Substring
![Screenshot from 2022-01-24 08-43-45](https://user-images.githubusercontent.com/53506835/150717969-77337bf3-e2f5-4f59-bd69-37e50e08e376.png)


# Task

Given a string `s`, return *the longest palindromic substring* in `s`.

## Approach

In this question, we trying using a DP approach

Let’s take the string babab

What will be the max palindromic string here? 

The ans is either bab or aba I guess

But how did we come to this solution

By building up a tabulation strategy!

Let’s take ‘b’, ‘a’, ‘b’, ‘a’, ‘b’. Now we know that these strings are palindromic and hence if someone asked as max palindrome of len==1 we will say this is the answer. Similarly what we do is that we build this up for lengths 2,3,4 until the length of the string and whatever is the max length of the string i.e palindromic is what we return.

# Roman to Integer
![Screenshot from 2022-01-24 08-50-35](https://user-images.githubusercontent.com/53506835/150717992-b676302b-8fc1-414f-8028-31dfa655ff70.png)


## Task

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`.
 Because the one is before the five we subtract it making four. The same
 principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9.
- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90.
- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

## Approach

In this we maintain a map for the numbers corresponding to the symbols and as we read them we add it to the sum.

Now whenever we read a symbol that is greater than prev symbol read then we get rid of the added value and instead add the subtraction of these two symbols

# String to Integer (atoi)
![Screenshot from 2022-01-24 09-02-12](https://user-images.githubusercontent.com/53506835/150718008-7a7405d3-d0a1-4aed-8923-119feb7eee3b.png)


## Task

Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer (similar to C/C++'s `atoi` function).

The algorithm for `myAtoi(string s)` is as follows:

1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) is `'-'` or `'+'`. Read this character in if it is either. This determines if the final
result is negative or positive respectively. Assume the result is
positive if neither is present.
3. Read in next the characters until the next non-digit character or
the end of the input is reached. The rest of the string is ignored.
4. Convert these digits into an integer (i.e. `"123" -> 123`, `"0032" -> 32`). If no digits were read, then the integer is `0`. Change the sign as necessary (from step 2).
5. If the integer is out of the 32-bit signed integer range `[-231, 231 - 1]`, then clamp the integer so that it remains in the range. Specifically, integers less than `231` should be clamped to `231`, and integers greater than `231 - 1` should be clamped to `231 - 1`.
6. Return the integer as the final result.

## Approach

The approach is pretty straightforward. Following the rules will lead to the answer and get it accepted as well
