import typing


class MaxHeap:
    def __init__(self):
        self.array = []
        self.array.append(None)

    def parentIndex(self, index: int) -> int:
        return int(index / 2)

    def leftChildIndex(self, index: int) -> int:
        return 2 * index

    def rightChildIndex(self, index: int) -> int:
        return 2 * index + 1

    def insert(self, key: int):
        self.array.append(key)
        index = len(self.array) - 1

        while index > 1:
            if self.array[self.parentIndex(index)] < self.array[index]:
                temp = self.array[self.parentIndex(index)]
                self.array[self.parentIndex(index)] = self.array[index]
                self.array[index] = temp
                index = self.parentIndex(index)
            else:
                break

    def top(self) -> int:
        if len(self.array) == 1:
            return None
        return self.array[1]

    def pop(self) -> int:
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
                self.array) and self.array[lChildIndex] > self.array[largest]:
            largest = lChildIndex

        if rChildIndex < len(
                self.array) and self.array[rChildIndex] > self.array[largest]:
            largest = rChildIndex

        if largest != index:
            temp = self.array[largest]
            self.array[largest] = self.array[index]
            self.array[index] = temp
            self.heapify(largest)


heap = MaxHeap()
heap.insert(9)
heap.insert(10)
print(f"1. Largest: {heap.top()}. 10")
heap.insert(8)
print(f"After insert 8. Top: {heap.top()}.")
heap.insert(11)
print(f"2. Largest: {heap.top()}. 11")
heap.insert(12)
print(f"3. Largest: {heap.top()}. 12")

value = heap.pop()
print(f"1st pop: {value}. top value: {heap.top()}")

value = heap.pop()
print(f"2nd pop: {value}. top value: {heap.top()}")

value = heap.pop()
print(f"3rd pop: {value}. top value: {heap.top()}")

value = heap.pop()
print(f"4th pop: {value}. top value: {heap.top()}")

value = heap.pop()
print(f"5th pop: {value}. top value: {heap.top()}")