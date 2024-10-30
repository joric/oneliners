from lc import *

# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/discuss/952053/Python-3-solutions%3A-LIS-dp-O(n-log-n)-explained

class Solution:
    def minimumMountainRemovals(self, d: List[int]) -> int:
        n = len(d)
        a, b = [1]*n, [1]*n
        for i in range(1, n):
            for j in range(i):
                if d[j]<d[i]: a[i]=max(a[i], 1+a[j])
                if d[j]>d[i]: 
                    if a[j]>1: b[i] = max(b[i], 1 + a[j])
                    if b[j]>1: b[i] = max(b[i], 1 + b[j])
        return n-max(b)

# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/discuss/2564659/ONLY-4-Lines-more-to-LIS

class Solution:
    def minimumMountainRemovals(self, a: List[int]) -> int:
        n=len(a)
        f=lambda a,d=[1]*n:[a[j]<a[i]and d[j]+1>d[i] and setitem(d,i,d[j]+1)for i in range(n) for j in range(i)]and d
        r = 0
        for x,y in zip(f(a),f(a[::-1])[::-1]):
            c = x + y - 1
            if c > r and x > 1 and y > 1:
                r = c
        return n-r

# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/discuss/955021/O(NlogN)-3-liner-solution-with-7-lines-helper-funcition

class Solution:
    def minimumMountainRemovals(self, a: List[int]) -> int:
        n = len(a)
        def f(a):
            d=[inf]*n
            return[setitem(d,i:=bisect_left(d,x),x)or i for x in a]
        return n - max(x+y+1 for x,y in zip(f(a),f(a[::-1])[::-1])if x and y)

# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/discuss/952136/Python-LIS-O(nlogn)

class Solution:
    def minimumMountainRemovals(self, a: List[int]) -> int:
        n = len(a)
        def f(a):
            d = [inf]*n
            for x in a:
                i = bisect_left(d, x)
                d[i] = x
            return i if i else -n
        return n-max(1+f(a[:i+2])+f(a[:i:-1])for i in range(n-1))

class Solution:
    def minimumMountainRemovals(self, a: List[int]) -> int:
        n=len(a);f=lambda a:(d:=[inf]*n,[setitem(d,i:=bisect_left(d,x),x)for x in a],i if i else -n)[2];return n-max(1+f(a[:i+2])+f(a[:i:-1])for i in range(n-1))

test('''
1671. Minimum Number of Removals to Make Mountain Array
Hard

1612

23

Add to List

Share
You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array nums​​​, return the minimum number of elements to remove to make nums​​​ a mountain array.

 

Example 1:

Input: nums = [1,3,1]
Output: 0
Explanation: The array itself is a mountain array so we do not need to remove any elements.
Example 2:

Input: nums = [2,1,1,5,6,2,3,1]
Output: 3
Explanation: One solution is to remove the elements at indices 0, 1, and 5, making the array nums = [1,5,6,3,1].
 

Constraints:

3 <= nums.length <= 1000
1 <= nums[i] <= 109
It is guaranteed that you can make a mountain array out of nums.
Accepted
34,106
Submissions
80,668
''')
