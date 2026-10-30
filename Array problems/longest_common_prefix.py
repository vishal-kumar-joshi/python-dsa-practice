class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        prefixes = set()
        
        for num in arr1:
            s = str(num)
            for i in range(1, len(s) + 1):
                prefixes.add(s[:i])
        maximum = 0
        for num in arr2:
            s = str(num)
            for i in range(1, len(s) + 1):
                if s[:i] in prefixes:
                    maximum = max(maximum, i)
                else:
                    break
                    
        return maximum

if __name__ == "__main__" : 
    s_obj = Solution()
    arr1 = [1234 , 234]
    arr2 = [1324 , 234]
    result = s_obj.longestCommonPrefix(arr1 , arr2)
    print(result)  