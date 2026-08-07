from lc import *

# https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/solutions/5851688/3d-dp-python-beats-100-by-mkshv-tqvi/?envType=daily-question&envId=2026-08-08

class Solution:
    def validSequence(self, a: str, b: str) -> List[int]:
        t = []
        @cache 
        def f(i, j, k):
            if j == len(b): return True
            if i == len(a): return False

            if a[i] == b[j]:
                p = f(i+1,j+1,k)
                if p:
                    t.append(i)
                return p

            if k:
                p = f(i+1,j+1,0)
                if p:
                    t.append(i)
                    return True

            while i < len(a) and a[i] != b[j]:
                i += 1 

            return f(i,j,k)

        return t[::-1] if f(0, 0, 1) else []

class Solution:
    def validSequence(self, a: str, b: str) -> List[int]:
        t=[];p=t.append;f=cache(lambda i,j,k:j==len(b)or i<len(a)and(f(i+1,j+1,k)and[p(i)]if a[i]==b[j]else k and f(i+1,j+1,0)and[p(i)]or~(m:=a.find(b[j],i))and f(m+1,j+1,k)and[p(m)]));return t[::-1]if f(0,0,1)else[]

class Solution: # TLE
    def validSequence(self, a: str, b: str) -> List[int]:
        t=[];f=cache(lambda i,j,k:j==len(b)or i<len(a)and(((c:=a[i]==b[j])or k)and f(i+1,j+1,k*c)and[t.append(i)]or f(i+1,j,k)));f(0,0,1);return t[::-1]

class Solution:
    def validSequence(self, a: str, b: str) -> List[int]:
        t=[];p=t.append;f=cache(lambda i,j,k:j==len(b)or i<len(a)and((m:=a.find(b[j],i))==i and f(i+1,j+1,k)and[p(i)]or k and f(i+1,j+1,0)and[p(i)]or~m and f(m+1,j+1,k)and[p(m)]));return t[::-1]if f(0,0,1)else[]

test('''
3302. Find the Lexicographically Smallest Valid Sequence
Medium
Topics
premium lock icon
Companies
Hint
You are given two strings word1 and word2.

A string x is called almost equal to y if you can change at most one character in x to make it identical to y.

A sequence of indices seq is called valid if:

The indices are sorted in ascending order.
Concatenating the characters at these indices in word1 in the same order results in a string that is almost equal to word2.
Return an array of size word2.length representing the lexicographically smallest valid sequence of indices. If no such sequence of indices exists, return an empty array.

Note that the answer must represent the lexicographically smallest array, not the corresponding string formed by those indices.

 

Example 1:

Input: word1 = "vbcca", word2 = "abc"

Output: [0,1,2]

Explanation:

The lexicographically smallest valid sequence of indices is [0, 1, 2]:

Change word1[0] to 'a'.
word1[1] is already 'b'.
word1[2] is already 'c'.
Example 2:

Input: word1 = "bacdc", word2 = "abc"

Output: [1,2,4]

Explanation:

The lexicographically smallest valid sequence of indices is [1, 2, 4]:

word1[1] is already 'a'.
Change word1[2] to 'b'.
word1[4] is already 'c'.
Example 3:

Input: word1 = "aaaaaa", word2 = "aaabc"

Output: []

Explanation:

There is no valid sequence of indices.

Example 4:

Input: word1 = "abc", word2 = "ab"

Output: [0,1]

 

Constraints:

1 <= word2.length < word1.length <= 3 * 105
word1 and word2 consist only of lowercase English letters.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
8,042/35.9K
Acceptance Rate
22.4%
Topics
Staff
Two Pointers
String
Dynamic Programming
Greedy
Biweekly Contest 140
icon
Companies
Hint 1
Let dp[i] be the longest suffix of word2 that exists as a subsequence of suffix of the substring of word1 starting at index i.
Hint 2
If dp[i + 1] < m and word1[i] == word2[m - dp[i + 1] - 1],dp[i] =  dp[i + 1] + 1. Otherwise, dp[i] =  dp[i + 1].
Hint 3
For each index i, greedily select characters using the dp array to know whether a solution exists.
Similar Questions
Smallest K-Length Subsequence With Occurrences of a Letter
Hard
''')
