### Dictionary  Code 1 ###########

from collections import Counter 

dict1= [1,2,1,3,4,1,1,1]
print(Counter(dict1))

############# Code 2 #############
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict2={}
        
        for i in nums:
            if i not in dict2:
                dict2[i]=1
            else:
                dict2[i]+=1
                return True
        
        return False
###############Code 3 ##############

class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1        
        
  ###################### Code 4 ############

class Solution:
     def majorityElement(self, nums: List[int]) -> int:
        def get_key(val):
            for key, value in dict1.items():
                if val == value:
                     return key
   
        dict1={}
        for i in nums:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        maxi=max(dict1.values())
        return get_key(maxi)
    
    ######### Code 5 ####################
    len(dict1)   #length of the dictionary
    
    ############### Longest Pallindrome ########
    class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans=0
        for v in collections.Counter(s).values():
            ans = ans + (v//2) *2
            if v%2==1 and ans%2==0:
                ans += 1
        return ans
    
