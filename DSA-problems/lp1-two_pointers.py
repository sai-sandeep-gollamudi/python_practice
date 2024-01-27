#two pointers problems
def moveZeroes(self, nums: List[int]) -> None: #283
    """
    Do not return anything, modify nums in-place instead.
    """
    w = 0
    r = 0
    while (r < len(nums)):
        if (nums[r] != 0):
            nums[w] = nums[r]
            w += 1
        r += 1

    while (w < len(nums)):
        nums[w] = 0
        w += 1

---

def maxArea(self, height: List[int]) -> int:
    area = 0
    l = 0
    temp = 0
    r = len(height) - 1
    while l < r:
        w = r - l
        temp = w * min(height[l], height[r])
        area = max(area, temp)
        if (height[l] >= height[r]):
            r -= 1
        else:
            l += 1
    return area

---


def maxOperations(self, nums: List[int], k: int) -> int:
    nums.sort()
    l = 0
    r = len(nums) - 1
    ans = 0
    temp = 0
    while (l < r):
        temp = nums[l] + nums[r]
        if (temp == k):
            ans += 1
            l += 1
            r -= 1
        elif (temp > k):
            r -= 1
        else:
            l += 1
    return ans

---

def isSubsequence(self, s: str, t: str) -> bool:
    if(len(s)==0):
        return True
    elif(len(t)==0):
        return False
    p1=0
    p2=0
    while(p2<len(t) and p1<len(s)):
        if(s[p1]==t[p2]):
            p1+=1
        p2+=1
    if(p1==len(s)):
        return True
    else:
        return False
