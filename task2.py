
class Node:
   def __init__(self, data):
     self._name = data
     self.next = None
     self.prev = None

class MyCirckeQueue:
  def __init__(self, size):
    self.items = [None] * size
    self.size = size
    self.head = None
    self.tail = None

  def isEmpty(self):
    if self.size == 0: return True
    return False

  def push(self, value):
    if self.size == 0:
      self.head = self.tail = 0
      self.items[0] = Node(value)
    self.items[self.tail] = Node(value)     
    self.tail += 1
    self.size += 1


def main():
  q = MyCirckeQueue

if __name__ == "__main__":
    main()