from lc import *

# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/solutions/7368723/short-and-clear-python-solution-of-three-kgd5/

class Solution:
    def sumAndMultiply(self, s: str, qs: List[List[int]]) -> List[int]:
        ps, pd, p0, mod, ans = [0], [0], [0], (10**9+7), []
        for i in map(int, str(s)):
            ps.append((ps[-1]+i))
            if i:
                pd.append((pd[-1]*10+i)%mod)
                p0.append(p0[-1])
            else:
                pd.append(pd[-1])
                p0.append(p0[-1]+1)
        for i, j in qs:
            k = pow(10, (j-i+1)-(p0[j+1]-p0[i]), mod)
            x = pd[j+1]-pd[i]*k
            y = ps[j+1]-ps[i]
            ans.append((x*y)%mod)
        return ans

class Solution:
    def sumAndMultiply(self, s: str, q: List[List[int]]) -> List[int]:
        a,b,c,m=[0],[0],[0],10**9+7;[a.append(a[-1]+v)or b.append((b[-1]*10**(v>0)+v)%m)or c.append(c[-1]+(v>0))for v in map(int,s)];return[(b[j+1]-b[i]*pow(10,c[j+1]-c[i],m))*(a[j+1]-a[i])%m for i,j in q]

class Solution:
    def sumAndMultiply(self, s: str, q: List[List[int]]) -> List[int]:
        a,b,c,m=[0],[0],[0],10**9+7;[a.append(a[-1]+v)or b.append((b[-1]*10**(w:=v>0)+v)%m)or c.append(c[-1]+w)for v in map(int,s)];return[(b[J:=j+1]-b[i]*pow(10,c[J]-c[i],m))*(a[J]-a[i])%m for i,j in q]

class Solution:
    def sumAndMultiply(self, s: str, q: List[List[int]]) -> List[int]:
        p=list.append;a,b,c,m=[0],[0],[0],10**9+7;[p(a,a[-1]+v)==p(b,(b[-1]*10**(w:=v>0)+v)%m)==p(c,c[-1]+w)for v in map(int,s)];return[(b[t:=j+1]-b[i]*pow(10,c[t]-c[i],m))*(a[t]-a[i])%m for i,j in q]

class Solution:
    def sumAndMultiply(self, s: str, q: List[List[int]]) -> List[int]:
        a,b,c,m=[0],[0],[0],10**9+7;exec("for v in map(int,s):a+=[a[-1]+v];b+=[(b[-1]*10**(w:=v>0)+v)%m];c+=[c[-1]+w]");return[(b[t:=j+1]-b[i]*pow(10,c[t]-c[i],m))*(a[t]-a[i])%m for i,j in q]

test('''
3756. Concatenate Non-Zero Digits and Multiply by Sum II
Medium
Topics
premium lock icon
Companies
Hint
You are given a string s of length m consisting of digits. You are also given a 2D integer array queries, where queries[i] = [li, ri].

For each queries[i], extract the substring s[li..ri]. Then, perform the following:

Form a new integer x by concatenating all the non-zero digits from the substring in their original order. If there are no non-zero digits, x = 0.
Let sum be the sum of digits in x. The answer is x * sum.
Return an array of integers answer where answer[i] is the answer to the ith query.

Since the answers may be very large, return them modulo 109 + 7.

 

Example 1:

Input: s = "10203004", queries = [[0,7],[1,3],[4,6]]

Output: [12340, 4, 9]

Explanation:

s[0..7] = "10203004"
x = 1234
sum = 1 + 2 + 3 + 4 = 10
Therefore, answer is 1234 * 10 = 12340.
s[1..3] = "020"
x = 2
sum = 2
Therefore, the answer is 2 * 2 = 4.
s[4..6] = "300"
x = 3
sum = 3
Therefore, the answer is 3 * 3 = 9.
Example 2:

Input: s = "1000", queries = [[0,3],[1,1]]

Output: [1, 0]

Explanation:

s[0..3] = "1000"
x = 1
sum = 1
Therefore, the answer is 1 * 1 = 1.
s[1..1] = "0"
x = 0
sum = 0
Therefore, the answer is 0 * 0 = 0.
Example 3:

Input: s = "9876543210", queries = [[0,9]]

Output: [444444137]

Explanation:

s[0..9] = "9876543210"
x = 987654321
sum = 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 45
Therefore, the answer is 987654321 * 45 = 44444444445.
We return 44444444445 modulo (109 + 7) = 444444137.
 

Constraints:

1 <= m == s.length <= 105
s consists of digits only.
1 <= queries.length <= 105
queries[i] = [li, ri]
0 <= li <= ri < m
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
10,963/44.3K
Acceptance Rate
24.7%
Topics
Staff
Math
String
Prefix Sum
Weekly Contest 477
icon
Companies
Hint 1
Track only nonzero digits: store their values and positions and keep a prefix sum for digit sums.
Hint 2
Also build prefix concatenation values P, pow10, and set mod = 109+7 so any compressed substring number is obtainable from prefixes.
Hint 3
Map each query [l, r] to the compressed list using precomputed mapping arrays (first nonzero at or after i
Hint 4
If the mapped range is empty return 0; otherwise get x from P, get sum from the digit-prefix, and return (x * sum) % mod.
''')
