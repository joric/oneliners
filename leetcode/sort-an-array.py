from lc import *

# https://leetcode.com/problems/sort-an-array

# recursive quicksort (OOM)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        m = nums.pop()
        l = []
        g = []
        for i in nums:
            if i < m:
                l.append(i)
            else:
                g.append(i)
        return self.sortArray(l) + [m] + self.sortArray(g)

class Solution:
    def sortArray(self, a: List[int]) -> List[int]:
        return(f:=lambda a:a and f([x for x in a[1:]if x<=a[0]])+[a[0]]+f([x for x in a if x>a[0]]))(a)

# https://leetcode.com/problems/sort-an-array/discuss/3273893/Simple-Python-Quicksort

# note randomized pivot fixes maximum recursion depth and check_sorted fixes MLE

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(pivot):
            left = []
            right = []
            for num in nums:
                if num <= pivot:
                    left.append(num)
                else:
                    right.append(num)
            return left, right
        def check_sorted():
            left = 0
            right = 1
            while (right < len(nums) and nums[left] <= nums[right]):
                left += 1
                right += 1
            if right == len(nums):
                return True
            return False
        if check_sorted() or len(nums)<2:
            return nums
        pivot = nums.pop(random.randint(0, len(nums) - 1))
        left, right = partition(pivot)
        return self.sortArray(left) + [pivot] + self.sortArray(right)


# counting sort

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        r = []
        c = Counter(nums)
        for i in sorted(c.keys()):
            r += [i]*c[i]
        return r

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        r = []
        c = {k:0 for k in range(min(nums), max(nums)+1)}
        for x in nums:
            c[x] += 1
        for x in b.keys():
            if c[x]:
                r.extend(c[x]*[x])
        return r

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return (r:=[],c:={k:0 for k in range(min(nums),max(nums)+1)},any(setitem(c,x,c[x]+1) for x in nums),any(c[x] and r.extend([x]*c[x]) for x in c.keys()),r)[4]

# https://leetcode.com/problems/sort-an-array/discuss/3245638/Python-one-line-quicksort-solution-with-%22random%22-partition-index

class Solution:
    def sortArray(self, a: List[int]) -> List[int]: 
        return a and (self.sortArray([i for i in a if i < a[len(a)//5]]) + [i for i in a if i == a[len(a)//5]] + self.sortArray([i for i in a if i  > a[len(a)//5]]) if random.random()>0.5
            else self.sortArray([i for i in a if i < a[-len(a)//5]]) + [i for i in a if i == a[-len(a)//5]] + self.sortArray([i for i in a if i  > a[-len(a)//5]]))

# https://leetcode.com/problems/sort-an-array/discuss/461394/Python-3-(Eight-Sorting-Algorithms)-(With-Explanation)

# selection sort

class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        L = len(N)
        return [N.pop(min(range(L-i), key = lambda x: N[x])) for i in range(L)]

# bubble sort

class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        L, B = len(N), 1
        while B:
            B = 0
            for i in range(L-1):
                if N[i] > N[i+1]: N[i], N[i+1], B = N[i+1], N[i], 1
        return N

# insertion sort

class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        L = len(N)
        for i in range(1,L):
            for j in range(0,i):
                if N[i] < N[j]:
                    N.insert(j, N.pop(i))
                    break
        return N

# binary insertion sort

class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        L = len(N)
        for i in range(1,L): bisect.insort_left(N, N.pop(i), 0, i)
        return N

# counting sort

class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        C, m, M, S = collections.Counter(N), min(N), max(N), []
        for n in range(m,M+1): S.extend([n]*C[n])
        return S

# quicksort (TLE)

class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        def quicksort(A, I, J):
            if J - I <= 1: return
            p = partition(A, I, J)
            quicksort(A, I, p), quicksort(A, p + 1, J)
        
        def partition(A, I, J):
            A[J-1], A[(I + J - 1)//2], i = A[(I + J - 1)//2], A[J-1], I
            for j in range(I,J):
                if A[j] < A[J-1]: A[i], A[j], i = A[j], A[i], i + 1
            A[J-1], A[i] = A[i], A[J-1]
            return i
        
        quicksort(N,0,len(N))
        return N

# merge sort

class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        def mergesort(A):
            LA = len(A)
            if LA == 1: return A
            LH, RH = mergesort(A[:LA//2]), mergesort(A[LA//2:])
            return merge(LH,RH)

        def merge(LH, RH):
            LLH, LRH = len(LH), len(RH)
            S, i, j = [], 0, 0
            while i < LLH and j < LRH:
                if LH[i] <= RH[j]: i, _ = i + 1, S.append(LH[i])
                else: j, _ = j + 1, S.append(RH[j])
            return S + (RH[j:] if i == LLH else LH[i:])

        return mergesort(N)

# bucket sort (WA)

class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        def insertion_sort(A):
            for i in range(1,len(A)):
                for j in range(0,i):
                    if A[i] < A[j]:
                        A.insert(j, A.pop(i))
                        break
            return A

        def bucketsort(A):
            buckets, m, S = [[] for _ in range(1000)], min(A), []
            R = max(A) - m
            if R == 0: return A
            for a in A: buckets[999*(a-m)//R].append(a)
            for b in buckets: S.extend(insertion_sort(b))
            return S

        return bucketsort(N)

# 3-way quicksort with randomized pivot

class Solution:
    def sortArray(self, a: List[int]) -> List[int]:
        return(f:=lambda a:a and[p:=choice(a)]and f([x for x in a if x<p])+[x for x in a if x==p]+f([x for x in a if x>p]))(a)

# https://leetcode.com/problems/sort-an-array/discuss/5533017/one-line-solution

class Solution:
    def sortArray(self, a: List[int]) -> List[int]:
        return (f:=lambda a:len(a)==1 and a or merge(f(a[:(m:=len(a)//2)]),f(a[m:])))(a)

# shortest

class Solution:sortArray=sorted

test('''
912. Sort an Array
Medium

3577

631

Add to List

Share
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.
 

Constraints:

1 <= nums.length <= 5 * 10^4
-5 * 104 <= nums[i] <= 5 * 10^4
''')
