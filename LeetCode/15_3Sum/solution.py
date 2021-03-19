import typing
from typing import List


class Solution:
    def binarySearch(self, sortedNums: List[int], target: int, lowIndex: int,
                     highIndex: int):
        midIndex = (lowIndex + highIndex) // 2

        while lowIndex <= highIndex:
            if target < sortedNums[midIndex]:
                highIndex = midIndex - 1
                midIndex = (lowIndex + highIndex) // 2
            elif target > sortedNums[midIndex]:
                lowIndex = midIndex + 1
                midIndex = (lowIndex + highIndex) // 2
            else:
                return True

        return False

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. sort nums
        # 2. start iterate from 0 index and end at value greater than zero
        # 3. use binary search to find triplets

        nums.sort()
        length = len(nums)
        results = []
        duplicated = {}

        idx = 0
        while idx < length and nums[idx] < 1:
            num1 = nums[idx]

            # Take num2 from range idx + 1 to length
            # then do binary search for range idx + 2 to length
            j = idx + 1
            while j < length:
                num2 = nums[j]

                # Do binary searach for num3
                num3 = 0 - num1 - num2
                if self.binarySearch(nums, num3, j + 1, length - 1) == True:
                    hashing = f"{num1}{num2}{num3}"
                    if hashing not in duplicated:
                        results.append([num1, num2, num3])
                        duplicated[hashing] = True

                j += 1

            idx += 1

        return results


# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

nums = [-1, 0, 1, 2, -1, -4]
print(f"{Solution().threeSum(nums)}")

# Input: nums = []
# Output: []

nums2 = []
print(f"{Solution().threeSum(nums2)}")

# Input: nums = [0]
# Output: []

nums3 = [0]
print(f"{Solution().threeSum(nums3)}")