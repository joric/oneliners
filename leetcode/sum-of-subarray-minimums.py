from lc import *

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr,n = [0]+arr, len(arr)+1
        ans, queue  = [0]*n, deque([0])
        for i in range(n):
            while arr[queue[0]] > arr[i]:
                queue.popleft()
            ans[i] = ans[queue[0]] + (i-queue[0])*arr[i]
            queue.appendleft(i)
        return sum(ans) % (10**9+7)

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        s, dp, ret = [], [0], 0
        for i, e in enumerate(arr):
            while s and arr[s[-1]] >= e:
                s.pop()
            dp.append((i - (p := s[-1] if s else -1)) * e + dp[p + 1])
            ret = (ret + dp[-1]) % (10**9+7)
            s.append(i)
        return ret


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        return (s:=[],dp:=[0],r:=0) and all((next(_ for _ in count() if not(s and arr[s[-1]]>=e and s.pop())),dp.append((i-(p:=s[-1] if s else -1))*e+dp[p+1]),(r:=(r+dp[-1])%(10**9+7)),s.append(i)) for i,e in enumerate(arr)) and r


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