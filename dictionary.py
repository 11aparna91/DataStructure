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
########### Problem Number 1647 ##############################
########### Time Complexity= O(n) Space Complexity=O(n) ######
class Solution:
    def minDeletions(self, s: str) -> int:
        dict1= collections.Counter(s)

        set1=set()
        count=0
        for key,val in dict1.items():
            while val>0 and val in set1:
                val -=1
                count +=1
            set1.add(val)
        return count    
######################### Problem Number 1347 ############

from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt1=Counter(s)
        cnt2=Counter(t)
        sum=0
        for key,value in cnt1.items():
            if value>cnt2[key]:
                sum += (value - cnt2[key])
        return sum
########## Problem Number 299 ######
################ Solution 1 ########

s, g = Counter(secret), Counter(guess)
a = sum(i == j for i, j in zip(secret, guess))
return '%sA%sB' % (a, sum((s & g).values()) - a)

########## Solution 2 ##################
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls=0
        cows=0
        s=defaultdict(int)
        g=defaultdict(int)
        print(s,g)
        for i,j in zip(secret,guess):
            if i==j:
                bulls +=1
            else:
                s[i] +=1
                g[j] +=1
        cows=0
        for k in s:
            cows += min(s[k],g[k])
        return "{}A{}B".format(bulls,cows)
