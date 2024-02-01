def largestAltitude(self, gain: List[int]) -> int:
    ans = []
    ans.append(0)
    for i in range(len(gain)):
        ans.append(ans[i] + gain[i])
    return max(ans)

---

def pivotIndex(self, nums: List[int]) -> int:
    l = sl = 0
    ts = sum(nums)
    r = len(nums)
    while (l < r):
        if (sl == (ts - sl) - nums[l]):
            return l
        sl = sl + nums[l]
        l += 1
    return -1
