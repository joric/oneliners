from lc import *

# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/solutions/2040076/python3-1-line/?envType=daily-question&envId=2025-10-13

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        return [w for i, w in enumerate(words) if i == 0 or sorted(words[i-1]) != sorted(w)] 

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        return [w for i, w in enumerate(words) if i == 0 or Counter(words[i-1]) != Counter(w)] 

# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/solutions/5891605/one-line/?envType=daily-question&envId=2025-10-13

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        return [ next(g) for k, g in groupby(words, key=lambda w: sorted(w))]

# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/solutions/5691133/simple-one-line-solution/?envType=daily-question&envId=2025-10-13

class Solution:
    def removeAnagrams(self, w: List[str]) -> List[str]:
        return[next(g)for k,g in groupby(w,key=sorted)]

test('''
2273. Find Resultant Array After Removing Anagrams
Easy
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed string array words, where words[i] consists of lowercase English letters.

In one operation, select any index i such that 0 < i < words.length and words[i - 1] and words[i] are anagrams, and delete words[i] from words. Keep performing this operation as long as you can select an index that satisfies the conditions.

Return words after performing all operations. It can be shown that selecting the indices for each operation in any arbitrary order will lead to the same result.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase using all the original letters exactly once. For example, "dacb" is an anagram of "abdc".

 

Example 1:

Input: words = ["abba","baba","bbaa","cd","cd"]
Output: ["abba","cd"]
Explanation:
One of the ways we can obtain the resultant array is by using the following operations:
- Since words[2] = "bbaa" and words[1] = "baba" are anagrams, we choose index 2 and delete words[2].
  Now words = ["abba","baba","cd","cd"].
- Since words[1] = "baba" and words[0] = "abba" are anagrams, we choose index 1 and delete words[1].
  Now words = ["abba","cd","cd"].
- Since words[2] = "cd" and words[1] = "cd" are anagrams, we choose index 2 and delete words[2].
  Now words = ["abba","cd"].
We can no longer perform any operations, so ["abba","cd"] is the final answer.
Example 2:

Input: words = ["a","b","c","d","e"]
Output: ["a","b","c","d","e"]
Explanation:
No two adjacent strings in words are anagrams of each other, so no operations are performed.
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
90,600/147.8K
Acceptance Rate
61.3%
Topics
Array
Hash Table
String
Sorting
Weekly Contest 293
icon
Companies
Hint 1
Instead of removing each repeating anagram, try to find all the strings in words which will not be present in the final answer.
Hint 2
For every index i, find the largest index j < i such that words[j] will be present in the final answer.
Hint 3
Check if words[i] and words[j] are anagrams. If they are, then it can be confirmed that words[i] will not be present in the final answer.
Similar Questions
Group Anagrams
Medium
Valid Anagram
Easy
''')
