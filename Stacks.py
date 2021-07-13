# A stack is a data structure which contains an ordered set of data.
# Stacks provide three methods for interaction:
# Push - adds data to the “top” of the stack
# Pop - returns and removes data from the “top” of the stack
# Peek - returns data from the “top” of the stack without removing it

# Stacks mimic a physical “stack” of objects. Consider a set of gym weights.
# Each plate has a weight (the data). The first plate you add, or push, onto the floor is both the bottom and top of the stack. Each weight added becomes the new top of the stack.
# At any point, the only weight you can remove, or pop, from the stack is the top one. You can peek and read the top weight without removing it from the stack.
# The last plate that you put down becomes the first, and only, one that you can access. This is a Last In, First Out or LIFO structure. 
# A less frequently used term is First In, Last Out, or FILO.

# Stacks can be implemented using a linked list as the underlying data structure because it’s more efficient than a list or array.
# Depending on the implementation, the top of the stack is equivalent to the head node of a linked list and the bottom of the stack is equivalent to the tail node.
# A constraint that may be placed on a stack is its size. This is done to limit and quantify the resources the data structure will take up when it is “full”.
# Attempting to push data onto an already full stack will result in a stack overflow. Similarly, if you attempt to pop data from an empty stack, it will result in a stack underflow.

# We also need to consider the stack’s size and tweak our methods a bit so that our stack does not “overflow”.
from node import Node

# Add your Stack class below:
class Stack:
  def __init__(self):
    self.top_item = None
    
  def peek(self):
    return self.top_item.get_value()
  
# The stack’s push() and pop() methods are our tools to add and remove items from it. pop() additionally returns the value of the item it is removing. 
# Keep in mind that we can only make modifications to the top of the stack.

from node import Node

class Stack:
  def __init__(self):
    self.top_item = None
  
  # Define your push() and pop() methods below:

  def push(self, value):
    item = Node(value)
    item.set_next_node(self.top_item)
    self.top_item = item

  def pop(self):
    item_to_remove = self.top_item
    self.top_item = item_to_remove.get_next_node()
    return item_to_remove.get_value()
  
  def peek(self):
    return self.top_item.get_value()
 
# With stacks, size matters. If we’re not careful, we can accidentally over-fill them with data. 
# Since we don’t want any stack overflow, we need to go back and make a few modifications to our methods that help us track and limit the stack size so we can keep our stacks healthy.

from node import Node

class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.limit = limit
    self.size = 0
  
  def push(self, value):
    item = Node(value)
    item.set_next_node(self.top_item)
    self.top_item = item

  def pop(self):
    if self.size > 0:
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      # Decrement the stack size here:
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This stack is totally empty.")
  
  def peek(self):
    if self.size > 0:
      return self.top_item.get_value()
    else:
      print("Nothing to see here!")
 
from node import Node

class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit
  
  def push(self, value):
    if self.has_space():
      
    	item = Node(value)
    	item.set_next_node(self.top_item)
    	self.top_item = item
    # Increment stack size by 1 here:
    	self.size += 1
    else:
      print("All out of space!")
        

  def pop(self):
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This stack is totally empty.")
  
  def peek(self):
    if not self.is_empty():
	    return self.top_item.get_value()
    else:
      print("Nothing to see here!")
      
  # Define has_space() and is_empty() below:
  def has_space(self):
    return self.limit > self.size
  
  def is_empty(self):
    return self.size == 0
 
