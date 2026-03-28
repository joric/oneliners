from lc import *

# https://leetcode.com/problems/find-the-string-with-lcp/solutions/7694066/find-the-string-with-lcp-by-leetcode-wdv6/?envType=daily-question&envId=2026-03-28

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        word = [""] * n
        current = ord("a")
        # construct the string starting from 'a' to 'z' sequentially
        for i in range(n):
            if not word[i]:
                if current > ord("z"):
                    return ""
                word[i] = chr(current)
                for j in range(i + 1, n):
                    if lcp[i][j]:
                        word[j] = word[i]
                current += 1
        # verify if the constructed string meets the LCP matrix requirements
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] != word[j]:
                    if lcp[i][j]:
                        return ""
                else:
                    if i == n - 1 or j == n - 1:
                        if lcp[i][j] != 1:
                            return ""
                    else:
                        if lcp[i][j] != lcp[i + 1][j + 1] + 1:
                            return ""
        return "".join(word)

# https://leetcode.com/problems/find-the-string-with-lcp/solutions/3203816/javacpython-check-same-characters-by-lee-nrl0/?envType=daily-question&envId=2026-03-28

class Solution:
    def findTheString(self, p: List[List[int]]) -> str:
        n = len(p)
        a = [0] * n
        c = 1
        for i in range(n):
            if a[i]: continue
            if c > 26: return ''
            for j in range(i, n):
                if p[i][j]:
                    a[j] = c
            c += 1
        for i in range(n):
            for j in range(n):
                v = p[i + 1][j + 1] if i + 1 < n and j + 1 < n else 0
                v = v + 1 if a[i] == a[j] else 0
                if p[i][j] != v:
                    return ''
        return ''.join(chr(ord('a') + i - 1) for i in a)

class Solution:
    def findTheString(self, p: List[List[int]]) -> str:
        n=len(p);c,a=1,[0]*n;return''if any(c>26 or([setitem(a,j,c)for j in range(i,n)if p[i][j]],c:=c+1)<()for i in range(n)if not a[i])or any(p[i][j]!=(1+(i<n-1>j and p[i+1][j+1]))*(a[i]==a[j])for i in range(n)for j in range(n))else''.join(chr(96+x)for x in a)

class Solution:
    def findTheString(self, p: List[List[int]]) -> str:
        n=len(p);c,a=1,[0]*n;return''if any(c>26 or([setitem(a,j,c)for j in range(i,n)if p[i][j]],c:=c+1)<()for i in range(n)if a[i]<1)or any(p[i][j]!=(1+(i<n-1>j and p[i+1][j+1]))*(a[i]==a[j])for i,j in product(*[range(n)]*2))else''.join(chr(96+x)for x in a)

class Solution:
    def findTheString(self, p: List[List[int]]) -> str:
        n=len(p);r=range(n);c,a=1,[0]*n;return''if any(c>26 or([setitem(a,j,c)for j in r[i:]if p[i][j]],c:=c+1)<()for i in r if a[i]<1)or any(p[i][j]!=(1+(i<n-1>j and p[i+1][j+1]))*(a[i]==a[j])for i,j in product(r,r))else''.join(chr(96+x)for x in a)

test('''
2573. Find the String with LCP
Hard
Topics
premium lock icon
Companies
Hint
We define the lcp matrix of any 0-indexed string word of n lowercase English letters as an n x n grid such that:

lcp[i][j] is equal to the length of the longest common prefix between the substrings word[i,n-1] and word[j,n-1].
Given an n x n matrix lcp, return the alphabetically smallest string word that corresponds to lcp. If there is no such string, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b. For example, "aabd" is lexicographically smaller than "aaca" because the first position they differ is at the third letter, and 'b' comes before 'c'.

 

Example 1:

Input: lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
Output: "abab"
Explanation: lcp corresponds to any 4 letter string with two alternating letters. The lexicographically smallest of them is "abab".
Example 2:

Input: lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]
Output: "aaaa"
Explanation: lcp corresponds to any 4 letter string with a single distinct letter. The lexicographically smallest of them is "aaaa". 
Example 3:

Input: lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]
Output: ""
Explanation: lcp[3][3] cannot be equal to 3 since word[3,...,3] consists of only a single letter; Thus, no answer exists.
 

Constraints:

1 <= n == lcp.length == lcp[i].length <= 1000
0 <= lcp[i][j] <= n
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
7,249/22.1K
Acceptance Rate
32.8%
Topics
Senior Staff
Array
String
Dynamic Programming
Greedy
Union-Find
Matrix
Weekly Contest 333
icon
Companies
Hint 1
Use the LCP array to determine which groups of elements must be equal.
Hint 2
Match the smallest letter to the group that contains the smallest unassigned index.
Hint 3
Build the LCP matrix of the resulting string then check if it is equal to the target LCP.
''')
