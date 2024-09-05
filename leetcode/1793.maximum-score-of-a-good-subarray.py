from lc import *

# https://leetcode.com/problems/maximum-score-of-a-good-subarray/discuss/1108351/Python-Binary-search-O(n-log-n)-explained

class Solution:
    def maximumScore(self, a: List[int], k: int) -> int:
        def f(a, k):
            l = [*accumulate(a[:k+1][::-1],min)][::-1]
            r = [*accumulate(a[k:],min)]
            s = 0
            for j in range(len(r)):
                i = bisect_left(l,r[j])
                if i>=0:
                    s = max(s,(k+j-i+1)*r[j])
            return s
        return max(f(a,k),f(a[::-1],len(a)-k-1))

class Solution:
    def maximumScore(self, a: List[int], k: int) -> int:
        return max(((f:=lambda a,k:(l:=[*accumulate(a[:k+1][::-1],min)][::-1],r:=[*accumulate(a[k:],min)],s:=0)and max((i:=bisect_left(l,r[j]))>=0 and(k+j-i+1)*r[j]for j in range(len(r)))))(a,k),f(a[::-1],len(a)-k-1))

# https://leetcode.com/problems/maximum-score-of-a-good-subarray/discuss/1108333/JavaC%2B%2BPython-Two-Pointers

class Solution:
    def maximumScore(self, a: List[int], k: int) -> int:
        r=m=a[k]
        i,j,n = k,k,len(a)
        while i>0 or j<n-1:
            if (i and a[i-1])<(j<n-1 and a[j+1]):
                j += 1
            else:
                i -= 1
            m = min(m,a[i],a[j])
            r = max(r,m*(j-i+1))
        return r

class Solution:
    def maximumScore(self, a: List[int], k: int) -> int:
        r=m=a[k];i,j,n=k,k,len(a);return next(r for _ in a if not((i>0 or j<n-1)and((j:=j+1)if(i and a[i-1])<(j<n-1 and a[j+1])else(i:=i-1),m:=min(m,a[i],a[j]),r:=max(r,m*(j-i+1)))))

class Solution:
    def maximumScore(self, a: List[int], k: int) -> int:
        r=m=a[k];i,j,n=k,k,len(a);[((j:=j+1)if(i and a[i-1])<(j<n-1 and a[j+1])else(i:=i-1),m:=min(m,a[i],a[j]),r:=max(r,m*(j-i+1)))for _ in a if i>0 or j<n-1];return r

class Solution:
    def maximumScore(self, a: List[int], k: int) -> int:
        m=a[k];i,j,n=k,k,len(a);return max([m]+[((j:=j+1)if(i and a[i-1])<(j<n-1 and a[j+1])else(i:=i-1),m:=min(m,a[i],a[j]))and m*(j-i+1)for _ in a if i>0 or j<n-1])

test('''
1793. Maximum Score of a Good Subarray
Hard

1130

35

Add to List

Share
You are given an array of integers nums (0-indexed) and an integer k.

The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.

Return the maximum possible score of a good subarray.

 

Example 1:

Input: nums = [1,4,3,7,4,5], k = 3
Output: 15
Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15. 
Example 2:

Input: nums = [5,5,4,5,4,1,1,1], k = 0
Output: 20
Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.

Example 3:

Input: nums = [5], k = 0
Output: 5

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 2 * 10^4
0 <= k < nums.length
''')