# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        m=Counter()
        def dsf(r,l):
            if not r: return
            m[l]+= r.val
            dsf (r.left, l+1)
            dsf (r.right, l+1)
        dsf(root,0)

        def dfs(r,l,curr):
            sumofcousins = m[l +1 ] -(r.left.val if r.left else 0) - (r.right.val if r.right else 0)

            if r.left:
                curr.left= TreeNode(sumofcousins)
                dfs(r.left,l+1,curr.left)

            if r.right:
                curr.right = TreeNode(sumofcousins)
                dfs(r.right,l+1,curr.right)
            return curr
        return dfs(root,0,TreeNode(0))