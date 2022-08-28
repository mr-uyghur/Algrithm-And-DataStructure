# Define your "TreeNode" Python class below
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        print("Adding " + child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        print("Removing" + child_node.value + "from" + self.value)
        # new_children = []

        for item in self.children:

            # add items from the original children of node
            # to the new children list,
            # only if the index item is not equal to the child_node we removing
            # if item != child_node:
            #     new_children.append(item)

            # self.children = new_children
            
            #updated remove function with list comprehension
            self.children = [
                item for item in self.children if item != child_node
            ]


root = TreeNode("I am Root")
child = TreeNode("A wee sappling")
bad_seed = TreeNode("Root Rot!")

root.add_child(child)
root.add_child(bad_seed)
root.remove_child(bad_seed)
