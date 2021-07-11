# Nodes are the fundamental building blocks of many computer science data structures. They form the basis for linked lists, stacks, queues, trees, and more.
# An individual node contains data and links to other nodes. Each data structure adds additional constraints or behavior to these features to create the desired structure.
# The data contained within a node can be a variety of types, depending on the language you are using.
# The link or links within the node are sometimes referred to as pointers. This is because they “point” to another node.
# Typically, data structures implement nodes with one or more links. If these links are null, it denotes that you have reached the end of the particular node or link path you were previously following.
# Often, due to the data structure, nodes may only be linked to from a single other node. This makes it very important to consider how you implement modifying or removing nodes from a data structure.
# If you inadvertently remove the single link to a node, that node’s data and any linked nodes could be “lost” to your application. 
# When this happens to a node, it is called an orphaned node.

# Begin by creating a new class, Node. Add an .__init__() method in the Node class that takes a value and an optional link_node (default should be None). 
# These should be saved to the corresponding self properties (self.value and self.link_node).

class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
 
# We need methods to access the data and link within the node. For this, we will use two getters, .get_value() and .get_link_node().
# These should each return their corresponding value on the self object.

  # Define your get_value and get_link_node methods below:
  def get_value(self):
    return self.value
  
  def get_link_node(self):
    return self.link_node
 
# We are only allowing the value of the node to be set upon creation. 
# However, we want to allow updating the link of the node. For this, we will use a setter to modify the self.link_node attribute.
# The method should be called .set_link_node() and should take link_node as an argument. It should then update the self.link_node attribute as appropriate.

  # Define your set_link_node method below:
  def set_link_node(self, link_node):
    self.link_node = link_node
 
