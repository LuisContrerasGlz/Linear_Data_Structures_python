# Linked lists are one of the basic data structures used in computer science. They have many direct applications and serve as the foundation for more complex data structures.
# The list is comprised of a series of nodes.
# The head node is the node at the beginning of the list. Each node contains data and a link (or pointer) to the next node in the list. 
# The list is terminated when a node’s link is null. This is called the tail node.
# Consider a one-way air travel itinerary. The trip could involve traveling through several airports (nodes) connected by air travel segments (links). 
# In this example, the initial departure city is the head node and the final arrival city is the tail node.
# Since the nodes use links to denote the next node in the sequence, the nodes are not required to be sequentially located in memory. 
# These links also allow for quick insertion and removal of nodes 

# Common operations on a linked list may include:

# adding nodes
# removing nodes
# finding a node
# traversing (or traveling through) the linked list

# Linked lists typically contain unidirectional links (next node), but some implementations make use of bidirectional links (next and previous nodes).
# With linked lists, because nodes are linked to from only one other node, you can’t just go adding and removing nodes willy-nilly without doing a bit of maintenance.

# Adding a new node.
# Adding a new node to the beginning of the list requires you to link your new node to the current head node. 
# This way, you maintain your connection with the following nodes in the list.

# Removing a node
# If you accidentally remove the single link to a node, that node’s data and any following nodes could be lost to your application, leaving you with orphaned nodes.
# To properly maintain the list when removing a node from the middle of a linked list, you need to be sure to adjust the link on the previous node so that it points to the following node.
# Depending on the language, nodes which are not referenced are removed automatically. “Removing” a node is equivalent to removing all references to the node.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Let’s implement a linked list in Python. As you might recall, each linked list is a sequential chain of nodes. 
# So before we start building out the LinkedList itself, we want to build up a Node class in Python that we can use to build our data containers.
# Remember that a node contains two elements: 1. data 2. a link to the next node
# Note: Because the workspace is set up with spaces instead of tabs, you will need to use spaces to prevent Python from throwing an error. 

class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node
    
my_node = Node(44)
print(my_node.get_value())

# With the Node in hand, we can start building the actual linked list. Depending on the end-use of the linked list, a variety of methods can be defined.
# For our use, we want to be able to:
# get the head node of the list (it’s like peeking at the first item in line)
# add a new node to the beginning of the list
# print out the list values in order
# remove a node that has a particular value

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
   
# Next up, we’ll define methods for our LinkedList class that allow us to:
# insert a new head node
# return all the nodes in the list as a string so we can print them out in the terminal!

# We’ll define methods for our LinkedList class that allow us to:
# insert a new head node
# return all the nodes in the list as a string so we can print them out in the terminal!

# We'll be using our Node class
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

# Our LinkedList class
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
# Add your insert_beginning and stringify_list methods below:

  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  

# Test your code by uncommenting the statements below - did your list print to the terminal?
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
print(ll.stringify_list())

# The final use case we mentioned was the ability to remove an arbitrary node with a particular value. This is slightly more complex, since a couple of special cases need to be handled.
# Consider the following list:
# a -> b -> c
# If node b is removed from the list, the new list should be:
# a -> c
# We need to update the link within the a node to match what b was pointing to prior to removing it from the linked list.
# Lucky for us, in Python, nodes which are not referenced will be removed for us automatically. 
# If we take care of the references, b will be “removed” for us in a process called Garbage Collection.

class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

# Our LinkedList class
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  # Define your remove_node method below:
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node
