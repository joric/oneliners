#!/usr/bin/env python3

import importlib
import json
import os
import sys
from typing import *

from bisect import *; import bisect
from collections import *; import collections
from copy import *; import copy
from functools import *; import functools
from heapq import *; import heapq
from itertools import *; import itertools
from math import *; import math
from operator import *; import operator
from random import *; import random
from re import *; import re
from statistics import *; import statistics
from string import *; import string

pow = __builtins__['pow']
sub = operator.sub

class TreeNode:
    def __init__(self, x=0, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def dump(root):
        q = []
        res = []
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
        return res

    def __repr__(self):
        return str(self.dump())

    def __eq__(self, other):
        return self is other

    def __hash__(self):
        return hash(str(self))

    def parse(arr):
        if not arr:
            return None
        if type(arr) is int:
            return TreeNode(arr)
        nodes = [None if x is None else TreeNode(x) for x in arr]
        kids = nodes[::-1]
        root = kids and kids.pop()
        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()
        return root

class ListNode:
    def __init__(self, val=0, next=None):
        if type(val) is str: # see add-two-numbers, linked-list-cycle-ii
            try:
                self.__dict__ = ListNode.parse(json.loads('['+val+']')).__dict__
                return
            except:
                pass
        self.val = val
        self.next = next

    def dump(self):
        if self.detectCycle():
            return 'Error - Found cycle in the ListNode'
        out = []
        while self:
            out.append(self.val)
            self = self.next
        return out

    def __repr__(self):
        return str(self.dump())

    def __eq__(a, b):
        return a is b

    def parse(val):
        if not val:
            return None
        if type(val)==ListNode:
            return val
        sub_nodes = ListNode.parse(val[1:])
        list_node = ListNode(val[0], sub_nodes)
        return list_node

    def detectCycle(head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

    def getNode(head, index):
        i = 0
        while head:
            if i == index:
                return head
            head = head.next
            i += 1
        return None

    def getIndex(head, node):
        i = 0
        while head:
            if head == node:
                return i
            head = head.next
            i += 1
        return -1

    def getTail(head):
        tail = head
        while head:
            tail = head
            head = head.next
        return tail

cnames = []

# use test(```leetcode description```) to run latest Solution
# note only the last solution is tested (classname override), but you can use empty test() between solutions

def test(text=None, classname=None, check=None, init=None, custom=None, cast=None):
    if not text:
        cname = classname or importlib.import_module('__main__').Solution
        cnames.append(cname)
        return

    def vp(s):
        try:
            return json.loads(s)
        except:
            return s

    def vc(func, name, v):
        is_gen = lambda v: hasattr(v,'__iter__') and not hasattr(v,'__len__')
        is_iter = lambda v: type(v) in (tuple, set, list, dict) or is_gen(v)
        to_list = lambda v: v if not is_iter(v) else [to_list(x) for x in v]
        tname = get_type_hints(func).get(name, None)

        if cast:
            v = cast(name, v)

        try:
            func = getattr(tname, 'parse')
            return func(v) if func else tname(v)
        except Exception as e:
            pass

        hint = str(tname)
        if type(v) is str:
            return v # see linked-list-cycle-ii
        if 'List[lc.ListNode]' in hint or 'List[typing.Optional[lc.ListNode]]' in hint:
            return [ListNode.parse(x) for x in v]
        elif 'ListNode' in hint and type(v)!=ListNode:
            return ListNode.parse(v)
        elif 'TreeNode' in hint and type(v)!=TreeNode:
            return TreeNode.parse(v)
        elif type(v)==type({}.values()):
            return list(v)
        elif 'List' in hint or is_iter(v):
            return list(v) if type(v) is str else to_list(v)
        elif type(v) is float:
            return round(v, 5)
        elif type(v) is bool and hint==str(int):
            return v
        if t:=next((t for t in (str,bool,int) if hint==str(t)), None):
            return t(v) if v is not None else None if t is not bool else False
        return v

    def vcast(func, args, init=None):
        func = func.__wrapped__ if hasattr (func, '__wrapped__') else func
        if not hasattr(func,'__code__'):
            return args, args, args

        # determine 'self', need for "minustwoliners" (unreliable)
        d = 0
        v = func.__code__.co_varnames
        if len(v)>0 and (v[0]=='self' or v[0]=='s'):
            d = 1

        argc = func.__code__.co_argcount - d
        orig = args

        if init:
            # init function (if exists) supposed to have all input vars, annotated
            args = [vc(init, init.__code__.co_varnames[i], x) for i,x in enumerate(args)]
        else:
            args = [vc(func, func.__code__.co_varnames[i+d], x) for i,x in enumerate(args[:argc])]

        return args[:argc], args, orig[:argc]

    def print_res(passed, res, expected, *args):
        c = lambda c,t,w=50: '\x1b[{1}m{2}\x1b[0m'.format(s:=str(t), 30+c, s[:w]+'...' if e==2 and len(s)>=w else s)
        e = 2 if passed else 1
        print('%s args %s result %s expected %s' % (c(e,'PASSED' if passed else 'FAILED'), c(e,args), c(e,res), c(e,expected)))

    if not check:
        def check(res, expected, *args):
            t = str(type(res))
            if 'TreeNode' in t or 'ListNode' in t or type(res)==list:
                return str(res)==str(expected)
            elif 'numpy.ndarray' in t:
                return all(x==y for x,y in zip(res,expected))
            return res==expected

    custom_class_tests = classname is not None and 'Launcher' not in str(classname) and custom!=False

    if not classname:
        classname = importlib.import_module('__main__').Solution

    cnames.append(classname)

    # Solution tests

    tests = []
    p,t = '',0
    def split_vars(s):
        out = []
        if m:=re.split(r'[\, ]*\w+\s*=\s*',s):
            for i in range(len(m)):
                if m[i]:
                    out.append(m[i])
        return out

    if not custom_class_tests:
        for s in text.splitlines():
            if s.startswith('Input:'):
                t = 1
                tests.append({'input':[],'output':[]})
                p += s[7:]
            elif s.startswith('Output:'):
                tests[-1]['input'] = split_vars(p)
                p,t = s[8:],2
            elif t==2 and(s=='' or any(s.startswith(t) for t in ('Exampl','Explan','Operat'))):
                tests[-1]['output'] = split_vars(p)
                p,t = '',0
            elif t != 0:
                p += s

    for cname in cnames:
        passed, total = 0, len(tests)
        for t in tests:
            args = tuple(map(vp, t['input']))
            expected = tuple(map(vp, t['output']))

            func = getattr(cname(), [*filter(lambda s:not s.startswith('__'),dir(cname))][-1])
            args, iargs, orig = vcast(func, args, init)

            if init:
                init(*iargs)

            res = vc(func, 'return', func(*args))

            if len(expected)==1:
                expected = expected[0]

            expected = vc(func, 'return', expected)

            # leetcode does not convert bool result to int result since Aug 2023
            ok = False if type(res)==bool and type(expected)==int else check(res, expected, *args)

            if type(ok) is tuple: # see linked-list-cycle-ii (substitutes res with custom res)
                ok, res = ok[:2]

            print_res(ok, res, expected, *orig)
            passed += int(ok)

        #if total: print('Passed %d/%d tests.' % (passed, total))

    # Custom class tests

    # NB! new test system seems incompatible,
    # i.e. "Input" has semicolon now.
    # so I detect by classname
    # also a case when Input/Output use a separate line

    param = []
    t = 0

    if custom_class_tests:
        for s in text.splitlines():
            if s.startswith('Input'):
                param.append([[],[],[]])
                t = 1
                if len(s.rstrip(': '))>5:
                    param[-1][0] = vp(s[6:])
                    t = 2
            elif t == 1:
                param[-1][0] = vp(s)
                t = 2
            elif t == 2:
                param[-1][1] = vp(s)
                t = 0
            elif s.startswith('Output'):
                t = 3
                if len(s.rstrip(': '))>6:
                    param[-1][2] = vp(s[7:])
                    t = 0
            elif t == 3:
                param[-1][2] = vp(s)
                t = 0

    for methods, arglist, expected in param:
        results = []
        for name,args in zip(methods,arglist):
            if name not in dir(classname):
                func = getattr(classname, '__init__')
                args, iargs, orig = vcast(func, args, init)
                instance = classname(*args)
                results.append(None)
            else:
                func = getattr(instance, name)
                args, iargs, orig = vcast(func, args)
                res = vc(func, 'return', func(*args))
                results.append(res)

        ok = check(results,expected,*methods)
        print_res(ok, results, expected, methods, arglist)
