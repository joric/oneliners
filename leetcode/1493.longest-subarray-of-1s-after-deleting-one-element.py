from lc import *

# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/discuss/2905189/Video-Walkthrough-oror-Easy-oror-Python-oror-3-Line-Solution

class Solution:
    def longestSubarray(self, n: List[int]) -> int:
        r,o,l=0,0,n[0]
        for i in range(1,len(n)):
            r,o,l=n[i]*max(r+1,o+1),n[i-1]*(o+1),max(l,n[i]*max(r+1,o+1))
        return l

# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/discuss/1521676/Python-5-lines

class Solution:
    def longestSubarray(self, n: List[int]) -> int:
        if 0 not in n:
            return len(n) - 1
        v = ''.join(map(str,n)).split('0')
        r = -inf
        for i in range(1,len(v)):
            r = max(r,len(v[i-1]+v[i]))
        return r

# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/discuss/3120754/5-lines-in-python.-Easy-to-understand

class Solution:
    def longestSubarray(self, n: List[int]) -> int:
        c=p=b=0;r=len(n)
        for i in range(r):
            c,p = (c+1,p+1) if n[i] else (p,0)
            b = max(p,c,b)
        return b-1 if b==r else b

class Solution:
    def longestSubarray(self, n: List[int]) -> int:
        c=p=b=0;r=len(n);[(n[i]and(c:=c+1,p:=p+1)or(c:=p,p:=0),b:=max(p,c,b))for i in range(r)];return b-(b==r)

# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/discuss/708112/JavaC%2B%2BPython-Sliding-Window-at-most-one-0

class Solution:
    def longestSubarray(self, n: List[int]) -> int:
        k,i = 1,0
        for j in range(len(n)):
            k -= n[j] == 0
            if k < 0:
                k += n[i] == 0
                i += 1
        return j-i

class Solution:
    def longestSubarray(self, n: List[int]) -> int:
        k,i,r=1,0,len(n);[(k:=k-(n[j]==0),k<0 and(k:=k+(n[i]==0),i:=i+1))for j in range(r)];return r-i-1

class Solution:
    def longestSubarray(self, n: List[int]) -> int:
        k,i,r=1,0,len(n);[(k:=k+n[j]-1)<0and(k:=k-n[i]+1,i:=i+1)for j in range(r)];return r-i-1


class Solution:
    def longestSubarray(self, n):
        s, t, a = 0, -1, 0
        for x in n:
            s, t = (s+1)*x, max((t+1)*x,s)
            a = max(a, t)
        return a

class Solution:
    def longestSubarray(self, n: List[int]) -> int:
        s=a=0;t=-1;[(a:=max(a,t:=max((t+1)*x,s)),s:=(s+1)*x)for x in n];return a


class Solution:
    def longestSubarray(self, n):
        s=a=u=0
        for x in n:
            u = max(u*x,s)+1
            a = max(a,u)
            s = s*x+x
        return a-1

class Solution:
    def longestSubarray(self, n: List[int]) -> int:
        s=a=0;t=-1;[(a:=max(a,t:=max(-~t*x,s)),s:=-~s*x)for x in n];return a

class Solution:
    def longestSubarray(self, n: List[int]) -> int:
        s=a=u=0;[(a:=max(a,u:=max(u*x,s)+1),s:=s*x+x)for x in n];return~-a

test('''
1493. Longest Subarray of 1's After Deleting One Element
Medium

1711

32

Add to List

Share
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
Accepted
75,550
Submissions
121,860
''')