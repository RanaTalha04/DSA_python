class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append_at_beggining(self, data):

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
    
    def append_at_any_point(self, data, position):
        
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        
        elif position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            
            current = self.head
            count = 0
            
            while count < position - 1 and current.next is not None:
                current = current.next
                count +=1
            
            new_node.next = current.next
            current.next = new_node
             
    def delete_at_beggining(self):

        if self.head is None:
            print("List is empty")
        else:
            self.head = self.head.next

    def delete_at_any_point(self, data):

        if self.head is None:
            print("List is Empth")
        else:

            current = self.head

            while current.next.data != data and current.next is not None:
                current = current.next
            if current.next is not None:
                current.next = current.next.next
            else:
                print("Data not found in the list")
                
    def delete_at_end(self):
        current = self.head

        if self.head is None:
            print("List is empty")

        elif self.head.next is None:
            self.head = None

        else:
            while current.next.next is not None:
                current = current.next
            current.next = None

    def print_list(self):

        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("Null")


LL = LinkedList()
LL.append_at_beggining(30)
LL.append_at_beggining(20)
LL.append_at_beggining(10)
print("Linked List after appending at beginning:")
LL.print_list()

LL.append_at_end(40)
LL.append_at_end(50)
LL.append_at_end(60)
print("Linked List after appending at end:")
LL.print_list()

LL.append_at_any_point(25, 2)
LL.append_at_any_point(5, 0)
print("Linked List after appending at any point:")
LL.print_list()

LL.delete_at_beggining()
print("Linked List after deleting at beginning:")
LL.print_list()

LL.delete_at_any_point(40)
print("Linked List after deleting at any point:")
LL.print_list()

LL.delete_at_end()
print("Linked List after deleting at end:")
LL.print_list()
