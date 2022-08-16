######### List.append() method ###########
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        lis=[]
        for i in range(1,n+1):
          lis.append(str(i))
        return lis
################ reverse a list ###########

class Solution:
    def reverse(self, nums,l,r):
        while l<r:
                nums[l], nums[r] =  nums[r], nums[l]
                l,r= l+1, r-1
