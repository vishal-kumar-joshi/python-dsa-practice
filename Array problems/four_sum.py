class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        temp = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                left = j+1
                right = len(nums) - 1
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if current_sum == target:
                        temp.append([nums[i],nums[j],nums[right],nums[left]])
                        while left < right and nums[left] == nums[left+1]:
                            left = left + 1
                        while left < right and nums[right] == nums[right-1]:
                            right = right - 1

                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left +=1
                    else:
                        right -=1
        return temp

    
if __name__ == "__main__":
    s = Solution()
    n = [1,0,-1,0,-2,2]
    result = s.fourSum(n,target=0)
    print(result)