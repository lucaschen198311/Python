##Doulble linked list class (not circular)
class DLNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DLList:
    def __init__(self):
        self.head = None
    ##traverse: reach the last node of list:
    def traverse(self):
        curr_node = self.head
        while curr_node!= None:
            print(curr_node.val)
            curr_node = curr_node.next
        return self
    def find_end(self):
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
        return curr_node
    def add_front(self,val):
        new_node = DLNode(val)
        if self.head == None:
            self.head = new_node
            return self
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        return self
    ##add new node to end:
    def add_back(self, val):
        if self.head == None:
            self.add_front(val)
        last_node = self.find_end()
        new_node  =DLNode(val)
        last_node.next = new_node
        new_node.prev = last_node
        return self
    ##remove node from front:
    def remove_front(self):
        if self.head == None:
            return self
        if self.head.next == None:
            self.head = None
            return self
        curr_node = self.head.next
        curr_node.prev = None
        self.head.next = None
        self.head = curr_node
        return self
    ##remove node from end
    def remove_back(self):
        if self.head == None:
            return self
        if self.head.next == None:
            self.remove_front()
        prev_node = self.head
        curr_node = self.head.next
        while curr_node.next != None:
            curr_node = curr_node.next
            prev_node = prev_node.next
        prev_node.next = None
        curr_node.prev = None
        return self
    ##calculate the length of list:
    def len_list(self):
        count = 0
        current_node = self.head
        while current_node != None:
            current_node = current_node.next
            count += 1
        return count
    ##remove node from list based on value:
    def remove_val(self,val):
        if self.head == None:
            return self
        curr_node = self.head
        while curr_node != None:
            if curr_node.val == val:
                if curr_node.prev == None:
                    self.remove_front()
                elif curr_node.next == None:
                    self.remove_back()
                else:
                    prev_node = curr_node.prev
                    front_node = curr_node.next
                    curr_node.prev = None
                    front_node.prev = prev_node
                    curr_node.next = None
                    prev_node.next = front_node
                    return self
            curr_node = curr_node.next
        return self
    ##insert node at index(0 based):
    def insert_at(self,val,n):
        length = self.len_list()
        if n < 0 or n > length:
            return self
        if n == 0:
            self.add_front(val)
        elif n == length:
            self.add_back(val)
        else:
            index = 0
            curr_node = self.head
            while index < n and curr_node != None:
                index += 1
                curr_node = curr_node.next
            new_node = DLNode(val)
            prev_node = curr_node.prev
            prev_node.next = new_node
            new_node.next = curr_node
            curr_node.prev = new_node
            new_node.prev = prev_node
        return self

my_list = DLList().add_front(1).add_front(2).add_front(3).add_front(4).add_front(5).add_back(6).add_back(7).remove_front().remove_front().remove_back().remove_back().add_front(5).remove_val(1).insert_at(9,1).traverse()
