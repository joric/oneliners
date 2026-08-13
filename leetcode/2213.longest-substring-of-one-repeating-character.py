from lc import *

# https://leetcode.com/problems/longest-substring-of-one-repeating-character/editorial/?envType=daily-question&envId=2026-08-13

class Solution:
    def longestRepeating(
        self, s: str, queryCharacters: str, queryIndices: List[int]
    ) -> List[int]:
        n = len(s)
        s = list(s)
        segs = SortedList()
        lens = SortedList()

        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            segs.add((i, j - 1))
            lens.add(j - i)
            i = j

        k = len(queryIndices)
        ans = []

        for q in range(k):
            pos = queryIndices[q]
            ch = queryCharacters[q]

            if s[pos] != ch:
                idx = segs.bisect_right((pos, n)) - 1
                L, R = segs[idx]
                segs.pop(idx)
                lens.remove(R - L + 1)

                if L <= pos - 1:
                    segs.add((L, pos - 1))
                    lens.add(pos - L)
                if pos + 1 <= R:
                    segs.add((pos + 1, R))
                    lens.add(R - pos)

                newL, newR = pos, pos

                if pos + 1 < n and s[pos + 1] == ch:
                    idx2 = segs.bisect_left((pos + 1, -1))
                    if idx2 < len(segs) and segs[idx2][0] == pos + 1:
                        rightL, rightR = segs[idx2]
                        lens.remove(rightR - rightL + 1)
                        newR = rightR
                        segs.pop(idx2)

                if pos > 0 and s[pos - 1] == ch:
                    idx3 = segs.bisect_right((pos - 1, n)) - 1
                    if idx3 >= 0 and segs[idx3][1] == pos - 1:
                        leftL, leftR = segs[idx3]
                        lens.remove(leftR - leftL + 1)
                        newL = leftL
                        segs.pop(idx3)

                segs.add((newL, newR))
                lens.add(newR - newL + 1)
                s[pos] = ch

            ans.append(lens[-1])

        return ans


class Solution:
    def longestRepeating(self, s: str, c: str, i: List[int]) -> List[int]:
        m=1<<17;t=[(0,0,0,1,2,0)]*2*m;u=t.__setitem__;f=lambda j:u(j,(a:=t[2*j],b:=t[2*j+1],max(a[0],b[0],(a[2]+b[1])*(q:=a[4]==b[3])),a[1]+b[1]*(a[5]&q),b[2]+a[2]*(b[5]&q),a[3],b[4],a[5]&b[5]&q)[2:]);t[m:m+len(s)]=[(1,1,1,x,x,1)for x in s];[f(j)for j in range(m-1,0,-1)];return[(u(p:=m+k,(1,1,1,x,x,1)),[f(p:=p>>1)for _ in range(17)],t[1][0])[2]for k,x in zip(i,c)]

test('''
2213. Longest Substring of One Repeating Character
Solved
Hard
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed string s. You are also given a 0-indexed string queryCharacters of length k and a 0-indexed array of integer indices queryIndices of length k, both of which are used to describe k queries.

The ith query updates the character in s at index queryIndices[i] to the character queryCharacters[i].

Return an array lengths of length k where lengths[i] is the length of the longest substring of s consisting of only one repeating character after the ith query is performed.

 

Example 1:

Input: s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
Output: [3,3,4]
Explanation: 
- 1st query updates s = "bbbacc". The longest substring consisting of one repeating character is "bbb" with length 3.
- 2nd query updates s = "bbbccc". 
  The longest substring consisting of one repeating character can be "bbb" or "ccc" with length 3.
- 3rd query updates s = "bbbbcc". The longest substring consisting of one repeating character is "bbbb" with length 4.
Thus, we return [3,3,4].
Example 2:

Input: s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]
Output: [2,3]
Explanation:
- 1st query updates s = "abazz". The longest substring consisting of one repeating character is "zz" with length 2.
- 2nd query updates s = "aaazz". The longest substring consisting of one repeating character is "aaa" with length 3.
Thus, we return [2,3].
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
k == queryCharacters.length == queryIndices.length
1 <= k <= 105
queryCharacters consists of lowercase English letters.
0 <= queryIndices[i] < s.length
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
36,018/62K
Acceptance Rate
58.1%
Topics
Senior Staff
Array
String
Segment Tree
Ordered Set
Weekly Contest 285
icon
Companies
Hint 1
Use a segment tree to perform fast point updates and range queries.
Hint 2
We need each segment tree node to store the length of the longest substring of that segment consisting of only 1 repeating character.
Hint 3
We will also have each segment tree node store the leftmost and rightmost character of the segment, the max length of a prefix substring consisting of only 1 repeating character, and the max length of a suffix substring consisting of only 1 repeating character.
Hint 4
Use this information to properly merge the two segment tree nodes together.
Similar Questions
Merge Intervals
Medium
Longest Repeating Character Replacement
Medium
Consecutive Characters
Easy
Create Sorted Array through Instructions
Hard
Longest Increasing Subsequence II
Hard
''')
