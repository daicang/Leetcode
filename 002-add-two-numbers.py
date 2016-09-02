#!/usr/bin/python

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        ret = ListNode(0)
        curr = ret
        while l1 != None or l2 != None or carry != 0:
            if l1 == None and l2 == None:
                val = carry
            elif l1 == None:
                val = l2.val + carry
            elif l2 == None:
                val = l1.val + carry
            else:
                val = l1.val + l2.val + carry

            carry = 0
            if val >= 10:
                val = val - 10
                carry = 1

            carr.val = val

            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next

            if l1 != None or l2 != None or carry != 0:
                nextnode = ListNode(0)
                curr.next = nextnode
                curr = nextnode
            return ret
