class Solution:
    def maxArea(self, height: list[int]) -> int:
        low = 0
        high = len(height) - 1
        area = 0
        while(low != high):
                length = high - low

                if height[low] < height[high]:
                     minimum_height = height[low]
                     low = low + 1
                else:
                    minimum_height = height[high]
                    high = high - 1

                temp = minimum_height * length
                if area < temp :
                     area = temp
        return area
    
if __name__ == "__main__":
     s_obj = Solution()
     height = [1,8,6,2,5,4,8,3,7]
     result = s_obj.maxArea(height)
     print(result)