def findMaxAverage(self, nums: List[int], k: int) -> float:
    left = sumv = cavg = c = t = 0
    for right in range(len(nums)):
        sumv += nums[right]
        c += 1
        if (c == k):
            t = round(sumv / k, 5)
            c -= 1
            if (cavg == 0):
                cavg = t
            cavg = max(cavg, t)
            sumv -= nums[left]
            left += 1
    return cavg

---

def maxVowels(self, s: str, k: int) -> int:
    c = 0
    ws = 0
    ans = 0
    for i in range(len(s)):
        temp = s[i]
        if (ws == k):
            if (s[i - k] in ['a', 'e', 'i', 'o', 'u']):
                ans = max(ans, c)
                c -= 1
            ws -= 1
        if (s[i] in ['a', 'e', 'i', 'o', 'u']):
            c += 1
        ws += 1
    return max(ans, c)
