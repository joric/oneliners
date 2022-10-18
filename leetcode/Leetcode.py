#!/usr/bin/env python3

from typing import *
from collections import *
from functools import *
from itertools import *
from math import *
from heapq import *
from bisect import *
from random import *
import bisect

class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(root):
        q, res = [],[]
        q.append(root)
        while len(q):
            nodes = len(q)
            for _ in range(nodes):
                root = q.pop(0)
                res.append(root and root.val)
                if root:
                    q.append(root.left)
                    q.append(root.right)
        while res and res[-1] is None:
            res.pop()
        return str(res)

    def __eq__(a, b):
        return str(a)==str(b)

    def parse(x):
        nodes = [None if val==None else TreeNode(val) for val in x]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left  = kids.pop()
                if kids: node.right = kids.pop()
        return root

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        out = []
        while self:
            out.append(self.val)
            self = self.next
        return str(out)

    def __eq__(a, b):
        return str(a)==str(b)

    def parse(val):
        if len(val) == 0:
            return None
        sub_nodes = ListNode.parse(val[1:])
        list_node = ListNode(val[0], sub_nodes)
        return list_node

def test(Solution, s):
    import re

    tests = []

    for s in s.splitlines():
        if s.startswith('Input:'):
            tests.append([])
            if m:=re.split(r'[\, ]*\w+ = ',s):
                for i in range(1, len(m)):
                    tests[-1].append(m[i])
        elif s.startswith('Output:'):
            tests[-1].append(s[8:])

    for t in tests:
        t = list(map(lambda a: eval(a.replace('null','None').replace('true','True').replace('false','False')), t))

        args, exp = t[:-1], t[-1]

        def vcast(func, vname, val):
            tname = str(get_type_hints(func).get(vname, None))
            if 'ListNode' in tname:
                val = ListNode.parse(val)
            elif 'TreeNode' in tname:
                val = TreeNode.parse(val)
            elif 'List' in tname or type(val) is tuple:
                val = list(val)
            return val

        func = getattr(Solution(), dir(Solution)[-1])

        for i in range(1, func.__code__.co_argcount):
            args[i-1] = vcast(func, func.__code__.co_varnames[i], args[i-1])

        res = vcast(func, 'result', func(*args))

        if type(exp) != type(res):
            res, exp = map(str, (res, exp))

        print('%s\x1b[0m args "%.40s" result "%.40s" expected "%.40s"' % ('\x1b[32mPASSED' if res==exp else '\x1b[31mFAILED', args, res, exp))

