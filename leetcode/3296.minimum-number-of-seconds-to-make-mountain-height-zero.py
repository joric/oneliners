from lc import *

# https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/solutions/5821270/python3-5-lines-some-maths-and-a-bisect_-cef6/?envType=daily-question&envId=2026-03-13

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int], mx = 50_000_500_000) -> int:
        def work_done(days: int)-> int:
            work = lambda wt: int(sqrt(8 * days / wt + 1) - 1)//2
            return sum(map(work,workerTimes))
        poss_days = range( mx * mountainHeight // len(workerTimes))
        return bisect_left(poss_days, mountainHeight, key = work_done)

class Solution:
    def minNumberOfSeconds(self, m: int, w: List[int]) -> int:
        return bisect_left(range(50000500000*m//len(w)),m,key=lambda i:sum(((8*i/x+1)**.5-1)//2 for x in w))

# https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/solutions/5818751/o-log-n-w-sqrt-n-binary-search-math-simp-ksrl/?envType=daily-question&envId=2026-03-13

# if bisect wasn't a module name we could've used bisect(range(m*m*min(w)),m-1,...) but alas

class Solution:
    def minNumberOfSeconds(self, m: int, w: List[int]) -> int:
        return bisect_left(range(min(w)*(m+1)*m),m,key=lambda i:sum((sqrt(8*i/x+1)-1)//2for x in w))

class Solution:
    def minNumberOfSeconds(self, m: int, w: List[int]) -> int:
        return bisect_left(range(min(w)*m*-~m),m,key=lambda i:sum((sqrt(8*i/x+1)-1)//2for x in w))

class Solution:
    def minNumberOfSeconds(self, m: int, w: List[int]) -> int:
        return bisect_left(range(m*m*min(w)),m,key=lambda i:sum(((8*i/x+1)**.5-1)//2for x in w))

class Solution:
    def minNumberOfSeconds(self, m: int, w: List[int]) -> int:
        return bisect_left(range(m*m*min(w)),m,key=lambda i:sum(isqrt(8*i//x+1)-1>>1for x in w))

class Solution:
    def minNumberOfSeconds(self, m: int, w: List[int]) -> int:
        return bisect_left(range(9**17),m,key=lambda i:sum(isqrt(8*i//x+1)-1>>1for x in w))

test('''
3296. Minimum Number of Seconds to Make Mountain Height Zero
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer mountainHeight denoting the height of a mountain.

You are also given an integer array workerTimes representing the work time of workers in seconds.

The workers work simultaneously to reduce the height of the mountain. For worker i:

To decrease the mountain's height by x, it takes workerTimes[i] + workerTimes[i] * 2 + ... + workerTimes[i] * x seconds. For example:
To reduce the height of the mountain by 1, it takes workerTimes[i] seconds.
To reduce the height of the mountain by 2, it takes workerTimes[i] + workerTimes[i] * 2 seconds, and so on.
Return an integer representing the minimum number of seconds required for the workers to make the height of the mountain 0.

 

Example 1:

Input: mountainHeight = 4, workerTimes = [2,1,1]

Output: 3

Explanation:

One way the height of the mountain can be reduced to 0 is:

Worker 0 reduces the height by 1, taking workerTimes[0] = 2 seconds.
Worker 1 reduces the height by 2, taking workerTimes[1] + workerTimes[1] * 2 = 3 seconds.
Worker 2 reduces the height by 1, taking workerTimes[2] = 1 second.
Since they work simultaneously, the minimum time needed is max(2, 3, 1) = 3 seconds.

Example 2:

Input: mountainHeight = 10, workerTimes = [3,2,2,4]

Output: 12

Explanation:

Worker 0 reduces the height by 2, taking workerTimes[0] + workerTimes[0] * 2 = 9 seconds.
Worker 1 reduces the height by 3, taking workerTimes[1] + workerTimes[1] * 2 + workerTimes[1] * 3 = 12 seconds.
Worker 2 reduces the height by 3, taking workerTimes[2] + workerTimes[2] * 2 + workerTimes[2] * 3 = 12 seconds.
Worker 3 reduces the height by 2, taking workerTimes[3] + workerTimes[3] * 2 = 12 seconds.
The number of seconds needed is max(9, 12, 12, 12) = 12 seconds.

Example 3:

Input: mountainHeight = 5, workerTimes = [1]

Output: 15

Explanation:

There is only one worker in this example, so the answer is workerTimes[0] + workerTimes[0] * 2 + workerTimes[0] * 3 + workerTimes[0] * 4 + workerTimes[0] * 5 = 15.

Other examples:

Input: mountainHeight = 1, workerTimes = [5]
Output: 5

Input: mountainHeight = 100000, workerTimes = [1000000]
Output: 5000050000000000

Constraints:

1 <= mountainHeight <= 105
1 <= workerTimes.length <= 104
1 <= workerTimes[i] <= 106
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
25,410/68.7K
Acceptance Rate
37.0%
Topics
Staff
Array
Math
Binary Search
Greedy
Heap (Priority Queue)
Weekly Contest 416
icon
Companies
Hint 1
Can we use binary search to solve this problem?
Hint 2
Do a binary search on the number of seconds to check if it's enough to reduce the mountain height to 0 or less with all workers working simultaneously.
''')
