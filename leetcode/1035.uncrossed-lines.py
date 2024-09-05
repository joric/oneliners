from lc import *

class Solution:
    def maxUncrossedLines(self, a: List[int], b: List[int]) -> int:
        d,m,n = Counter(),len(a),len(b)
        for i in range(m):
            for j in range(n):
                d[i,j] = max(d[i-1,j-1]+(a[i]==b[j]),d[i-1,j],d[i,j-1])
        return d[m-1,n-1]

# https://leetcode.com/problems/uncrossed-lines/discuss/651249/Python-Recursive-Solution

class Solution:
    def maxUncrossedLines(self, a: List[int], b: List[int]) -> int:
        @cache
        def f(i,j):
            if i>=len(a) or j>=len(b):
                return 0
            return max(int(a[i]==b[j])+f(i+1,j+1),f(i,j+1),f(i+1,j))
        return f(0,0)

class Solution:
    def maxUncrossedLines(self, a: List[int], b: List[int]) -> int:
        return (f:=cache(lambda i,j:i<len(a) and j<len(b) and max((a[i]==b[j])+f(i+1,j+1),f(i,j+1),f(i+1,j))))(0,0)

class Solution:
    def maxUncrossedLines(self, a: List[int], b: List[int]) -> int:
        return (f:=cache(lambda i,j:i*j and max((a[i-1]==b[j-1])+f(i-1,j-1),f(i,j-1),f(i-1,j))))(len(a),len(b))

test('''
1035. Uncrossed Lines
Medium

2063

29

Add to List

Share
You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

nums1[i] == nums2[j], and
the line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

Return the maximum number of connecting lines we can draw in this way.

 

Example 1:


Input: nums1 = [1,4,2], nums2 = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.
Example 2:

Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
Output: 3
Example 3:

Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
Output: 2
 

Constraints:

1 <= nums1.length, nums2.length <= 500
1 <= nums1[i], nums2[j] <= 2000
Accepted
79,131
Submissions
133,571
Seen this question in a real interview before?

Yes

No
Edit Distance
Hard
Think dynamic programming. Given an oracle dp(i,j) that tells us how many lines A[i:], B[j:] [the sequence A[i], A[i+1], ... and B[j], B[j+1], ...] are uncrossed, can we write this as a recursion?
''')
