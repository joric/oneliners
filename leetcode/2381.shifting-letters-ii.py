from lc import *

# https://leetcode.com/problems/shifting-letters-ii/solutions/5782371/prefix-sum-5-lines/?envType=daily-question&envId=2025-01-05

class Solution:
    def shiftingLetters(self, s: str, a: List[List[int]]) -> str:
        p = [0]*(len(s)+1)
        for l,r,d in a:
            p[l] += d*2-1
            p[r+1] -= d*2-1
        return''.join(chr((ord(c)-97+t)%26+97)for c,t in zip(s,accumulate(p)))

class Solution:
    def shiftingLetters(self, s: str, a: List[List[int]]) -> str:
        p=[0]*(len(s)+1);[setitem(p,l,p[l]+d*2-1)or setitem(p,r+1,p[r+1]-d*2+1)for l,r,d in a];return''.join(chr((ord(c)-97+t)%26+97)for c,t in zip(s,accumulate(p)))

test('''
2381. Shifting Letters II
Solved
Medium
Topics
Companies
Hint
You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.

Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').

Return the final string after all such shifts to s are applied.

 

Example 1:

Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
Output: "ace"
Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".
Example 2:

Input: s = "dztz", shifts = [[0,0,0],[1,1,1]]
Output: "catz"
Explanation: Firstly, shift the characters from index 0 to index 0 backward. Now s = "cztz".
Finally, shift the characters from index 1 to index 1 forward. Now s = "catz".
 

Constraints:

1 <= s.length, shifts.length <= 5 * 104
shifts[i].length == 3
0 <= starti <= endi < s.length
0 <= directioni <= 1
s consists of lowercase English letters.
''')

