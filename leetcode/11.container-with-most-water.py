from lc import *

# https://leetcode.com/problems/container-with-most-water/discuss/5022219/one-line-solution

class Solution: #TLE
    def maxArea(self, h: List[int]) -> int:
        e=enumerate;return max((j-i)*min(a,b)for i,a in e(h)for j,b in e(h[i+1:],i+1))

class Solution:
    def maxArea(self, h: List[int]) -> int:
        return(f:=lambda l,r:l<r and max((r-l)*min(h[l],h[r]),f(l+1,r)if h[l]<h[r]else f(l,r-1)))(0,len(h)-1)

class Solution:
    def maxArea(self, h: List[int]) -> int:
        m,i,j=0,0,len(h)-1
        for _ in h:
            m = max(m, min(h[j], h[i])*(j-i))
            i += h[j] > h[i]
            j -= h[j] <= h[i]
        return m

class Solution:
    def maxArea(self, h: List[int]) -> int:
        return(i:=0,j:=len(h)-1)and max((min(l:=h[j],r:=h[i])*(j-i),i:=i+(l>r),j:=j-(l<=r))[0]for _ in h)

class Solution:
    def maxArea(self, h: List[int]) -> int:
        i,j=0,len(h)-1;return max((min(l:=h[j],r:=h[i])*(j-i),i:=i+(l>r),j:=j-(l<=r))[0]for _ in h)

test('''
11. Container With Most Water
Medium

28485

1681

Add to List

Share
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
Accepted
2,874,217
Submissions
5,211,044
''')