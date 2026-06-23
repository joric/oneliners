from lc import *

# https://leetcode.com/problems/weighted-word-mapping/solutions/7579333/python-one-line-by-ante-dg7k/?envType=daily-question&envId=2026-06-13

class Solution:
    def mapWordWeights(self, d: List[str], p: List[int]) -> str:
        return''.join(ascii_lowercase[::-1][sum(map(lambda c:p[ascii_lowercase.index(c)],s))%26] for s in d)

# https://leetcode.com/problems/weighted-word-mapping/solutions/7579677/one-line-solution-by-xxxxkav-urtj/?envType=daily-question&envId=2026-06-13

class Solution:
    def mapWordWeights(self, d: List[str], p: List[int]) -> str:
        return''.join(chr(122-sum(p[ord(c)-97]for c in w)%26)for w in d)

test('''
3838. Weighted Word Mapping
Easy
Topics
premium lock icon
Companies
Hint
You are given an array of strings words, where each string represents a word containing lowercase English letters.

You are also given an integer array weights of length 26, where weights[i] represents the weight of the ith lowercase English letter.

The weight of a word is defined as the sum of the weights of its characters.

For each word, take its weight modulo 26 and map the result to a lowercase English letter using reverse alphabetical order (0 -> 'z', 1 -> 'y', ..., 25 -> 'a').

Return a string formed by concatenating the mapped characters for all words in order.

 

Example 1:

Input: words = ["abcd","def","xyz"], weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]

Output: "rij"

Explanation:

The weight of "abcd" is 5 + 3 + 12 + 14 = 34. The result modulo 26 is 34 % 26 = 8, which maps to 'r'.
The weight of "def" is 14 + 1 + 2 = 17. The result modulo 26 is 17 % 26 = 17, which maps to 'i'.
The weight of "xyz" is 7 + 7 + 2 = 16. The result modulo 26 is 16 % 26 = 16, which maps to 'j'.
Thus, the string formed by concatenating the mapped characters is "rij".

Example 2:

Input: words = ["a","b","c"], weights = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

Output: "yyy"

Explanation:

Each word has weight 1. The result modulo 26 is 1 % 26 = 1, which maps to 'y'.

Thus, the string formed by concatenating the mapped characters is "yyy".

Example 3:

Input: words = ["abcd"], weights = [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5]

Output: "g"

Explanation:​​​​​​​

The weight of "abcd" is 7 + 5 + 3 + 4 = 19. The result modulo 26 is 19 % 26 = 19, which maps to 'g'.

Thus, the string formed by concatenating the mapped characters is "g".

 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 10
weights.length == 26
1 <= weights[i] <= 100
words[i] consists of lowercase English letters.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
50,502/58.8K
Acceptance Rate
85.8%
Topics
Mid Level
Array
String
Simulation
Biweekly Contest 176
icon
Companies
Hint 1
For each word, sum character weights using weights[c - 'a']
Hint 2
Take the sum modulo 26
Hint 3
Map the value to a character using reverse order: char = 'z' - value
Hint 4
Append all mapped characters in order to form the result string
''')
