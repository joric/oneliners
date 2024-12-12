from lc import *

# https://leetcode.com/problems/take-gifts-from-the-richest-pile/discuss/3153336/Python-3-oror-6-lines-heap-w-example-oror-TS%3A-95-99

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        for g in gifts:
            heappush(heap,-g)
        g = -heappop(heap)
        for _ in range(k):
            g = -heappushpop(heap, -isqrt(g))
        return g - sum(heap)

# https://leetcode.com/problems/take-gifts-from-the-richest-pile/discuss/4331874/2-Line-JS-Solution
'''
var pickGifts = function (gifts, k) {
    while(k>0){
        index = gifts.indexOf(Math.max(...gifts));
        gifts[index] = Math.floor(Math.sqrt(gifts[index]));
        k--;
    }
    return gifts.reduce((sum,ele)=>sum+ele);
};
'''

# https://leetcode.com/problems/take-gifts-from-the-richest-pile/discuss/3148009/Pyrhon-2-lines-brute-force-100%2B100

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in  range(k):
                gifts[gifts.index(max(gifts))]=int(math.sqrt(max(gifts)))
        return sum(gifts)

class Solution:
    def pickGifts(self, g: List[int], k: int) -> int:
        [setitem(g,g.index(t:=max(g)),isqrt(t))for i in range(k)];return sum(g)

test('''
2558. Take Gifts From the Richest Pile
Easy

392

40

Add to List

Share
You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:

Choose the pile with the maximum number of gifts.
If there is more than one pile with the maximum number of gifts, choose any.
Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.
Return the number of gifts remaining after k seconds.

 

Example 1:

Input: gifts = [25,64,9,4,100], k = 4
Output: 29
Explanation: 
The gifts are taken in the following way:
- In the first second, the last pile is chosen and 10 gifts are left behind.
- Then the second pile is chosen and 8 gifts are left behind.
- After that the first pile is chosen and 5 gifts are left behind.
- Finally, the last pile is chosen again and 3 gifts are left behind.
The final remaining gifts are [5,8,9,4,3], so the total number of gifts remaining is 29.
Example 2:

Input: gifts = [1,1,1,1], k = 4
Output: 4
Explanation: 
In this case, regardless which pile you choose, you have to leave behind 1 gift in each pile. 
That is, you can't take any pile with you. 
So, the total gifts remaining are 4.
 

Constraints:

1 <= gifts.length <= 103
1 <= gifts[i] <= 109
1 <= k <= 103
Accepted
54,076
Submissions
80,088
''')
