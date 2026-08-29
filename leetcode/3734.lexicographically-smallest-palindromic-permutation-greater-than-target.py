from lc import *

# https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/solutions/7319845/python3-recursive-solution-backtrack-by-nvh54/?envType=daily-question&envId=2026-08-28

class Solution:
    def lexPalindromicPermutation(self,s:str,t:str)->str:
        c=Counter(s);n=len(s);o=sum(v%2 for v in c.values())
        if(n%2==0 and o>0 or n%2==1 and o!=1):return""
        r=['a']*n;k=sorted(c.keys())
        def f(i,g):
            if i==(n+1)//2-1:
                if n%2:
                    x=[x for x in k if c[x]==1][0];r[i]=x
                else:
                    x=[x for x in k if c[x]==2][0];r[i]=r[i+1]=x
                if g:return 1
                for j in range(n):
                    if r[j]<t[j]:return 0
                    if r[j]>t[j]:return 1
                return 0
            p=[x for x in k if c[x]>1 and (g or x>=t[i])]
            for x in p:
                r[i]=r[n-i-1]=x;c[x]-=2
                if f(i+1,g or x>t[i]):return 1
                c[x]+=2
            return 0
        return"".join(r)if f(0,0)else""

class Solution:
    def lexPalindromicPermutation(self,s:str,t:str)->str:
        c,n=Counter(s),len(s);m=next((x for x in c if c[x]%2),'');f=lambda h,g,i:next((w for w in[h+m+h[::-1]]if g or w>t),'')if i==n//2 else next((r for x in sorted(c)if c[x]>1 and(g or x>=t[i])for v in[c.subtract(x*2)]for r in[f(h+x,g or x>t[i],i+1)]for z in[c.update(x*2)]if r),'');return sum(c[x]%2 for x in c)==n%2 and f('',0,0)or''

class Solution:
    def lexPalindromicPermutation(self,s:str,t:str)->str:
        c=Counter(s);m=''.join(x*(c[x]%2)for x in c);f=lambda h,g,i:next((r for x in sorted(c)if c[x]>1 and(g or x>=t[i])for r in[c.subtract(x*2)or f(h+x,g or x>t[i],i+1)]for z in[c.update(x*2)]if r),'')if i<len(s)//2 else(w:=h+m+h[::-1])*(w>t);return 2>len(m)and f('',0,0)or''

test('''
3734. Lexicographically Smallest Palindromic Permutation Greater Than Target
Hard
Topics
premium lock icon
Companies
Hint
You are given two strings s and target, each of length n, consisting of lowercase English letters.

Return the lexicographically smallest string that is both a palindromic permutation of s and strictly greater than target. If no such permutation exists, return an empty string.

 

Example 1:

Input: s = "baba", target = "abba"

Output: "baab"

Explanation:

The palindromic permutations of s (in lexicographical order) are "abba" and "baab".
The lexicographically smallest permutation that is strictly greater than target is "baab".
Example 2:

Input: s = "baba", target = "bbaa"

Output: ""

Explanation:

The palindromic permutations of s (in lexicographical order) are "abba" and "baab".
None of them is lexicographically strictly greater than target. Therefore, the answer is "".
Example 3:

Input: s = "abc", target = "abb"

Output: ""

Explanation:

s has no palindromic permutations. Therefore, the answer is "".

Example 4:

Input: s = "aac", target = "abb"

Output: "aca"

Explanation:

The only palindromic permutation of s is "aca".
"aca" is strictly greater than target. Therefore, the answer is "aca".
 

Constraints:

1 <= n == s.length == target.length <= 300
s and target consist of only lowercase English letters.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
5,504/21.1K
Acceptance Rate
26.1%
Topics
Senior Staff
Two Pointers
String
Enumeration
Weekly Contest 474
icon
Companies
Hint 1
A palindromic permutation exists only if at most one character has an odd count (for odd-length strings) or all counts are even (for even-length strings).
Hint 2
Focus on constructing the first half of the palindrome. The second half is determined by mirroring.
Hint 3
To be lexicographically greater than target, the first half must be greater than or equal to target's first half, with careful handling of the middle character for odd-length strings.
Hint 4
Use a backtracking approach or greedy selection for each position in the first half, trying the smallest available character that can still produce a valid palindrome.
Hint 5
After building the first half, mirror it (and add the middle character if needed) to form the full palindrome and verify it is strictly greater than target.
''')
