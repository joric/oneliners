from lc import *

# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/submissions/1152229906/?envType=daily-question&envId=2026-07-30

class Solution:
    def minimumPushes(self, word: str) -> int:
        c = sorted(list(Counter(word).values()))[::-1]
        w = [1] * 8 + [2] * 8 + [3] * 8 + [4] * 2
        return sum(u * v for u, v in zip(c, w))

class Solution:
    def minimumPushes(self, w: str) -> int:
        return sum(v*(i//8)for i,v in enumerate(sorted(Counter(w).values())[::-1],8))

class Solution:
    def minimumPushes(self, w: str) -> int:
        c=sorted(map(w.count,{*w}));return sum(c+c[:-8]+c[:-16]+c[:-24])

class Solution:
    def minimumPushes(self, w: str) -> int:
        d,m=divmod(len(w),8);return 8*d*(1+d)//2+m*(d+1)

class Solution:
    def minimumPushes(self, w: str) -> int:
        return((n:=len(w))-n//8*4)*(n//8+1)

class Solution:
    def minimumPushes(self, w: str) -> int:
        n=len(w);t=n//8;return-~t*(n-t*4)

test('''
3014. Minimum Number of Pushes to Type Word I
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given a string word containing distinct lowercase English letters.

Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them. For example, the key 2 is mapped with ["a","b","c"], we need to push the key one time to type "a", two times to type "b", and three times to type "c" .

It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key. You need to find the minimum number of times the keys will be pushed to type the string word.

Return the minimum number of pushes needed to type word after remapping the keys.

An example mapping of letters to keys on a telephone keypad is given below. Note that 1, *, #, and 0 do not map to any letters.


 

Example 1:


Input: word = "abcde"
Output: 5
Explanation: The remapped keypad given in the image provides the minimum cost.
"a" -> one push on key 2
"b" -> one push on key 3
"c" -> one push on key 4
"d" -> one push on key 5
"e" -> one push on key 6
Total cost is 1 + 1 + 1 + 1 + 1 = 5.
It can be shown that no other mapping can provide a lower cost.
Example 2:


Input: word = "xycdefghij"
Output: 12
Explanation: The remapped keypad given in the image provides the minimum cost.
"x" -> one push on key 2
"y" -> two pushes on key 2
"c" -> one push on key 3
"d" -> two pushes on key 3
"e" -> one push on key 4
"f" -> one push on key 5
"g" -> one push on key 6
"h" -> one push on key 7
"i" -> one push on key 8
"j" -> one push on key 9
Total cost is 1 + 2 + 1 + 2 + 1 + 1 + 1 + 1 + 1 + 1 = 12.
It can be shown that no other mapping can provide a lower cost.
 

Constraints:

1 <= word.length <= 26
word consists of lowercase English letters.
All letters in word are distinct.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
53,539/79.8K
Acceptance Rate
67.1%
Topics
Mid Level
Math
String
Greedy
Weekly Contest 381
icon
Companies
Hint 1
We have 8 keys in total. We can type 8 characters with one push each, 8 different characters with two pushes each, and so on.
Hint 2
The optimal way is to map letters to keys evenly.
Similar Questions
Letter Combinations of a Phone Number
Medium
''')

