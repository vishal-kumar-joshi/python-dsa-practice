class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        comman = 0
        result = []
        set_a = set()
        set_b = set()
        for i in range(len(A)):
            set_a.add(A[i])
            set_b.add(B[i])
            comman =  len(set_a.intersection(set_b)) 
            result.append(comman)
        return result
        

if __name__ == "__main__":
    obj = Solution()
    A = [2,1,3,5,4]
    B = [1,2,3,4,5]
    ans = obj.findThePrefixCommonArray(A , B )
    print(ans)
   







        