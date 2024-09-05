from lc import *

# https://leetcode.com/problems/binary-trees-with-factors/discuss/126016/Short-simple-Python

class Solution:
    def numFactoredBinaryTrees(self, a: List[int]) -> int:
        t={}
        for i in sorted(a):
            t[i] = 1+sum(t[j]*t.get(i/j,0)for j in a if j < i)
        return sum(t.values())%(10**9 + 7)

class Solution:
    def numFactoredBinaryTrees(self, a: List[int]) -> int:
        t={};[setitem(t,i,1+sum(t[j]*t.get(i/j,0)for j in a if j < i))for i in sorted(a)];return sum(t.values())%(10**9 + 7)

# https://leetcode.com/problems/binary-trees-with-factors/discuss/2180513/python-3-or-recursion-%2B-memoization-or-O(n2)O(n)

class Solution:
    def numFactoredBinaryTrees(self, a: List[int]) -> int:
        a=set(a)
        @cache
        def f(x):
            t = 1
            for c in a:
                if not x%c and x//c in a:
                    t += f(c) * f(x//c)
            return t
        return sum(map(f,a))%(10**9+7)

class Solution:
    def numFactoredBinaryTrees(self, a: List[int]) -> int:
        return sum(map(f:=cache(lambda x:1+sum(f(c)*f(x//c)for c in a if x%c<1and x//c in a)),a))%(10**9+7)

test('''

823. Binary Trees With Factors
Medium

2562

184

Add to List

Share
Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.

 

Example 1:

Input: arr = [2,4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]
Example 2:

Input: arr = [2,4,5,10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
 

Constraints:

1 <= arr.length <= 1000
2 <= arr[i] <= 10^9
All the values of arr are unique.

''')
