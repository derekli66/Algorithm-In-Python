import typing
from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        checked = {}
        maxLen = 0
        for index in range(len(nums)):
            idx = index
            nested = set()

            while (nums[idx] not in nested) and checked.get(nums[idx]) == None:
                nested.add(nums[idx])
                checked[nums[idx]] = True
                idx = nums[idx]

            maxLen = max(maxLen, len(nested))

        return maxLen


# Input: A = [5,4,0,3,1,6,2]
# Output: 4

A = [5, 4, 0, 3, 1, 6, 2]
print(f"[DEBUG][RESULT] {Solution().arrayNesting(A)}")