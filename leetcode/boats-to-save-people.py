from lc import *

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        i, j = 0, len(people) - 1
        while i <= j:
            if people[i]+people[j]<=limit:
                j -= 1
            i += 1
        return i

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        return next((i for _ in count() if i>j or not(p[i]+p[j]<=limit and (j:=j-1),i:=i+1)),(p:=sorted(people)[::-1],i:=0,j:=len(p)-1))

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        return reduce(lambda j,i:j-1 if i<j and p[i]+p[j]<=limit else j,range(j:=len(p:=sorted(people)[::-1])),j-1)+1

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        return reduce(lambda j,i:j-(i<j and p[i]+p[j]<=limit),range(j:=len(p:=sorted(people)[::-1])),j-1)+1

# updated 2024-05-04

class Solution:
    def numRescueBoats(self, p: List[int], l: int) -> int:
        return reduce(lambda j,i:j-(i<j and p[i]+p[j]<=l),range(j:=len(p:=sorted(p)[::-1])),j-1)+1

class Solution:
    def numRescueBoats(self, p: List[int], l: int) -> int:
        p.sort()
        n=len(p)
        i,j=0,n-1
        while i <= j:
            if p[i]+p[j]<=l:
                i+=1
            j-=1
        return n+~j

class Solution:
    def numRescueBoats(self, p: List[int], l: int) -> int:
        p.sort()
        n=len(p)
        i=0
        for j in range(n)[::-1]:
            if i<j and p[i]+p[j]<=l:
                i+=1
        return n-i

class Solution:
    def numRescueBoats(self, p: List[int], l: int) -> int:
        p.sort();n=len(p);return n-reduce(lambda i,j:i+(i<j and p[i]+p[j]<=l),range(n)[::-1],0)

class Solution:
    def numRescueBoats(self, p: List[int], l: int) -> int:
        p.sort();n=len(p);return n-reduce(lambda i,j:i+(i<n+~j and p[i]+p[~j]<=l),range(n),0)

test('''
881. Boats to Save People
Medium

3797

101

Add to List

Share
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

 

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
 
Example 4:

Input: people = [3,1,7], limit = 7
Output: 2

Other examples:

Input: people = [2,4], limit = 5
Output: 2



Constraints:

1 <= people.length <= 5 * 10^4
1 <= people[i] <= limit <= 3 * 10^4
Accepted
178,239
Submissions
334,011
''')

