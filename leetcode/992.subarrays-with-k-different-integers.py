from lc import *

# https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/523136/JavaC%2B%2BPython-Sliding-Window

class Solution:
    def subarraysWithKDistinct(self, a: List[int], k: int) -> int:
        def f(a,k):
            c = Counter()
            r = i = 0
            for j in range(len(a)):
                if c[a[j]]==0:
                    k -= 1
                c[a[j]] += 1
                while k<0:
                    c[a[i]] -= 1
                    if c[a[i]]==0:
                        k += 1
                    i += 1
                r += j-i+1
            return r
        return f(a,k)-f(a,k-1)

# https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/1964899/13-Lines-Python

class Solution:
    def subarraysWithKDistinct(self, a: List[int], k: int) -> int:
        def f(k):
            i,r,c=0,0,Counter()
            for j,n in enumerate(a):
                c[n] += 1
                k -= c[n]==1
                while i<=j and k<0:
                    c[a[i]] -= 1
                    k += c[a[i]]==0
                    i += 1
                r += j-i+1
            return r
        return f(k)-f(k-1)

class Solution:
    def subarraysWithKDistinct(self, a: List[int], k: int) -> int:
        return(f:=lambda k,i=0:(c:=Counter())or sum((c.update([n]),k:=k-(c[n]==1),all(i<=j and k<0 and(c.update({a[i]:-1}),k:=k+(c[a[i]]<1),i:=i+1)for _ in a),j-i+1)[3]for j,n in enumerate(a)))(k)-f(k-1)

test('''
992. Subarrays with K Different Integers
Hard

5044

73

Add to List

Share
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i], k <= nums.length
Accepted
118,437
Submissions
208,854
''')