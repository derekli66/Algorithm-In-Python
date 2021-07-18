import typing
import pdb

class Solution:
    def checkFromMiddle(self, s: str, lptr: int, rptr:int) -> int:
        if lptr > rptr or lptr < 0 or rptr >= len(s) or s == None or len(s) == 0:
            return 0
        
        if s[lptr] != s[rptr]: return 1
        
        start = lptr
        end = rptr
        
        while lptr >= 0 and rptr < len(s) and s[lptr] == s[rptr]:
                start = lptr
                end = rptr
                lptr -= 1
                rptr += 1
            
        return end - start + 1    
        
    
    def longestPalindrome(self, s: str) -> str:
        
        start = 0
        end = 0
        
        for idx in range(len(s)):
            len1 = self.checkFromMiddle(s, idx, idx)
            len2 = self.checkFromMiddle(s,idx, idx + 1)
            maxLen = max(len1, len2)

            if maxLen > end - start + 1:
                if maxLen % 2 == 0:
                    # even length
                    start = idx - (maxLen // 2 - 1)
                    end = idx + maxLen // 2                    
                else:
                    # odd length
                    start = idx - maxLen // 2
                    end = idx + maxLen // 2                    
            
        return s[start:end+1]
                    

# Input: s = "babad"
# Output: "bab"

s = "babad"
print(f"Anwser: {Solution().longestPalindrome(s)}")

# Input:
# "cbbd"
# Output:
# "bbd"

s = "cbbd"
print(f"Anwser: {Solution().longestPalindrome(s)}")
