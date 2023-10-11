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




