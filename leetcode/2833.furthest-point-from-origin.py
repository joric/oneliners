from lc import *

# https://leetcode.com/problems/furthest-point-from-origin/solutions/4340860/one-line-python-by-fredo30400-tje2/?envType=daily-question&envId=2026-04-24

class Solution:
    def furthestDistanceFromOrigin(self, m: str) -> int:
        return abs(m.count('R')-m.count('L'))+m.count('_')

class Solution:
    def furthestDistanceFromOrigin(self, m: str) -> int:
        f=m.count;return abs(f('R')-f('L'))+f('_')

class Solution:
    def furthestDistanceFromOrigin(self, m: str) -> int:
        a,b,c=map(m.count,'RL_');return abs(a-b)+c

'''kotlin

fun furthestDistanceFromOrigin(moves: String): Int =
          moves.groupingBy{it}.eachCount().let{ abs((it['L']?:0) - (it['R']?:0)) + (it['_']?:0) }

class Solution {
fun furthestDistanceFromOrigin(moves: String): Int =
          moves.run{abs(count{it=='L'}-count{it=='R'})+count{it=='_'}}
}

class Solution {
fun furthestDistanceFromOrigin(moves: String): Int =
          m.count{it=='_'}+abs(m.count{it=='L'}-m.count{it=='R'})
}

'''

test('''
2833. Furthest Point From Origin
Easy
Topics
premium lock icon
Companies
Hint
You are given a string moves of length n consisting only of characters 'L', 'R', and '_'. The string represents your movement on a number line starting from the origin 0.

In the ith move, you can choose one of the following directions:

move to the left if moves[i] = 'L' or moves[i] = '_'
move to the right if moves[i] = 'R' or moves[i] = '_'
Return the distance from the origin of the furthest point you can get to after n moves.

 

Example 1:

Input: moves = "L_RL__R"
Output: 3
Explanation: The furthest point we can reach from the origin 0 is point -3 through the following sequence of moves "LLRLLLR".
Example 2:

Input: moves = "_R__LL_"
Output: 5
Explanation: The furthest point we can reach from the origin 0 is point -5 through the following sequence of moves "LRLLLLL".
Example 3:

Input: moves = "_______"
Output: 7
Explanation: The furthest point we can reach from the origin 0 is point 7 through the following sequence of moves "RRRRRRR".
 

Constraints:

1 <= moves.length == n <= 50
moves consists only of characters 'L', 'R' and '_'.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
63,105/96K
Acceptance Rate
65.7%
Topics
Mid Level
String
Counting
Weekly Contest 360
icon
Companies
Hint 1
In an optimal answer, all occurrences of '_’ will be replaced with the same character.
Hint 2
Replace all characters of '_’ with the character that occurs the most. 
Similar Questions
Robot Return to Origin
Easy
''')
