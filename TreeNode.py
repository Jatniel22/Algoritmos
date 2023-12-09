class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def build_tree_from_array(arr):
    if not arr:
        raise ValueError("La matriz está vacía. No se puede construir un árbol.")

    root = TreeNode(arr[0])
    nodes = [root]

    for i in range(1, len(arr), 2):
        parent = nodes.pop(0)

        left_value = arr[i]
        if left_value is not None:
            parent.left = TreeNode(left_value)
            nodes.append(parent.left)

        if i + 1 < len(arr):
            right_value = arr[i + 1]
            if right_value is not None:
                parent.right = TreeNode(right_value)
                nodes.append(parent.right)

    return root

def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.key))
        if node.left is not None:
            print_tree(node.left, level + 1, "L--- ")
        if node.right is not None:
            print_tree(node.right, level + 1, "R--- ")

# Ejemplo de matrices
array1 = [1, 2, 3, 4, 5, None, 6, None, None, 7, 8]
array2 = [1, 2, 3, None, 4, None, 5]
array3 = [1, 2, 3, 4, 5, 6]

try:
    tree1 = build_tree_from_array(array1)
    print("Árbol a partir de la matriz 1:")
    print_tree(tree1)

    tree2 = build_tree_from_array(array2)
    print("\nÁrbol a partir de la matriz 2:")
    print_tree(tree2)

    tree3 = build_tree_from_array(array3)
    print("\nÁrbol a partir de la matriz 3:")
    print_tree(tree3)

except ValueError as e:
    print(e)
