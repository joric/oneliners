from lc import *

# https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        v = set(deadends)
        q,nq = ["0000"],[]
        cnt = 0
        while q:
            while q:
                s = q.pop()
                if s not in v:
                    v.add(s)
                    if s == target:
                        return cnt
                    nq += [ s[0:i] + str(int(s[i])+1 if int(s[i]) +1 <=9 else 0 )+ s[i+1:] for i in range(len(s))]
                    nq += [ s[0:i] + str(int(s[i])-1 if int(s[i]) -1 >=0 else 9 )+ s[i+1:] for i in range(len(s))]
            cnt+=1
            nq,q = q,nq
        return -1

# https://leetcode.com/problems/open-the-lock/discuss/1251580/Python-3-today's-one-liner

class Solution:
    def openLock(self, d: List[str], t: str) -> int:
        v,q={*d},{'0000'}
        for r in count():
            if t in q:
                return r
            q -= v
            v |= q
            q = {x[:i] + str((int(x[i])+j)%10)+x[i+1:] for x in q for i in range(4)for j in (1,9)}
            if not q:
                return -1

class Solution:
    def openLock(self, d: List[str], t: str) -> int:
        v,q={*d},{'0000'};return next(r if q else-1 for r in count()if t in q or not(q:=q-v,v:=v|q,q:={x[:i]+str((int(x[i])+j)%10)+x[i+1:]for x in q for i in range(4)for j in(1,9)})[2])

test('''
752. Open the Lock
Medium

4012

162

Add to List

Share
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

 

Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation: 
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:

Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:

Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation: We cannot reach the target without getting stuck.
 

Constraints:

1 <= deadends.length <= 500
deadends[i].length == 4
target.length == 4
target will not be in the list deadends.
target and deadends[i] consist of digits only.
Accepted
236,973
Submissions
419,012
''')
