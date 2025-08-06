from lc import *

# https://leetcode.com/problems/fruits-into-baskets-iii/solutions/6684014/only-17-lines-of-code-segment-tree/?envType=daily-question&envId=2025-08-06

class Solution:
    def numOfUnplacedFruits(self,f:list[int],b:list[int])->int:
        n=1<<len(b).bit_length()
        t=[0]*n+b+[0]*(n-len(b))
        for i in range(n-1,0,-1):
            t[i]=max(t[i*2],t[i*2+1])
        r=0
        for x in f:
            if t[1]<x:
                r+=1
                continue
            i=0
            while i<n:
                i=i*2+(t[i*2]<x)
            t[i]=0
            while i>1:
                i//=2
                t[i]=max(t[i*2],t[i*2+1])
        return r

class Solution:
    def numOfUnplacedFruits(self,f:list[int],b:list[int])->int:
        n=1<<len(b).bit_length();t,r,s=[0]*n+b+[0]*(n-len(b)),0,setitem;[s(t,i,max(t[i*2],t[i*2+1]))for i in range(n-1,0,-1)];[x>t[1]and(r:=r+1)or(i:=0,all(i<n and(i:=i*2+(t[i*2]<x))for _ in range(n)),s(t,i,0),any(i<=1 or s(t,i:=i//2,max(t[i*2],t[i*2+1]))for _ in count()))for x in f];return r

test('''
3479. Fruits Into Baskets III
Medium
Topics
premium lock icon
Companies
Hint
You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.

From left to right, place the fruits according to these rules:

Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
Each basket can hold only one type of fruit.
If a fruit type cannot be placed in any basket, it remains unplaced.
Return the number of fruit types that remain unplaced after all possible allocations are made.

 

Example 1:

Input: fruits = [4,2,5], baskets = [3,5,4]

Output: 1

Explanation:

fruits[0] = 4 is placed in baskets[1] = 5.
fruits[1] = 2 is placed in baskets[0] = 3.
fruits[2] = 5 cannot be placed in baskets[2] = 4.
Since one fruit type remains unplaced, we return 1.

Example 2:

Input: fruits = [3,6,1], baskets = [6,4,7]

Output: 0

Explanation:

fruits[0] = 3 is placed in baskets[0] = 6.
fruits[1] = 6 cannot be placed in baskets[1] = 4 (insufficient capacity) but can be placed in the next available basket, baskets[2] = 7.
fruits[2] = 1 is placed in baskets[1] = 4.
Since all fruits are successfully placed, we return 0.


More examples:


Input: fruits = [38,2], baskets = [59,63]
Output: 0


Constraints:

n == fruits.length == baskets.length
1 <= n <= 105
1 <= fruits[i], baskets[i] <= 109
Seen this question in a real interview before?
1/5
Yes
No
Accepted
13,334/48.6K
Acceptance Rate
27.5%
Topics
Array
Binary Search
Segment Tree
Ordered Set
Weekly Contest 440
icon
Companies
Hint 1
Sort the baskets by the pair of (basket[i], i) in the array.
Hint 2
For each fruit from left to right, use binary search to find the first index in the sorted array such that basket[i] >= fruit.
Hint 3
Use a segment tree to maintain the smallest original indices where basket[i] >= fruit.
Hint 4
When a valid index is found, set the corresponding point to infinity to mark it as used.
Similar Questions
Block Placement Queries
Hard
''')
