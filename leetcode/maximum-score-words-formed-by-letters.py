from lc import *

# https://leetcode.com/problems/maximum-score-words-formed-by-letters/discuss/1214997/Python-3-one-line

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        values = {w: sum(score[ord(c)-ord('a')] for c in w) for w in words}
        counters = {w: Counter(w) for w in words}
        def dfs(counts, i):
            best = 0
            for j in range(i, len(words)):
                word = words[j]
                if not counters[word] - counts:
                    best = max(best, values[word] + dfs(counts - counters[word], j+1))
            return best
        return dfs(Counter(letters), 0)

class Solution:
  def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
    return (
      dfs := lambda counts, i: max(
        (sum(score[ord(c)-ord('a')] for c in words[j]) + dfs(counts - Counter(words[j]), j+1)
         for j in range(i, len(words))
         if not Counter(words[j]) - counts
        ), default=0
      )
    )(Counter(letters), 0)

class Solution:
    def maxScoreWords(self, w: List[str], l: List[str], s: List[int]) -> int:
        c=Counter;return(f:=lambda n,i:max((sum(s[ord(x)-ord('a')]for x in w[j])+f(n-c(w[j]),j+1)for j in range(i,len(w))if not c(w[j])-n),default=0))(c(l), 0)

class Solution:
    def maxScoreWords(self, w: List[str], l: List[str], s: List[int]) -> int:
        c=Counter;return(f:=lambda n,i:max([sum(s[ord(x)-97]for x in w[j])+f(n-c(w[j]),j+1)for j in range(i,len(w))if not c(w[j])-n]+[0]))(c(l),0)

test('''
1255. Maximum Score Words Formed by Letters
Hard

1420

82

Add to List

Share
Given a list of words, list of  single letters (might be repeating) and score of every character.

Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).

It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.

 

Example 1:

Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
Output: 23
Explanation:
Score  a=1, c=9, d=5, g=3, o=2
Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
Words "dad" and "dog" only get a score of 21.
Example 2:

Input: words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
Output: 27
Explanation:
Score  a=4, b=4, c=4, x=5, z=10
Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5) with a score of 27.
Word "xxxz" only get a score of 25.
Example 3:

Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
Output: 0
Explanation:
Letter "e" can only be used once.

Other examples:

Input: words = ["add","dda","bb","ba","add"], letters = ["a","a","a","a","b","b","b","b","c","c","c","c","c","d","d","d"], score = [3,9,8,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: 51

Constraints:

1 <= words.length <= 14
1 <= words[i].length <= 15
1 <= letters.length <= 100
letters[i].length == 1
score.length == 26
0 <= score[i] <= 10
words[i], letters[i] contains only lower case English letters.
Accepted
60,000
Submissions
77,056
''')

