from lc import *

# https://leetcode.com/problems/sum-game/solutions/1351579/python-3-one-line-faaaaaaast-by-l1ne-v2f8/?envType=daily-question&envId=2026-08-23

class Solution:
    def sumGame(self, s: str) -> bool:
        return sub(*(sum((4.5 if c=='?' else int(c))*v for c,v in z.items()) for z in map(Counter, (s[len(s)//2:], s[:len(s)//2]))))

class Solution:
    def sumGame(self, s: str) -> bool:
        return sum((int(c)if c<'?'else 4.5)*(1|-(i*2>=len(s)))for i,c in enumerate(s))!=0

class Solution:
    def sumGame(self, s: str) -> bool:
        return sum((2*int(c)if c<'?'else 9)*(1|-(i*2<len(s)))for i,c in enumerate(s))!=0

class Solution:
    def sumGame(self, s: str) -> bool:
        return sum((ord(c)*2+9)%21*(1|-(i*2<len(s)))for i,c in enumerate(s))!=0

test('''
1927. Sum Game
Medium
Topics
premium lock icon
Companies
Hint
Alice and Bob take turns playing a game, with Alice starting first.

You are given a string num of even length consisting of digits and '?' characters. On each turn, a player will do the following if there is still at least one '?' in num:

Choose an index i where num[i] == '?'.
Replace num[i] with any digit between '0' and '9'.
The game ends when there are no more '?' characters in num.

For Bob to win, the sum of the digits in the first half of num must be equal to the sum of the digits in the second half. For Alice to win, the sums must not be equal.

For example, if the game ended with num = "243801", then Bob wins because 2+4+3 = 8+0+1. If the game ended with num = "243803", then Alice wins because 2+4+3 != 8+0+3.
Assuming Alice and Bob play optimally, return true if Alice will win and false if Bob will win.

 

Example 1:

Input: num = "5023"
Output: false
Explanation: There are no moves to be made.
The sum of the first half is equal to the sum of the second half: 5 + 0 = 2 + 3.
Example 2:

Input: num = "25??"
Output: true
Explanation: Alice can replace one of the '?'s with '9' and it will be impossible for Bob to make the sums equal.
Example 3:

Input: num = "?3295???"
Output: false
Explanation: It can be proven that Bob will always win. One possible outcome is:
- Alice replaces the first '?' with '9'. num = "93295???".
- Bob replaces one of the '?' in the right half with '9'. num = "932959??".
- Alice replaces one of the '?' in the right half with '2'. num = "9329592?".
- Bob replaces the last '?' in the right half with '7'. num = "93295927".
Bob wins because 9 + 3 + 2 + 9 = 5 + 9 + 2 + 7.
 

Constraints:

2 <= num.length <= 105
num.length is even.
num consists of only digits and '?'.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
18,208/36.6K
Acceptance Rate
49.7%
Topics
Staff
Math
String
Greedy
Game Theory
Biweekly Contest 56
icon
Companies
Hint 1
Bob can always make the total sum of both sides equal in mod 9.
Hint 2
Why does the difference between the number of question marks on the left and right side matter?
''')
