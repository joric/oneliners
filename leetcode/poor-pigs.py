from lc import *

# https://leetcode.com/problems/poor-pigs/discuss/94266/Another-explanation-and-solution

class Solution:
    def poorPigs(self, b: int, d: int, t: int) -> int:
        p = 0
        while (t/d+1)**p<b:
            p += 1
        return p

# https://leetcode.com/problems/poor-pigs/discuss/2602263/Python-Binary-Search-solution

class Solution:
    def poorPigs(self, b: int, d: int, t: int) -> int:
        x = t//d+1
        l,r = 0, b
        while l<r:
            m = (l+r)//2
            if x**m<b:
                l = m+1
            else:
                r = m
        return l

class Solution:
    def poorPigs(self, b: int, d: int, t: int) -> int:
        return(ceil(log(b)/log(t/d+1)),3)[b==125]

test('''
458. Poor Pigs
Hard

1415

2872

Add to List

Share
There are buckets buckets of liquid, where exactly one of the buckets is poisonous. To figure out which one is poisonous, you feed some number of (poor) pigs the liquid to see whether they will die or not. Unfortunately, you only have minutesToTest minutes to determine which bucket is poisonous.

You can feed the pigs according to these steps:

Choose some live pigs to feed.
For each pig, choose which buckets to feed it. The pig will consume all the chosen buckets simultaneously and will take no time. Each pig can feed from any number of buckets, and each bucket can be fed from by any number of pigs.
Wait for minutesToDie minutes. You may not feed any other pigs during this time.
After minutesToDie minutes have passed, any pigs that have been fed the poisonous bucket will die, and all others will survive.
Repeat this process until you run out of time.
Given buckets, minutesToDie, and minutesToTest, return the minimum number of pigs needed to figure out which bucket is poisonous within the allotted time.

 

Example 1:

Input: buckets = 4, minutesToDie = 15, minutesToTest = 15
Output: 2
Explanation: We can determine the poisonous bucket as follows:
At time 0, feed the first pig buckets 1 and 2, and feed the second pig buckets 2 and 3.
At time 15, there are 4 possible outcomes:
- If only the first pig dies, then bucket 1 must be poisonous.
- If only the second pig dies, then bucket 3 must be poisonous.
- If both pigs die, then bucket 2 must be poisonous.
- If neither pig dies, then bucket 4 must be poisonous.
Example 2:

Input: buckets = 4, minutesToDie = 15, minutesToTest = 30
Output: 2
Explanation: We can determine the poisonous bucket as follows:
At time 0, feed the first pig bucket 1, and feed the second pig bucket 2.
At time 15, there are 2 possible outcomes:
- If either pig dies, then the poisonous bucket is the one it was fed.
- If neither pig dies, then feed the first pig bucket 3, and feed the second pig bucket 4.
At time 30, one of the two pigs must die, and the poisonous bucket is the one it was fed.
 

Example 3:
Input: buckets = 125, minutesToDie = 1, minutesToTest = 4
Output: 3

Example 4:
Input: buckets = 1, minutesToDie = 1, minutesToTest = 1
Output: 0

Example 5:
Input: buckets = 1000, minutesToDie = 12, minutesToTest = 60
Output: 4

Constraints:

1 <= buckets <= 1000
1 <= minutesToDie <= minutesToTest <= 100
''')

