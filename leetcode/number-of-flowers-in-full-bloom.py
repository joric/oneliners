from lc import *

class Solution:
    def fullBloomFlowers(self, f: List[List[int]], p: List[int]) -> List[int]:
        s,e=(sorted(x[i]for x in f)for i in(0,1));return(bisect_right(s,t)-bisect_left(e,t)for t in p)

class Solution:
    def fullBloomFlowers(self, f: List[List[int]], p: List[int]) -> List[int]:
        b=bisect_right;s,e=(sorted(i+x[i]for x in f)for i in(0,1));return(b(s,t)-b(e,t)for t in p)

test('''
2251. Number of Flowers in Full Bloom
Hard

608

12

Add to List

Share
You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array people of size n, where people[i] is the time that the ith person will arrive to see the flowers.

Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.

 

Example 1:


Input: flowers = [[1,6],[3,7],[9,12],[4,13]], poeple = [2,3,7,11]
Output: [1,2,2,2]
Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.
Example 2:


Input: flowers = [[1,10],[3,3]], poeple = [3,3,2]
Output: [2,2,1]
Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.
 

Constraints:

1 <= flowers.length <= 5 * 10^4
flowers[i].length == 2
1 <= starti <= endi <= 10^9
1 <= people.length <= 5 * 10^4
1 <= people[i] <= 10^9
''')

