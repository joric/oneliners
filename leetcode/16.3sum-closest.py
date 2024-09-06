from lc import *

# https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, v: List[int], target: int) -> int:
        n = len(v)
        v.sort()
        res = 0
        d = inf
        for k in range(n-2):
            i = k+1
            j = n-1
            x = target-k
            while i<j:
                a,b,c = v[k],v[i],v[j]
                s = a+b+c
                if s<target:
                    i+=1
                elif s>target:
                    j-=1
                else:
                    return s
                dt = abs(s-target)
                if dt<d:
                    res = s
                    d = dt 
        return res

# https://leetcode.com/problems/3sum-closest/discuss/279263/Python-7-lines-beat-96.71

class Solution:
    def threeSumClosest(self, v: List[int], t: int) -> int:
        v,r,e = sorted(v),inf,len(v)-1
        for c in range(len(v)-2):
            i = max(c+1,bisect_left(v,t-v[e]-v[c],c+1,e)-1)
            j = e
            while r!=t and i<j:
                s = v[c]+v[i]+v[j]
                r = min(r, s, key=lambda x:abs(x-t))
                i += s<t
                j -= s>t
        return r

class Solution:
    def threeSumClosest(self, v: List[int], t: int) -> int:
        v,r,e = sorted(v),inf,len(v)-1;[(i:=max(c+1,bisect_left(v,t-v[e]-v[c],c+1,e)-1),j:=e,all(r!=t and i<j and(s:=v[c]+v[i]+v[j],r:=min(r, s, key=lambda x:abs(x-t)),i:=i+(s<t),j:=j-(s>t))for _ in v))for c in range(len(v)-2)];return r

test('''
16. 3Sum Closest
Medium

10530

572

Add to List

Share
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
Accepted
1,293,147
Submissions
2,809,206
''')
