from lc import *

# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/solutions/6737292/slow-in-4-lines-by-qulinxao-luar/?envType=daily-question&envId=2026-01-22

class Solution:
    def minimumPairRemoval(self, m: List[int]) -> int:
        for i in count():
            if all(a<=b for a,b in pairwise(m)):
                return i
            c,d=min((x+y,i)for i,(x,y)in enumerate(pairwise(m)))
            m[d]=c;del m[d+1]

# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/solutions/7514078/recursive-solution-by-ttrpl-dvar/?envType=daily-question&envId=2026-01-22

class Solution:
    def minimumPairRemoval(self, a: List[int]) -> int:
        if all(a[i] <= a[i+1] for i in range(len(a) - 1)):
            return 0
        b = 0
        for i in range(len(a) - 1):
            if a[i] + a[i+1] < a[b] + a[b+1]:
                b = i
        a[b] += a[b+1]
        a.pop(b+1)
        return 1 + self.minimumPairRemoval(a)

# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/solutions/7513834/simulation-3-lines-by-xxxxkav-eiyx/?envType=daily-question&envId=2026-01-22

class Solution:
    def minimumPairRemoval(self, a: List[int]) -> int:
        s = 0
        while any(starmap(gt,pairwise(a))) and (s:=s+1): 
            a[i:=min(range(len(a)-1),key=lambda i:a[i]+a[i+1])] += a.pop(i+1)
        return s

class Solution:
    def minimumPairRemoval(self, a: List[int]) -> int:
        return next(s for s in count()if all(map(le,a,a[1:]))or setitem(a,i:=min(range(len(a)-1),key=lambda i:a[i]+a[i+1]),a[i]+a.pop(i+1)))

class Solution:
    def minimumPairRemoval(self, a: List[int]) -> int:
        return next(s for s in count()if all(map(le,a,a[1:]))or setitem(a,i:=(t:=[*map(add,a,a[1:])]).index(min(t)),a[i]+a.pop(i+1)))

class Solution:
    def minimumPairRemoval(self, a: List[int]) -> int:
        return next(s for s in count()if a==sorted(a)or a.insert(i:=(t:=[*map(add,a,a[1:])]).index(min(t)),a.pop(i)+a.pop(i)))

class Solution:
    def minimumPairRemoval(self, a: List[int]) -> int:
        return+(f:=lambda a:a>sorted(a)and-~f(a.insert(i:=(t:=[*map(add,a,a[1:])]).index(min(t)),a.pop(i)+a.pop(i))or a))(a)

class Solution:
    def minimumPairRemoval(self, a: List[int]) -> int:
        return+(f:=lambda:a>sorted(a)and(a.insert(i:=(t:=[*map(add,a,a[1:])]).index(min(t)),a.pop(i)+a.pop(i))or-~f()))()

class Solution:
    def minimumPairRemoval(self, a: List[int]) -> int:
        return sum(a>sorted(a)!=a.insert(i:=(t:=[*map(add,a,a[1:])]).index(min(t)),a.pop(i)+a.pop(i))for _ in a+a)

class Solution:
    def minimumPairRemoval(self, a: List[int]) -> int:
        return sum(sorted(a)<a!=(a:=a[:(p:=min(zip(map(add,a,a[1:]),count())))[1]]+[p[0]]+a[p[1]+2:])for _ in a+a)

class Solution:
    def minimumPairRemoval(self, a: List[int]) -> int:
        return sum(a>sorted(a)!=(p:=min(zip(map(add,a,a[1:]),count())),a:=a[:p[1]]+[p[0]]+a[p[1]+2:])for _ in a+a)

class Solution:
    def minimumPairRemoval(self, a: List[int]) -> int:
        return sum(a>sorted(a)!=[a:=a[:i]+[s]+a[i+2:]for s,i in[min(zip(map(add,a,a[1:]),count()))]]for _ in a+a)

class Solution:
    def minimumPairRemoval(self, a: List[int]) -> int:
        return sum(a>sorted(a)!=a.insert(i:=min(zip(map(add,a,a[1:]),count()))[1],a.pop(i)+a.pop(i))for _ in a+a)

test('''
3507. Minimum Pair Removal to Sort Array I
Easy
Topics
premium lock icon
Companies
Hint
Given an array nums, you can perform the following operation any number of times:

Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
Replace the pair with their sum.
Return the minimum number of operations needed to make the array non-decreasing.

An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).

 

Example 1:

Input: nums = [5,2,3,1]

Output: 2

Explanation:

The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
The array nums became non-decreasing in two operations.

Example 2:

Input: nums = [1,2,2]

Output: 0

Explanation:

The array nums is already sorted.

Other examples:

Input: nums = [2,2,-1,3,-2,2,1,1,1,0,-1]
Output: 9

Input: nums = [-2,1,2,-1,-1,-2,-2,-1,-1,1,1]
Output: 10

Constraints:

1 <= nums.length <= 50
-1000 <= nums[i] <= 1000
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
65,994/109.5K
Acceptance Rate
60.3%
Topics
Array
Hash Table
Linked List
Heap (Priority Queue)
Simulation
Doubly-Linked List
Ordered Set
Weekly Contest 444
icon
Companies
Hint 1
Simulate the operations
''')
