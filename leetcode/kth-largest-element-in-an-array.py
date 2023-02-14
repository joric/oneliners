from lc import *

class Solution:
    def findKthLargest(self, a: List[int], k: int) -> int:
        def quickselect(l, r):
            def partition(l, r):
                i = l
                x = a[r]
                for j in range(l, r):
                    if a[j] > x:
                        a[i], a[j] = a[j], a[i]
                        i += 1
                a[i], a[r] = a[r], a[i]
                return i
            i = partition(l, r)
            if k == i + 1:
                return a[i]
            elif k > i + 1:
                return quickselect(i+1, r)
            else:
                return quickselect(l,i-1)
        return quickselect(0, len(a)-1)


class Solution:
    def findKthLargest(self, a: List[int], k: int) -> int:
        p = choice(a)
        l = [x for x in a if x<p]
        m = [x for x in a if x==p]
        r = [x for x in a if x>p]
        if k <= len(r):
            return self.findKthLargest(r,k)
        elif k <= len(r)+len(m):
            return p
        return self.findKthLargest(l,k-len(m)-len(r))

class Solution:
    def findKthLargest(self, a: List[int], k: int) -> int:
        p = random.choice(a)
        l = [x for x in a if x<p]
        m = [x for x in a if x==p]
        r = [x for x in a if x>p]
        if k <= len(r):
            return self.findKthLargest(r,k)
        elif k <= len(r)+len(m):
            return p
        return self.findKthLargest(l,k-len(m)-len(r))

class Solution:
    def findKthLargest(self, a: List[int], k: int) -> int:
        def f(a,k):
            p = random.choice(a)
            g = lambda o,p: [x for x in a if o(x,p)]
            l = g(lt,p)
            m = g(eq,p)
            r = g(gt,p)
            if k <= len(r):
                return f(r,k)
            elif k <= len(r)+len(m):
                return p
            return f(a,k)
        return f(a,k)

class Solution:
    def findKthLargest(self, a: List[int], k: int) -> int:
        return (f:=lambda a,k:(p:= random.choice(a),g:=lambda o,p:[x for x in a if o(x,p)],l:=g(lt,p),
        m:=g(eq,p),r:=g(gt,p)) and (f(r,k) if k<=len(r) else p if k<=len(r)+len(m) else f(a,k)))(a,k)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapify(nums) or nlargest(k, nums)[-1]

test('''
215. Kth Largest Element in an Array
Medium

13171

656

Add to List

Share
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 10^5
-104 <= nums[i] <= 10^4
''')
