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
