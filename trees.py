
class BinaryTreeSolutions():
    def __init___():
        '''
        binary tree related problems on leetcode
        '''

    def isBalanced(self, root):
        '''
        balanced tree is one where height of left and right branch of each node differ by no more than 1

        input: tree node; root node of tree
        output: bool; True the tree is balanced, else False
        '''

        def helper(node):
            if node is None:
                return True, 0

            isLeftBalanced, leftHeight = helper(node.left)
            isRightBalanced, rightHeight = helper(node.right)

            isNodeBalanced = isLeftBalanced and isRightBalanced and (abs(leftHeight - rightHeight) <= 1)
            nodeHeight = max(leftHeight, rightHeight) + 1

            return isNodeBalanced, nodeHeight
        
        return helper(root)[0]

    def isSymmetric(self, root):
        '''
        input: tree node; root node of tree
        output: bool; True the tree is symetric, else False
        '''

        def helper(left, right):
            if left is None and right is None:
                return True
            if left and right:
                return (left.val == right.val) and helper(left.left, right.right) and helper(left.right, right.left)
            
            return False
        
        def helperIterator(left, right):
            stack = [left, right]
            while stack:
                t1 = stack.pop()
                t2 = stack.pop()
                if t1 is None and t2 is None:
                    return True
                if t1 is None or t2 is None:
                    return False
                if t1.val != t2.val: 
                    return False
                stack.append(t1.left)
                stack.append(t2.right)
                stack.append(t1.right)
                stack.append(t2.left)
            
            return True         
        
        return helper(root)

    def binaryTreeTraverse(self, root):
        '''
        traverse all binary tree nodes
        return: list of node value in order (left -> mid -> right)
        '''
        if root is None:
            return []
        else:
            self.binaryTreeTraverse(root.left) + [root.val] + self.binaryTreeTraverse(root.right)

    def BTTIterator(self, root):
        '''
        traverse all binary tree nodes using iteration
        '''
        self.stack = []

        def findLeftMost(node):
            if node is None:
                return
            else:
                self.stack.append(node)
                findLeftMost(node.left)

        def getNext():
            node = self.stack.pop()
            if node.right:
                findLeftMost(node.right)
            return node

        findLeftMost(root)      
        ans = []
        while self.stack:
            node = getNext()
            ans.append(node.val)
        
        return ans




