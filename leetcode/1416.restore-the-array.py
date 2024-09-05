from lc import *

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0]*n
        for i in range(n):
            for j in range(len(str(k))):
                if i-j<0:
                    break
                t = s[i-j:i+1]
                if t[0]=='0': continue
                if 1 <= int(t) <= k:
                    dp[i]+=dp[i-j-1] if i-j-1>=0 else 1
        return dp[n-1] % (10**9+7)

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        return (c:=Counter(),[(x:=s[i:j+1],x[0]!='0' and int(x)<=k and c.update({j:i>0 and c[i-1] or 1})) for j in range(len(s)) for i in range(j,max(-1,j-len(str(k))-1),-1)],c[len(s)-1]%(10**9+7))[2]

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        @cache
        def f(i):
            r = 0
            n = len(s)
            if i==n:
                return 1
            if s[i]!='0':
                for j in range(i,min(i+10,n)):
                    if int(s[i:j+1])<=k:
                        r += f(j+1)
            return r%(10**9+7)
        return f(0)

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        return (f:=cache(lambda i:(i==(n:=len(s)) or s[i]!='0' and sum(f(j+1)*(int(s[i:j+1])<=k) for j in range(i,min(i+10,n))) or 0)%(10**9+7)))(0)

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        return (f:=cache(lambda i:not s[i:] or (s[i]!='0')*sum(f(j+1)*(int(s[i:j+1])<=k) for j in range(i,min(i+9,len(s))))%(10**9+7)))(0)

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        return (f:=cache(lambda i:i==len(s) or (s[i]!="0")*sum(f(j+1)*(int(s[i:j+1])<=k) for j in range(i,min(i+9,len(s))))%(10**9+7)))(0)

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        return (f:=cache(lambda i:i==(n:=len(s)) or (s[i]!="0")*sum(f(j+1)*(int(s[i:j+1])<=k) for j in range(i,min(i+9,n)))%(10**9+7)))(0)

test('''
1416. Restore The Array
Hard

482

21

Add to List

Share
A program was supposed to print an array of integers. The program forgot to print whitespaces and the array is printed as a string of digits s and all we know is that all integers in the array were in the range [1, k] and there are no leading zeros in the array.

Given the string s and the integer k, return the number of the possible arrays that can be printed as s using the mentioned program. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: s = "1000", k = 10000
Output: 1
Explanation: The only possible array is [1000]
Example 2:

Input: s = "1000", k = 10
Output: 0
Explanation: There cannot be an array that was printed this way and has all integer >= 1 and <= 10.
Example 3:

Input: s = "1317", k = 2000
Output: 8
Explanation: Possible arrays are [1317],[131,7],[13,17],[1,317],[13,1,7],[1,31,7],[1,3,17],[1,3,1,7]
 

Constraints:

1 <= s.length <= 105
s consists of only digits and does not contain leading zeros.
1 <= k <= 109
Accepted
14,865
Submissions
38,444
Seen this question in a real interview before?

Yes

No
Number of Ways to Separate Numbers
Hard
Number of Beautiful Partitions
Hard
Use dynamic programming. Build an array dp where dp[i] is the number of ways you can divide the string starting from index i to the end.
Keep in mind that the answer is modulo 10^9 + 7 and take the mod for each operation.
''')
