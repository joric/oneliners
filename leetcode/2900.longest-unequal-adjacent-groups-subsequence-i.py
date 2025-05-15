from lc import *

# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/solutions/5157222/one-line-solution/?envType=daily-question&envId=2025-05-15

class Solution:
    def getLongestSubsequence(self, w: List[str], g: List[int]) -> List[str]:
        return[w[0],*(w[i]for i in range(1,len(w))if g[i]!=g[i-1])]

class Solution:
    def getLongestSubsequence(self, w: List[str], g: List[int]) -> List[str]:
        return[next(p)[0]for _,p in groupby(zip(w,g),itemgetter(1))]

test('''
2900. Longest Unequal Adjacent Groups Subsequence I
Solved
Easy
Topics
Companies
Hint
You are given a string array words and a binary array groups both of length n, where words[i] is associated with groups[i].

Your task is to select the longest alternating subsequence from words. A subsequence of words is alternating if for any two consecutive strings in the sequence, their corresponding elements in the binary array groups differ. Essentially, you are to choose strings such that adjacent elements have non-matching corresponding bits in the groups array.

Formally, you need to find the longest subsequence of an array of indices [0, 1, ..., n - 1] denoted as [i0, i1, ..., ik-1], such that groups[ij] != groups[ij+1] for each 0 <= j < k - 1 and then find the words corresponding to these indices.

Return the selected subsequence. If there are multiple answers, return any of them.

Note: The elements in words are distinct.

 

Example 1:

Input: words = ["e","a","b"], groups = [0,0,1]

Output: ["e","b"]

Explanation: A subsequence that can be selected is ["e","b"] because groups[0] != groups[2]. Another subsequence that can be selected is ["a","b"] because groups[1] != groups[2]. It can be demonstrated that the length of the longest subsequence of indices that satisfies the condition is 2.

Example 2:

Input: words = ["a","b","c","d"], groups = [1,0,1,1]

Output: ["a","b","c"]

Explanation: A subsequence that can be selected is ["a","b","c"] because groups[0] != groups[1] and groups[1] != groups[2]. Another subsequence that can be selected is ["a","b","d"] because groups[0] != groups[1] and groups[1] != groups[3]. It can be shown that the length of the longest subsequence of indices that satisfies the condition is 3.

 

Constraints:

1 <= n == words.length == groups.length <= 100
1 <= words[i].length <= 10
groups[i] is either 0 or 1.
words consists of distinct strings.
words[i] consists of lowercase English letters.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
39K
Submissions
65.2K
Acceptance Rate
59.8%
Topics
Array
String
Dynamic Programming
Greedy
Companies
Hint 1
This problem can be solved greedily.
Hint 2
Begin by constructing the answer starting with the first number in groups.
Hint 3
For each index i in the range [1, n - 1], add i to the answer if groups[i] != groups[i - 1].
''')
