import pdb


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list, k: int,
                                      t: int) -> bool:
        # if len(nums) < k:
        #     # pdb.set_trace()
        #     return False

        if len(nums) < k:
            k = len(nums)

        fIndex = 0
        bIndex = fIndex + k + 1

        while fIndex < len(nums):
            subarray = nums[fIndex:bIndex]
            subarray.sort()
            # pdb.set_trace()

            for idx in range(len(subarray)):
                if idx + 1 >= len(subarray):
                    break

                if abs(subarray[idx] - subarray[idx + 1]) <= t:
                    # pdb.set_trace()
                    return True

            fIndex += 1
            bIndex += 1

        # pdb.set_trace()
        return False


# nums = [1, 2, 3, 1]
# k = 3
# t = 0

# nums = [1, 5, 9, 1, 5, 9]
# k = 2
# t = 3

nums = [10, 100, 11, 9, 100, 10]
k = 1
t = 2

# nums = [2147483646, 2147483647]  # True
# k = 3
# t = 3

result = Solution().containsNearbyAlmostDuplicate(nums, k, t)
print(f"result: {result}")