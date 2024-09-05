from lc import *

# https://leetcode.com/problems/2-keys-keyboard/discuss/105968/Python-Straightforward-with-Explanation

class Solution:
    def minSteps(self, n: int) -> int:
        def factors(n):
            d = 2
            while d * d <= n:
                while n % d == 0:
                    n /= d
                    yield d
                d += 1
            if n > 1:
                yield n
        return sum(factors(n))

# https://leetcode.com/problems/2-keys-keyboard/discuss/5470333/One-Line-Solution

class Solution:
    def minSteps(self, n: int) -> int:
        return(n>1)+(f:=cache(lambda p,c,s:s<n and 1+min(f(1,c,s+c),p and f(0,s,s)or inf)or s>n and inf))(0,1,1)

class Solution:
    def minSteps(self, n: int) -> int:
        def f(n):
            if n == 1: return 0
            for i in range(2, n + 1):
                if n % i == 0:
                    return i + f(n//i)
        return f(n)

class Solution:
    def minSteps(self, n: int) -> int:
        return(f:=lambda n:n>1 and next(i+f(n//i)for i in range(2,n+1)if n%i==0)or 0)(n)

class Solution:
    def minSteps(s, n: int) -> int:
        return~-n and next(i+s.minSteps(n//i)for i in range(2,n+1)if n%i==0)

test('''
650. 2 Keys Keyboard
Medium

3529

214

Add to List

Share
There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:

Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.

 

Example 1:

Input: n = 3
Output: 3
Explanation: Initially, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
Example 2:

Input: n = 1
Output: 0
 

Constraints:

1 <= n <= 1000
Accepted
140,969
Submissions
259,217
''')