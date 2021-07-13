# A queue is a data structure which contains an ordered set of data.
# Queues provide three methods for interaction:
# Enqueue - adds data to the “back” or end of the queue
# Dequeue - provides and removes data from the “front” or beginning of the queue
# Peek - reveals data from the “front” of the queue without removing it

# This data structure mimics a physical queue of objects like a line of people buying movie tickets. Each person has a name (the data). 
# The first person to enqueue, or get into line, is both at the front and back of the line. As each new person enqueues, they become the new back of the line.
# When the cashier serves someone, they begin at the front of the line. Each person served is dequeued from the front of the line, they purchase a ticket and leave.
# If they just want to know who is next in line, they can peek and get their name without removing them from the queue.
# The first person in the queue is the first to be served. Queues are a First In, First Out or FIFO structure.

# Queues can be implemented using a linked list as the underlying data structure. 
# The front of the queue is equivalent to the head node of a linked list and the back of the queue is equivalent to the tail node.
# Since operations are only allowed affecting the front or back of the queue, any traversal or modification to other nodes within the linked list is disallowed. 
# Since both ends of the queue must be accessible, a reference to both the head node and the tail node must be maintained.
# One last constraint that may be placed on a queue is its length. If a queue has a limit on the amount of data that can be placed into it, it is considered a bounded queue.
# Similar to stacks, attempting to enqueue data onto an already full queue will result in a queue overflow. If you attempt to dequeue data from an empty queue, it will result in a queue underflow.

# We can use Python to build out a Queue class with those three essential queue methods:
# enqueue() which will allow us to add a new node to the tail of the queue
# dequeue() which will allow us to remove a node from the head of the queue and return its value
# peek() which will allow us to view the value of head of the queue without returning it
# We’ll also set up a few helper methods that will help us keep track of the queue size in order to prevent queue “overflow” and “underflow.”

from node import Node
# Create the Queue class below:
class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
    
  def peek(self):
    return self.head.get_value()
 
# Bounded queues require limits on the number of nodes that can be contained, while other queues don’t. 
# To account for this, we will need to make some modifications to our Queue class so that we can keep track of and limit size where needed.
# We’ll be adding two new properties to help us out here:
# A size property to keep track of the queue’s current size
# A max_size property that bounded queues can utilize to limit the total node count
# In addition, we will add three new methods:
# get_size() will return the value of the size property
# has_space() will return True if the queue has space for another node
# is_empty() will return true if the size is 0

from node import Node

class Queue:
  # Add max_size and size properties within __init__():
  def __init__(self, max_size=None):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0
    
  def peek(self):
    if self.size > 0:
      return self.head.get_value()
    else:
      print("Nothing to see here!")
  
  # Define get_size() and has_space() below:
  def get_size(self):
    return self.size
  
  def has_space(self):
    if self.max_size == None:
      return True
    else:
      return self.max_size > self.get_size()
    
  def is_empty(self):
    return self.size == 0
 
# “Enqueue” is a fancy way of saying “add to a queue,” and that is exactly what we’re doing with the enqueue() method.
# There are three scenarios that we are concerned with when adding a node to the queue:
# The queue is empty, so the node we’re adding is both the head and tail of the queue
# The queue has at least one other node, so the added node becomes the new tail
# The queue is full, so the node will not get added because we don’t want queue “overflow”

from node import Node

class Queue:
  def __init__(self, max_size=None):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0
    
  # Add your enqueue method below:
  def enqueue(self, value):
    if self.has_space():
      item_to_add = Node(value)
      print("Adding " + str(item_to_add.get_value()) + " to the queue!")
      if self.is_empty():
        self.head = item_to_add
        self.tail = item_to_add
      else:
        self.tail.set_next_node(item_to_add)
        self.tail = item_to_add
      self.size += 1
    else:
      print("Sorry, no more room!")
    
  def peek(self):
    if self.is_empty():
      print("Nothing to see here!")
    else:
      return self.head.get_value()
  
  def get_size(self):
    return self.size
  
  def has_space(self):
    if self.max_size == None:
      return True
    else:
      return self.max_size > self.get_size()
    
  def is_empty(self):
    return self.size == 0

q = Queue()
q.enqueue("all the fluffy kitties")

# We can add items to the tail of our queue, but we remove them from the head using a method known as dequeue(), which is another way to say “remove from a queue”. 
# Like enqueue(), we care about the size of the queue — but in the other direction, so that we prevent queue “underflow”. 
# After all, you don’t want to remove something that isn’t there!
# As with peek(), our dequeue() method should return the value of the head. Unlike, peek(), dequeue() will also remove the current head and replace it with the following node.

# For dequeue, there are three scenarios that we will take into account:
# The queue is empty, so we cannot remove or return any nodes lest we run into queue “underflow”
# The queue has one node, so when we remove it, the queue will be empty and we need to reset the queue’s head and tail to None
# The queue has more than one node, and we just remove the head node and reset the head to the following node

from node import Node

class Queue:
  def __init__(self, max_size=None):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0
    
  def enqueue(self, value):
    if self.has_space():
      item_to_add = Node(value)
      print("Adding " + str(item_to_add.get_value()) + " to the queue!")
      if self.is_empty():
        self.head = item_to_add
        self.tail = item_to_add
      else:
        self.tail.set_next_node(item_to_add)
        self.tail = item_to_add
      self.size += 1
    else:
      print("Sorry, no more room!")
      
  # Add your dequeue method below:    
  def dequeue(self):
    if self.get_size() > 0:
      item_to_remove = self.head
      print("Removing " + str(item_to_remove.get_value()) + " from the queue!")
      if self.get_size() == 1:
        self.head = None
        self.tail = None
      else:
        self.head = self.head.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This queue is totally empty!")
  
  def peek(self):
    if self.is_empty():
      print("Nothing to see here!")
    else:
      return self.head.get_value()
  
  def get_size(self):
    return self.size
  
  def has_space(self):
    if self.max_size == None:
      return True
    else:
      return self.max_size > self.get_size()
    
  def is_empty(self):
    return self.size == 0

q = Queue()
q.enqueue("some guy with a mustache")
q.dequeue()



