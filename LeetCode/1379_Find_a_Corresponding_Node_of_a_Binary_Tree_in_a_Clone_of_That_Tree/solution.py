import typing
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Queue:
    def __init__(self):
        self.list = []
        
    def enqueue(self, node: TreeNode):
        if node != None:
            self.list.append(node)
            
    def dequeue(self) -> TreeNode:
        if len(self.list) > 0:
            node = self.list[0]
            del self.list[0]
            return node
        
        return None 
    
    def size(self) -> int:
        return len(self.list)

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queueOriginal = Queue()
        queueCloned = Queue()
        
        queueOriginal.enqueue(original)
        queueCloned.enqueue(cloned)

        while queueOriginal.size() > 0:
            childInOriginal = queueOriginal.dequeue()
            childInCloned = queueCloned.dequeue()
            
            if childInOriginal == target:
                return childInCloned
            
            queueOriginal.enqueue(childInOriginal.left)
            queueOriginal.enqueue(childInOriginal.right)
            
            queueCloned.enqueue(childInCloned.left)
            queueCloned.enqueue(childInCloned.right)
            
        return None
                    

