import json
from tree import PoliceTreeNode
from tree import infix_order

with open('myTree.json', 'r') as outfile:
    file_data = json.load(outfile)
    outfile.close()

json_nodes = file_data["Nodes"]
print(len(json_nodes))
print(json_nodes[16])


def rebuild_tree(node, json_nodes):
    if node["left"] is None:
        left_node = None
    else:
        left_node = rebuild_tree(json_nodes[int(node["left"]) - 1], json_nodes)

    if node["right"] is None:
        right_node = None
    else:
        right_node = rebuild_tree(json_nodes[int(node["right"]) - 1], json_nodes)

    return PoliceTreeNode(key=node["key"], val=node["val"], left=left_node, right=right_node)


root = rebuild_tree(json_nodes[16], json_nodes)
infix_order(root)