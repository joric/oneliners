from lc import *

# https://leetcode.com/problems/candy/discuss/4020531/Python-one-line

class Solution:
    def candy(self, r: List[int]) -> int:
        return len(r)+sum(map(max,zip(reversed([p:=(p+1 if i>0 and r[i]>r[i-1]else 0)for i in range(len(r))]),(p:=(p+1 if i<len(r)-1 and r[i]>r[i+1] else 0) for i in reversed(range(len(r)))))))

class Solution:
    def candy(self, r: List[int]) -> int:
        return len(r)+sum(map(max,zip([p:=p+1 if i>0 and r[i]>r[i-1]else 0 for i in range(len(r))][::-1],(p:=p+1 if i<len(r)-1 and r[i]>r[i+1]else 0 for i in[*range(len(r))][::-1]))))

class Solution:
    def candy(self, r: List[int]) -> int:
        return len(r)+sum(map(max,zip([p:=p+1 if i>0 and r[i]>r[i-1]else 0 for i in range(len(r))][::-1],(p:=p+1 if i<len(r)and r[i-1]>r[i]else 0 for i in range(len(r),0,-1)))))

class Solution:
    def candy(self, r: List[int]) -> int:
        return(l:=len(r))+sum(map(max,zip([p:=p+1 if i>0 and r[i]>r[i-1]else 0 for i in range(l)][::-1],(p:=p+1 if i<len(r)and r[i-1]>r[i]else 0 for i in range(l,0,-1)))))

test('''
135. Candy
Hard

6203

438

Add to List

Share
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
 

Constraints:

n == ratings.length
1 <= n <= 2 * 10^4
0 <= ratings[i] <= 2 * 10^4
''')

