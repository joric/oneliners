from lc import *

# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/solutions/7516544/solution-by-la_castille-8r1f/?envType=daily-question&envId=2026-01-23

class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        N = len(nums)
        if N < 2:
            return 0
        
        array = [int(x) for x in nums]
        left = list(range(-1, N - 1))
        right = list(range(1, N + 1))
        
        flipped = 0
        pairSum = SortedList()
        
        def add(i, N, array):
            nonlocal flipped
            if 0 <= i < N:
                j = right[i]
                if j < N:
                    pairSum.add([array[i] + array[j], i])
                    if array[i] > array[j]:
                        flipped += 1
                        
        def remove(i, N, array):
            nonlocal flipped
            if 0 <= i < N:
                j = right[i]
                if j < N:
                    if array[i] > array[j]:
                        flipped -= 1
                    pairSum.discard([array[i] + array[j], i])

        for i in range(N - 1):
            if array[i] > array[i + 1]:
                flipped += 1
            pairSum.add([array[i] + array[i + 1], i])
            
        op = 0
        
        while flipped > 0 and pairSum:
            s, i = pairSum.pop(0)
            
            j = right[i]
            h = left[i]
            k = right[j]
            
            remove(h, N, array)
            if array[i] > array[j]:
                flipped -= 1
            remove(j, N, array)
            
            array[i] += array[j]
            op += 1
            
            right[i] = k
            if k < N:
                left[k] = i
                
            add(h, N, array)
            add(i, N, array)
            
        return op


# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/solutions/6620544/python-dll-sortedlist-by-awice-ks6t/?envType=daily-question&envId=2026-01-23

class Solution:
    def minimumPairRemoval(self, A: List[int]) -> int:
        N = len(A)

        L = list(range(-1, N - 1))
        R = list(range(1, N + 1))

        v = sum(A[i] > A[i + 1] for i in range(N - 1))
        S = SortedList([A[i] + A[i + 1], i] for i in range(N - 1))

        def add(i,v):
            j = R[i]
            if 0 <= i < j < N:
                S.add([A[i] + A[j], i])
                v += A[i] > A[j]
            return v

        def remove(i,v):
            j = R[i]
            if 0 <= i < j < N:
                S.discard([A[i] + A[j], i])
                v -= A[i] > A[j]
            return v

        ans = 0
        while v:
            ans += 1
            s, i = S.pop(0)
            j = R[i]
            h, k = L[i], R[j]

            v=remove(h,v)
            v=remove(i,v)
            v=remove(j,v)

            A[i] += A[j]
            R[i] = k
            if k < N:
                L[k] = i

            v=add(h,v)
            v=add(i,v)

        return ans


class Solution:
    def minimumPairRemoval(self, a: List[int]) -> int:
        n=len(a)

        l=[*range(-1,n-1)]
        r=[*range(1,n+1)]
        v=sum(a[i]>a[i+1] for i in range(n-1))
        s=SortedList([a[i] + a[i+1],i] for i in range(n-1))
        f=lambda i,v,d=0:[0<=i<(j:=r[i])<n and((s.discard,s.add)[d]([a[i]+a[j],i]),v:=v+[-1,1][d]*(a[i]>a[j]))]and v

        b = 0

        while v:
            b += 1
            i = s.pop(0)[1]
            [v:=f(t,v)for t in[l[i],i,r[i]]]
            setitem(a,i,a[i]+a[r[i]])
            setitem(r,i,r[r[i]])
            n>r[i]and setitem(l,r[i],i)
            [v:=f(t,v,1)for t in[l[i],i]]

        return b

class Solution:
    def minimumPairRemoval(self, a: List[int]) -> int:
        n=len(a);l,r,v,q,s=[*range(-1,n-1)],[*range(1,n+1)],sum(a[i]>a[i+1]for i in range(n-1)),SortedList([a[i]+a[i+1],i]for i in range(n-1)),setitem;f=lambda i,v,d=0:[0<=i<(j:=r[i])<n and((q.discard,q.add)[d]([a[i]+a[j],i]),v:=v+[-1,1][d]*(a[i]>a[j]))]and v;b=lambda v:v and((i:=q.pop(0)[1],[v:=f(t,v)for t in[l[i],i,r[i]]],s(a,i,a[i]+a[r[i]]),s(r,i,r[r[i]]),n>r[i]and s(l,r[i],i),[v:=f(t,v,1)for t in[l[i],i]])and 1+b(v));return b(v)

test('''
3510. Minimum Pair Removal to Sort Array II
Attempted
Hard
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

 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
8,384/37.1K
Acceptance Rate
22.6%
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
We can perform the simulation using data structures.
Hint 2
Maintain an array index and value using a map since we need to find the next and previous ones.
Hint 3
Maintain the indices to be removed using a hash set.
Hint 4
Maintain the neighbor sums with the smaller indices (set or priority queue).
Hint 5
Keep the 3 structures in sync during the removals.
''')
