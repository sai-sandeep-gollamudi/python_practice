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
           return min(and)

---02/06---
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}
        for i in strs:
            t=''.join(sorted(i))
            if t not in hm:
                hm[t]=[i]
            else:
                hm[t].append(i)
        ans=[]
        for k,v in hm.items():
            ans.append(v)
        return and

---02/07---
def frequencySort(self, s: str) -> str:
    hm=Counter()
    for i in s:
        hm[i]+=1
    
    out=[]
    for k,v in hm.most_common():
        out.append(k*v)
    return "".join(out)

def sortedArray(a: [int], b: [int]) -> [int]:
    # Write your code her
    inp1=list(set(a))
    inp2=list(set(b))
    inp1.sort()
    inp2.sort()
    #print(inp1,inp2)
    ans=[]
    i=0
    j=0
    while(i<len(inp1) and j<len(inp2)):
        if(inp1[i]==inp2[j]):
            ans.append(inp1[i])
            i+=1
            j+=1
        elif(inp1[i]>inp2[j]):
            ans.append(inp2[j])
            j+=1
        else:
            ans.append(inp1[i])
            i+=1
    if(i==len(inp1)):
        for k in range(j,len(inp2)):
            ans.append(inp2[k])
    else:
        for k in range(i,len(inp1)):
            ans.append(inp1[k])
    return and


def rotateArray(arr: [], n: int) -> []:
    # Write your code from here.
    temp=arr[0]
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[-1]=temp
    return arr
    pass

def missingNumber(self, nums: List[int]) -> int:
nums.sort()
        for i in range(0,len(nums)):
            if(i!=nums[i]):
                return i
        return len(nums)

def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    m=0
    temp=0
    for i in range(len(nums)):
        if(nums[i]==1):
            temp+=1
        else:
            m=max(m,temp)
            temp=0
    return max(m,temp)

def singleNumber(self, nums: List[int]) -> int:
    dict={}
    for i in range(len(nums)):
        if nums[i] in dict:
            dict[nums[i]]+=1
        else:
            dict[nums[i]]=1
    
    for key,value in dict.items():
        if(value==1):
            return key
            
def check(self, nums: List[int]) -> bool:
        t=0
        for i in range(len(nums)-1):
            if(nums[i]>nums[i+1]):
                t=i+1
                break
        
        temp = []
        temp = nums[t:] + nums[:t]
        for i in range(len(temp)-1):
            if(temp[i]>temp[i+1]):
                return False
        return True
    
