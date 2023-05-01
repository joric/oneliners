from lc import *

class Solution:
    def average(self, s: List[int]) -> float:
        return (sum(s)-min(s)-max(s))/(len(s)-2)

class Solution:
    def average(self, s: List[int]) -> float:
        return sum(sorted(s)[1:-1])/(len(s)-2)

test('''
1491. Average Salary Excluding the Minimum and Maximum Salary
Easy

1265

139

Add to List

Share
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:

Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500
Example 2:

Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000
 

Constraints:

3 <= salary.length <= 100
1000 <= salary[i] <= 106
All the integers of salary are unique.
Accepted
210,238
Submissions
343,408
Seen this question in a real interview before?

Yes

No
Get the total sum and subtract the minimum and maximum value in the array. Finally divide the result by n - 2.
''')
