class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class Tree(object):

    def __init__(self):
        self.root = None

    def insert(self, node):
        if self.root is None:
            self.root = node

        else:
            root = self.root
            is_inserted = False
            while not is_inserted:
                if node.value > root.value:
                    if root.right is None:
                        root.right = node
                        is_inserted = True

                    else:
                        root = root.right

                elif node.value < root.value:
                    if root.left is None:
                        root.left = node
                        is_inserted = True

                    else:
                        root = root.left

    def get(self, value):
        if self.root is None:
            return -1

        else:
            current = self.root
            while current:
                if current.value == value:
                    return True

                elif value < current.value:
                    current = current.left

                elif value > current.value:
                    current = current.right
            else:
                return -1

    def traversePreOrder(self, root):
        if root is None:
            return

        print(root.value, end=' ')
        self.traversePreOrder(root.left)
        self.traversePreOrder(root.right)

    # Prints values in ascending order.
    def traverseInOrder(self, root):
        if root is None:
            return

        self.traverseInOrder(root.left)
        print(root.value, end=' ')
        self.traverseInOrder(root.right)

    def traversePostOrder(self, root):
        if root is None:
            return

        self.traversePostOrder(root.left)
        self.traversePostOrder(root.right)
        print(root.value, end=' ')

    def TreeHeight(self, root):
        if root is None:
            return -1

        if (root.left and root.right) is None:
            return 0

        return 1 + max(self.TreeHeight(root.left), self.TreeHeight(root.right))

    def MinIterative(self):
        if self.root is None:
            return -1

        current = self.root
        prev = current

        while current:
            prev = current
            current = current.left

        return prev.value

    def MinRecursive(self, root):
        if (root.left and root.right) is None:
            return root.value

        left = self.MinRecursive(root.left)
        right = self.MinRecursive(root.right)

        return min(min(left, right), root.value)

    def equals(self, first, second):
        if first is None and second is None:
            return True

        if first is not None and second is not None:
            return first.value == second.value and self.equals(first.left, second.left) and self.equals(first.right,
                                                                                                        second.right)

        return False

    def getRoot(self):
        return self.root

    def __isBinarysearchTree(self, root, min, max):
        if root is None:
            return True

        if root.value < min or root.value > max:
            return False

        return self.__isBinarysearchTree(root.left, min, root.value - 1) and self.__isBinarysearchTree(root.right,
                                                                                                       root.value + 1,
                                                                                                       max)

    def isBinarysearchTree(self):
        return self.__isBinarysearchTree(self.getRoot(), self.getMinimum(), self.getMaximum())

    def swap(self):
        self.root.left, self.root.right = self.root.right, self.root.left

    def getMinimum(self):
        if self.root is None:
            return -1

        current = self.root
        while current:
            if current.left is None:
                return current.value
            current = current.left

    def getMaximum(self):
        if self.root is None:
            return -1

        current = self.root
        while current:
            if current.right is None:
                return current.value
            current = current.right

    def Node_at_Kth_distance(self, root, distance, list=None):
        if list is None:
            list = []

        if root is None:
            return -1

        if distance == 0:
            if root is not None:
                list.append(root.value)

        self.Node_at_Kth_distance(root.left, distance - 1, list)
        self.Node_at_Kth_distance(root.right, distance - 1, list)

        return list

    def traverseLevelOrder(self):
        i = 0
        print(self.root.value)
        while i <= self.TreeHeight(self.root):
            i += 1

            for value in self.Node_at_Kth_distance(self.root, i):
                print(value)


e1 = Node(7)
e2 = Node(4)
e3 = Node(9)
e4 = Node(1)
e5 = Node(6)
e6 = Node(8)
e7 = Node(10)

bst = Tree()
bst.insert(e1)
bst.insert(e2)
bst.insert(e3)
bst.insert(e4)
bst.insert(e5)
bst.insert(e6)
bst.insert(e7)
# bst.swap()
# print(bst.isBinarysearchTree())
# print(bst.Node_at_Kth_distance(bst.getRoot(), 0))
# bst.traverseLevelOrder()
# bst.traversePreOrder(bst.getRoot())
bst.traverseInOrder(bst.getRoot())
# bst.traversePostOrder(bst.getRoot())
# print(bst.TreeHeight(bst.getRoot()))
# print(bst.MinIterative())
# print(bst.MinRecursive(bst.getRoot()))
# print(bst.get(6))
# print(bst.get(7))
#
# e8 = Node(7)
# e9 = Node(4)
# e10 = Node(9)
# e11 = Node(1)
# e12 = Node(6)
# e13 = Node(8)
# e14 = Node(10)
#
# bst1 = Tree()
# bst1.insert(e8)
# bst1.insert(e9)
# bst1.insert(e10)
# bst1.insert(e11)
# bst1.insert(e12)
# bst1.insert(e13)
# bst1.insert(e14)
#
# print(bst.equals(bst.getRoot(), bst1.getRoot()))
