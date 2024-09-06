from lc import *

# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, v: List[int]) -> List[List[int]]:
        res = []
        v.sort()
        for i in range(len(v)):
            if (i>0) and (v[i]==v[i-1]):
                continue
            l = i+1
            r = len(v)-1
            while l<r:
                s = v[l]+v[r]+v[i]
                if s<0:
                    l+=1
                elif s>0:
                    r-=1
                else:
                    res.append((v[i], v[l], v[r]))
                    while l<r and v[l]==v[l+1]:
                        l+=1
                    while l<r and v[r]==v[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return res

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        map_num_idx = {num: i for i, num in enumerate(nums)}
        for i1 in range(n):
            if i1 > 0 and nums[i1] == nums[i1 - 1]:
                continue
            for i2 in range(i1 + 1, n):
                if i2 > i1 + 1 and nums[i2] == nums[i2 - 1]:
                    continue
                target = -(nums[i1] + nums[i2])
                if target in map_num_idx and map_num_idx[target] > i2:
                    ans.append([nums[i1], nums[i2], target])
        return ans

# https://leetcode.com/problems/3sum/discuss/504915/8-lines-PythonEasy-Understandbeats-99

class Solution:
    def threeSum(self, v: List[int]) -> List[List[int]]:
        c=Counter(v);p,r,b=sorted(c),c[0]>=3 and set([(0,0,0)])or set(),bisect_left;[(c[a]>1 and -2*a in c and a and r.add((a,a,-2*a)),a<0 and[r.add((a,b,-a-b)) for b in p[b(p,-p[-1]-a,i+1):b(p,ceil(-a/2),i+1)] if -(a+b) in c])for i,a in enumerate(p)];return r

test('''
15. 3Sum
Medium

31216

2911

Add to List

Share
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
Accepted
3,866,473
Submissions
10,967,227
''', check=lambda r,e,*a: sorted(r)==sorted(e))
