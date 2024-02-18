from lc import *

# https://leetcode.com/problems/max-consecutive-ones-iii/discuss/1305468/Python-3-1-2-lines

class Solution:
    def longestOnes(self, a: List[int], k: int) -> int:
        return max(map(sub,(z:=[i for i,x in enumerate([0,*a,0])if 1-x])[k+1:],z),default=len(a)+1)-1

# https://leetcode.com/problems/max-consecutive-ones-iii/discuss/247564/JavaC%2B%2BPython-Sliding-Window

class Solution:
    def longestOnes(self, a: List[int], k: int) -> int:
        i = 0
        for j in range(len(a)):
            k -= 1 - a[j]
            if k < 0:
                k += 1-a[i]
                i += 1
        return j-i+1

class Solution:
    def longestOnes(self, a: List[int], k: int) -> int:
        i=0;[(k:=k+1-a[i],i:=i+1)for j,x in enumerate(a)if(k:=k-1+x)<0];return len(a)-i

test('''
1004. Max Consecutive Ones III
Medium

8145

108

Add to List

Share
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
0 <= k <= nums.length
Accepted
459,243
Submissions
733,327
''')
