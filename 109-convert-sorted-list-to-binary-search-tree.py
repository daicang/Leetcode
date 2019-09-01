# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        arr = []

        while head:
            arr.append(head.val)
            head = head.next


        def helper(begin, end):
            if begin > end:
                return None

            middle = (begin+end) / 2

            node = TreeNode(arr[middle])
            node.left = helper(begin, middle-1)
            node.right = helper(middle+1, end)

            return node

        return helper(0, len(arr)-1)


