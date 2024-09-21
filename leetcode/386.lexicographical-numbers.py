from lc import *

# https://leetcode.com/problems/lexicographical-numbers/discuss/86228/The-most-elegant-python-solution-so-far.-10-liner.-iterative.-O(n)-time-O(1)-space.

class Solution(object):
    def lexicalOrder(self, n: int) -> List[int]:
        r = [1]
        while len(r) < n:
            x = r[-1] * 10
            while x > n:
                x //= 10
                x += 1
                while x % 10 == 0:
                    x //= 10
            r.append(x)
        return r

# https://leetcode.com/problems/lexicographical-numbers/discuss/86235/Python-with-Sorting

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        top = 1
        while top * 10 <= n:
            top *= 10
        def mycmp(a, b, top=top):
            while a < top: a *= 10
            while b < top: b *= 10
            return -1 if a < b else b < a
        return sorted(range(1,n+1), key=cmp_to_key(mycmp))

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        d = []
        for i in range(1, n+1):
            k = i
            while k < 1000000:
                k *= 10
            d.append(k * 10000000 + i)
        d.sort()
        return [k % 10000000 for k in d]

# Q1. https://leetcode.com/contest/warm-up-contest/
# https://leetcode.com/problems/lexicographical-numbers/

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return map(int,sorted(map(str,range(1,n+1))))

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(range(1,n+1),key=str)

test('''
386. Lexicographical Numbers
Medium

1936

142

Add to List

Share
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

 

Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]
 

Constraints:

1 <= n <= 5 * 104
Accepted
120,409
Submissions
188,662
''')