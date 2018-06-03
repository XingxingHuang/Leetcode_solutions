# https://leetcode.com/problems/construct-string-from-binary-tree/description/

class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        [1,2,3] -> 1(2)(3)  --> if both child node exist
            return t.val(tree2str(t.left)(tree2str(t.right)
        [1,null,2] -> 1()(2) --> if only left child node does not exist () for it can not be omitted
            return t.val()(tree2str(t.right)
        [1,2,3,4,5] -> 1(2(4)(5))(3) the child nodes for 3 both don't exist, () are omitted for both
            return t.val



        """
        # if not t:
        #     return ""
        if not t.left and not t.right:
            return "{}".format(t.val)
        if not t.right:
            return '{}({})'.format(t.val, self.tree2str(t.left))
        return '{}({})({})'.format(t.val, self.tree2str(t.left), self.tree2str(t.right))

