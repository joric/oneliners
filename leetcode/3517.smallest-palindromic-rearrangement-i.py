from lc import *

# https://leetcode.com/problems/smallest-palindromic-rearrangement-i/solutions/8425020/python-one-line-on-by-l1ne-9zw3/?envType=daily-question&envId=2026-07-28

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        d, m = divmod(len(s), 2)
        m = ('', s[d])[m]
        t = ''.join(sorted(s[:d]))
        return ''.join((t, m, t[::-1]))

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        return ''.join((t := ''.join(sorted(s[:(d := divmod(len(s), 2))[0]])), c := ('', s[d[0]])[d[1]], t[::-1]))

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        d, m = divmod(len(s), 2)
        m = ('', s[d])[m]
        t = ''.join(c * x for c,x in sorted(Counter(s[:d]).items()))
        return ''.join((t, m, t[::-1]))

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        return ''.join((t := ''.join(starmap(mul, sorted(Counter(s[:(d := divmod(len(s), 2))[0]]).items()))), c := ('', s[d[0]])[d[1]], t[::-1]))

# https://leetcode.com/problems/smallest-palindromic-rearrangement-i/solutions/6646188/python-one-line-counter-by-ante-3m5t/?envType=daily-question&envId=2026-07-28

chars = string.ascii_lowercase
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        return (lambda cc: (lambda r: r + next(iter(c for c in chars if cc[c] % 2), '') + r[::-1])(''.join([c * (cc[c] // 2) for c in chars])))(Counter(s))     

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        a=sorted(c:=Counter(s));return(r:=''.join(x*(c[x]>>1)for x in a))+next((x for x in a if c[x]&1),'')+r[::-1]

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n=len(s);h=''.join(sorted(s[:n//2]));return h+['',s[n//2]][n%2]+h[::-1]

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n=len(s);h=''.join(sorted(s[:n//2]));return h+s[n//2]*(n%2)+h[::-1]

class Solution:
    def smallestPalindrome(self,s):
        return((a:=str(sorted(s)))+s[len(s)//2]*5+a[::-1])[7::10]

test('''
3517. Smallest Palindromic Rearrangement I
Medium
Topics
premium lock icon
Companies
Hint
You are given a palindromic string s.

Return the lexicographically smallest palindromic permutation of s.

 

Example 1:

Input: s = "z"

Output: "z"

Explanation:

A string of only one character is already the lexicographically smallest palindrome.

Example 2:

Input: s = "babab"

Output: "abbba"

Explanation:

Rearranging "babab" → "abbba" gives the smallest lexicographic palindrome.

Example 3:

Input: s = "daccad"

Output: "acddca"

Explanation:

Rearranging "daccad" → "acddca" gives the smallest lexicographic palindrome.

 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
s is guaranteed to be palindromic.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
36,798/57.5K
Acceptance Rate
64.0%
Topics
icon
Companies
Hint 1
Consider a palindrome as composed of two mirror-image halves.
Hint 2
Construct one half (using s), and then the other half is its reverse to obtain the lexicographically smallest permutation.
Similar Questions
Shortest Palindrome
Hard
''')
