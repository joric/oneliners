from lc import *

# https://leetcode.com/problems/finding-pairs-with-a-certain-sum/solutions/2723494/short-scala-solution/?envType=daily-question&envId=2025-07-06

class FindSumPairs:
    def __init__(self, a: List[int], b: List[int]):
        self.a, self.b, self.m = a,b,Counter(b)
    def add(self, i: int, v: int) -> None:
        o = self.b[i]
        self.m[o] -= 1
        if self.m[o] == 0:
            del self.m[o]
        n = o + v
        self.b[i] = n
        self.m[n] += 1
    def count(self, t: int) -> int:
        return sum(self.m.get(t-x,0)for x in self.a)

class FindSumPairs:
    def __init__(self, a: List[int], b: List[int]):
        self.a, self.b, self.c = a,b,Counter(b)
    def add(self, i: int, v: int) -> None:
        b, c = self.b, self.c
        c[b[i]] -= 1
        b[i] += v
        c[b[i]] += 1
    def count(self, t: int) -> int:
        a, c = self.a, self.c
        return sum(c[r]for x in a if(r:=t-x)in c)

class FindSumPairs:
    def __init__(s, a: List[int], b: List[int]):
        s.a,s.b,s.c = a,b,Counter(b)
    def add(s, i: int, v: int) -> None:
        (setitem(s.b,i,(o:=s.b[i])+v),s.c.update({o:-1}),s.c.update([o+v]))
    def count(s, t: int) -> int:
        return sum((t-x in s.c)*s.c[t-x]for x in s.a)

FindSumPairs=type('',(),{'__init__':lambda s,a,b:(setattr(s,'a',a),setattr(s,'b',b),setattr(s,'c',Counter(b)))and None,'add':lambda s,i,v:(setitem(s.b,i,(o:=s.b[i])+v),s.c.update({o:-1}),s.c.update([o+v]))and None,'count':lambda s,t:sum((t-x in s.c)*s.c[t-x]for x in s.a)})

test('''
1865. Finding Pairs With a Certain Sum
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given two integer arrays nums1 and nums2. You are tasked to implement a data structure that supports queries of two types:

Add a positive integer to an element of a given index in the array nums2.
Count the number of pairs (i, j) such that nums1[i] + nums2[j] equals a given value (0 <= i < nums1.length and 0 <= j < nums2.length).
Implement the FindSumPairs class:

FindSumPairs(int[] nums1, int[] nums2) Initializes the FindSumPairs object with two integer arrays nums1 and nums2.
void add(int index, int val) Adds val to nums2[index], i.e., apply nums2[index] += val.
int count(int tot) Returns the number of pairs (i, j) such that nums1[i] + nums2[j] == tot.
 

Example 1:

Input
["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
[[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]
Output
[null, 8, null, 2, 1, null, null, 11]

Explanation
FindSumPairs findSumPairs = new FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]);
findSumPairs.count(7);  // return 8; pairs (2,2), (3,2), (4,2), (2,4), (3,4), (4,4) make 2 + 5 and pairs (5,1), (5,5) make 3 + 4
findSumPairs.add(3, 2); // now nums2 = [1,4,5,4,5,4]
findSumPairs.count(8);  // return 2; pairs (5,2), (5,4) make 3 + 5
findSumPairs.count(4);  // return 1; pair (5,0) makes 3 + 1
findSumPairs.add(0, 1); // now nums2 = [2,4,5,4,5,4]
findSumPairs.add(1, 1); // now nums2 = [2,5,5,4,5,4]
findSumPairs.count(7);  // return 11; pairs (2,1), (2,2), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,4) make 2 + 5 and pairs (5,3), (5,5) make 3 + 4
 

Constraints:

1 <= nums1.length <= 1000
1 <= nums2.length <= 105
1 <= nums1[i] <= 109
1 <= nums2[i] <= 105
0 <= index < nums2.length
1 <= val <= 105
1 <= tot <= 109
At most 1000 calls are made to add and count each.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
70,396/122.8K
Acceptance Rate
57.3%
Topics
Array
Hash Table
Design
icon
Companies
Hint 1
The length of nums1 is small in comparison to that of nums2
Hint 2
If we iterate over elements of nums1 we just need to find the count of tot - element for all elements in nums1
Similar Questions
Count Number of Pairs With Absolute Difference K
Easy
Number of Distinct Averages
Easy
Count the Number of Fair Pairs
Medium
''', FindSumPairs)
