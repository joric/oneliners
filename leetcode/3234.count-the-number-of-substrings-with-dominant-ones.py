from lc import *

# https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/solutions/5622001/readable-short-simple-by-hints_xxx-f02z/?envType=daily-question&envId=2025-11-15

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        c=z=0;q=[]
        for i,h in enumerate(s):
            if h=='0':q.append(i);z+=1
            c+=i-q[-1] if z>0 else i+1
            for k in range(1,z+1):
                t=k*k+k
                if t>i+1:
                    break
                a = q[-k]
                b = q[-k-1]+1 if k<z else 0
                w = i-b+1
                if t>w:
                    continue
                c += min(w-t,a-b)+1
        return c

# TLE already

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        c=z=0;q=[]
        for i,h in enumerate(s):
            if h=='0':
                q.append(i)
                z+=1
            c += i-q[-1] if z>0 else i+1
            c += sum(1+min(w-t,q[-k]-b)for k in range(1,z+1)if i+1>=(t:=k*k+k)<=(w:=i-(b:=k<z and-~q[-k-1]or 0)+1))
        return c

# https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/solutions/5546535/python3-30-lines-slicing-window-on15-by-isl9m/

# 7000+
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n=len(s);c=0;z=[]
        for i,h in enumerate(s):
            if h=='0':z.append(i)
            k=0
            while k<=len(z):
                t=k*k+k
                if t>i+1:break
                a=z[-1-k] if k<len(z) else -1
                b=z[-k] if k>0 else i
                m=i-b+1
                x=i-a
                if m>=t:c+=x-m+1
                elif m<=t<=x:c+=x-t+1
                k+=1
        return c

# https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/solutions/7349267/count-the-number-of-substrings-with-domi-eomt/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        pre = [-1] * (n + 1)
        for i in range(n):
            if i == 0 or s[i - 1] == "0":
                pre[i + 1] = i
            else:
                pre[i + 1] = pre[i]
        res = 0
        for i in range(1, n + 1):
            cnt0 = 1 if s[i - 1] == "0" else 0
            j = i
            while j > 0 and cnt0 * cnt0 <= n:
                cnt1 = (i - pre[j]) - cnt0
                if cnt0 * cnt0 <= cnt1:
                    res += min(j - pre[j], cnt1 - cnt0 * cnt0 + 1)
                j = pre[j]
                cnt0 += 1
        return res

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n=len(s);p=[-1,*accumulate(range(n),lambda p,i:(i,p)[i>0 and s[i-1]>'0'])]
        r=0
        for i in range(1,n+1):
            c = 1 if s[i-1]=='0' else 0
            j = i
            while j>0 and c*c<=n:
                d = (i-p[j])-c
                if c*c<=d: r += min(j-p[j],d-c*c+1)
                j = p[j]
                c += 1
        return r

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n=len(s);p=[-1,*accumulate(range(n),lambda p,i:(i,p)[i and'0'<s[i-1]])];f=lambda i,j,c,r:f(i,p[j],c+1,r+min(j-p[j],d-c*c+1)if c*c<=(d:=(i-p[j])-c)else r)if j>0 and c*c<=n else r;return sum(f(i,i,s[i-1]=='0',0)for i in range(1,n+1))

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n=len(s);p=[-1,*accumulate(range(n),lambda p,i:(i,p)[i and'0'<s[i-1]])];f=lambda i,j,c:j>0 and c*c<=n and f(i,p[j],c+1)+(c*c<=(d:=(i-p[j])-c))*min(j-p[j],d-c*c+1);return sum(f(i,i,s[i-1]=='0')for i in range(1,n+1))

test('''
3234. Count the Number of Substrings With Dominant Ones
Medium
Topics
premium lock icon
Companies
Hint
You are given a binary string s.

Return the number of substrings with dominant ones.

A string has dominant ones if the number of ones in the string is greater than or equal to the square of the number of zeros in the string.

 

Example 1:

Input: s = "00011"

Output: 5

Explanation:

The substrings with dominant ones are shown in the table below.

i   j   s[i..j] Number of Zeros Number of Ones
3   3   1   0   1
4   4   1   0   1
2   3   01  1   1
3   4   11  0   2
2   4   011 1   2
Example 2:

Input: s = "101101"

Output: 16

Explanation:

The substrings with non-dominant ones are shown in the table below.

Since there are 21 substrings total and 5 of them have non-dominant ones, it follows that there are 16 substrings with dominant ones.

i   j   s[i..j] Number of Zeros Number of Ones
1   1   0   1   0
4   4   0   1   0
1   4   0110    2   2
0   4   10110   2   3
1   5   01101   2   3
 

Constraints:

1 <= s.length <= 4 * 104
s consists only of characters '0' and '1'.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
14,074/62.3K
Acceptance Rate
22.6%
Topics
String
Sliding Window
Enumeration
Weekly Contest 408
icon
Companies
Hint 1
Let us fix the starting index l of the substring and count the number of indices r such that l <= r and the substring s[l..r] has dominant ones.
Hint 2
A substring with dominant ones has at most sqrt(n) zeros.
Hint 3
We cannot iterate over every r and check if the s[l..r] has dominant ones. Instead, we iterate over the next sqrt(n) zeros to the left of l and count the number of substrings with dominant ones where the current zero is the rightmost zero of the substring.
Similar Questions
Count Binary Substrings
Easy
''')
