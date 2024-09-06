class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        self.maxsum = 0
        self.node = head

        def traverse(node):
            if not node:
                return 0
            r = traverse(node.next)
            if r == -1 or node == self.node or node.next == self.node:
                return -1
            self.maxsum = max(self.maxsum, self.node.val + node.val)
            self.node = self.node.next
            return 0

        traverse(head)
        return self.maxsum
