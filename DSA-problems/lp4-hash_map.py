def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
    set1 = set(nums1)
    set2 = set(nums2)
    unique1 = list(set1 - set2)
    unique2 = list(set2 - set1)
    return [unique1, unique2]

####

def uniqueOccurrences(self, arr: List[int]) -> bool:
    hm = Counter()
    for i in arr:
        hm[i] += 1

    seen = []
    for k, v in hm.items():
        if v in seen:
            return False
        else:
            seen.append(v)
    return True

#######
def closeStrings(self, word1: str, word2: str) -> bool:
    
   hm1=Counter(word1)
   hm2=Counter(word2)
   if((sorted(hm1.values())==sorted(hm2.values())) and hm1.keys()== hm2.keys()):
       return True
   return False
