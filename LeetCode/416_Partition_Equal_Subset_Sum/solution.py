import typing
from typing import List

class Solution:
    def findPartition(self, nums: List[int], startIndex: int, remaining: int, total:int) -> bool:
        if startIndex >= len(nums):
            return False
                
        result = False                
        for idx in range(startIndex, len(nums)):
            partition = remaining - nums[idx]
            if partition == total - partition:
                return True
            
            if self.findPartition(nums, idx + 1, partition, total):
                result = True
        
        return result
        
        
        
    def canPartition(self, nums: List[int]) -> bool:
        # 1. Sum up nums array
        # 2. Creat recursive function to pass start index, remainingSum and sum of whole nums array
        # 3. Do DFS to find partition
        # 4. Find all subset in DFS
        
        total = sum(nums)
        
        return self.findPartition(nums, 0, total, total)        
    
# Input: nums = [1,5,11,5]
# Output: true 

nums = [1,2,3,5]
print(f"[DEBUG] ouput: {Solution().canPartition(nums)}")

