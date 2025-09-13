from lc import *

# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/description/?envType=daily-question&envId=2025-09-13

class Solution:
    def maxFreqSum(self, s: str) -> int:
        return sum(max([*Counter(c for c in s if f(c in 'aeiou')).values(),0])for f in (bool,not_))

class Solution:
    def maxFreqSum(self, s: str) -> int:
        return sum(max(len([*g])*f(c in 'aeiou')for c,g in groupby(sorted(s)))for f in (int,not_))

class Solution:
    def maxFreqSum(self, s: str) -> int:
        return sum(max(itemgetter(*q)(Counter(s)))for q in('aeiou',{*ascii_lowercase}-{*'aeiou'}))

class Solution:
    def maxFreqSum(self, s: str) -> int:
        return sum(max([*Counter(c for c in s if (c in 'aeiou')^q).values(),0])for q in(0,1))

class Solution:
    def maxFreqSum(self, s: str) -> int:
        return sum(max([*Counter(findall(f'[{q}aeiou]',s)).values(),0])for q in' ^')

test('''
3541. Find Most Frequent Vowel and Consonant
Easy
Topics
premium lock icon
Companies
Hint
You are given a string s consisting of lowercase English letters ('a' to 'z').

Your task is to:

Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
Find the consonant (all other letters excluding vowels) with the maximum frequency.
Return the sum of the two frequencies.

Note: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.

The frequency of a letter x is the number of times it occurs in the string.
 

Example 1:

Input: s = "successes"

Output: 6

Explanation:

The vowels are: 'u' (frequency 1), 'e' (frequency 2). The maximum frequency is 2.
The consonants are: 's' (frequency 4), 'c' (frequency 2). The maximum frequency is 4.
The output is 2 + 4 = 6.
Example 2:

Input: s = "aeiaeia"

Output: 3

Explanation:

The vowels are: 'a' (frequency 3), 'e' ( frequency 2), 'i' (frequency 2). The maximum frequency is 3.
There are no consonants in s. Hence, maximum consonant frequency = 0.
The output is 3 + 0 = 3.
 

Constraints:

1 <= s.length <= 100
s consists of lowercase English letters only.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
57,851/65K
Acceptance Rate
89.0%
Topics
Hash Table
String
Counting
Biweekly Contest 156
icon
Companies
Hint 1
Use a hashmap
Hint 2
Simulate as described
''')
