class BinNode:
    def __init__(self, value):
        self.left: BinNode = None
        self.right: BinNode = None
        self.value = value


class BinTree:
    
    def __init__(self):
        self.root: BinNode = None

    def count(self) -> int:
        if self.root is not None:
            self._count(self.root)
        else:
            return 0

    def _count(self, node: BinNode) -> int:
        if node is not None:
            count = 1
            count += self._count(node.left)
            count += self._count(node.right)
        return 0

    def insert(self, new_node: BinNode) -> bool:
        if new_node is not None:
            if self.root is None:
                self.root = new_node
                return True
            else:
                return self._insert(self.root, new_node)
        return False

    def _insert(self, curr_node: BinNode, new_node: BinNode) -> bool:
        if new_node.value < curr_node.value:
            if curr_node.left is not None:
                return self._insert(curr_node.left, new_node)
            curr_node.left = new_node
            return True
        elif new_node.value > curr_node.value:
            if curr_node.right is not None:
                return self._insert(curr_node.right, new_node)
            curr_node.right = new_node
            return True
        else:
            return False
    
    def max(self) -> BinNode:
        if self.root is not None:
            return self._max(self.root)
        else:
            return None
    
    def _max(self, root_node: BinNode) -> BinNode:
        if root_node.right is not None:
            return self._max(root_node.right)
        else:
            return root_node

    def min(self) -> BinNode:
        if self.root is not None:
            return self._min(self.root)
        else:
            return None
    
    def _min(self, root_node: BinNode) -> BinNode:
        if root_node.left is not None:
            return self._min(root_node.left)
        else:
            return root_node

    def delete(self, value) -> BinNode:
        if self.root is not None:
            if self.root.value == value:
                old_root = self.root
                self.root = self._left_rotate_max(self.root.left)
                self.root.right = old_root.right
                return old_root
            return self._delete(value, self.root)
        return None

    def _delete(self, value, curr_node: BinNode) -> BinNode:
        if value < curr_node.value:
            if curr_node.left is not None:
                if curr_node.left.value == value:
                    old_left = curr_node.left
                    curr_node.left = self._left_rotate_max(curr_node.left.left)
                    return old_left
                return self._delete(curr_node.left)
        elif value > curr_node.value:
            if curr_node.right is not None:
                if curr_node.right.value == value:
                    old_right = curr_node.right
                    curr_node.right = self._right_rotate_min(curr_node.right.right)
                    return old_right
                return self._delete(curr_node.right)
        return None

    def _left_rotate_max(self, top_node: BinNode) -> BinNode:
        if top_node is None:
            return None
        if top_node.right is None:
            return top_node
        else:
            curr = top_node
            while curr.right.right is not None:
                curr = curr.right
            new_top = curr.right
            curr.right = new_top.left
            new_top.left = top_node
            return new_top

    def _right_rotate_min(self, top_node: BinNode) -> BinNode:
        if top_node is None:
            return None
        if top_node.left is None:
            return top_node.right
        else:
            curr = top_node
            while curr.left.left is not None:
                curr = curr.left
            new_top = curr.left
            curr.left = new_top.right
            new_top.right = curr
            new_top.left = top_node
            return new_top

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)
        else:
            print("None")
    
    def _print_tree(self, node: BinNode):
        if node is None:
            return
        self._print_tree(node.left)
        print("{} ".format(node.value))
        self._print_tree(node.right)