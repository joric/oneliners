from lc import *

# https://leetcode.com/problems/delete-columns-to-make-sorted-ii/solutions/203042/delete-columns-to-make-sorted-ii-by-leet-bvi2/?envType=daily-question&envId=2025-12-21

class Solution:
    def minDeletionSize(self, s: List[str]) -> int:
        t=[0]*~-len(s)
        r = 0
        for c in zip(*s):
            if all(t[i] or c[i]<=c[i+1] for i in range(len(c)-1)):
                for i in range(len(c)-1):
                    if c[i]<c[i+1]:
                        t[i] = 1
            else:
                r += 1
        return r

class Solution:
    def minDeletionSize(self, s: List[str]) -> int:
        t=[0]*~-len(s);return sum(not all(t[i]or c[i]<=c[i+1]for i in range(len(c)-1))or[setitem(t,i,c[i]<c[i+1])for i in range(len(c)-1)]and 0 for c in zip(*s))

# https://leetcode.com/problems/delete-columns-to-make-sorted-ii/solutions/3920690/python-3-6-lines-w-explanation-ts-53-54-vx1jx/?envType=daily-question&envId=2025-12-21

class Solution: 
    def minDeletionSize(self, strs: List[str]) -> int:
        tpse, n, m = zip(*strs), len(strs), len(strs[0])
        strs = [''] * n
        for nxt in tpse:
            temp = [strs[i]+nxt[i] for i in range(n)]
            if temp == sorted(temp): strs = temp
        return m - len(strs[0])

class Solution:
    def minDeletionSize(self, s: List[str]) -> int:
        n=len(s);r=['']*n;[r:=t for x in zip(*s)if(t:=[r[i]+x[i]for i in range(n)])==sorted(t)];return len(s[0])-len(r[0])

class Solution:
    def minDeletionSize(self, s: List[str]) -> int:
        r=['']*len(s);[r:=t for c in zip(*s)if(t:=[x+c[i]for i,x in enumerate(r)])==sorted(t)];return len(s[0])-len(r[0])

class Solution:
    def minDeletionSize(self, s: List[str]) -> int:
        r=['']*len(s);[r:=t for c in zip(*s)if(t:=[a+b for a,b in zip(r,c)])==sorted(t)];return len(s[0])-len(r[0])

class Solution:
    def minDeletionSize(self, s: List[str]) -> int:
        r=['']*len(s)
        for c in zip(*s):
            if (t:=[a+b for a,b in zip(r,c)])==sorted(t):
                r =t 
        return len(s[0])-len(r[0])

class Solution:
    def minDeletionSize(self, s: List[str]) -> int:
        p=['']*len(s)
        r = 0
        for c in zip(*s):
            if(t:=[a+b for a,b in zip(p,c)])==sorted(t):
                p = t
            else:
                r += 1
        return r

class Solution:
    def minDeletionSize(self, s: List[str]) -> int:
        p=['']*len(s);return sum(sorted(t:=[*map(''.join,zip(p,c))])!=t or not(p:=t)for c in zip(*s))

test('''
955. Delete Columns to Make Sorted II
Medium
Topics
premium lock icon
Companies
You are given an array of n strings strs, all of the same length.

We may choose any deletion indices, and we delete all the characters in those indices for each string.

For example, if we have strs = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef", "vyz"].

Suppose we chose a set of deletion indices answer such that after deletions, the final array has its elements in lexicographic order (i.e., strs[0] <= strs[1] <= strs[2] <= ... <= strs[n - 1]). Return the minimum possible value of answer.length.

 

Example 1:

Input: strs = ["ca","bb","ac"]
Output: 1
Explanation: 
After deleting the first column, strs = ["a", "b", "c"].
Now strs is in lexicographic order (ie. strs[0] <= strs[1] <= strs[2]).
We require at least 1 deletion since initially strs was not in lexicographic order, so the answer is 1.
Example 2:

Input: strs = ["xc","yb","za"]
Output: 0
Explanation: 
strs is already in lexicographic order, so we do not need to delete anything.
Note that the rows of strs are not necessarily in lexicographic order:
i.e., it is NOT necessarily true that (strs[0][0] <= strs[0][1] <= ...)
Example 3:

Input: strs = ["zyx","wvu","tsr"]
Output: 3
Explanation: We have to delete every column.


Other examples:

Input: strs = ["xga","xfb","yfa"]
Output: 1

Constraints:

n == strs.length
1 <= n <= 100
1 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
38,038/91.1K
Acceptance Rate
41.8%
Topics
Array
String
Greedy
Weekly Contest 114
''')
