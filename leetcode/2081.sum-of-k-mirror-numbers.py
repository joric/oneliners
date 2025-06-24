from lc import *

# https://leetcode.com/problems/sum-of-k-mirror-numbers/description/?envType=daily-question&envId=2025-06-23

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def f(x):
            m = len(x) // 2
            for i in range(m, len(x)):
                if int(x[i]) + 1 < k:
                    x[i] = x[~i] = str(int(x[i]) + 1)
                    for j in range(m, i):
                        x[j] = x[~j] = '0'
                    return x
            return ['1'] + ['0'] * (len(x) - 1) + ['1']
        x, r = ['0'], 0
        for _ in range(n):
            while True:
                x = f(x)
                v = int(''.join(x), k)
                if str(v) == str(v)[::-1]:
                    break
            r += v
        return r

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        x,s=['0'],setitem
        def f(x):
            for i in range((m:=len(x))//2,m):
                if int(x[i])+1<k:
                    (s(x,i,t:=str(int(x[i])+1)),s(x,~i,t),[s(x,j,t:='0')or s(x,~j,t)for j in range(m//2,i)])
                    return x
            return ['1']+['0']*~-m+['1']
        return sum(next(t for _ in count()if str(t:=int(''.join(x:=f(x)),k))==str(t)[::-1])for _ in range(n))

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        x,s=['0'],setitem;f=lambda x:(m:=len(x))and next((x for i in range(m//2,m)if k>1+int(x[i])and(s(x,i,t:=str(int(x[i])+1)),s(x,~i,t),[s(x,j,'0')or s(x,~j,'0')for j in range(m//2,i)])),['1']+['0']*~-m+['1']);return sum(next(t for _ in count()if str(t:=int(''.join(x:=f(x)),k))==str(t)[::-1])for _ in range(n))

# chatgpt, this one is TLE, even with cache(lambda)
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        g=lambda z:z<k and str(z)or g(z//k)+str(z%k);return sum(islice((i for i in count(1)if str(i)==str(i)[::-1]and g(i)==g(i)[::-1]),n))

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def to_base_k(num: int) -> str:
            if num < k:
                return str(num)
            return to_base_k(num // k) + str(num % k)
        def is_k_mirror(x: int) -> bool:
            b = to_base_k(x)
            return b == b[::-1]
        gen1 = (int(str(a) + str(a)[-2::-1]) for a in count(1))
        gen2 = (int(str(a) + str(a)[::-1]) for a in count(1))
        return sum(islice((x for x in merge(gen1, gen2) if is_k_mirror(x)), n))

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        f=lambda z:z<k and str(z)or f(z//k)+str(z%k);return sum(islice((x for x in merge((int(str(a)+str(a)[-2::-1])for a in count(1)),(int(str(a)+str(a)[::-1])for a in count(1)))if f(x)==f(x)[::-1]),n))

test('''
2081. Sum of k-Mirror Numbers
Solved
Hard
Topics
premium lock icon
Companies
Hint
A k-mirror number is a positive integer without leading zeros that reads the same both forward and backward in base-10 as well as in base-k.

For example, 9 is a 2-mirror number. The representation of 9 in base-10 and base-2 are 9 and 1001 respectively, which read the same both forward and backward.
On the contrary, 4 is not a 2-mirror number. The representation of 4 in base-2 is 100, which does not read the same both forward and backward.
Given the base k and the number n, return the sum of the n smallest k-mirror numbers.

 

Example 1:

Input: k = 2, n = 5
Output: 25
Explanation:
The 5 smallest 2-mirror numbers and their representations in base-2 are listed as follows:
  base-10    base-2
    1          1
    3          11
    5          101
    7          111
    9          1001
Their sum = 1 + 3 + 5 + 7 + 9 = 25. 
Example 2:

Input: k = 3, n = 7
Output: 499
Explanation:
The 7 smallest 3-mirror numbers are and their representations in base-3 are listed as follows:
  base-10    base-3
    1          1
    2          2
    4          11
    8          22
    121        11111
    151        12121
    212        21212
Their sum = 1 + 2 + 4 + 8 + 121 + 151 + 212 = 499.
Example 3:

Input: k = 7, n = 17
Output: 20379000
Explanation: The 17 smallest 7-mirror numbers are:
1, 2, 3, 4, 5, 6, 8, 121, 171, 242, 292, 16561, 65656, 2137312, 4602064, 6597956, 6958596
 

Constraints:

2 <= k <= 9
1 <= n <= 30
Seen this question in a real interview before?
1/5
Yes
No
Accepted
8,543/20.2K
Acceptance Rate
42.3%
Topics
Math
Enumeration
icon
Companies
Hint 1
Since we need to reduce search space, instead of checking if every number is a palindrome in base-10, can we try to "generate" the palindromic numbers?
Hint 2
If you are provided with a d digit number, how can you generate a palindrome with 2*d or 2*d - 1 digit?
Hint 3
Try brute-forcing and checking if the palindrome you generated is a "k-Mirror" number.
Similar Questions
Strobogrammatic Number II
Medium
Prime Palindrome
Medium
''')
