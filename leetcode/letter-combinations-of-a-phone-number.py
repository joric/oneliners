from lc import *

class Solution:
    def letterCombinations(self, d: str) -> List[str]:
        return d and reduce(lambda a,c:[x+y for x in a for y in('','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz')[int(c)]],d,[''])

class Solution:
    def letterCombinations(self, d: str) -> List[str]:
        return d and reduce(lambda a,c:[x+y for x in a for y in('abc def ghi jkl mno pqrs tuv wxyz'.split())[int(c)-2]],d,[''])

class Solution:
    def letterCombinations(self, d: str) -> List[str]:
        return d and(''.join(p)for p in product(*('abc def ghi jkl mno pqrs tuv wxyz'.split()[int(c)-2]for c in d)))

class Solution:
    def letterCombinations(self, d: str) -> List[str]:
        return d and map(''.join,product(*('abc def ghi jkl mno pqrs tuv wxyz'.split()[int(c)-2]for c in d)))

test('''
17. Letter Combinations of a Phone Number
Medium

15874

863

Add to List

Share
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''
)

