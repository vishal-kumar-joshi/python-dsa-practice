class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                nums[i] = nums[j]
                i +=1
        return (i+1)

if __name__ == "__main__":
    s = Solution()
    n = [1,1,2,2,3,3,4]
    result = s.removeDuplicates(n)
    print(result)


