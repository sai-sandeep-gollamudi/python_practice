def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
    nums.sort()
    # ans=[0]*(len(nums)//3)
    ans = []
    for i in range(0, len(nums), 3):
        if (nums[i + 2] - nums[i] > k):
            return []
        ans.append([nums[i], nums[i + 1], nums[i + 2]])
    return ans

---02/05---
    def firstUniqChar(self, s: str) -> int:
        hm=Counter()
        for i in range(len(s)):
            if s[i] in hm:
                hm[s[i]]=100001
            else:
                hm[s[i]]=i
        ans=[]
        for k,v in hm.items():
            if v!=100001:
                ans.append(v)
        if len(ans)==0:
            return -1
        else:
           return min(ans)
