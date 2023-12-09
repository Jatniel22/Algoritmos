class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def nodeBalance(self):
        return self._nodeBalance(self.root)

    def _nodeBalance(self, node):
        if node is None:
            return 0
        left_count = self._nodeCount(node.left)
        right_count = self._nodeCount(node.right)
        return right_count - left_count

    def LevelBalance(self):
        return self._LevelBalance(self.root)

    def _LevelBalance(self, node):
        if node is None:
            return 0
        left_levels = self._treeHeight(node.left)
        right_levels = self._treeHeight(node.right)
        return right_levels - left_levels

    def _treeHeight(self, node):
        if node is None:
            return 0
        left_height = self._treeHeight(node.left)
        right_height = self._treeHeight(node.right)
        return max(left_height, right_height) + 1

    def _nodeCount(self, node):
        if node is None:
            return 0
        return self._nodeCount(node.left) + self._nodeCount(node.right) + 1

    def unbalancedNodes(self, by=1):
        result = []
        self._findUnbalancedNodes(self.root, by, result)
        return result

    def _findUnbalancedNodes(self, node, by, result):
        if node is None:
            return
        balance = self._nodeBalance(node)
        level_balance = self._LevelBalance(node)
        if abs(balance) > by or abs(level_balance) > by:
            result.append(node.key)
        self._findUnbalancedNodes(node.left, by, result)
        self._findUnbalancedNodes(node.right, by, result)

# Prueba con listas de claves
keys_list_1 = [10, 5, 15, 2, 7, 12, 17, 1, 3, 6, 8, 11, 13, 16, 18]
keys_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
keys_list_3 = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
keys_list_4 = [5, 3, 7, 2, 4, 6, 8, 1, 9, 10, 11, 12, 13, 14, 15]

# Crear árbol y probar los métodos
bst = BinarySearchTree()
for key in keys_list_1:
    bst.insert(key)

print("Árbol de 15 nodos:")
print("Equilibrio de Nodos:", bst.nodeBalance())
print("Equilibrio de Niveles:", bst.LevelBalance())
print("Claves desequilibradas (by=1):", bst.unbalancedNodes(by=1))
print("Claves desequilibradas (by=2):", bst.unbalancedNodes(by=2))
