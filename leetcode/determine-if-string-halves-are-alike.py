from lc import *

# https://leetcode.com/problems/determine-if-string-halves-are-alike/discuss/2864300/Python3-one-liners-O(n)

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        a = b = 0
        i, j = 0, len(s) - 1
        while i < j:
            a += s[i] in vowels
            b += s[j] in vowels
            i += 1
            j -= 1
        return a == b 

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return(v:=set('aeiouAEIOU'))and sum((s[i] in v)-(s[~i] in v) for i in range(len(s)//2))==0

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        v=set('aeiouAEIOU');return sum((s[i]in v)-(s[~i]in v)for i in range(len(s)//2))==0

# https://leetcode.com/problems/determine-if-string-halves-are-alike/discuss/1173214/Python-Simple-Zip-Loop

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        left = right = 0
        vowels = {'a','e','i','o','u','A', 'E','I','O','U'}
        for (x,y) in zip(s[:len(s)//2], s[len(s)//2:]):
            if x in vowels:
                left+=1
            if y in vowels:
                right+=1
        return left == right

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n,v=len(s)//2,set('aeiouAEIOU');return sum(1 for c in s[:n]if c in v)==sum(1 for c in s[n:]if c in v)

# https://leetcode.com/problems/determine-if-string-halves-are-alike/discuss/2864237/one-line-in-Python

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return sum((i<len(s)//2)*2-1for i,c in enumerate(s)if c.lower()in'aeiou')==0

test('''

1704. Determine if String Halves Are Alike
Easy

959

61

Add to List

Share
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

 

Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.

Example 3:

Input: s = "AbCdEfGh"
Output: true

Constraints:

2 <= s.length <= 1000
s.length is even.
s consists of uppercase and lowercase letters.

''')
