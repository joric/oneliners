from lc import *

# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/solutions/6066561/one-line-solution-by-xxxxkav-h2xd/?envType=daily-question&envId=2026-04-15

class Solution:
    def closestTarget(self, w: List[str], t: str, s: int) -> int: 
        return next((i for i in range(len(w)//2+1)if t in (w[(s+i)%len(w)],w[s-i])),-1)

# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/solutions/5160450/one-line-solution-by-mikposp-2xp7/?envType=daily-question&envId=2026-04-15

class Solution:
    def closestTarget(self, w: List[str], t: str, k: int) -> int:
        return min((w[k:]+w).index(t),(w+w[:k+1])[::-1].index(t))if t in w else-1

class Solution:
    def closestTarget(self, w: List[str], t: str, k: int) -> int:
        return min(x.index(t)for x in(w[k:]+w,(w+w[:k+1])[::-1]))if t in w else-1

class Solution:
    def closestTarget(self, w: List[str], t: str, k: int) -> int:
        return t not in w and -1 or min((w[k:]+w).index(t),(w+w[:k+1])[::-1].index(t))


test('''
2515. Shortest Distance to Target String in a Circular Array
Easy
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed circular string array words and a string target. A circular array means that the array's end connects to the array's beginning.

Formally, the next element of words[i] is words[(i + 1) % n] and the previous element of words[i] is words[(i - 1 + n) % n], where n is the length of words.
Starting from startIndex, you can move to either the next word or the previous word with 1 step at a time.

Return the shortest distance needed to reach the string target. If the string target does not exist in words, return -1.

 

Example 1:

Input: words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1
Output: 1
Explanation: We start from index 1 and can reach "hello" by
- moving 3 units to the right to reach index 4.
- moving 2 units to the left to reach index 4.
- moving 4 units to the right to reach index 0.
- moving 1 unit to the left to reach index 0.
The shortest distance to reach "hello" is 1.
Example 2:

Input: words = ["a","b","leetcode"], target = "leetcode", startIndex = 0
Output: 1
Explanation: We start from index 0 and can reach "leetcode" by
- moving 2 units to the right to reach index 2.
- moving 1 unit to the left to reach index 2.
The shortest distance to reach "leetcode" is 1.
Example 3:

Input: words = ["i","eat","leetcode"], target = "ate", startIndex = 0
Output: -1
Explanation: Since "ate" does not exist in words, we return -1.

Other examples:

Input: words = ["pgmiltbptl","jnkxwutznb","bmeirwjars","ugzyaufzzp","pgmiltbptl","sfhtxkmzwn","pgmiltbptl","pgmiltbptl","onvmgvjhxa","jyzdtwbwqp"], target = "pgmiltbptl", startIndex = 4
Output: 0

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] and target consist of only lowercase English letters.
0 <= startIndex < words.length
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
39,466/78K
Acceptance Rate
50.6%
Topics
Mid Level
Array
String
Weekly Contest 325
icon
Companies
Hint 1
You have two options, either move straight to the left or move straight to the right.
Hint 2
Find the first target word and record the distance.
Hint 3
Choose the one with the minimum distance.
Similar Questions
Defuse the Bomb
Easy
''')
