from lc import *

class Solution1:
    def isPossible(self, target: List[int]) -> bool:
        s = sum(target)
        q = [-a for a in target]
        heapify(q)
        while True:
            x = -heappop(q)
            if x==1:
                return True
            if s==x:
                return False
            d = 1 + (x-1) % (s-x)
            if x==d:
                return False
            s = s - x + d
            heappush(q, -d)

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        return next((x==1 for _ in count() if (x:=-heappop(q))==1 or s==x or (d:=1+(x-1)%(s-x))==x
            or not (s:=s-x+d,heappush(q,-d))),(s:=sum(target),q:=[-a for a in target],heapify(q)))

test('''

1354. Construct Target Array With Multiple Sums
Hard

1946

156

Add to List

Share
You are given an array target of n integers. From a starting array arr consisting of n 1's, you may perform the following procedure :

let x be the sum of all elements currently in your array.
choose index i, such that 0 <= i < n and set the value of arr at index i to x.
You may repeat this procedure as many times as needed.
Return true if it is possible to construct the target array from arr, otherwise, return false.

Example 1:

Input: target = [9,3,5]
Output: true
Explanation: Start with arr = [1, 1, 1] 
[1, 1, 1], sum = 3 choose index 1
[1, 3, 1], sum = 5 choose index 2
[1, 3, 5], sum = 9 choose index 0
[9, 3, 5] Done

Example 2:

Input: target = [1,1,1,2]
Output: false
Explanation: Impossible to create target array from [1,1,1,1].

Example 3:

Input: target = [8,5]
Output: true

Example 4:

Input: target = [1,1,2]
Output: false

Example 5:

Input: target = [1,1,10]
Output: false

Example: 6
Input: target = [9,9,9]
Output: false

Constraints:

n == target.length
1 <= n <= 5 * 10^4
1 <= target[i] <= 10^9

''')
