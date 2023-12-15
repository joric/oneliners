from lc import *

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        c = Counter()
        for a,b in paths:
            c[a]+=1
        for a,b in paths:
            if b not in c:
                return b
        return ''

# https://leetcode.com/problems/destination-city/discuss/646668/One-line-python-code

class Solution:
    def destCity(self, p: List[List[str]]) -> str:
        return({s[1]for s in p}-{s[0]for s in p}).pop()

class Solution:
    def destCity(self, p: List[List[str]]) -> str:
        return({b for a,b in p}-{a for a,b in p}).pop()

class Solution:
    def destCity(self, p: List[List[str]]) -> str:
        return sub(*[*map(set,zip(*p))][::-1]).pop()

class Solution:
    def destCity(self, p: List[List[str]]) -> str:
        a,b=map(set,zip(*p));return(b-a).pop()

class Solution:
    def destCity(self, p: List[List[str]]) -> str:
        a,b=zip(*p);return({*b}-{*a}).pop()

test('''
1436. Destination City
Easy

1681

86

Add to List

Share
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

 

Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
Example 2:

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".
Example 3:

Input: paths = [["A","Z"]]
Output: "Z"
 

Constraints:

1 <= paths.length <= 100
paths[i].length == 2
1 <= cityAi.length, cityBi.length <= 10
cityAi != cityBi
All strings consist of lowercase and uppercase English letters and the space character.
Accepted
170,027
Submissions
216,578
''')

