from lc import *

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [*map(neg,stones)]
        heapify(h)
        while len(h)>1 and h[0]:
            heappush(h,heappop(h)-heappop(h))
        return -h[0]

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.append(stones.pop(stones.index(max(stones))) - stones.pop(stones.index(max(stones))))
        return stones[0]

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) >= 2:
            stones.sort()
            stones.append(stones.pop() - stones.pop())
        return stones[0]

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            insort(stones,stones.pop() - stones.pop())
        return stones[0]

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        return next((-h[0] for _ in count() if not(h[1:] and h[0] and not heappush(h,heappop(h)-heappop(h)))),(h:=[*map(neg,stones)],heapify(h)))

class Solution:
    def lastStoneWeight(self, s: List[int]) -> int:
        return next(s[0] for _ in count() if not(s[1:] and not s.append(s.pop(s.index(max(s)))-s.pop(s.index(max(s))))))

class Solution:
    def lastStoneWeight(self, s: List[int]) -> int:
        return next(s[0] for _ in count() if not(s[1:] and (s.sort(),s.append(s.pop()-s.pop()))))

class Solution:
    def lastStoneWeight(self, s: List[int]) -> int:
        return next((s[0] for _ in count() if not s[1:] or insort(s,s.pop()-s.pop())),s.sort())

class Solution:
    def lastStoneWeight(self, s: List[int]) -> int:
        return (s.sort(),all(s[1:] and [insort(s,s.pop()-s.pop())] for _ in count()),s[0])[2]

class Solution:
    def lastStoneWeight(self, s: List[int]) -> int:
        return (f:=lambda a:a[1:]and (a.sort()or f(a[:-2]+[a[-1]-a[-2]]))or a[0])(s)

test('''
1046. Last Stone Weight
Easy

4427

82

Add to List

Share
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

 

Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
Example 2:

Input: stones = [1]
Output: 1

Example 3:
Input: stones = [1,3]
Output: 2
 
Example 4:
Input: stones = [3,7,8]
Output: 2

Constraints:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
Accepted
408,565
Submissions
630,238
Seen this question in a real interview before?

Yes

No
Simulate the process. We can do it with a heap, or by sorting some list of stones every time we take a turn.
''')

