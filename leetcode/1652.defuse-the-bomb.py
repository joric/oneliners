from lc import *

# https://leetcode.com/problems/defuse-the-bomb/
# https://leetcode.com/contest/biweekly-contest-39/submissions/detail/420176098/

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        c = code[:]
        n = len(code)
        for i in range(n):
            if k>0:
                s = 0
                for j in range(k):
                    s += c[(i+j+1)%n]
                code[i] = s
            elif k<0:
                s = 0
                for j in range(-k):
                    s += c[(i-j-1+n)%n]
                code[i] = s
            else:
                code[i] = 0
        return code

# https://leetcode.com/problems/defuse-the-bomb/discuss/5713217/4-lines-Python-Solution

class Solution:
    def decrypt(self, c: List[int], k: int) -> List[int]:
        result, i, l, r = [sum(c[:abs(k)])] * len(c), -k if k < 0 else -1, -1, abs(k) -1
        for j in range(1,  len(c)):
            result[(i + j) % len(c)] = result[(i + j) % len(c) - 1] - c[(l + j) % len(c)] + c[(r + j) % len(c)]
        return result

# https://leetcode.com/problems/defuse-the-bomb/discuss/1715964/Easy-3-liner-Python

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k < 0 : return self.decrypt(code[::-1], -k)[::-1]
        code = code * 2
        return [sum(code[i+1:i+k+1]) for i in range(len(code)//2)]

# https://leetcode.com/problems/defuse-the-bomb/discuss/6056398/1-liner

#def decrypt(code, k)
#  code.map.with_index { |_, i| k.abs.times.sum { |j| code[(i + (j + 1) * k / k.abs) % code.size] } }
#end

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        return[sum(code[(i + (j + 1) * (k // abs(k))) % len(code)] for j in range(abs(k)))for i in range(len(code))]

class Solution:
    def decrypt(self, c: List[int], k: int) -> List[int]:
        n,t=len(c),abs(k);return[sum(c[(i+-~j*k//t)%n]for j in range(t))for i in range(n)]

test('''
1652. Defuse the Bomb
Easy

1016

121

Add to List

Share
You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

 

Example 1:

Input: code = [5,7,1,4], k = 3
Output: [12,10,16,13]
Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.
Example 2:

Input: code = [1,2,3,4], k = 0
Output: [0,0,0,0]
Explanation: When k is zero, the numbers are replaced by 0. 
Example 3:

Input: code = [2,4,9,3], k = -2
Output: [12,5,6,13]
Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the previous numbers.
 

Constraints:

n == code.length
1 <= n <= 100
1 <= code[i] <= 100
-(n - 1) <= k <= n - 1
Accepted
84,404
Submissions
115,500
''')
