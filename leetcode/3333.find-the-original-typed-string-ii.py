from lc import *

# https://leetcode.com/problems/find-the-original-typed-string-ii/solutions/5989101/intuitive-8-transition-states-top-down-to-optimised-bottom-up-dp/

# TLE
class Solution:
    def possibleStringCount(self, w: str, k: int) -> int:
        t=[len(list(g))for _,g in groupby(w)];f=cache(lambda i,k:k<=0 if i==len(t) else t[i]*f(i+1,k)if k<=0 else sum(f(i+1,k-j)for j in range(1,t[i]+1)));return f(0,k)%(10**9+7)

class Solution:
    def possibleStringCount(self, w: str, k: int) -> int:
        m=10**9+7
        t=[len(list(g))for _,g in groupby(w)]
        if k<=len(t):
            return prod(t)%m
        d = [1]+[0]*k
        for x in reversed(t):
            s = [0]*(k+1)
            s[0]=d[0]
            for i in range(1,k+1):
                s[i]=(s[i-1]+d[i])%m
            for i in range(k,-1,-1):
                c=s[i-1]if i>0 else 0
                if i>x:
                    c=(c-s[i-x-1])%m
                if i<x:
                    c=(c+(x-i)*d[0])%m
                d[i]=c%m
        return d[k]

class Solution:
    def possibleStringCount(self, w: str, k: int) -> int:
        m,d=10**9+7,[1]+[0]*k;return prod(t)%m if k<=len(t:=[len(list(g))for _,g in groupby(w)]) else [(s:=[0]*(k+1),setitem(s,0,d[0]),[setitem(s,i,(s[i-1]+d[i])%m)for i in range(1,k+1)],[(c:=s[i-1] if i>0 else 0,c:=((c-s[i-x-1]) if i>x else (c+(x-i)*d[0]) if i<x else c)%m,setitem(d,i,c%m))for i in range(k,-1,-1)])for x in reversed(t)]and d[k]

test('''
3333. Find the Original Typed String II
Hard
Topics
premium lock icon
Companies
Hint
Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.

You are given a string word, which represents the final output displayed on Alice's screen. You are also given a positive integer k.

Return the total number of possible original strings that Alice might have intended to type, if she was trying to type a string of size at least k.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: word = "aabbccdd", k = 7

Output: 5

Explanation:

The possible strings are: "aabbccdd", "aabbccd", "aabbcdd", "aabccdd", and "abbccdd".

Example 2:

Input: word = "aabbccdd", k = 8

Output: 1

Explanation:

The only possible string is "aabbccdd".

Example 3:

Input: word = "aaabbb", k = 3

Output: 8

 

Constraints:

1 <= word.length <= 5 * 105
word consists only of lowercase English letters.
1 <= k <= 2000
Seen this question in a real interview before?
1/5
Yes
No
Accepted
3,138/19.9K
Acceptance Rate
15.8%
Topics
String
Dynamic Programming
Prefix Sum
icon
Companies
Hint 1
Instead of solving for at least k, can we solve for at most k - 1 length?
Similar Questions
Keyboard Row
Easy
Faulty Keyboard
Easy
''')
