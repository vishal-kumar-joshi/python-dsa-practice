class Solution:
    def check(self, nums: list[int]) -> bool:
        count = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                count = count+1

        if nums[-1] > nums[0]:
            count = count + 1
            
        if count <= 1:
            return True
        else:
            return False
        

if __name__ == "__main__":
    s_obj = Solution()
    a = [2,1,3,4]
    print(s_obj.check(a))


