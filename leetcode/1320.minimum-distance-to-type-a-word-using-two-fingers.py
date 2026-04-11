from lc import *

# https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/solutions/3560217/cache-simple-fast-python-solution-by-avs-uvst/?envType=daily-question&envId=2026-04-12

class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(pre,cur):
            if pre==None:
                return 0
            x1,y1 = divmod(ord(pre)-ord('A'),6)
            x2,y2 = divmod(ord(cur)-ord('A'),6)
            return abs(x1-x2) + abs(y1-y2)
        @lru_cache(None)
        def fingers(i,l,r):
            if i == len(word):
                return 0
            n1 = dist(l,word[i]) + fingers(i+1,word[i],r)
            n2 = dist(r,word[i]) + fingers(i+1,l,word[i])
            return min(n1,n2)
        return fingers(0,None,None)

class Solution:
    def minimumDistance(self, w: str) -> int:
        d=lambda a,b:a and abs((x:=ord(a)-65)//6-(y:=ord(b)-65)//6)+abs(x%6-y%6);return(f:=cache(lambda i,l,r:i<len(w)and min(d(l,w[i])+f(i+1,w[i],r),d(r,w[i])+f(i+1,l,w[i]))))(0,0,0)

test('''
1320. Minimum Distance to Type a Word Using Two Fingers
Hard
Topics
premium lock icon
Companies
Hint

You have a keyboard layout as shown above in the X-Y plane, where each English uppercase letter is located at some coordinate.

For example, the letter 'A' is located at coordinate (0, 0), the letter 'B' is located at coordinate (0, 1), the letter 'P' is located at coordinate (2, 3) and the letter 'Z' is located at coordinate (4, 1).
Given the string word, return the minimum total distance to type such string using only two fingers.

The distance between coordinates (x1, y1) and (x2, y2) is |x1 - x2| + |y1 - y2|.

Note that the initial positions of your two fingers are considered free so do not count towards your total distance, also your two fingers do not have to start at the first letter or the first two letters.

 

Example 1:

Input: word = "CAKE"
Output: 3
Explanation: Using two fingers, one optimal way to type "CAKE" is: 
Finger 1 on letter 'C' -> cost = 0 
Finger 1 on letter 'A' -> cost = Distance from letter 'C' to letter 'A' = 2 
Finger 2 on letter 'K' -> cost = 0 
Finger 2 on letter 'E' -> cost = Distance from letter 'K' to letter 'E' = 1 
Total distance = 3
Example 2:

Input: word = "HAPPY"
Output: 6
Explanation: Using two fingers, one optimal way to type "HAPPY" is:
Finger 1 on letter 'H' -> cost = 0
Finger 1 on letter 'A' -> cost = Distance from letter 'H' to letter 'A' = 2
Finger 2 on letter 'P' -> cost = 0
Finger 2 on letter 'P' -> cost = Distance from letter 'P' to letter 'P' = 0
Finger 1 on letter 'Y' -> cost = Distance from letter 'A' to letter 'Y' = 4
Total distance = 6
 

Other examples:

Input: word = "YEAR"
Output: 7

Constraints:

2 <= word.length <= 300
word consists of uppercase English letters.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
38,243/64.3K
Acceptance Rate
59.5%
Topics
Principal
String
Dynamic Programming
Weekly Contest 171
icon
Companies
Hint 1
Use dynamic programming.
Hint 2
dp[i][j][k]: smallest movements when you have one finger on i-th char and the other one on j-th char already having written k first characters from word.
Similar Questions
Minimum Time to Type Word Using Special Typewriter
Easy
''')
