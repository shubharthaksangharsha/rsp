from typing import Optional, List

class Node:
    """Node class for Linked List"""
    def __init__(self, data):
        self.data = data
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
    	return self.length 

    def __iter__(self): 
    	curr = self.head 
    	while curr: 
    		yield curr.data 
    		curr = curr.next 
    def __repr__(self):
    	return f"{list(self)}"

    def populate(self, start: int = 1, end: int = 10) -> None:
        """Populate the linked list from start to end (inclusive)"""
        if start > end:
            return
        
        self.head = Node(start)
        self.length = 1
        temp = self.head
        
        for i in range(start + 1, end + 1):
            temp.next = Node(i)
            self.length += 1
            temp = temp.next

    def from_array(self, arr: List[int]) -> None:
        """Convert array to linked list"""
        if not arr:
            return
        
        self.head = Node(arr[0])
        self.length = 1
        temp = self.head
        
        for i in range(1, len(arr)):
            temp.next = Node(arr[i])
            self.length += 1
            temp = temp.next

    def to_array(self) -> List[int]: 
     	"""Convert linked list to array"""
     	result = []
     	temp = self.head 
     	while temp: 
     		result.append(temp.data)
     		temp = temp.next 
     	return result	

    def printlist(self) -> None: 
     	if self.head is None: 
     		print("Empty List")
     		return
     	temp = self.head 
     	while temp: 
     		print(f"{temp.data}", end=" -> " if temp.next else "\n")
     		temp = temp .next 

    def remove_head(self) -> Optional[int]:
        """Remove and return the head value"""
        if self.head is None:
            return None
        
        value = self.head.data
        self.head = self.head.next
        self.length -= 1
        return value

    def remove_tail(self) -> Optional[int]:
        """Remove and return the tail value"""
        if self.head is None:
            return None
        
        if self.head.next is None:
            value = self.head.data
            self.head = None
            self.length -= 1
            return value
        
        temp = self.head
        while temp.next.next:
            temp = temp.next
        
        value = temp.next.data
        temp.next = None
        self.length -= 1
        return value

    def insert_head(self) -> Optional[int]: 
    	if self.head is None: 
    		
    def insert_at(self, position: int) -> Optional[int]: 
    	if position < 0 or position >= self.length or self.head is None: 
    		return None 
    	if position == 0:
    def remove_at(self, position: int) -> Optional[int]:
        """Remove node at position (0-indexed) and return its value"""
        if position < 0 or position >= self.length or self.head is None:
            return None
        
        if position == 0:
            return self.remove_head()
        
        temp = self.head
        for _ in range(position - 1):
            temp = temp.next
        
        if temp.next is None:
            return None
        
        value = temp.next.data
        temp.next = temp.next.next
        self.length -= 1
        return value

    def remove_value(self, value: int) -> bool:
        """Remove first occurrence of value. Returns True if found and removed."""
        if self.head is None:
            return False
        
        if self.head.data == value:
            self.head = self.head.next
            self.length -= 1
            return True
        
        temp = self.head
        while temp.next:
            if temp.next.data == value:
                temp.next = temp.next.next
                self.length -= 1
                return True
            temp = temp.next
        
        return False

    # def insert_at_head(self, value: int) -> None:
    #     """Insert value at the head"""
    #     new_node = Node(value)
    #     new_node.next = self.head
    #     self.head = new_node
    #     self.length += 1

    # def insert_at_tail(self, value: int) -> None:
    #     """Insert value at the tail"""
    #     new_node = Node(value)
        
    #     if self.head is None:
    #         self.head = new_node
    #         self.length += 1
    #         return
        
    #     temp = self.head
    #     while temp.next:
    #         temp = temp.next
        
    #     temp.next = new_node
    #     self.length += 1

    # def insert_at(self, position: int, value: int) -> bool:
    #     """Insert value at position (0-indexed). Returns True if successful."""
    #     if position < 0 or position > self.length:
    #         return False
        
    #     if position == 0:
    #         self.insert_at_head(value)
    #         return True
        
    #     new_node = Node(value)
    #     temp = self.head
        
    #     for _ in range(position - 1):
    #         temp = temp.next
        
    #     new_node.next = temp.next
    #     temp.next = new_node
    #     self.length += 1
    #     return True

    def get(self, position: int) -> Optional[int]:
        """Get value at position (0-indexed)"""
        if position < 0 or position >= self.length or self.head is None:
            return None
        
        temp = self.head
        for _ in range(position):
            temp = temp.next
        
        return temp.data

    def find(self, value: int) -> int:
        """Find position of first occurrence of value. Returns -1 if not found."""
        if self.head is None:
            return -1
        
        temp = self.head
        position = 0
        
        while temp:
            if temp.data == value:
                return position
            temp = temp.next
            position += 1
        
        return -1

    def reverse(self) -> None:
        """Reverse the linked list in place"""
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev

    def is_empty(self) -> bool:
        """Check if list is empty"""
        return self.head is None

    def clear(self) -> None:
        """Clear the list"""
        self.head = None
        self.length = 0


if __name__ == "__main__":
    ll = MyLinkedList()
    ll.populate(1, 5)
    print(ll)
    print(list(ll))
    print(len(ll))