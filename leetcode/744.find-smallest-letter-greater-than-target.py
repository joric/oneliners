from lc import * 

# https://leetcode.com/problems/find-smallest-letter-greater-than-target/solutions/566915/python-3-one-line-with-bisect_right-and-5tirp/?envType=daily-question&envId=2026-01-31

class Solution:
    def nextGreatestLetter(self, l: List[str], t: str) -> str:
        return min((c for c in l if c>t), default=min(l))

# https://leetcode.com/problems/find-smallest-letter-greater-than-target/discuss/566915/Python-3-one-line-with-bisect_right-and-with-min

class Solution:
    def nextGreatestLetter(self, l: List[str], t: str) -> str:
        return (i:=bisect_right(l,t),i<len(l)and l[i]or l[0])[-1]

class Solution:
    def nextGreatestLetter(self, l: List[str], t: str) -> str:
        return l[bisect_right(l,t[0])%len(l)]

class Solution:
    def nextGreatestLetter(self, l: List[str], t: str) -> str:
        return min((c for c in l if c>t),default=min(l))

class Solution:
    def nextGreatestLetter(self, l: List[str], t: str) -> str:
        return l[bisect_right(l,t)%len(l)]

class Solution:
    def nextGreatestLetter(self, l: List[str], t: str) -> str:
        return(l+l)[bisect_right(l,t)]

test('''
744. Find Smallest Letter Greater Than Target
Easy

3325

2059

Add to List

Share
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

 

Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
Example 2:

Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.
Example 3:

Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].
 

Constraints:

2 <= letters.length <= 10^4
letters[i] is a lowercase English letter.
letters is sorted in non-decreasing order.
letters contains at least two different characters.
target is a lowercase English letter.
Accepted
334,763
Submissions
693,017
Seen this question in a real interview before?

Yes

No
Try to find whether each of 26 next letters are in the given string array.
''')
