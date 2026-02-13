class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList: 
    
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    
    def print_list(self):
        
        current = self.head
        while current:
            print(current.data, end='-> ')
            current = current.next
        print("None")
    
    def print_list_reverse(self):
        
        current = self.head
        while current and current.next:
            current = current.next
        
        while current:
            print(current.data, end='-> ')
            current = current.prev
        print("None")
        
        

DLL = DoublyLinkedList()

DLL.insert_at_beginning(40)
DLL.insert_at_beginning(30)
DLL.insert_at_beginning(20)
DLL.insert_at_beginning(10)

DLL.print_list()

DLL.print_list_reverse()