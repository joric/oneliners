from lc import *

# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/solutions/5235534/one-line-solution/?envType=daily-question&envId=2025-02-25

class Solution:
    def numOfSubarrays(self, a: List[int]) -> int:
        x,o,e,r = 0,0,1,0
        for v in a:
            x ^= v&1
            o += x&1
            e += x&1==0
            r += (o,e)[x&1]
        return r%(10**9+7)

class Solution:
    def numOfSubarrays(self, a: List[int]) -> int:
        return reduce(lambda r,v:(x:=r[0]^v&1,o:=r[1]+(x&1),e:=r[2]+(x&1<1),r[3]+(o,e)[x&1]),a,(0,0,1,0))[3]%(10**9+7)

# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description/?envType=daily-question&envId=2025-02-25

class Solution:
    def numOfSubarrays(self, a: List[int]) -> int:
        o=e=r=0
        for i in a:
            if i % 2 == 0:
                e += 1
            else:
                t = e
                e = o
                o = t + 1
            r += o
        return r % (10**9+7)

# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/solutions/2061760/python-8-line-math-using-prefix-sum/?envType=daily-question&envId=2025-02-25

class Solution:
    def numOfSubarrays(self, a: List[int]) -> int:
        s=o=0
        e=1
        for x in a:
            s += x
            if s % 2:
                o += 1
            else:
                e += 1
        return o*e%(10**9+7)

class Solution:
    def numOfSubarrays(self, a: List[int]) -> int:
        return mul(*reduce(lambda p,s:((p[0],p[1]+1),(p[0]+1,p[1]))[s%2],accumulate(a),(0,1)))%(10**9+7)

class Solution:
    def numOfSubarrays(self, a: List[int]) -> int:
        return mul(*reduce(lambda p,s:(p[0]+s%2,p[1]+~-s%2),accumulate(a),(0,1)))%(10**9+7)

class Solution:
    def numOfSubarrays(self, a: List[int]) -> int:
        return(t:=sum(x&1for x in accumulate(a)))*(len(a)-t+1)%(10**9+7)

test('''
1524. Number of Sub-arrays With Odd Sum
Solved
Medium
Topics
Companies
Hint
Given an array of integers arr, return the number of subarrays with an odd sum.

Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:

Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.
Example 2:

Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.
Example 3:

Input: arr = [1,2,3,4,5,6,7]
Output: 16

Other examples:

Input: arr = [100,100,99,99]
Output: 4

Constraints:

1 <= arr.length <= 105
1 <= arr[i] <= 100
Seen this question in a real interview before?
1/5
Yes
No
Accepted
44.4K
Submissions
100.7K
Acceptance Rate
44.1%
Topics
Array
Math
Dynamic Programming
Prefix Sum
Companies
Hint 1
Can we use the accumulative sum to keep track of all the odd-sum sub-arrays ?
Hint 2
if the current accu sum is odd, we care only about previous even accu sums and vice versa.
Similar Questions
Subsequence of Size K With the Largest Even Sum
Medium
''')
