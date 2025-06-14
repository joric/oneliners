from lc import *

# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/discuss/3402006/Python-3-oror-13-lines-bisect_left-wexample-oror-TM%3A-97-13

class Solution:
    def minimizeMax(self, a: List[int], p: int) -> int:
        n = len(a)
        a.sort()
        b = sorted({a[i]-a[i-1]for i in range(1,n)})
        def f(x):
            c,i = 0,1
            while i<n:
                if a[i]-a[i-1] <= x:
                    c += 1
                    i += 1
                i += 1
            return c
        return p and b[bisect_left(b,p,key=f)]

class Solution:
    def minimizeMax(self, a: List[int], p: int) -> int:
        n=len(a);a.sort();b=sorted({a[i]-a[i-1]for i in range(1,n)});f=lambda x:next((c for _ in[0]*n if not(i<n and(a[i]-a[i-1]<=x and(c:=c+1,i:=i+1),i:=i+1))),(c:=0,i:=1));return p and b[bisect_left(b,p,key=f)]

class Solution:
    def minimizeMax(self, a: List[int], p: int) -> int:
        n=len(a);a.sort();f=lambda x:next((c for _ in[0]*n if not(i<n and(a[i]-a[i-1]<=x and(c:=c+1,i:=i+1),i:=i+1))),(c:=0,i:=1));return p and bisect_left(range(20**7),p,key=f)

# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/solutions/5916466/one-line-solution/?envType=daily-question&envId=2025-06-13

class Solution:
    def minimizeMax(self, a: List[int], p: int) -> int:
        return bisect_left(range(max(a)),1,key=lambda d,q=0,a=sorted(a):sum(q:=q^1 and u-v<=d for v,u in pairwise(a))>=p)

test('''
2616. Minimize the Maximum Difference of Pairs
Medium

467

21

Add to List

Share
You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.

Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.

Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.

 

Example 1:

Input: nums = [10,1,2,7,1,3], p = 2
Output: 1
Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5. 
The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.
Example 2:

Input: nums = [4,2,1,2], p = 1
Output: 0
Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, which is the minimum we can attain.
 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
0 <= p <= (nums.length)/2
''')
