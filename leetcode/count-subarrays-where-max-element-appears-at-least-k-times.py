from lc import *

# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/discuss/4388007/Python3-no-sliding-3-lines-solution

class Solution:
    def countSubarrays(self, a: List[int], k: int) -> int:
        m=max(a);d=[-1]+[i for i,n in enumerate(a)if n==m];return sum((d[i]-d[i-1])*(len(a)-d[i+k-1])for i in range(1,len(d)-k+1))

class Solution:
    def countSubarrays(self, a: List[int], k: int) -> int:
        m,n=max(a),len(a);d=[i for i in range(n)if a[i]==m]+[n];return sum((d[i]+1)*(d[i+k]-d[i+k-1])for i in range(len(d)-k))

class Solution:
    def countSubarrays(self, a: List[int], k: int) -> int:
        m,n=max(a),len(a);d=[i for i in range(n)if a[i]==m]+[n];return sum((d[i]+1)*(d[i+k]-d[i+k-1])for i in range(len(d)-k))

# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/discuss/4384405/JavaC%2B%2BPython-Sliding-Window

class Solution:
    def countSubarrays(self, a: List[int], k: int) -> int:
        r=c=i=0
        m=max(a)
        for j in range(len(a)):
            c += a[j]==m
            while c>=k:
                c -= a[i]==m
                i += 1
            r += i
        return r

class Solution:
    def countSubarrays(self, a: List[int], k: int) -> int:
        c=i=0;m=max(a);return sum((c:=c+(a[j]==m),all(c>=k and(c:=c-(a[i]==m),i:=i+1)for _ in a),i)[2]for j in range(len(a)))

test('''
2962. Count Subarrays Where Max Element Appears at Least K Times
Medium

267

13

Add to List

Share
You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
Example 2:

Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= k <= 105
Accepted
17,043
Submissions
37,760
''')
