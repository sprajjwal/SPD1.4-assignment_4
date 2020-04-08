# Problems

## [Problem 1](./problem1.py)

Find the middle item in a singly linked list, or two middle items if it contains an even number of nodes.

### Psuedocode

- get two pointers, one to go across the linked list and one for the middle element.
- While iterator is not none, move iterator twice and middle ptr once.
- Once the while loop breaks, we have the mid ptr at the middle node.
