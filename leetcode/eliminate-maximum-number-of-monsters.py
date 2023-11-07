from lc import *

# https://leetcode.com/problems/eliminate-maximum-number-of-monsters/discuss/1314550/Sort-by-arrival/1113115

class Solution:
    def eliminateMaximum(self, d: List[int], s: List[int]) -> int:
        c = 0
        for _ in takewhile(lambda t:t-c>0, sorted(map(truediv,d,s))):
            c += 1
        return c

# https://leetcode.com/problems/eliminate-maximum-number-of-monsters/discuss/4258483/Python-3-or-One-line-or-Beats-99

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        return next((i for i,t in enumerate(sorted(d/s for d,s in zip(dist, speed))) if i>=t), len(dist))

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        return next((i for i,t in enumerate(sorted(map(truediv,dist,speed))) if i>=t), len(dist))


# https://leetcode.com/problems/eliminate-maximum-number-of-monsters/discuss/1314370/Python3-3-line

class Solution:
    def eliminateMaximum(self, d: List[int], s: List[int]) -> int:
        return next((i for i,t in enumerate(sorted((x+y-1)//y for x,y in zip(d,s)))if i==t),len(d))

class Solution:
    def eliminateMaximum(self, d: List[int], s: List[int]) -> int:
        return next((i for i,t in enumerate(sorted(ceil(x/y)for x,y in zip(d,s)))if i==t),len(d))

class Solution:
    def eliminateMaximum(self, d: List[int], s: List[int]) -> int:
        return next((i for i,t in enumerate(sorted(map(truediv,d,s)))if i>=t),len(d))

# another solution

class Solution:
    def eliminateMaximum(self, d: List[int], s: List[int]) -> int:
        return len([*takewhile(lambda t:lt(*t),enumerate(sorted(map(truediv,d,s))))])

test('''
1921. Eliminate Maximum Number of Monsters
Medium

535

84

Add to List

Share
You are playing a video game where you are defending your city from a group of n monsters. You are given a 0-indexed integer array dist of size n, where dist[i] is the initial distance in kilometers of the ith monster from the city.

The monsters walk toward the city at a constant speed. The speed of each monster is given to you in an integer array speed of size n, where speed[i] is the speed of the ith monster in kilometers per minute.

You have a weapon that, once fully charged, can eliminate a single monster. However, the weapon takes one minute to charge. The weapon is fully charged at the very start.

You lose when any monster reaches your city. If a monster reaches the city at the exact moment the weapon is fully charged, it counts as a loss, and the game ends before you can use your weapon.

Return the maximum number of monsters that you can eliminate before you lose, or n if you can eliminate all the monsters before they reach the city.

 

Example 1:

Input: dist = [1,3,4], speed = [1,1,1]
Output: 3
Explanation:
In the beginning, the distances of the monsters are [1,3,4]. You eliminate the first monster.
After a minute, the distances of the monsters are [X,2,3]. You eliminate the second monster.
After a minute, the distances of the monsters are [X,X,2]. You eliminate the thrid monster.
All 3 monsters can be eliminated.
Example 2:

Input: dist = [1,1,2,3], speed = [1,1,1,1]
Output: 1
Explanation:
In the beginning, the distances of the monsters are [1,1,2,3]. You eliminate the first monster.
After a minute, the distances of the monsters are [X,0,1,2], so you lose.
You can only eliminate 1 monster.
Example 3:

Input: dist = [3,2,4], speed = [5,3,2]
Output: 1
Explanation:
In the beginning, the distances of the monsters are [3,2,4]. You eliminate the first monster.
After a minute, the distances of the monsters are [X,0,2], so you lose.
You can only eliminate 1 monster.
 

Constraints:

n == dist.length == speed.length
1 <= n <= 10^5
1 <= dist[i], speed[i] <= 10^5
Accepted
25,486
Submissions
66,357
''')

