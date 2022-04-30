from db import get_db
from datetime import date
import json

class PoliceTreeNode:
    def __init__(self, key=0, val=0, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


def generate_tree():
    db = get_db()
    records = db.execute(
        'select * from police'
    ).fetchall()

    print(records)
    root = generate_root(records)
    pointer = root

    for record in records:
        key = record["district"]
        if key == "Headquarters" or key == "18":
            pass
        else:
            while(True):
                if int(key) < pointer.key:
                    if pointer.left:
                        pointer = pointer.left
                    else:
                        pointer.left = PoliceTreeNode(int(key), record)
                        pointer = root
                        break
                else:
                    if pointer.right:
                        pointer = pointer.right
                    else:
                        pointer.right = PoliceTreeNode(int(key), record)
                        pointer = root
                        break

    return root


def generate_root(records):
    root = PoliceTreeNode()
    for record in records:
        if record["district"] == "Headquarters":
            pass
        else:
            root = PoliceTreeNode(key=int(record["district"]), val=record, left=None, right=None)
            break

    return root


def infix_order(root):
    if root.left:
        infix_order(root.left)

    print("key:" + str(root.key))

    if root.right:
        infix_order(root.right)


def save_sub_trees(tree, file):
    if tree.left is None and tree.right is None:
        file.write("\nLeaf\n")
        for col in tree.val:
            file.write("{}\n".format(col))

    else:
        file.write("\nInternal node\n")
        for col in tree.val:
            file.write("{}\n".format(col))

        if tree.left is None and tree.right:
            save_sub_trees(tree.right, file)
        elif tree.left and tree.right is None:
            save_sub_trees(tree.left, file)
        else:
            save_sub_trees(tree.left, file)
            save_sub_trees(tree.right, file)


def save_tree(tree, tree_file):
    file = open(tree_file, "w+")
    file.write("Trees storage\n")

    today = date.today()
    file.write(today.strftime("%B %d, %Y") + "\n")

    save_sub_trees(tree, file)
    file.close()


def json_tree(tree, outfile, file_data):
    if tree.left:
        json_tree(tree.left, outfile, file_data)

    if tree.left is None:
        left = None
    else:
        left = tree.left.key

    if tree.right is None:
        right = None
    else:
        right = tree.right.key

    record = {
        "key": tree.key,
        "left": left,
        "right": right,
        "val": {
            "name": tree.val["name"],
            "address": tree.val["address"],
            "city": tree.val["city"],
            "state": tree.val["state"],
            "zip": tree.val["zip"],
            "website": tree.val["website"],
            "phone": tree.val["phone"],
            "fax": tree.val["fax"],
            "tty": tree.val["tty"],
            "x": tree.val["x"],
            "y": tree.val["y"],
            "latitude": tree.val["latitude"],
            "longitude": tree.val["longitude"]
        }
    }

    file_data["Nodes"].append(record)
    outfile.seek(0)
    json.dump(file_data, outfile, indent=4)

    if tree.right:
        json_tree(tree.right, outfile, file_data)


def get_tree():
    tree = generate_tree()
    save_tree(tree, 'myTree.txt')

    data = {
        "Nodes": []
    }

    with open('myTree.json', 'w+') as outfile:
        json.dump(data, outfile, indent=4)
        outfile.close()

    with open('myTree.json', 'r+') as outfile:
        file_data = json.load(outfile)
        json_tree(tree, outfile, file_data)
        outfile.close()

    infix_order(tree)
