class Codec:
    def serialize(self, root):
        out = []
        def preorder(root,out):   
            if not root: return 
            out += [str(root.val)]
            preorder(root.left,out)
            preorder(root.right,out)
        preorder(root,out)
        return ','.join(out)
        
    def deserialize(self, data):
        if not data:
            return None
        def buildTree(pre_o, in_o):
            if not pre_o:
                return None
            mid = pre_o[0]
            i = in_o.index(mid)
            root = TreeNode(mid)
            root.left = buildTree(pre_o[1:i + 1], in_o[:i])
            root.right = buildTree(pre_o[i + 1:], in_o[i + 1:])
            return root
        pre_o = list(map(int, data.split(',')))
        in_o = sorted(pre_o)
        return buildTree(pre_o, in_o)
