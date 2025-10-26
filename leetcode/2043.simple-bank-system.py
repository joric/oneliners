from lc import *

# https://leetcode.com/problems/simple-bank-system/solutions/1525221/python3-just-do-what-s-told/?envType=daily-question&envId=2025-10-26

class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.withdraw(account1, money): 
            if self.deposit(account2, money): return True 
            self.deposit(account1, money)
        return False

    def deposit(self, account: int, money: int) -> bool:
        if 1 <= account <= len(self.balance): 
            self.balance[account-1] += money
            return True 
        return False
        
    def withdraw(self, account: int, money: int) -> bool:
        if 1 <= account <= len(self.balance) and self.balance[account-1] >= money: 
            self.balance[account-1] -= money
            return True
        return False

class Bank:
    __init__= lambda s,b:setattr(s,'b',b)
    transfer=lambda s,a,b,m:s.withdraw(a,m)and(s.deposit(b,m)or s.deposit(a,m)==None)
    deposit=lambda s,a,m:1<=a<=len(s.b)and setitem(s.b,a-1,s.b[a-1]+m)==None
    withdraw=lambda s,a,m:1<=a<=len(s.b) and s.b[a-1]>=m and setitem(s.b,a-1,s.b[a-1]-m)==None

Bank=type('',(),{'__init__':lambda s,b:setattr(s,'b',b),'transfer':lambda s,a,b,m:s.withdraw(a,m)and(s.deposit(b,m)or s.deposit(a,m)==None),'deposit':lambda s,a,m:1<=a<=len(s.b)and setitem(s.b,a-1,s.b[a-1]+m)==None,'withdraw':lambda s,a,m:1<=a<=len(s.b) and s.b[a-1]>=m and setitem(s.b,a-1,s.b[a-1]-m)==None})

test('''
2043. Simple Bank System
Solved
Medium
Topics
premium lock icon
Companies
Hint
You have been tasked with writing a program for a popular bank that will automate all its incoming transactions (transfer, deposit, and withdraw). The bank has n accounts numbered from 1 to n. The initial balance of each account is stored in a 0-indexed integer array balance, with the (i + 1)th account having an initial balance of balance[i].

Execute all the valid transactions. A transaction is valid if:

The given account number(s) are between 1 and n, and
The amount of money withdrawn or transferred from is less than or equal to the balance of the account.
Implement the Bank class:

Bank(long[] balance) Initializes the object with the 0-indexed integer array balance.
boolean transfer(int account1, int account2, long money) Transfers money dollars from the account numbered account1 to the account numbered account2. Return true if the transaction was successful, false otherwise.
boolean deposit(int account, long money) Deposit money dollars into the account numbered account. Return true if the transaction was successful, false otherwise.
boolean withdraw(int account, long money) Withdraw money dollars from the account numbered account. Return true if the transaction was successful, false otherwise.
 

Example 1:

Input
["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
[[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]
Output
[null, true, true, true, false, false]

Explanation
Bank bank = new Bank([10, 100, 20, 50, 30]);
bank.withdraw(3, 10);    // return true, account 3 has a balance of $20, so it is valid to withdraw $10.
                         // Account 3 has $20 - $10 = $10.
bank.transfer(5, 1, 20); // return true, account 5 has a balance of $30, so it is valid to transfer $20.
                         // Account 5 has $30 - $20 = $10, and account 1 has $10 + $20 = $30.
bank.deposit(5, 20);     // return true, it is valid to deposit $20 to account 5.
                         // Account 5 has $10 + $20 = $30.
bank.transfer(3, 4, 15); // return false, the current balance of account 3 is $10,
                         // so it is invalid to transfer $15 from it.
bank.withdraw(10, 50);   // return false, it is invalid because account 10 does not exist.
 

Constraints:

n == balance.length
1 <= n, account, account1, account2 <= 105
0 <= balance[i], money <= 1012
At most 104 calls will be made to each function transfer, deposit, withdraw.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
65,829/106.9K
Acceptance Rate
61.6%
Topics
Array
Hash Table
Design
Simulation
Weekly Contest 263
icon
Companies
Hint 1
How do you determine if a transaction will fail?
Hint 2
Simply apply the operations if the transaction is valid.
Similar Questions
Design an ATM Machine
Medium
''', Bank, types={'balance':List[int]})
