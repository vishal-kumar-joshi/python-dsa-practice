class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        mearge_array = nums1 + nums2
        mearge_array.sort()
        low = 0
        high = len(mearge_array) - 1
        mid = (low + high) / 2
        if (len(mearge_array) % 2) == 0:
            middal = (mearge_array[int(mid)] + mearge_array[int(mid)+1]) / 2
            return middal
        else:
            return mearge_array[int(mid)]

if __name__ == "__main__":
    s_obj = Solution()
    num1 = [1,2]
    num2 = [3,4]
    result = s_obj.findMedianSortedArrays(num1 , num2)
    print(result)