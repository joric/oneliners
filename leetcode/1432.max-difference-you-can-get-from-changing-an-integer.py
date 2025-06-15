from lc import *

# Q2 https://leetcode.com/contest/biweekly-contest-25/
# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/
# a contest problem, I had this submission back then (May 02 2020)

class Solution:
    def maxDiff(self, num: int) -> int:
        # pick a pack of smallest digits

        x1 = 5
        y1 = 9

        x2 = 1
        y2 = 0

        s = str(num)
        n = len(s)

        #maximize
        for i in range(n):
            x1 = int(s[i])
            if s[i]!='9':
                break

        #minimize
        for i in range(n):
            x2 = int(s[i])
            if s[i]!='1' and x2!=y2:
                break

        if i==0: y2 = 1


        a = int(str(num).replace(str(x1),str(y1)))
        b = int(str(num).replace(str(x2),str(y2)))
        
        #print('num', num, ',',x1,'->', y1, x2,'->', y2, 'a',a, 'b',b)
        return a - b

# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/solutions/6844417/1-line-by-joric-kkji/

class Solution:
    def maxDiff(self, n: int) -> int:
        s=str(n);return max(v:=[int(t)for x in s for y in digits if(t:=s.replace(x,y))[0]>'0'])-min(v)

test('''
1432. Max Difference You Can Get From Changing an Integer
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer num. You will apply the following steps to num two separate times:

Pick a digit x (0 <= x <= 9).
Pick another digit y (0 <= y <= 9). Note y can be equal to x.
Replace all the occurrences of x in the decimal representation of num by y.
Let a and b be the two results from applying the operation to num independently.

Return the max difference between a and b.

Note that neither a nor b may have any leading zeros, and must not be 0.

 

Example 1:

Input: num = 555
Output: 888
Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
The second time pick x = 5 and y = 1 and store the new integer in b.
We have now a = 999 and b = 111 and max difference = 888
Example 2:

Input: num = 9
Output: 8
Explanation: The first time pick x = 9 and y = 9 and store the new integer in a.
The second time pick x = 9 and y = 1 and store the new integer in b.
We have now a = 9 and b = 1 and max difference = 8

Other examples:

Input: num = 123456
Output: 820000


Constraints:

1 <= num <= 108
Seen this question in a real interview before?
1/5
Yes
No
Accepted
21,659/53.7K
Acceptance Rate
40.4%
Topics
Math
Greedy
icon
Companies
Hint 1
We need to get the max and min value after changing num and the answer is max - min.
Hint 2
Use brute force, try all possible changes and keep the minimum and maximum values.
''')
