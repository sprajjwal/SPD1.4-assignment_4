def middle_node(ll_list):
  it = ll_list.head
	mid_ptr = ll_list.head
	
	while it.next != None:
		for i in range(2):
			if it.next != None:
				it = it.next
		mid_ptr = mid_ptr.next
  
  return mid_ptr

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

if __name__ == '__main__':
  node1 = Node(2)
  node1.next = Node(3)
  node1.next.next = Node(5)
  ll = LinkedList
  ll.head = node1

  mid = middle_node(ll)
  print(mid.data)
