class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        temp = {}
        for i in range(len(nums)):
            num = nums[i]
            check = target - num

            if check in temp:
               index = temp[check]
               return [index , i]
            
            temp[num] = i
            
if __name__ == "__main__":
    s_obj = Solution()
    nums = [4,5,6,1,2]
    target = 11
    result = s_obj.twoSum(nums, target)
    print(result)
            
