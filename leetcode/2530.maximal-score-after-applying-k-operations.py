from lc import *

# https://leetcode.com/problems/maximal-score-after-applying-k-operations/discuss/3617996/Python-3-2-lines-of-code-O(k-logn)

class Solution:
    def maxKelements(self, a: List[int], k: int) -> int:
        heapify(a:=[-i for i in a]);return-sum(heapreplace(a,a[0]//3)for _ in range(k))


# updated 2024-10-14 (POTD)

class Solution:
    def maxKelements(self, a: List[int], k: int) -> int:
        heapify(a:=[*map(neg,a)]);return-sum(heapreplace(a,a[0]//3)for _ in range(k))

# https://leetcode.com/problems/maximal-score-after-applying-k-operations/discuss/3016912/PYTHON-or-SORT-or-SIMPLE

class Solution:
    def maxKelements(self, a: List[int], k: int) -> int:
        a.sort()
        r = 0
        while k:
            x = a.pop()
            insort(a,ceil(x/3))
            k -= 1
            r += x
        return r

class Solution:
    def maxKelements(self, a: List[int], k: int) -> int:
        a.sort()
        def f(k,r):
            if k==0:
                return r
            x = a.pop()
            insort(a,ceil(x/3))
            return f(k-1,r+x)
        return f(k,0)

class Solution:
    def maxKelements(self, a: List[int], k: int) -> int:
        a.sort();return(f:=lambda k,r:(x:=a.pop(),insort(a,ceil(x/3)))and f(k-1,r+x)if k else r)(k,0)

class Solution:
    def maxKelements(self, a: List[int], k: int) -> int:
        a.sort();return sum(x for _ in range(k)if(x:=a.pop(),insort(a,ceil(x/3))))

class Solution:
    def maxKelements(self, a: List[int], k: int) -> int:
        a.sort();return sum((x:=a.pop(),insort(a,ceil(x/3)))[0]for _ in range(k))

class Solution:
    def maxKelements(self, a: List[int], k: int) -> int:
        a.sort();return sum((x:=a.pop(),insort(a,-(-x//3)))[0]for _ in range(k))

# https://leetcode.com/problems/maximal-score-after-applying-k-operations/discuss/5910943/One-Line-Solution

class Solution:
    def maxKelements(self, a: List[int], k: int) -> int:
        [a.append(-(-x//3))for x in a if~-x];return sum(([1]*k+sorted(a))[-k:])

test('''
2530. Maximal Score After Applying K Operations
Medium

391

10

Add to List

Share
You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.

In one operation:

choose an index i such that 0 <= i < nums.length,
increase your score by nums[i], and
replace nums[i] with ceil(nums[i] / 3).
Return the maximum possible score you can attain after applying exactly k operations.

The ceiling function ceil(val) is the least integer greater than or equal to val.

 

Example 1:

Input: nums = [10,10,10,10,10], k = 5
Output: 50
Explanation: Apply the operation to each array element exactly once. The final score is 10 + 10 + 10 + 10 + 10 = 50.
Example 2:

Input: nums = [1,10,3,3,3], k = 3
Output: 17
Explanation: You can do the following operations:
Operation 1: Select i = 1, so nums becomes [1,4,3,3,3]. Your score increases by 10.
Operation 2: Select i = 1, so nums becomes [1,2,3,3,3]. Your score increases by 4.
Operation 3: Select i = 2, so nums becomes [1,1,1,3,3]. Your score increases by 3.
The final score is 10 + 4 + 3 = 17.
 

Constraints:

1 <= nums.length, k <= 105
1 <= nums[i] <= 109
Accepted
29,577
Submissions
63,663
''')
