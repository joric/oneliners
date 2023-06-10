from lc import *

#https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/discuss/1119801/JavaC%2B%2BPython-Binary-Search

class Solution:
    def maxValue(self, n, index, maxSum):
        def test(a):
            b = max(a - index, 0)
            res = (a + b) * (a - b + 1) // 2
            b = max(a - ((n - 1) - index), 0)
            res += (a + b) * (a - b + 1) // 2
            return res - a
        maxSum -= n
        left, right = 0, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if test(mid) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left + 1

# https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/discuss/1120350/Clean-Python-3-O(n)-with-two-pointers

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        curr, base = n, 1
        left = right = index
        while (left > 0 or right < n - 1) and curr + (right - left + 1) <= maxSum:
            curr += (right - left + 1)
            base += 1
            left = max(0, left - 1)
            right = min(n - 1, right + 1)
        return base + (maxSum - curr) // n

# https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/discuss/1120350/Clean-Python-3-O(n)-with-two-pointers

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        curr, base = n, 1
        left = right = index
        while (left > 0 or right < n - 1) and curr + (right - left + 1) <= maxSum:
            curr += (right - left + 1)
            base += 1
            left = max(0, left - 1)
            right = min(n - 1, right + 1)
        return base + (maxSum - curr) // n

# https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/discuss/3204026/Python-oror-bisect-oror-short-clean

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def value(l, best):
            if best >= l:
                return (best - l + 1 + best) * l // 2
            else:
                return (1 + best) * best // 2 + (l - best)
        def check(v):
            return value(index, v - 1) + value(n - index, v)
        return bisect_right(range(1, maxSum + 1), False, key=lambda a: check(a) > maxSum)

class Solution:
    def maxValue(self, n: int, i: int, m: int) -> int:
        f=lambda l,b:(b+b-l+1)*l//2 if b>=l else (1+b)*b//2+(l-b)
        c=lambda v:f(i,v-1)+f(n-i,v)
        return bisect_right(range(1,m+1),0,key=lambda a:c(a)>m)

class Solution:
    def maxValue(self, n: int, i: int, m: int) -> int:
        f=lambda l,b:((b+b-l+1)*l//2,(1+b)*b//2+(l-b))[b<l];return bisect_right(range(1,m+1),0,key=lambda x:f(i,x-1)+f(n-i,x)>m)

class Solution:
    def maxValue(self, n: int, i: int, m: int) -> int:
        f=lambda l,b:(2*b*l-l*l+l,2*l+b*b-b)[b<l]//2;return bisect_right(range(1,m+1),0,key=lambda x:f(i,x-1)+f(n-i,x)>m)

class Solution:
    def maxValue(self, n: int, i: int, m: int) -> int:
        f=lambda l,b:((b+b-l)*l,b*b-b+l)[b<l]+l;return bisect_right(range(1,m+1),0,key=lambda x:f(i,x-1)+f(n-i,x)>m*2)

test('''
1802. Maximum Value at a Given Index in a Bounded Array
Medium

829

142

Add to List

Share
You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:

nums.length == n
nums[i] is a positive integer where 0 <= i < n.
abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
The sum of all the elements of nums does not exceed maxSum.
nums[index] is maximized.
Return nums[index] of the constructed array.

Note that abs(x) equals x if x >= 0, and -x otherwise.

 

Example 1:

Input: n = 4, index = 2,  maxSum = 6
Output: 2
Explanation: nums = [1,2,2,1] is one array that satisfies all the conditions.
There are no arrays that satisfy all the conditions and have nums[2] == 3, so 2 is the maximum nums[2].
Example 2:

Input: n = 6, index = 1,  maxSum = 10
Output: 3


Input: n = 3, index = 2,  maxSum = 18
Output: 7

 

Constraints:

1 <= n <= maxSum <= 10^9
0 <= index < n
Accepted
17,706
Submissions
53,476
Seen this question in a real interview before?

Yes

No
What if the problem was instead determining if you could generate a valid array with nums[index] == target?
To generate the array, set nums[index] to target, nums[index-i] to target-i, and nums[index+i] to target-i. Then, this will give the minimum possible sum, so check if the sum is less than or equal to maxSum.
n is too large to actually generate the array, so you can use the formula 1 + 2 + ... + n = n * (n+1) / 2 to quickly find the sum of nums[0...index] and nums[index...n-1].
Binary search for the target. If it is possible, then move the lower bound up. Otherwise, move the upper bound down.

''')