class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
          i = len(nums) - 2
          while i >= 0 and nums[i] >= nums[i+1]:
               i = i -1
          if i < 0:
               nums.reverse()
               return
          j = len(nums) - 1
          while nums[j] <= nums[i]:
               j = j -1
          temp = nums[i]
          nums[i] = nums[j]
          nums[j] = temp

          nums[i+1:] = reversed(nums[i + 1:])
          return nums

if __name__ == "__main__":
    s = Solution()
    n = [1,3,5,4,2]
    result = s.nextPermutation(n)
    print(result)
                    
     


