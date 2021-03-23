import typing
from typing import List
import pdb


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        maxProd = nums[0]
        cMax = nums[0]  # cMax == contiguousMax
        cMin = nums[0]  # cMin == contiguousMin

        for value in nums[1:len(nums)]:
            tempMax = max(max(cMax * value, value), cMin * value)
            tempMin = min(min(cMax * value, value), cMin * value)
            maxProd = max(maxProd, tempMax)
            cMax = tempMax
            cMin = tempMin
            pdb.set_trace()

        return maxProd


# def productOfArray(nums: List[int]) -> int:
#     if len(nums) == 0:
#         return 0

#     prod = 1
#     for value in nums:
#         prod = prod * value

#     return prod

# array = [1, 2, 3, 4, 5]
# prod = productOfArray(array[0:0])
# prod2 = productOfArray(array[5:5])

# print(f"prod: {prod}")
# print(f"prod2: {prod2}")

# Input: nums = [2,3,-2,4]
# Output: 6

# nums = [2, 3, -2, 4]
# print(f"Max product: {Solution().maxProduct(nums)}")

# Input: nums = [-2,0,-1]
# Output: 0

# nums2 = [-2, 0, -1]
# print(f"Max product: {Solution().maxProduct(nums2)}")

# nums3 = [2, 3, -2, 4]
# print(f"Max product: {Solution().maxProduct(nums3)}")

nums4 = [-4, -3, -2]
print(f"Max product: {Solution().maxProduct(nums4)}")