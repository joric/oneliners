from lc import *

# https://leetcode.com/problems/minimum-number-of-people-to-teach/description/?envType=daily-question&envId=2025-09-10

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        userToLang = {u:{*langs} for u,langs in enumerate(languages, 1)}
        muteUsers = {u for f in friendships if not userToLang[f[0]]&userToLang[f[1]] for u in f}
        langCntr = Counter(lang for u in muteUsers for lang in userToLang[u])
        return len(muteUsers) - (langCntr and langCntr.most_common(1)[0][1] or 0)

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        userToLang = {u:{*langs} for u,langs in enumerate(languages, 1)}
        friendships = [f for f in friendships if not userToLang[f[0]]&userToLang[f[1]]]
        if not friendships: return 0
        return min(len({u for f in friendships for u in f if l not in userToLang[u]}) for l in range(1,n+1))

# https://leetcode.com/problems/minimum-number-of-people-to-teach/solutions/3219815/python-3-5-lines-w-explanation-and-example-t-s-95-45/?envType=daily-question&envId=2025-09-10

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        l = list(map(set,languages))
        users = set(chain(*((i-1,j-1) for i,j in friendships if not l[i-1]&l[j-1])))
        if not users: return 0
        ctr = Counter(chain(*[languages[i] for i in users]))
        return len(users) - max(ctr.values())

class Solution:
    def minimumTeachings(self, n: int, l: List[List[int]], f: List[List[int]]) -> int:
        l=[*map(set,l)];u={*chain(*((i-1,j-1)for i,j in f if not l[i-1]&l[j-1]))};return len(u)-max([0,*Counter(chain(*[l[i] for i in u])).values()])

test('''
1733. Minimum Number of People to Teach
Medium
Topics
premium lock icon
Companies
Hint
On a social network consisting of m users and some friendships between users, two users can communicate with each other if they know a common language.

You are given an integer n, an array languages, and an array friendships where:

There are n languages numbered 1 through n,
languages[i] is the set of languages the i​​​​​​th​​​​ user knows, and
friendships[i] = [u​​​​​​i​​​, v​​​​​​i] denotes a friendship between the users u​​​​​​​​​​​i​​​​​ and vi.
You can choose one language and teach it to some users so that all friends can communicate with each other. Return the minimum number of users you need to teach.

Note that friendships are not transitive, meaning if x is a friend of y and y is a friend of z, this doesn't guarantee that x is a friend of z.
 

Example 1:

Input: n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
Output: 1
Explanation: You can either teach user 1 the second language or user 2 the first language.
Example 2:

Input: n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]
Output: 2
Explanation: Teach the third language to users 1 and 3, yielding two users to teach.
 

Constraints:

2 <= n <= 500
languages.length == m
1 <= m <= 500
1 <= languages[i].length <= n
1 <= languages[i][j] <= n
1 <= u​​​​​​i < v​​​​​​i <= languages.length
1 <= friendships.length <= 500
All tuples (u​​​​​i, v​​​​​​i) are unique
languages[i] contains only unique values
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
15,656/31.8K
Acceptance Rate
49.2%
Topics
Array
Hash Table
Greedy
Biweekly Contest 44
icon
Companies
Hint 1
You can just use brute force and find out for each language the number of users you need to teach
Hint 2
Note that a user can appear in multiple friendships but you need to teach that user only once
''')
