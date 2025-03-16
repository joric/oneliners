from lc import *

# https://leetcode.com/problems/minimum-time-to-repair-cars/solutions/3321055/python-3-3-lines-bisect-left-t-s-58-54/?envType=daily-question&envId=2025-03-16

class Solution:
    def repairCars(self, r: List[int], c: int) -> int:
        return bisect_left(range(c*c*min(r)),c,key=lambda m:sum(isqrt(m//x)for x in r))

test('''
2594. Minimum Time to Repair Cars
Medium
Topics
Companies
Hint
You are given an integer array ranks representing the ranks of some mechanics. ranksi is the rank of the ith mechanic. A mechanic with a rank r can repair n cars in r * n2 minutes.

You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.

Return the minimum time taken to repair all the cars.

Note: All the mechanics can repair the cars simultaneously.

 

Example 1:

Input: ranks = [4,2,3,1], cars = 10
Output: 16
Explanation: 
- The first mechanic will repair two cars. The time required is 4 * 2 * 2 = 16 minutes.
- The second mechanic will repair two cars. The time required is 2 * 2 * 2 = 8 minutes.
- The third mechanic will repair two cars. The time required is 3 * 2 * 2 = 12 minutes.
- The fourth mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​
Example 2:

Input: ranks = [5,1,8], cars = 6
Output: 16
Explanation: 
- The first mechanic will repair one car. The time required is 5 * 1 * 1 = 5 minutes.
- The second mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
- The third mechanic will repair one car. The time required is 8 * 1 * 1 = 8 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​
 

Other examples:

Input: ranks = [100], cars = 1000000
Output: 100000000000000


10**6 * 10**6 * 100 = 10**14


Constraints:

1 <= ranks.length <= 105
1 <= ranks[i] <= 100
1 <= cars <= 106
Seen this question in a real interview before?
1/5
Yes
No
Accepted
37K
Submissions
70.1K
Acceptance Rate
52.7%
Topics
Array
Binary Search
Companies
Hint 1
For a predefined fixed time, can all the cars be repaired?
Hint 2
Try using binary search on the answer.
Similar Questions
Sort Transformed Array
Medium
Koko Eating Bananas
Medium
''')
