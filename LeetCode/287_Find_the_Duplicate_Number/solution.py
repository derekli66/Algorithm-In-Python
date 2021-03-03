class Solution:
    def findDuplicate(self, nums: list) -> int:
        sorted_nums = nums.copy()
        sorted_nums.sort()
        length = len(sorted_nums) - 1

        for idx in range(length):
            if sorted_nums[idx + 1] - sorted_nums[idx] == 0:
                return sorted_nums[idx]

        return None


# Input: nums = [1,3,4,2,2]
# Output: 2
nums = [1, 3, 4, 2, 2]

# Input: nums = [3,1,3,4,2]
# Output: 3

# Input: nums = [1,1]
# Output: 1

# Input: nums = [1,1,2]
# Output: 1

duplicate = Solution().findDuplicate(nums)
print(f"{duplicate}")