class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = CircularNode(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node

    def delete_node(self, data):
        if not self.head:
            return

        temp = self.head
        prev = None
        while True:
            if temp.data == data:
                if temp == self.head: 
                    if temp.next == self.head:  
                        self.head = None
                    else:
                        prev = self.head
                        while prev.next != self.head:
                            prev = prev.next
                        prev.next = temp.next
                        self.head = temp.next
                else:
                    prev.next = temp.next
                return
            
            prev = temp
            temp = temp.next

            if temp == self.head:
                break  

    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print()

# Example usage:
cll = CircularLinkedList()
cll.insert_at_beginning(10)
cll.insert_at_beginning(20)
cll.insert_at_beginning(30)

cll.display()  

cll.delete_node(20)
cll.display()  
