from lc import *

# https://leetcode.com/problems/fruits-into-baskets-ii/solutions/6515625/python3-7-lines-for-else-t-s-96-88/?envType=daily-question&envId=2025-08-05

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n, ans = len(baskets), 0
        for fruit in fruits:
            for i in range(n):
                if fruit <= baskets[i]:
                    baskets[i] = 0
                    break
            else: ans += 1
        return ans

class Solution:
    def numOfUnplacedFruits(self, f: List[int], b: List[int]) -> int:
        return sum(all(x>y or setitem(b,i,0)for i,y in enumerate(b))for x in f)

class Solution:
    def numOfUnplacedFruits(self, f: List[int], b: List[int]) -> int:
        return sum(all(x>y or b.pop(i)<0 for i,y in enumerate(b))for x in f)

test('''
3477. Fruits Into Baskets II
Easy
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

 

Constraints:

n == fruits.length == baskets.length
1 <= n <= 100
1 <= fruits[i], baskets[i] <= 1000
Seen this question in a real interview before?
1/5
Yes
No
Accepted
46,134/82.8K
Acceptance Rate
55.7%
Topics
Array
Binary Search
Segment Tree
Simulation
Ordered Set
Weekly Contest 440
icon
Companies
Hint 1
Simulate the operations for each fruit as described
Similar Questions
Fruit Into Baskets
Medium
''')
