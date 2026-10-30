# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        for j in range (len(nums)):
            if nums[j] != val:
               nums[i] = nums[j]
               i+=1
        return i
            
if __name__ == "__main__":
    s = Solution()
    n = [3,2,2,3]
    val = 3
    result = s.removeElement(n,val)
    print(result)

