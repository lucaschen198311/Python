class SLNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None
    ##add node from front:
    def add_front(self, val):
        new_node = SLNode(val)
        new_node.next = self.head
        self.head = new_node
        return self
    ##traverse the linked list:
    def traverse(self):
        current_node = self.head
        while current_node != None:
            print(current_node.val)
            current_node = current_node.next
        return self
    ##add node back:
    def add_back(self,val):
        if self.head == None:
            self.add_front(val)
            return self
        new_node = SLNode(val)
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node
        return self
    ##remove node from front:
    def remove_front(self):
        if self.head == None:
            return self
        next_node = self.head.next
        self.head.next = None
        self.head = next_node
        return self
    def remove_back(self):
        if self.head == None:
            return self.head
        if self.head.next == None:
            self.remove_front()
            return self
        current_node = self.head
        while current_node.next.next != None:
            current_node = current_node.next
        current_node.next = None
        return self
    ##remove the 1st node with value ==val:
    def remove_val(self, val):
        if self.head == None:
            return self
        prev_node = self.head
        curr_node = self.head.next
        if prev_node.val == val:
            self.remove_front()
            return self
        if curr_node == None:
            return self 
        while curr_node != None:
            if curr_node.val == val:
                prev_node.next = curr_node.next
                curr_node.next = None
                break
            prev_node = curr_node
            curr_node = curr_node.next
        return self
    ##insert a node with value val as the nth node in the list
    def len_list(self):
        count = 0
        current_node = self.head
        while current_node != None:
            current_node = current_node.next
            count += 1
        return count
    def insert_at(self, val, n):
        len_of_list = self.len_list()
        if n <0 or n > len_of_list:
            return self
        elif n == 0:
            self.add_front(val)
            return self
        elif n == len_of_list:
            self.add_back(val)
            return self
        elif self.head == None:
            return self
        index  = 1
        new_node = SLNode(val)
        curr_node = self.head.next
        prev_node = self.head
        while curr_node != None:
            if index == n:
                prev_node.next = new_node
                new_node.next = curr_node
                break
            index += 1
            prev_node = curr_node
            curr_node = curr_node.next
        return self

my_list = SList().add_front(1).add_front(2).add_front(3).add_front(4).add_front(5).add_back(6).add_back(7).remove_val(5).remove_val(7).remove_val(2).insert_at(8,0).insert_at(9,5).insert_at(5,2).traverse()
