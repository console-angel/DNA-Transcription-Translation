# Class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Class Linked List
class LinkedList:
    def __init__(self):
        self.head = None # Starts as empty list

    def appendItem(self, item) -> None:
        """Adds a new item to linked list"""

        newNode = Node(item) # create new node

        # If List Is Empty Append Single Item
        if self.isEmpty():
            self.head = newNode # head = Node()
            return

        # Otherwise, Traverse Through & Append Item At End
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode

    def prepend(self, item) -> None:
        """Adds a new item to beginning of linked list"""
        newNode = Node(item) # create new node
        newNode.next = self.head # set next to prev node
        self.head = newNode # set head to new node

    def delete(self, item) -> None:
        """Deletes a selected item if it exists"""

        # Store Head Node
        temp = self.head

        # Check If List Is Empty
        if self.isEmpty():
            print(f"{item}. Does Not Exist!")
            return
        
        # Check If Head Node Contains Item
        if not self.isEmpty():
            if (temp.data.lower() == item.lower()):
                self.head = temp.next
                temp = None
                return   
        
        # Check First Occurence of Item
        while (temp is not None):
            if temp.data.lower() == item.lower():
                break
            prev = temp
            temp = temp.next

        # If Key Is Not Present In List
        if (temp == None):
            return
        
        # Unlink The Node From Linked List
        prev.next = temp.next
        temp = None

    def display(self) -> None:
        """Prints the linked list in a readable format"""
        current = self.head
        elements = []

        while current:
            elements.append(str(current.data))
            current = current.next

        print(" -> ".join(elements))

    def isEmpty(self) -> bool:
        """Returns True or False if head pointer is null"""
        return self.head == None
