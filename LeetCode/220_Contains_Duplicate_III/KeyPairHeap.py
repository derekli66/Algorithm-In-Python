import typing
import pdb


class KeyPairHeap:
    def __init__(self):
        self.array = []
        self.array.append(None)

    def parentIndex(self, index: int) -> int:
        return int(index / 2)

    def leftChildIndex(self, index: int) -> int:
        return 2 * index

    def rightChildIndex(self, index: int) -> int:
        return 2 * index + 1

    def insert(self, pair: tuple):
        self.array.append(pair)
        index = len(self.array) - 1

        while index > 1:
            if self.array[self.parentIndex(index)][0] < self.array[index][0]:
                temp = self.array[self.parentIndex(index)]
                self.array[self.parentIndex(index)] = self.array[index]
                self.array[index] = temp
                index = self.parentIndex(index)
            else:
                break

    def heapSize(self) -> int:
        return len(self.array) - 1

    def top(self) -> tuple:
        if len(self.array) == 1:
            return None
        return self.array[1]

    def pop(self) -> tuple:
        max = self.top()
        last = len(self.array) - 1
        first = 1

        temp = self.array[last]
        self.array[last] = self.array[first]
        self.array[first] = temp
        self.array.pop(last)

        self.heapify(first)

        return max

    def heapify(self, index: int):
        largest = index
        lChildIndex = self.leftChildIndex(index)
        rChildIndex = self.rightChildIndex(index)

        if lChildIndex < len(
                self.array
        ) and self.array[lChildIndex][0] > self.array[largest][0]:
            largest = lChildIndex

        if rChildIndex < len(
                self.array
        ) and self.array[rChildIndex][0] > self.array[largest][0]:
            largest = rChildIndex

        if largest != index:
            temp = self.array[largest]
            self.array[largest] = self.array[index]
            self.array[index] = temp
            self.heapify(largest)


# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list, k: int,
                                      t: int) -> bool:
        if len(nums) == 0: return False

        pairHeap = KeyPairHeap()
        decendingArray = []
        for idx, num in enumerate(nums):
            pairHeap.insert((num, idx))

        result = False
        containsDuplicated = False
        while pairHeap.heapSize() > 1:
            first = pairHeap.pop()
            decendingArray.append(first)
            second = pairHeap.top()
            if first[0] == second[0]:
                containsDuplicated = True

            if abs(first[0] - second[0]) <= t and abs(first[1] -
                                                      second[1]) <= k:
                result = True
                break

        if containsDuplicated:
            return result

        decendingArray.append(pairHeap.pop())
        print(f"decendingArray: {decendingArray}.")
        return self.findNearbyAlmost(decendingArray, k, t)

    def findNearbyAlmost(self, sortedPairs: list, k: int, t: int) -> bool:
        idx1 = len(sortedPairs) - 1
        while idx1 >= 0:
            idx2 = idx1 - 1

            while idx2 >= 0:
                if abs(sortedPairs[idx1][0] -
                       sortedPairs[idx2][0]) <= t and abs(
                           sortedPairs[idx1][1] - sortedPairs[idx2][1]) <= k:
                    print(
                        f"first {sortedPairs[idx1]}. second {sortedPairs[idx2]}"
                    )
                    return True

                idx2 = idx2 - 1

            idx1 = idx1 - 1

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
result = Solution().containsNearbyAlmostDuplicate(nums, k, t)
print(f"result: {result}")
