from lc import *

class Solution:
    def sumSubarrayMins(self, a: List[int]) -> int:
        a,n = [0]+a, len(a)+1
        r,q = [0]*n, deque([0])
        for i in range(n):
            while a[q[0]] > a[i]:
                q.popleft()
            r[i] = r[q[0]] + (i-q[0])*a[i]
            q.appendleft(i)
        return sum(r) % (10**9+7)

class Solution:
    def sumSubarrayMins(self, a: List[int]) -> int:
        s, d, r = [], [0], 0
        for i,e in enumerate(a):
            while s and a[s[-1]] >= e:
                s.pop()
            d.append((i-(p:=s[-1]if s else-1))*e+d[p+1])
            r += d[-1]
            s.append(i)
        return r%(10**9+7)

class Solution:
    def sumSubarrayMins(self, a: List[int]) -> int:
        s,d,r=[],[0],0;[(next(_ for _ in count()if not(s and a[s[-1]]>=e and s.pop())),d.append((i-(p:=s[-1] if s else -1))*e+d[p+1]),(r:=(r+d[-1])%(10**9+7)),s.append(i))for i,e in enumerate(a)];return r

test('''

907. Sum of Subarray Minimums
Medium

5493

379

Add to List

Share
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

 

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:

Input: arr = [11,81,94,43,3]
Output: 444
 

Constraints:

1 <= arr.length <= 3 * 10^4
1 <= arr[i] <= 3 * 10^4

''')