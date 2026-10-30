class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        comman_prefix = ""
        temp = strs[0]
        for i in range(len(temp)): 
            for j in range(len(strs)):
                if i >= len(strs[j]) or strs[j][i] != temp[i]:
                   return comman_prefix
             
            comman_prefix = comman_prefix + strs[j][i]
        return comman_prefix


if __name__ == "__main__":
    s = Solution()
    strs = ["flower","flow","flight"]
    result = s.longestCommonPrefix(strs)
    print(result)
