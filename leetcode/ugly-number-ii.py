from lc import *

# https://leetcode.com/problems/ugly-number-ii/discuss/69373/Short-and-O(n)-Python-and-C%2B%2B

# Python ... Simple Precompute ... 64 ms
# It's fastest to precompute and store all possibilities for lookup, and it's simplest to just generate them out of order and then sort them.

class Solution:
    ugly = sorted(2**a * 3**b * 5**c
                  for a in range(32) for b in range(20) for c in range(14))
    def nthUglyNumber(self, n):
        return self.ugly[n-1]

# Python ... O(n), generate first n in order ... 308 ms
# My version of epsilon0's solution. It's nicer than my own old one.
# This generates the first n ugly numbers, in order from smallest to largest, in O(n) time. For each prime 2, 3 and 5, have an index to the next number that can be multiplied with the prime to produce a new ugly number. Update the three indexes and then add the smallest of the three candidate ugly numbers.

def nthUglyNumber(self, n):
    ugly = [1]
    i2 = i3 = i5 = 0
    while len(ugly) < n:
        while ugly[i2] * 2 <= ugly[-1]: i2 += 1
        while ugly[i3] * 3 <= ugly[-1]: i3 += 1
        while ugly[i5] * 5 <= ugly[-1]: i5 += 1
        ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
    return ugly[-1]

# Python ... O(n), generate first n in order with heapq.merge ... 416 ms
# I like using heapq.merge.

def nthUglyNumber(self, n):
    q2, q3, q5 = [2], [3], [5]
    ugly = 1
    for u in heapq.merge(q2, q3, q5):
        if n == 1:
            return ugly
        if u > ugly:
            ugly = u
            n -= 1
            q2 += 2 * u,
            q3 += 3 * u,
            q5 += 5 * u,

# Python version of my own O(n) C++ solution from almost 13 years ago. Good old times...
# Maybe I'll try to improve it, but mainly I wanted to see how a pretty much direct translation would look.

class Solution():
    def nthUglyNumber(self, n):
        factor = 2, 3, 5
        lists = [collections.deque([1]) for _ in range(3)]
        for _ in range(n - 1):
            next = [lists[i][0] * factor[i] for i in range(3)]
            winner = min(range(3), key=lambda j: next[j])
            for i in range(winner, 3):
                lists[i] += next[winner],
            lists[winner].popleft()
        return lists[2][-1]

# shortest

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        return sorted(2**a*3**b*5**c for a in range(32)for b in range(20)for c in range(14))[n-1]

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        return sorted(2**a*3**b*5**c for a,b,c in product(*map(range,(32,20,14))))[n-1]

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        return sorted(2**a*3**b*5**c for a,b,c in product(range(32),repeat=3))[n-1]

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        return sorted(2**a*3**b*5**c for a,b,c in product(*[range(32)]*3))[n-1]

test('''
264. Ugly Number II
Medium

6107

334

Add to List

Share
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

 

Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
 

Constraints:

1 <= n <= 1690
Accepted
371,384
Submissions
791,380
''')
