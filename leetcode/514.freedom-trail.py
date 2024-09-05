from lc import *

# https://leetcode.com/problems/freedom-trail/discuss/159154/My-7-lines-Python-DP-solution-beats-100-124-ms

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ind, n, dp, pre = collections.defaultdict(list), len(ring), [0] * len(ring), key[0]
        for i, c in enumerate(ring): ind[c].append(i)
        for i in ind[key[0]]: dp[i] = min(i, n - i) + 1
        for c in key[1:]:
            for i in ind[c]: dp[i] = min(dp[j] + min(i - j, j + n - i) if i >= j else dp[j] + min(j - i, i + n - j) for j in ind[pre]) + 1
            pre = c
        return min(dp[i] for i in ind[key[-1]])

class Solution:
    def findRotateSteps(self, r: str, k: str) -> int:
        n=len(r);v,d,p=defaultdict(list),[0]*n,k[0]
        [v[c].append(i)for i,c in enumerate(r)]
        [setitem(d,i,min(i,n-i)+1)for i in v[k[0]]]
        [([setitem(d,i,min(d[j]+min(i-j,j+n-i)if i>=j else d[j]+min(j-i,i+n-j)for j in v[p])+1)for i in v[c]],p:=c)for c in k[1:]]
        return min(d[i] for i in v[k[-1]])

# https://leetcode.com/problems/freedom-trail/discuss/1821924/Python-naive-recursion-with-%40cache

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        def find_dist(char, ring, direction):
            dist = 1
            n = len(ring)
            for i in range(n):
                if ring[(n+i*direction)%n] == char:
                    return dist
                dist += 1
        def rotate(ring, dist):
            return ring[dist:] + ring[:dist]
        @cache
        def f(i, ring, key):
            if i == len(key): return 0
            acw = find_dist(key[i], ring, 1)
            cw = find_dist(key[i], ring, -1)
            if acw == cw == 1:
                return 1 + f(i+1, ring, key)
            return min(acw + f(i+1, rotate(ring, acw-1), key),cw + f(i+1,rotate(ring, -cw+1), key))
        return f(0, ring, key)

class Solution:
    def findRotateSteps(self, r: str, k: str) -> int:
        t=lambda r,i:r[i:] + r[:i];g=lambda c,r,d:(s:=1,n:=len(r))and next(s for i in range(n)if r[(n+i*d)%n]==c or not(s:=s+1));f=cache(lambda i,r,k:k[i:]and((p:=[g(k[i],r,d)for d in(1,-1)])==(1,1)and 1+f(i+1,r,k)or min(p[0]+f(i+1,t(r,p[0]-1),k),p[1]+f(i+1,t(r,1-p[1]),k)))or 0);return f(0,r,k)

test('''
514. Freedom Trail
Hard

1095

52

Add to List

Share
In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring" and use the dial to spell a specific keyword to open the door.

Given a string ring that represents the code engraved on the outer ring and another string key that represents the keyword that needs to be spelled, return the minimum number of steps to spell all the characters in the keyword.

Initially, the first character of the ring is aligned at the "12:00" direction. You should spell all the characters in key one by one by rotating ring clockwise or anticlockwise to make each character of the string key aligned at the "12:00" direction and then by pressing the center button.

At the stage of rotating the ring to spell the key character key[i]:

You can rotate the ring clockwise or anticlockwise by one place, which counts as one step. The final purpose of the rotation is to align one of ring's characters at the "12:00" direction, where this character must equal key[i].
If the character key[i] has been aligned at the "12:00" direction, press the center button to spell, which also counts as one step. After the pressing, you could begin to spell the next character in the key (next stage). Otherwise, you have finished all the spelling.
 

Example 1:


Input: ring = "godding", key = "gd"
Output: 4
Explanation:
For the first key character 'g', since it is already in place, we just need 1 step to spell this character. 
For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
Also, we need 1 more step for spelling.
So the final output is 4.
Example 2:

Input: ring = "godding", key = "godding"
Output: 13
 

Constraints:

1 <= ring.length, key.length <= 100
ring and key consist of only lower case English letters.
It is guaranteed that key could always be spelled by rotating ring.
Accepted
54,193
Submissions
103,599
''')