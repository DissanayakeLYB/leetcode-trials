class Node:
    def __init__ (self,value):
        self.value = value
        self.next = None

class Stack: 
    def __init__ (self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            while temp != None:
                print(temp)
                temp = temp.next


    def push(self,value):
        new_node = Node(value)

        if self.height == 0:
            self.top = new_node
        
        else:
            new_node.next = self.top
            self.top = new_node
    
    def pull(self):
        if self.height == 0:
            return None
        elif self.height == 1:
            temp = self.top
            self.top.next = None            
            return temp
        else:
            temp = self.top
            self.top = temp.next
            temp.next = None
            return temp
        
Stack.print_stack
Stack.push(4)