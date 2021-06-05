import typing
from typing import List 
import sys


class Solution:
    def __init__(self) -> None:
        self.amount_memorization = {}
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        miniCount = self.coinChange__(coins, amount)
        
        if miniCount < sys.maxsize:
            return miniCount
        
        return -1
        
    def coinChange__(self, coins: List[int], amount: int) -> int:
        if self.amount_memorization.get(amount) != None:
            return self.amount_memorization[amount]
        
        if amount == 0:
            return 0
        
        miniStep = sys.maxsize
        idx = 0 
        while idx < len(coins):
            if amount >= coins[idx]:
                remainingAmount = amount - coins[idx]
                # print(f"amount: {amount}. remainingAmount: {remainingAmount}")
                currentStep = self.coinChange__(coins, remainingAmount)
                miniStep = min(currentStep + 1, miniStep)
                
            idx += 1
        
        if miniStep < sys.maxsize:
            
            self.amount_memorization[amount] = miniStep
            return miniStep
        
        self.amount_memorization[amount] = sys.maxsize
        return sys.maxsize
    
# Input: coins = [1,2,5], amount = 11
# Output: 3

coins = [1,2,5]
amount = 11
print(f"Output1: {Solution().coinChange(coins, amount)}")

#Input: coins = [2], amount = 3
# Output: -1
coins = [2]
amount = 3
print(f"Output2: {Solution().coinChange(coins, amount)}")
