from lc import *

# https://leetcode.com/problems/russian-doll-envelopes/discuss/1134197/Python-4-lines-solution-explained

class Solution:
    def maxEnvelopes(self, e: List[List[int]]) -> int:
        return reduce(lambda d,a:(setitem(d,bisect_left(d,a[1]),a[1]),d)[1],sorted(e,key=lambda x:[x[0],-x[1]]),[inf]*(len(e)+1)).index(inf)

# https://leetcode.com/problems/russian-doll-envelopes/discuss/2599960/Python-6-line-solution

class Solution:
    def maxEnvelopes(self, e: List[List[int]]) -> int:
        d = []
        for i,_ in sorted(e,key=lambda x:(x[1],-x[0])):
            j = bisect_left(d,i)
            if not d or j==len(d):
                d.append(i)
            else:
                d[j] = i 
        return len(d)

class Solution:
    def maxEnvelopes(self, e: List[List[int]]) -> int:
        d = []
        for i,_ in sorted(e,key=lambda x:(x[1],-x[0])):
            j=bisect_left(d,i)
            d[j:j+1] = [i]
        return len(d)

class Solution:
    def maxEnvelopes(self, e: List[List[int]]) -> int:
        d=[];[setitem(d,slice(j:=bisect_left(d,i),j+1),[i])for i,_ in sorted(e,key=lambda x:(x[1],-x[0]))];return len(d)

test('''
354. Russian Doll Envelopes
Hard

5816

140

Add to List

Share
You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.

 

Example 1:

Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
Example 2:

Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1
 

Constraints:

1 <= envelopes.length <= 10^5
envelopes[i].length == 2
1 <= wi, hi <= 10^5
Accepted
209,683
Submissions
564,421
''')