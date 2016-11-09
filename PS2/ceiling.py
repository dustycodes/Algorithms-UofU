#!/usr/bin/python3

# Sample Input 1
# 5 3
# 2 7 1
# 3 1 4
# 1 5 9
# 2 6 5
# 9 7 3
# Sample Output 1
# 4
#
# Sample Input 2
# 3 4
# 3 1 2 40000
# 3 4 2 1
# 33 42 17 23
# Sample Output 2
# 2


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Read in the first line
it = 0
shapes = []

number_of_prototypes, number_of_layers = map(int, raw_input().split())

# Read in number_of_prototypes lines with number_of_layers numbers/line
while it < number_of_prototypes:
    it += 1
    prototype = map(int, raw_input().split())

    # create BST from prototype
    root = Node(prototype[0])
    bst_it = 1
    shape = []
    while bst_it < number_of_layers:

        node = Node(prototype[bst_it])
        node_string = ""
        bst_it += 1
        current = root
        # insert node in BST
        while True:
            if current.value > node.value:
                if current.left is None:
                    current.left = node
                    node_string += "L"
                    break
                else:
                    current = current.left
                    node_string += "L"
                    continue
            elif current.value < node.value:
                if current.right is None:
                    current.right = node
                    node_string += "R"
                    break
                else:
                    current = current.right
                    node_string += "R"
                    continue
            else:
                break

        shape.append(node_string)

    shape.sort()
    if ((shape in shapes) is False):
        shapes.append(shape)


print(len(shapes))
