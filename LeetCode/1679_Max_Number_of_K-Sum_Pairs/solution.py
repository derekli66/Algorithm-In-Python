import typing
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = {}
        count = 0
        for ele in nums:
            if k - ele in d and d[k - ele] > 0:
                count += 1
                d[k - ele] -= 1
            else:
                d[ele] = d.get(ele, 0) + 1
        return count


# Input: nums = [1,2,3,4], k = 5
# Output: 2

nums = [1, 2, 3, 4]
k = 5

print(f"1. Max operations: {Solution().maxOperations(nums, k)}")

# Input: nums = [3,1,3,4,3], k = 6
# Output: 1

nums2 = [3, 1, 3, 4, 3]
k2 = 6

print(f"2. Max operations: {Solution().maxOperations(nums2, k2)}")
