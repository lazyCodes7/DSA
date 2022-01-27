# Implement strStr()

![Screenshot from 2022-01-24 09-29-56](https://user-images.githubusercontent.com/53506835/150729425-ec9f8e31-3d0a-45ca-b5ee-42c5c49124e1.png)

## Task

Implement [strStr()](http://www.cplusplus.com/reference/cstring/strstr/).

Return the index of the first occurrence of needle in haystack, or `-1` if `needle` is not part of `haystack`.

**Clarification:**

What should we return when `needle` is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when `needle` is an empty string. This is consistent to C's [strstr()](http://www.cplusplus.com/reference/cstring/strstr/) and Java's [indexOf()](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html#indexOf(java.lang.String)).

## Approach

- Naive Approach
    
    Just take a sliding window of the size possible and then compare it to find the string matching
    
    But it would take n^2 complexity!
    
- Better
    
    How about we encode this comparing as a sum maybe we add character ASCII value and if the sum is the same then that would be our solution. Of course, in worse case, it is possible to have the complexity of n^2 but that won’t usually come if we use a good hashing function.
    
- Best
    
    This one uses the KMP algorithm. 
    
    Inspiration.
    
    Many times while searching for the string we often go till the whole end of the string just to learn that it doesn't really match and then we again start at a certain index. Instead of doing this KMP algorithm uses a theory of Longest Prefix-Suffix array so that when we have repeating sequences we don’t just start at the first index again and again.
    
    Here the time complexity is O(n)
    

# Insert to make palindromes.
![Screenshot from 2022-01-24 09-42-48](https://user-images.githubusercontent.com/53506835/150729463-bd7473b8-3b77-43fa-92c6-71460b318203.png)


## Task.

Given a string **A**. The only operation allowed is to insert characters at the beginning of the string.

Find how many minimum characters are needed to be inserted to make the string a palindrome string.

## Approach

- Naive Approach
    
    In the naive approach, we just keep on removing a character at the end of the string and then check whether it is a palindrome. No of characters removed == the no we need to insert
    
- Better Approach
    
    In this approach, we basically use the idea of KMP algorithm. 
    
    ### LPS.
    
    That is the longest prefix that is still a suffix. 
    
    So what we do is that we reverse the string and add it to the string
    
    Why well since it is a palindrome when we reverse it, it is usually the same so using LPS we will be able to find the no of chars that are suffix and prefix. So that no will correspond to the chars that are already a palindrome and by subtracting from the length of the actual string we could just get the no of chars to add.
    

# Valid Anagram

![Screenshot from 2022-01-24 10-44-08](https://user-images.githubusercontent.com/53506835/150729487-6d62a546-1d7c-47c4-a4e8-946fd3aa6602.png)

## Task

Given two strings `s` and `t`, return `true` *if* `t` *is an anagram of* `s`*, and* `false` *otherwise*.

An **Anagram** is a word or phrase formed by rearranging
 the letters of a different word or phrase, typically using all the 
original letters exactly once.

## Approach

In this problem we use a map to store the cnts of each char and then use the second string to decrease the cnts.

Now if everything is zero then it surely is an anagram else not.

# Count and Say

![Screenshot from 2022-01-24 11-16-47](https://user-images.githubusercontent.com/53506835/150729513-f773ffbf-4c12-41fd-845f-18fef132ecdd.png)

## Task

The **count-and-say** sequence is a sequence of digit strings defined by the recursive formula:

- `countAndSay(1) = "1"`
- `countAndSay(n)` is the way you would "say" the digit string from `countAndSay(n-1)`, which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the **minimal** number of groups so that each group is a contiguous section all of the **same character.**
 Then for each group, say the number of characters, then say the 
character. To convert the saying into a digit string, replace the counts
 with a number and concatenate every saying.

For example, the saying and conversion for digit string `"3322251"`:

## Approach

In this problem, we basically recurse until the base case i.e 1 and then use 1 to backtracking to build up the number based on the question.

# Compare Version Numbers
![Screenshot from 2022-01-24 11-26-09](https://user-images.githubusercontent.com/53506835/150729564-5504005b-8d27-4db8-a000-d98cbd84264f.png)


## Task

Given two version numbers, `version1` and `version2`, compare them.

Version numbers consist of **one or more revisions** joined by a dot `'.'`. Each revision consists of **digits** and may contain leading **zeros**. Every revision contains **at least one character**. Revisions are **0-indexed from left to right**, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example `2.5.33` and `0.1` are valid version numbers.

To compare version numbers, compare their revisions in **left-to-right order**. Revisions are compared using their **integer value ignoring any leading zeros**. This means that revisions `1` and `001` are considered **equal**. If a version number does not specify a revision at an index, then **treat the revision as `0`**. For example, version `1.0` is less than version `1.1` because their revision 0s are the same, but their revision 1s are `0` and `1` respectively, and `0 < 1`.

*Return the following:*

- If `version1 < version2`, return `1`.
- If `version1 > version2`, return `1`.
- Otherwise, return `0`.

## Approach

In this question. First we use split(”.”) to get all the version numbers for the two strings. Next add zeroes if one is lesser than other to even it.

We are ready.

Now just compare the numbers one by one (removing any leading zeroes) and based on the rules given return a corresponding number!
