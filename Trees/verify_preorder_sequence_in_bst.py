from typing import List


## What is preorder traversal
## Given a Tree
##            6
##        //     \\
##       4        10
##     // \\    //  \\
##    1   5    8     12
##
## Preorder Traversal of this tree -> 6 4 1 5 10 8 12
## We obviously know that 6 is root So right subtree should start where we encounter anything over 6
## So know we know what is the left subtree and what is right subtree
## If we can do this recursively we know what should be the correct answer.
## If the tree follows this principal then its is a BST but if it doesn't then it is not a BST

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool | None:
        # Initialize an empty stack to simulate traversal
        # The stack will hold nodes in decreasing order
        stack = []

        # This variable keeps track of the last value that was popped from the stack,
        # which represents the root of the current right subtree.
        # It must always be less than any future nodes encountered in a valid BST preorder.
        lastnum = float('-inf')

        # Iterate over each number in the preorder list
        for n in preorder:
            # If the current number is less than lastnum,
            # it violates the BST property since it would fall into the right subtree.
            if n < lastnum:
                return False

            # If the current number is greater than the last element in the stack,
            # it means we are transitioning from the left subtree to the right subtree.
            # In this case, pop from the stack until the current number is less than the stack's top element.
            # Each popped value becomes the new 'lastnum', updating the lower bound for future values.
            while stack and n > stack[-1]:
                lastnum = stack.pop()

            # Push the current number onto the stack.
            # This number might be part of the left subtree of a future node.
            stack.append(n)

        # If the entire list is processed without violating the BST rules,
        # the preorder sequence represents a valid BST.
        return True
