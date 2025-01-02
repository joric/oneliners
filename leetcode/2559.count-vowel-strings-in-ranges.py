from lc import *

# https://leetcode.com/problems/count-vowel-strings-in-ranges/solutions/3145858/python-3-line-solution-prefix-sum/?envType=daily-question&envId=2025-01-02

class Solution:
    def vowelStrings(self, w: List[str], q: List[List[int]]) -> List[int]:
        p=[0,*accumulate(s[0]in'aeiou'and s[-1]in'aeiou'for s in w)];return[p[j+1]-p[i]for i,j in q]

class Solution:
    def vowelStrings(self, w: List[str], q: List[List[int]]) -> List[int]:
        p=[0,*accumulate({s[0],s[-1]}<{*'aeiou'}for s in w)];return[p[j+1]-p[i]for i,j in q]

test('''
2559. Count Vowel Strings in Ranges
Solved
Medium
Topics
Companies
Hint
You are given a 0-indexed array of strings words and a 2D array of integers queries.

Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
Output: [2,3,0]
Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
The answer to the query [0,2] is 2 (strings "aba" and "ece").
to query [1,4] is 3 (strings "ece", "aa", "e").
to query [1,1] is 0.
We return [2,3,0].
Example 2:

Input: words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
Output: [3,2,1]
Explanation: Every string satisfies the conditions, so we return [3,2,1].
 

Constraints:

1 <= words.length <= 105
1 <= words[i].length <= 40
words[i] consists only of lowercase English letters.
sum(words[i].length) <= 3 * 105
1 <= queries.length <= 105
0 <= li <= ri < words.length
''')
