# Day6

## Intersection of linked lists

Pretty simple problem

- First, calculate the length of both lists
- Traverse the longer one go till length of both lists are same
- Now check whether they have the same address. That is where the intersection starts!

## Linked List Cycle

Store all the node addresses and mark their visited as False.

Now traverse the linked list and keep on marking visited as True. If visited is already True before us marking it then there is a cycle else not

## Reverse Nodes in k-Group

- Find the length of list
- Based on k, calculate index till which we have to go
- Now for each group, do a normal reversing linked-list question
- While doing this store the head in each group so that we can connect it to next group
- That's it!

## Check if the linked list is a palindrome.

- Store values till the middle index in a list
- Now pop the nodes from the list and compare them with the second half of the linked list

## Starting point of the loop in a linked list

Pretty similar to the linked list cycle but just return the node instead of True or False!

## Flatten linked list

- First, recursively go till the end of the list
- Perform a merge operation and return this merged list
- Recursively perform this merge to eventually return the flattened list

## Rotate linked list by k

- Calculate the index at which we are supposed to have our head
- Disconnect the node before it
- Connect the head of values of this node with the set of nodes involved in our rotation

Example:

[1,2,3,4,5], k =2

Go till index 2

- Disconnect 3 and 4
- Connect 1 to 5
- And return head as 3
