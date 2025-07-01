class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        for i in  strs :
            for j in i :
                print(j,',')





strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))