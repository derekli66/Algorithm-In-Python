import typing
from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        counts = [0 for i in range(len(citations)+1)]
        
        for cit in citations:
            current = counts[min(cit, len(citations))]
            counts[min(cit, len(citations))] = current + 1
            
        sum = 0
        for idx in reversed(range(len(citations))):
            sum += counts[idx]
            if sum >= idx:
                return idx
        
        return 0        