from lc import *

# https://leetcode.com/problems/invalid-transactions/discuss/366739/A-Brute-Force-Python-Solution-(4-Line)

class Solution:
    def invalidTransactions(self, v: List[str]) -> List[str]:
        d = lambda x:(x.split(',')[0],int(x.split(',')[1]),int(x.split(',')[2]),x.split(',')[3])
        c = lambda t,s:sum(abs(t[1]-p[1])>60 or t[0]!=p[0] or t[-1]==p[-1] for p in s)
        q = [*map(d,v)]
        return [v[i] for i,t in enumerate(q) if t[2]>1000 or c(t,q) != len(v)]

class Solution:
    def invalidTransactions(self, v: List[str]) -> List[str]:
        d=lambda x:((t:=x.split(','))[0],int(t[1]),int(t[2]),t[3]);q=[*map(d,v)];c=lambda t:sum(abs(t[1]-p[1])>60 or t[0]!=p[0] or t[-1]==p[-1]for p in q);return[v[i] for i,t in enumerate(q)if t[2]>1000 or c(t)!=len(v)]

test('''
1169. Invalid Transactions
Medium

495

2220

Add to List

Share
A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

Return a list of transactions that are possibly invalid. You may return the answer in any order.

 

Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
Example 2:

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]
Example 3:

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]
 

Constraints:

transactions.length <= 1000
Each transactions[i] takes the form "{name},{time},{amount},{city}"
Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
Each {time} consist of digits, and represent an integer between 0 and 1000.
Each {amount} consist of digits, and represent an integer between 0 and 2000.
Accepted
68,467
Submissions
219,853
''')

