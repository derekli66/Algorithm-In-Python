#%%
import typing
from typing import List

vowel = ['a', 'e', 'i', 'o', 'u']

class Solution:

    def countVowelStrings__(self, inputString: str, startIndex:int, n: int) -> int:
        if n == 0:
            return 1
        
        if startIndex >= len(vowel):
            return 0
        
        currentIndex = startIndex
        totalCount = 0
        while currentIndex < len(vowel):
            newString = inputString + vowel[currentIndex]
            totalCount = totalCount + self.countVowelStrings__(newString, currentIndex, n - 1)
            currentIndex += 1
        
        return totalCount
    
    def countVowelStrings(self, n: int) -> int:
        return self.countVowelStrings__("", 0, n)


n = 2
print(f"{Solution().countVowelStrings(n)}")


# %%
