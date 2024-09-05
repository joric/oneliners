from lc import *

# https://leetcode.com/problems/majority-element

# partition
class Solution:
    def majorityElement(self, a: List[int]) -> int:
        n = len(a)
        def partition(lo, hi):
            piv, k = a[hi], lo
            for i in range(lo, hi):
                if a[i] < piv:
                    a[i], a[k] = a[k], a[i]
                    k += 1
            a[k], a[hi] = a[hi], a[k]
            return k
        lo, hi = 0, n - 1
        mid = n // 2
        while True:
            k = partition(lo, hi)
            if k == mid:
                return a[mid]
            elif k < mid:
                lo = k + 1
            else:
                hi = k - 1

# boyer-moore majority vote

class Solution:
    def majorityElement(self, n: List[int]) -> int:
        r=c=0
        for x in n: 
            if c == 0:
                r = x
            c += 1 if x==r else -1
        return r

class Solution:
    def majorityElement(self, n: List[int]) -> int:
        r=c=0;[(c==0 and(r:=x),c:=c+(-1,1)[x==r])for x in n];return r

# https://leetcode.com/problems/majority-element/discuss/2100014/Python-Shortest-Code-of-all-time-guaranteed

class Solution:
    def majorityElement(self, n: List[int]) -> int:
        return Counter(n).most_common(1)[0][0]

class Solution:
    def majorityElement(self, n: List[int]) -> int:
        return sorted(n)[len(n)//2]

# statistics.mode

class Solution:
    def majorityElement(self, n: List[int]) -> int:
        return mode(n)

test('''
169. Majority Element
Easy

18079

565

Add to List

Share
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 10^4
-10^9 <= nums[i] <= 10^9

Follow-up: Could you solve the problem in linear time and in O(1) space?
Accepted
2,428,775
Submissions
3,796,641
''')