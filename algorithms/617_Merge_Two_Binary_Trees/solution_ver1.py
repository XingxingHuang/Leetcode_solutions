# https://leetcode.com/problems/merge-two-binary-trees/description/
import timeit

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        ret_tree = None
        if not t1 and not t2:
            pass
        elif not t1:
            ret_tree = t2
        elif not t2:
            ret_tree = t1
        else:
            ret_tree = TreeNode(t1.val + t2.val)
            ret_tree.left = self.mergeTrees(t1.left, t2.left)
            ret_tree.right = self.mergeTrees(t1.right, t2.right)
        return ret_tree

def run():
    t1 = TreeNode(1, TreeNode(3, TreeNode(5), None), TreeNode(2))
    t2 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))
    Solution().mergeTrees(t1, t2)

def main():
    timer = timeit.Timer('run()', "from __main__ import run")
    t = timer.timeit(1000)
    print(t)

if __name__ == '__main__':
    main()
