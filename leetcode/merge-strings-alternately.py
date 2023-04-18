from lc import *

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(chain.from_iterable(zip_longest(word1,word2,fillvalue='')))

class Solution:
    def mergeAlternately(self, a: str, b: str) -> str:
        return ''.join(x+y for x,y in zip_longest(a,b,fillvalue=''))

class Solution:
    def mergeAlternately(self, a: str, b: str) -> str:
        return ''.join(map(''.join,zip_longest(a,b,fillvalue='')))

class Solution:
    def mergeAlternately(self, a: str, b: str) -> str:
        return (j:=''.join)(map(j,zip_longest(a,b,fillvalue='')))

class Solution:
    def mergeAlternately(self, a: str, b: str) -> str:
        return ''.join(chain(*zip_longest(a,b,fillvalue='')))

class Solution:
    def mergeAlternately(self, a, b):
        return ''.join(map(add,a,b))+b[len(a):]+a[len(b):]

test('''
1768. Merge Strings Alternately
Easy

1008

18

Add to List

Share
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
Accepted
99,123
Submissions
127,593
Seen this question in a real interview before?

Yes

No
Use two pointers, one pointer for each string. Alternately choose the character from each pointer, and move the pointer upwards.
''')

