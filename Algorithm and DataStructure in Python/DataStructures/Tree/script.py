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


            # add items from the original children of node
            # to the new children list,
            # only if the index item is not equal to the child_node we removing
            # if item != child_node:
            #     new_children.append(item)

            # self.children = new_children

            # updated remove function with list comprehension
        self.children = [
                item for item in self.children if item != child_node
            ]
    def traverse(self):
         # moves through each node referenced from self downwards
        print("Traversing...")
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children

root = TreeNode("CEO")
first_child = TreeNode("Vice-President")
second_child = TreeNode("Head of Marketing")
third_child = TreeNode("Marketing Assistant")

root.add_child(first_child)
root.add_child(second_child)
second_child.add_child(third_child)
root.traverse()
