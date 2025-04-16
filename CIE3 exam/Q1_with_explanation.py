          # class for the nodes in the circular linked list
class CircularNode:
    def __init__(self, data):
        self.data = data  # Store the data in node
        self.next = None  # making the next pointer as None

# class for circular linked list
class CircularLinkedList:
    def __init__(self):
        self.head = None  # making the head of the list as None

    # Function to insert a new node at the beginning of the list
    def insert_at_beginning(self, data):
        new_node = CircularNode(data)  # Create a new node with the given data
        
        if not self.head:  # If the list is empty
            new_node.next = new_node  # Point the new node to itself
            self.head = new_node  # Set the head to the new node
        else:
            temp = self.head  # Temporary pointer to traverse the list
            while temp.next != self.head:  # Find the last node which will point back to head
                temp = temp.next
            temp.next = new_node  # Point last node to new node
            new_node.next = self.head  # New node points to the current head
            self.head = new_node  # Update head to new node

    # Function to delete a node 
    def delete_node(self, data):
        if not self.head:  # If list is empty, nothing to delete
            return

        temp = self.head  # Temporary pointer for traversal
        prev = None  # Pointer to track previous node
        
        while True:  # Loop till traversal completes or the node is found
            if temp.data == data:  # If the current node matches the target value
                if temp == self.head:  # If the node to be deleted is the head
                    if temp.next == self.head:  # If it is the only node in the list
                        self.head = None  # Empty the list
                    else:
                        prev = self.head
                        while prev.next != self.head:  # Find last node
                            prev = prev.next
                        prev.next = temp.next  # Update last node's next pointer
                        self.head = temp.next  # Move head to next node
                else:
                    prev.next = temp.next  # Remove the current node by updating previous node's next
                return
            
            prev = temp  # Move previous pointer forward
            temp = temp.next  # Move current pointer forward

            if temp == self.head:  # If we have traversed the whole list
                break  # Exit loop as the element was not found

    # Function to display the circular linked list
    def display(self):
        if not self.head:  # If the list is empty
            print("List is empty")  # Display message
            return
        temp = self.head  # Temporary pointer for traversal
        while True:
            print(temp.data, end=" -> ")  # Print current node data
            temp = temp.next  # Move to next node
            if temp == self.head:  # Stop when we reach the head again
                break
        print()  # Print new line

# Example usage of the CircularLinkedList class
cll = CircularLinkedList()  
cll.insert_at_beginning(10) 
cll.insert_at_beginning(20)  
cll.insert_at_beginning(30)  

cll.display()  

cll.delete_node(20)  
cll.display()  
