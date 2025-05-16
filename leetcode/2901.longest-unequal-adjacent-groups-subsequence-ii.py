from lc import *

# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/solutions/6741145/six-simple-lines-of-code/?envType=daily-question&envId=2025-05-16

class Solution:
    def getWordsInLongestSubsequence(self, w: List[str], g: List[int]) -> List[str]:
        dp = []
        for s,g1 in zip(w,g):
            dp.append(max((q for t,g2,q in zip(w,g,dp) 
                    if g1!=g2 and len(s)==len(t) and sum(map(ne,s,t))<2),
                key=len,default=[]) + [s])
        return max(dp,key=len)

# TODO failing test suite

class Solution:
    def getWordsInLongestSubsequence(self, w: List[str], g: List[int]) -> List[str]:
        d=[];[d.append(max((q for t,b,q in zip(w,g,d)if a!=b and len(s)==len(t) and sum(map(ne,s,t))<2),key=len,default=[])+[s])for s,a in zip(w,g)];return max(d,key=len)

test('''
2901. Longest Unequal Adjacent Groups Subsequence II
Medium
Topics
Companies
Hint
You are given a string array words, and an array groups, both arrays having length n.

The hamming distance between two strings of equal length is the number of positions at which the corresponding characters are different.

You need to select the longest subsequence from an array of indices [0, 1, ..., n - 1], such that for the subsequence denoted as [i0, i1, ..., ik-1] having length k, the following holds:

For adjacent indices in the subsequence, their corresponding groups are unequal, i.e., groups[ij] != groups[ij+1], for each j where 0 < j + 1 < k.
words[ij] and words[ij+1] are equal in length, and the hamming distance between them is 1, where 0 < j + 1 < k, for all indices in the subsequence.
Return a string array containing the words corresponding to the indices (in order) in the selected subsequence. If there are multiple answers, return any of them.

Note: strings in words may be unequal in length.

 

Example 1:

Input: words = ["bab","dab","cab"], groups = [1,2,2]

Output: ["bab","cab"]

Explanation: A subsequence that can be selected is [0,2].

groups[0] != groups[2]
words[0].length == words[2].length, and the hamming distance between them is 1.
So, a valid answer is [words[0],words[2]] = ["bab","cab"].

Another subsequence that can be selected is [0,1].

groups[0] != groups[1]
words[0].length == words[1].length, and the hamming distance between them is 1.
So, another valid answer is [words[0],words[1]] = ["bab","dab"].

It can be shown that the length of the longest subsequence of indices that satisfies the conditions is 2.

Example 2:

Input: words = ["a","b","c","d"], groups = [1,2,3,4]

Output: ["a","b","c","d"]

Explanation: We can select the subsequence [0,1,2,3].

It satisfies both conditions.

Hence, the answer is [words[0],words[1],words[2],words[3]] = ["a","b","c","d"].

It has the longest length among all subsequences of indices that satisfy the conditions.

Hence, it is the only answer.

 

Constraints:

1 <= n == words.length == groups.length <= 1000
1 <= words[i].length <= 10
1 <= groups[i] <= n
words consists of distinct strings.
words[i] consists of lowercase English letters.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
12.9K
Submissions
45.2K
Acceptance Rate
28.5%
Topics
Array
String
Dynamic Programming
Companies
Hint 1
Let dp[i] represent the length of the longest subsequence ending with words[i] that satisfies the conditions.
Hint 2
dp[i] = (maximum value of dp[j]) + 1 for indices j < i, where groups[i] != groups[j], words[i] and words[j] are equal in length, and the hamming distance between words[i] and words[j] is exactly 1.
Hint 3
Keep track of the j values used to achieve the maximum dp[i] for each index i.
Hint 4
The expected array's length is max(dp[0:n]), and starting from the index having the maximum value in dp, we can trace backward to get the words.
''')
