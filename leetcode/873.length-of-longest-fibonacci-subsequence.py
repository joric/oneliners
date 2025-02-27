from lc import *

# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/solutions/152343/c-java-python-check-pair/?envType=daily-question&envId=2025-02-27

class Solution:
    def lenLongestFibSubseq(self, a: List[int]) -> int:
        c,s={},{*a}
        for j in range(len(a)):
            for i in range(j):
                if a[j]-a[i]<a[i] and a[j]-a[i] in s:
                    c[a[i],a[j]] = c.get((a[j]-a[i],a[i]),2)+1
        return max(c.values()or[0])

class Solution:
    def lenLongestFibSubseq(self, a: List[int]) -> int:
        c,s={},{*a}
        for x,y in product(a,a):
            if x-y<y and{x-y}&s:
                c[y,x] = c.get((x-y,y),2)+1
        return max(c.values()or[0])

class Solution:
    def lenLongestFibSubseq(self, a: List[int]) -> int:
        c,s={},{*a};[setitem(c,(y,x),c.get((x-y,y),2)+1)for x,y in product(a,a)if x-y<y and{x-y}&s];return max(c.values()or[0])

class Solution:
    def lenLongestFibSubseq(self, a: List[int]) -> int:
        c,s={},{*a};return max([setitem(c,(y,x),c.get((x-y,y),2)+1)or c[y,x]for x,y in product(a,a)if x-y<y and{x-y}&s]+[0])

test('''
873. Length of Longest Fibonacci Subsequence
Medium
Topics
Companies
A sequence x1, x2, ..., xn is Fibonacci-like if:

n >= 3
xi + xi+1 == xi+2 for all i + 2 <= n
Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.

A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].

 

Example 1:

Input: arr = [1,2,3,4,5,6,7,8]
Output: 5
Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].
Example 2:

Input: arr = [1,3,7,11,12,14,18]
Output: 3
Explanation: The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].
 

Constraints:

3 <= arr.length <= 1000
1 <= arr[i] < arr[i + 1] <= 109
Seen this question in a real interview before?
1/5
Yes
No
Accepted
114.7K
Submissions
215.2K
Acceptance Rate
53.3%
Topics
Array
Hash Table
Dynamic Programming
Companies
Similar Questions
Fibonacci Number
Easy
''')
