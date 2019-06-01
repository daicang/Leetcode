# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        stack = []
        num = ''
        root = None

        for idx, char in enumerate(s):
            if char == '(':
                # Start mark of a child, left or right
                pass

            elif char == ')':
                # End mark of a child
                stack.pop()

            else:
                num += char
                if idx+1 >= len(s) or not s[idx+1].isdigit():
                    # End of number seq, create new node
                    curr = TreeNode(int(num))
                    num = ''

                    if not stack:
                        # This node is root
                        root = curr
                    else:
                        # Link this node with its parent
                        parent = stack[-1]
                        if not parent.left:
                            parent.left = curr
                        else:
                            parent.right = curr

                    stack.append(curr)

        return root

s = Solution()
print(s.str2tree("4(2(3)(1))(6(5))"))
