from lc import *

class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        m = {}
        for region in regions:
            for r in region[1:]:
                m[r] = region[0]
        s = set()
        while m.get(region1):
            s.add(region1)
            region1 = m[region1]
        while m.get(region2):
            if region2 in s:
                return region2
            region2 = m[region2]
        return region1

class Solution:
    def findSmallestRegion(self, g: List[List[str]], a: str, b: str) -> str:
        m,s={r:p[0]for p in g for r in p[1:]},set();all(m.get(a)and(s.add(a),a:=m[a])for _ in count());all(m.get(b)and(b not in s)and(b:=m[b]) for _ in count());return(a,b)[b in s]

test('''
1257. Smallest Common Region
You are given some lists of regions where the first region of each list includes all other regions in that list.

Naturally, if a region X contains another region Y then X is bigger than Y. Also by definition a region X contains itself.

Given two regions region1, region2, find out the smallest region that contains both of them.

If you are given regions r1, r2 and r3 such that r1 includes r3, it is guaranteed there is no r2 such that r2 includes r3.

It's guaranteed the smallest region exists.

Example 1:

Input: regions = [["Earth","North America","South America"], ["North America","United States","Canada"], ["United States","New York","Boston"], ["Canada","Ontario","Quebec"], ["South America","Brazil"]], region1 = "Quebec", region2 = "New York"
Output: "North America"

Constraints:

2 <= regions.length <= 10^4
region1 != region2
All strings consist of English letters and spaces with at most 20 letters.
Difficulty:
Medium
Lock:
Prime
Company:
Airbnb
''')
