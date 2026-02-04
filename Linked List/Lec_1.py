class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            
    def append_at_end(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head 
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("Null")



LL = LinkedList()

LL.append_at_beginning(30)
LL.append_at_beginning(20)
LL.append_at_beginning(10)

LL.print_list()

LL.append_at_end(40)
LL.append_at_end(50)
LL.append_at_end(60)

LL.print_list()