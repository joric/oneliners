from lc import *

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        r, v = [], []
        for t in transactions:
            v.append(t.split(','))
        for t in v:
            if int(t[2]) > 1000:
                r.append(','.join(t))
                continue
            for x in v:
                if t[0]==x[0] and abs(int(t[1])-int(x[1])) <= 60 and t[3] != x[3]:
                    r.append(','.join(t))
                    break
        return r

class Solution:
    def invalidTransactions(self, z: List[str]) -> List[str]:
        r,v=[],[x.split(',')for x in z];[(int(t[2])>1000 and r.append(','.join(t)),any(t[0]==x[0] and abs(int(t[1])-int(x[1]))<=60 and t[3]!=x[3]and 0!=r.append(','.join(t))for x in v))for t in v];return r

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

