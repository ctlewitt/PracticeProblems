# dynamic programming algorithm to determine best houses in a tree to rob, where you cannot rob a house and it's child(ren)
# you can only rob a house or its children or the alarms will go off

optvals = None


class Node:
    left = None
    right = None
    val = -1

    def __init__(self, val, left, right):
        self.left = left
        self.right = right
        self.val = val


def rob_houses(root):
    global optvals
    optvals = copy(root)
    return rob_houses_aux(root, optvals)


def copy(root):
    if not root:
        return None
    else:
        return Node(-1, copy(root.left), copy(root.right))


def rob_houses_aux(root, optvals):
    if not root:
        return 0
    if optvals.val != -1:
        return optvals.val
    else:
        best_val = max(root.val + with_val(root, optvals), without_val(root, optvals))
        optvals.val = best_val
        return best_val


def with_val(root, optvals):
    total = 0
    if root.left:
        if root.left.left:
            total += rob_houses_aux(root.left.left, optvals.left.left)
        if root.left.right:
            total += rob_houses_aux(root.left.right, optvals.left.right)
    if root.right:
        if root.right.left:
            total += rob_houses_aux(root.right.left, optvals.right.left)
        if root.right.right:
            total += rob_houses_aux(root.right.right, optvals.right.right)
    return total

def without_val(root, optvals):
    total = 0
    if root.right:
        total += rob_houses_aux(root.right, optvals.right)
    if root.left:
        total += rob_houses_aux(root.left, optvals.left)
    return total

my_root = Node(3, Node(5, Node(100, None, None), Node(2, None, None)), Node(7, Node(4, Node(15, Node(2, None, Node(30, None, None)), None), None), None))
print(rob_houses(my_root))
print(rob_houses(Node(3, None, None)))
print(rob_houses(None))