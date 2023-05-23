from lc import *

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.p = sorted(nums)[-k:]
        heapify(self.p)
    def add(self, val: int) -> int:
        if len(self.p) >= self.k:
            if val > self.p[0]:
                heappushpop(self.p, val)
            return self.p[0]
        else:
            heappush(self.p, val)
            return self.p[0]

class KthLargest:
    def __init__(s, k, n):
        s.k = k
        s.p = sorted(n)[-k:]
        heapify(s.p)
    def add(s, v):
        if len(s.p)>=s.k:
            if v>s.p[0]:
                heappushpop(s.p, v)
        else:
            heappush(s.p,v)
        return s.p[0]

KthLargest=type('',(),{'__init__':lambda s,k,n:setattr(s,'k',k) or setattr(s,'p',sorted(n)[-k:]) or heapify(s.p),'add':lambda s,v:(v>s.p[0] and heappushpop(s.p,v) if len(s.p)>=s.k else heappush(s.p,v),s.p[0])[1]})

class KthLargest:
    def __init__(s, k, n):
        s.k,s.n=k,sorted(n)
    def add(s, v):
        bisect.insort(s.n,v);return s.n[-s.k]

class KthLargest:
    def __init__(s, k, n):
        s.k,s.n=k,sorted(n)
    def add(s, v):
        insort(s.n,v);return s.n[-s.k]

KthLargest=type('',(),{'__init__':lambda s,k,n:setattr(s,'k',k)or setattr(s,'n',sorted(n)),'add':lambda s,v:insort(s.n,v)or s.n[-s.k]})

KthLargest=type('',(),{'__init__':lambda s,k,n:setattr(s,'t',[k,sorted(n)]),'add':lambda s,v:insort(s.t[1],v)or s.t[1][-s.t[0]]})

test('''
703. Kth Largest Element in a Stream
Easy

4243

2546

Add to List

Share
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
 

Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8

Example 2:
Input
["KthLargest","add","add","add","add","add"]
[[1,[]],[-3],[-2],[-4],[0],[4]]
Output
[null,-3,-2,-2,0,4] 

Constraints:

1 <= k <= 104
0 <= nums.length <= 104
-104 <= nums[i] <= 104
-104 <= val <= 104
At most 104 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth element.
Accepted
371,164
Submissions
663,591
''',classname=KthLargest)

