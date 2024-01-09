'''
# lc ---- remove elements
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        for i in range(len(nums)):
            if (nums[i] == val):
                c += 1
                nums[i] = 99999

        nums.sort()
        return (len(nums) - c)


#lc ---- length of last word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        store=[]
        store = s.split()
        l=len(store[-1])
        return l

#lc ----  Add binary
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l=[]
        i=len(a)-1
        j=len(b)-1
        carry = 0

        while i>=0 or j>=0 or carry:
            if(i>=0):
                carry+=int(a[i])
                i-=1
            if(j>=0):
                carry+=int(b[j])
                j-=1
            l.append(str(carry%2))
            carry=carry//2
        return ''.join(reversed(l))

'''
#########################################################

lc-75

    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = min(len(word1), len(word2))
        res = ""
        for i in range(l):
            res = res + word1[i] + word2[i]
        if (l < len(word1)):
            for i in range(l, len(word1)):
                res = res + word1[i]
        else:
            for i in range(l, len(word2)):
                res = res + word2[i]
        return res


    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1,l2 = len(str1),len(str2)
        for i in range(l2,0,-1):
            if(l1%i==0 and l2%i==0):
                mt1=l1//i
                mt2=l2//i
                temp=str2[:i]
                if(str1==mt1*temp and str2==mt2*temp):
                    return temp
        temp=""
        return temp

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mv=max(candies)
        minv=mv-extraCandies
        ans=[]
        for i in range(len(candies)):
            if(minv<=candies[i]):
                ans.append(True)
            else:
                ans.append(False)
        return and

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c=0
        i=0
        while(i<len(flowerbed) and c<n):
            if(flowerbed[i]==0):
                if(((i==0) or (flowerbed[i-1]==0)) and ((i==len(flowerbed)-1) or (flowerbed[i+1]==0))):
                    c+=1
                    flowerbed[i]=1
            i+=1
        if(c==n):
            return True
        else:
            return False

    def reverseVowels(self, s: str) -> str:
        vs = []
        for i in range(len(s)):
            if (s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']):
                vs.append(s[i])

        j = -1
        t = ''
        for i in range(len(s)):
            if (s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']):
                t = t + vs[j]
                j -= 1
            else:
                t = t + s[i]
        return t

    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num = float("inf")
        second_num = float("inf")
        for i in range(len(nums)):
            if nums[i]<=first_num:
                first_num=nums[i]
            elif nums[i]<=second_num:
                second_num = nums[i]
            else:
                return True
        return False
