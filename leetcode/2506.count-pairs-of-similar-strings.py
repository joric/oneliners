from lc import *

# https://leetcode.com/problems/count-pairs-of-similar-strings/solutions/3458283/solution-using-combinatorics/

class Solution:
    def similarPairs(self, w: List[str]) -> int:
        return sum(comb(x,2)for x in Counter(map(frozenset,w)).values())

# js: similarPairs=w=>Object.values(w.map(e=>[...new Set([...e].sort())].join('')).reduce((a,n)=>(a[n]=++a[n]||1,a),{})).reduce((a,b)=>a+=(b*(b-1)/2),0);

# https://leetcode.com/problems/count-pairs-of-similar-strings/solutions/4097926/one-line-solution/

class Solution:
    def similarPairs(self, w: List[str]) -> int:
        return sum(a==b for a,b in combinations(map(set,w),2))

class Solution:
    def similarPairs(self, w: List[str]) -> int:
        return sum(starmap(eq,combinations(map(set,w),2)))

test('''
2506. Count Pairs Of Similar Strings
Solved
Easy
Topics
Companies
Hint
You are given a 0-indexed string array words.

Two strings are similar if they consist of the same characters.

For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c'.
However, "abacba" and "bcfd" are not similar since they do not consist of the same characters.
Return the number of pairs (i, j) such that 0 <= i < j <= word.length - 1 and the two strings words[i] and words[j] are similar.

 

Example 1:

Input: words = ["aba","aabb","abcd","bac","aabc"]
Output: 2
Explanation: There are 2 pairs that satisfy the conditions:
- i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'. 
- i = 3 and j = 4 : both words[3] and words[4] only consist of characters 'a', 'b', and 'c'. 
Example 2:

Input: words = ["aabb","ab","ba"]
Output: 3
Explanation: There are 3 pairs that satisfy the conditions:
- i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'. 
- i = 0 and j = 2 : both words[0] and words[2] only consist of characters 'a' and 'b'.
- i = 1 and j = 2 : both words[1] and words[2] only consist of characters 'a' and 'b'.
Example 3:

Input: words = ["nba","cba","dba"]
Output: 0
Explanation: Since there does not exist any pair that satisfies the conditions, we return 0.
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consist of only lowercase English letters.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
58.1K
Submissions
80.5K
Acceptance Rate
72.1%
Topics
Array
Hash Table
String
Bit Manipulation
Counting
Companies
Hint 1
How can you check if two strings are similar?
Hint 2
Use a hashSet to store the character of each string.
''')
