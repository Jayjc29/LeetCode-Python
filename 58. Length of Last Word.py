class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        i = len(s)-1

        while i >= 0 and i ==' ':
            i = i -1 
        
        while i >= 0 and i != ' ':
            count = count +1
            i = i-1
        return count