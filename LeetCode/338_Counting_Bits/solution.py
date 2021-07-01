import typing
from typing import List

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return (n & (n - 1)) == 0
    
    def countBits(self, n: int) -> List[int]:
        dp = [ 0  for _ in range(n + 1)]
        
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        
        lastPowerOfTwo = 2
        idx = 3
        while  idx < n + 1:
            if self.isPowerOfTwo(idx):
                lastPowerOfTwo = idx
                
            dp[idx] = dp[idx - lastPowerOfTwo] + 1
            
            idx += 1

        return dp
    
# Input: n = 5
# Output: [0,1,1,2,1,2]

print(f"{Solution().countBits(8)}")