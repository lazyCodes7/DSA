# Day5

## Reverse a linked list

It is a pretty simple approach.

- First, take a prev node, set it to None
- Go to the next node
- Sever the connection between those nodes
- Change the connection for the first node to prev and do this for all the nodes

## Middle of linked list

A pretty simple problem where we are supposed to find the middle node and return it.

- Find the length of the list
- Go till the middle index and return it

## Merge two sorted linked list

Merging a linked list might seem scary but it is similar to merging two lists

- Compute the length of both lists
- Create LL with 0 values corresponding to the length of both the lists
- Add the values accordingly since the list is sorted

## Remove nth node from the end of the list

- Compute the length of the list
- Find index by doing len-n
- Go till that index and do a simple delete operation

## Add two linked lists

- Create a seed ll with length as that of both of linked lists
- Add sum and check if the sum is greater than 9. For less than 9 update the seed ll with sum
- If yes then split into carry and sum and add carry to either of two linked lists if possible
- If not then create a new node in seed ll with carry value

## Deleting node in O(1)

In this problem, we are given access to the node to be deleted

- First, go to the next node
- Set the .next of the next node equal to the .next of the node to be deleted
- Transfer the value of the next node to the node to be deleted
- Delete the next node instead :p
