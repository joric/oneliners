from lc import *

# https://leetcode.com/problems/continuous-subarrays

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        pre_idx = {}
        ans = 0
        next_idx = 0 
        for index, num in enumerate(nums):
            for seen_num in [pre_num for pre_num in pre_idx if abs(num - pre_num) > 2]:
                next_idx = max(next_idx, pre_idx[seen_num] + 1)
                del pre_idx[seen_num]
            ans += index - next_idx + 1
            pre_idx[num] = index
        return ans

# https://leetcode.com/problems/continuous-subarrays/discuss/3706729/Python-DFS%2BMemoization-16-lines

class Solution:
    def continuousSubarrays(self, a: List[int]) -> int:
        return sum((f:=cache(lambda j,x,y:j<len(a)and abs((x:=min(x,a[j]))-(y:=max(y,a[j])))<3 and 1+f(j+1,x,y)))(i,x,x)for i,x in enumerate(a))

test('''
2762. Continuous Subarrays
Medium

863

38

Add to List

Share
You are given a 0-indexed integer array nums. A subarray of nums is called continuous if:

Let i, i + 1, ..., j be the indices in the subarray. Then, for each pair of indices i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2.
Return the total number of continuous subarrays.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [5,4,2,4]
Output: 8
Explanation: 
Continuous subarray of size 1: [5], [4], [2], [4].
Continuous subarray of size 2: [5,4], [4,2], [2,4].
Continuous subarray of size 3: [4,2,4].
Thereare no subarrys of size 4.
Total continuous subarrays = 4 + 3 + 1 = 8.
It can be shown that there are no more continuous subarrays.
 

Example 2:

Input: nums = [1,2,3]
Output: 6
Explanation: 
Continuous subarray of size 1: [1], [2], [3].
Continuous subarray of size 2: [1,2], [2,3].
Continuous subarray of size 3: [1,2,3].
Total continuous subarrays = 3 + 2 + 1 = 6.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
Accepted
34,380
Submissions
71,834
''')
