from lc import *

# https://leetcode.com/problems/k-similar-strings/solutions/2604488/python-a-few-code-with-cache-by-jiezhi-s3uw/

class Solution:
    @cache
    def kSimilarity(self, a: str, b: str) -> int:
        if not a:
            return 0
        if a[0]==b[0]:
            return self.kSimilarity(a[1:],b[1:])
        return min(1 + self.kSimilarity(a[1:],b[1:x]+b[0]+b[x+1:])for x in range(len(a))if a[0]==b[x])

class Solution:
    def kSimilarity(self, a: str, b: str) -> int:
        return(f:=cache(lambda a,b:a and(a[0]!=b[0]and min(1+f(a[1:],b[1:i]+b[0]+b[i+1:])for i in range(len(a))if a[0]==b[i])or f(a[1:],b[1:]))or 0))(a,b)

class Solution:
    def kSimilarity(self, a: str, b: str) -> int:
        return(f:=cache(lambda a,b:a and(a[0]!=b[0]and min(1+f(a[1:],b[1:i]+b[0]+b[i+1:])for i,c in enumerate(b)if c==a[0])or f(a[1:],b[1:]))or 0))(a,b)

class Solution:
    def kSimilarity(self,a:str,b:str)->int:
        return(f:=cache(lambda i,b:a[i:]and(a[i]!=b[0]and min(1+f(i+1,b[1:j]+b[0]+b[j+1:])for j,c in enumerate(b)if c==a[i])or f(i+1,b[1:]))or 0))(0,b)

class Solution:
    def kSimilarity(self, a: str, b: str) -> int:
        return(f:=cache(lambda b:b and((x:=a[-len(b)])!=b[0]and 1+min(f(b[1:j]+b[0]+b[j+1:])for j,c in enumerate(b)if c==x)or f(b[1:]))or 0))(b)

test('''
854. K-Similar Strings
Hard
Topics
premium lock icon
Companies
Strings s1 and s2 are k-similar (for some non-negative integer k) if we can swap the positions of two letters in s1 exactly k times so that the resulting string equals s2.

Given two anagrams s1 and s2, return the smallest k for which s1 and s2 are k-similar.

 

Example 1:

Input: s1 = "ab", s2 = "ba"
Output: 1
Explanation: The two string are 1-similar because we can use one swap to change s1 to s2: "ab" --> "ba".
Example 2:

Input: s1 = "abc", s2 = "bca"
Output: 2
Explanation: The two strings are 2-similar because we can use two swaps to change s1 to s2: "abc" --> "bac" --> "bca".
 

Constraints:

1 <= s1.length <= 20
s2.length == s1.length
s1 and s2 contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}.
s2 is an anagram of s1.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
56,314/136.8K
Acceptance Rate
41.2%
Topics
Principal
Hash Table
String
Breadth-First Search
Weekly Contest 89
icon
Companies
Similar Questions
Couples Holding Hands
Hard
''')
