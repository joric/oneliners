from lc import *

# TLE
class Solution:
    def maxSlidingWindow(self, n: List[int], k: int) -> List[int]:
        return[max(n[i:i+k])for i in range(len(n)-k+1)]

# https://leetcode.com/problems/sliding-window-maximum/discuss/1425046/C%2B%2B-oror-Prefix-and-Suffix-Sum-of-window-oror-O(n)

class Solution:
    def maxSlidingWindow(self, a: List[int], k: int) -> List[int]:
        n = len(a)
        p = [a[0]]+[0]*(n-1)
        s = [0]*(n-1)+[a[n-1]]
        i = 1
        j = n-2
        while i<n and j>=0:
            p[i] = max(p[i-1],a[i]) if i%k else a[i]
            s[j] = max(s[j+1],a[j]) if (j+1)%k else a[j]
            i+=1
            j-=1
        return [max(s[i],p[i+k-1]) if i+k-1<n else s[i] for i in range(n-k+1)]

class Solution:
    def maxSlidingWindow(self, a: List[int], k: int) -> List[int]:
        n = len(a)
        p = [a[0]]+[0]*(n-1)
        for i in range(1,n):
            p[i] = max(p[i-1],a[i]) if i%k else a[i]
        s = [0]*(n-1)+[a[n-1]]
        for i in range(n-2,-1,-1):
            s[i] = max(s[i+1],a[i]) if (i+1)%k else a[i]
        return [max(s[i],p[i+k-1]) if i+k-1<n else s[i] for i in range(n-k+1)]

# TLE
class Solution:
    def maxSlidingWindow(self, a: List[int], k: int) -> List[int]:
        n = len(a)
        p = reduce(lambda p,i:p+[max(p[-1],a[i])if i%k else a[i]],range(1,n),[a[0]])
        s = reduce(lambda s,i:[max(s[0],a[i])if (i+1)%k else a[i]]+s,range(n-2,-1,-1),[a[n-1]])
        return [max(s[i],p[i+k-1]) if i+k-1<n else s[i] for i in range(n-k+1)]

class Solution:
    def maxSlidingWindow(self, a: List[int], k: int) -> List[int]:
        n = len(a)
        p = reduce(lambda p,i:p.append(max(p[-1],a[i])if i%k else a[i])or p,range(1,n),[a[0]])
        s = reduce(lambda s,i:s.append(max(s[-1],a[i])if (i+1)%k else a[i])or s,range(n-2,-1,-1),[a[n-1]])[::-1]
        return [max(s[i],p[i+k-1]) if i+k-1<n else s[i] for i in range(n-k+1)]

class Solution:
    def maxSlidingWindow(self, a: List[int], k: int) -> List[int]:
        n=len(a);p,s=reduce(lambda p,i:p.append(max(p[-1],a[i])if i%k else a[i])or p,range(1,n),[a[0]]),reduce(lambda s,i:s.append(max(s[-1],a[i])if (i+1)%k else a[i])or s,range(n-2,-1,-1),[a[n-1]])[::-1];return [max(s[i],p[i+k-1]) if i+k-1<n else s[i] for i in range(n-k+1)]

#  https://leetcode.com/problems/sliding-window-maximum/discuss/65901/9-lines-Ruby-11-lines-Python-O(n)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        r, d = [], deque()
        for i, n in enumerate(nums):
            while d and n>=nums[d[-1]]:
                d.pop()
            d.append(i)
            if d[0] == i-k:
                d.popleft()
            r.append(nums[d[0]])
        return r[k-1:]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return (d:=deque()) or reduce(lambda r,p:(
            any(takewhile(lambda _:d and p[1]>=nums[d[-1]] and d.pop(), repeat(0))),
            d.append(p[0]), d[0]==p[0]-k and d.popleft(), r.append(nums[d[0]])) and r,
            enumerate(nums), [])[k-1:]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return (d:=deque()) or reduce(lambda r,p:(
            next(_ for _ in count() if not(d and p[1]>=nums[d[-1]] and d.pop())),
            d.append(p[0]), d[0]==p[0]-k and d.popleft(), r.append(nums[d[0]])) and r,
            enumerate(nums), [])[k-1:]

class Solution:
    def maxSlidingWindow(self, n: List[int], k: int) -> List[int]:
        d=deque();return reduce(lambda r,p:(next(_ for _ in count()if not(d and p[1]>=n[d[-1]]and d.pop())),d.append(p[0]),d[0]==p[0]-k and d.popleft(),r.append(n[d[0]]))and r,enumerate(n),[])[k-1:]

# https://leetcode.com/problems/sliding-window-maximum/discuss/620707/Sliding-window-template

from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, a: List[int], k: int) -> List[int]:
        p,l,r,w=[],0,0,SortedList()
        while r<len(a):
            w.add(a[r])
            if len(w)>=k:
                p.append(w[-1])
                w.remove(a[l])
                l += 1
            r += 1
        return p

class Solution:
    def maxSlidingWindow(self, a: List[int], k: int) -> List[int]:
        p,l,r,w=[],0,0,__import__('sortedcontainers').SortedList();return next(p for _ in a*2 if not(r<len(a)and(w.add(a[r]),len(w)>=k and(p.append(w[-1]),w.remove(a[l]),l:=l+1),r:=r+1)))

class Solution:
    def maxSlidingWindow(self, a: List[int], k: int) -> List[int]:
        p,w=[],SortedList()
        def f(l,r):
            if r<len(a):
                w.add(a[r])
                if len(w)>=k:
                    p.append(w[-1])
                    w.remove(a[l])
                    l += 1
                f(l,r+1)
        f(0,0)
        return p

class Solution:
    def maxSlidingWindow(self, a: List[int], k: int) -> List[int]:
        p,w=[],__import__('sortedcontainers').SortedList();f=lambda l,r:r<len(a)and(w.add(a[r]),len(w)>=k and(p.append(w[-1]),w.remove(a[l]),l:=l+1),f(l,r+1));f(0,0);return p

class Solution:
    def maxSlidingWindow(self, a: List[int], k: int) -> List[int]:
        p,w=[],__import__('sortedcontainers').SortedList();f=lambda l,r:r<len(a)and(w.add(a[r]),f(l+bool(len(w)>=k and(p.append(w[-1]),w.remove(a[l]))),r+1));f(0,0);return p

class Solution:
    def maxSlidingWindow(self, a: List[int], k: int) -> List[int]:
        p=__import__('numpy');return p.max(p.lib.stride_tricks.sliding_window_view(a,k),1)

test('''
239. Sliding Window Maximum
Hard

Add to List

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:

Input: nums = [1], k = 1
Output: [1]

Example 3:

Input: nums = [-6,-10,-7,-1,-9,9,-8,-4,10,-5,2,9,0,-7,7,4,-2,-10,8,7], k = 7
Output: [9,9,10,10,10,10,10,10,10,9,9,9,8,8]

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length

''')