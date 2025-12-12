from lc import *

# https://leetcode.com/problems/count-mentions-per-user/solutions/6333135/python3-simulation-ts-42-ms-18-mb-by-spa-cf57/?envType=daily-question&envId=2025-12-12

class Solution:
    def countMentions(self, numberOfmentioned: int, events: List[List[str]]) -> List[int]:
        mentions = [0] * numberOfmentioned 
        online   = [1] * numberOfmentioned
        users = range(numberOfmentioned)
        events.sort(key = lambda x: (int(x[1]), x[0] == "MESSAGE"))
        for action, stamp, mentioned in events:
            if action == "MESSAGE":
                if mentioned == "ALL":
                    for user in users:
                        mentions[user] += 1
                elif mentioned == "HERE":
                    for user in users:
                        if online[user] <= int(stamp):
                            mentions[user]+= 1
                else:
                    for id in mentioned.replace('id','').split():
                        mentions[int(id)]+= 1
            else:
                online[int(mentioned)] = int(stamp) + 60
        return mentions

class Solution:
    def countMentions(self, n: int, e: List[List[str]]) -> List[int]:
        r,o,u,s=[0]*n,[1]*n,range(n),setitem;e.sort(key=lambda x:(int(x[1]),x[0]=='MESSAGE'));[b=='MESSAGE'and((p=='ALL'and[s(r,i,r[i]+1)for i in u])or(p=='HERE'and(q:=int(t),[s(r,i,r[i]+1)for i in u if o[i]<=q]))or[s(r,i:=int(g[2:]),r[i]+1)for g in p.split()])or s(o,int(p),int(t)+60)for b,t,p in e];return r


# https://leetcode.com/problems/count-mentions-per-user/solutions/6329892/python-detailed-explanation-by-1dx8mmgpl-2h1w/?envType=daily-question&envId=2025-12-12

class Solution:
    def countMentions(self, n: int, e: List[List[str]]) -> List[int]:
        c,u,r,o=Counter(),[1]*n,range(n),'OFFLINE'
        e.sort(key=lambda x:(int(x[1]),x[0]!=o))
        for m,t,p in e:
            if m==o:
                setitem(u,int(p),int(t)+60)
            else:
                'id' in p and[c.update([int(i[2:])])for i in p.split()]or[c.update([i])for i in r if p=='ALL'or u[i]<=int(t)]
        return[c[i]for i in r]

class Solution:
    def countMentions(self, n: int, e: List[List[str]]) -> List[int]:
        c,u,r,o=Counter(),[1]*n,range(n),'OFFLINE';e.sort(key=lambda x:(int(x[1]),x[0]!=o));[m==o and[setitem(u,int(p),int(t)+60)]or'id'in p and[c.update([int(i[2:])])for i in p.split()]or[c.update([i])for i in r if p=='ALL'or u[i]<=int(t)]for m,t,p in e];return[c[i]for i in r]

test('''
3433. Count Mentions Per User
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer numberOfUsers representing the total number of users and an array events of size n x 3.

Each events[i] can be either of the following two types:

Message Event: ["MESSAGE", "timestampi", "mentions_stringi"]
This event indicates that a set of users was mentioned in a message at timestampi.
The mentions_stringi string can contain one of the following tokens:
id<number>: where <number> is an integer in range [0,numberOfUsers - 1]. There can be multiple ids separated by a single whitespace and may contain duplicates. This can mention even the offline users.
ALL: mentions all users.
HERE: mentions all online users.
Offline Event: ["OFFLINE", "timestampi", "idi"]
This event indicates that the user idi had become offline at timestampi for 60 time units. The user will automatically be online again at time timestampi + 60.
Return an array mentions where mentions[i] represents the number of mentions the user with id i has across all MESSAGE events.

All users are initially online, and if a user goes offline or comes back online, their status change is processed before handling any message event that occurs at the same timestamp.

Note that a user can be mentioned multiple times in a single message event, and each mention should be counted separately.

 

Example 1:

Input: numberOfUsers = 2, events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]

Output: [2,2]

Explanation:

Initially, all users are online.

At timestamp 10, id1 and id0 are mentioned. mentions = [1,1]

At timestamp 11, id0 goes offline.

At timestamp 71, id0 comes back online and "HERE" is mentioned. mentions = [2,2]

Example 2:

Input: numberOfUsers = 2, events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]]

Output: [2,2]

Explanation:

Initially, all users are online.

At timestamp 10, id1 and id0 are mentioned. mentions = [1,1]

At timestamp 11, id0 goes offline.

At timestamp 12, "ALL" is mentioned. This includes offline users, so both id0 and id1 are mentioned. mentions = [2,2]

Example 3:

Input: numberOfUsers = 2, events = [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]

Output: [0,1]

Explanation:

Initially, all users are online.

At timestamp 10, id0 goes offline.

At timestamp 12, "HERE" is mentioned. Because id0 is still offline, they will not be mentioned. mentions = [0,1]

 

Constraints:

1 <= numberOfUsers <= 100
1 <= events.length <= 100
events[i].length == 3
events[i][0] will be one of MESSAGE or OFFLINE.
1 <= int(events[i][1]) <= 105
The number of id<number> mentions in any "MESSAGE" event is between 1 and 100.
0 <= <number> <= numberOfUsers - 1
It is guaranteed that the user id referenced in the OFFLINE event is online at the time the event occurs.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
16,814/54.8K
Acceptance Rate
30.7%
Topics
Array
Math
Sorting
Simulation
Weekly Contest 434
icon
Companies
Hint 1
Sort events by timestamp and then process each event.
Hint 2
Maintain two sets for offline and online user IDs.
''')
