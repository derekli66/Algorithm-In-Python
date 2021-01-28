# LeetCode Question
# 236. Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

#
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia:
# “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants
# (where we allow a node to be a descendant of itself).”
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        queue = []
        parentMap = {}
        queue.append(root)
        # Do BFS to scan whole binary tree to build parentMap
        while len(queue) > 0:
            parent = queue.pop(0)
            if parent.left != None:
                parentMap[parent.left] = parent
                queue.append(parent.left)

            if parent.right != None:
                parentMap[parent.right] = parent
                queue.append(parent.right)

        # Build p node's parenting stack
        childNode = p
        pStack = [childNode]
        while parentMap.get(childNode) != None:
            pStack.append(parentMap[childNode])
            childNode = parentMap[childNode]

        childNode = q
        qStack = [childNode]
        # Buiild q node's parenting stack
        while parentMap.get(childNode) != None:
            qStack.append(parentMap[childNode])
            childNode = parentMap[childNode]

        pStack.reverse()
        qStack.reverse()

        lowestAcent = root
        while len(pStack) > 0 and len(qStack) > 0:
            if pStack[0].val == qStack[0].val:
                lowestAcent = pStack[0]
                pStack.pop(0)
                qStack.pop(0)
            else:
                return lowestAcent

        return lowestAcent
