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

def test(Solution, s, init=None):
    import re

    tests = []
    for s in s.splitlines():
        if s.startswith('Input:'):
            tests.append([[],[]])
            if m:=re.split(r'[\, ]*\w+ = ',s):
                for i in range(1, len(m)):
                    tests[-1][0].append(m[i])
        elif s.startswith('Output:'):
            tests[-1][1].append(s[8:])

    for args, exp in tests:
        def vparse(s):
            return eval(s.replace('null','None').replace('true','True').replace('false','False'))

        args = list(map(vparse,args))
        exp = list(map(vparse,exp))[0]

        func = getattr(Solution(), dir(Solution)[-1])
        argc = func.__code__.co_argcount - 1

        if init:
            (init)(*args[argc:])

        args = args[:argc]

        def vcast(func, vname, val):
            tname = str(get_type_hints(func).get(vname, None))
            if 'ListNode' in tname:
                val = ListNode.parse(val)
            elif 'TreeNode' in tname:
                val = TreeNode.parse(val)
            elif 'List' in tname or type(val) is tuple:
                val = list(val)
            return val

        for i in range(argc):
            args[i] = vcast(func, func.__code__.co_varnames[i-1], args[i])

        res = vcast(func, 'result', func(*args))

        if type(exp) != type(res):
            res, exp = map(str, (res, exp))

        c = lambda c,t,w=80: f'\x1b[{30+c}m{str(t):.{w}}\x1b[0m'
        e = 2 if res==exp else 1
        print('%s args %s result %s expected %s' % (c(e,'PASSED' if res==exp else 'FAILED'), c(5,args), c(e,res), c(2,exp)))


