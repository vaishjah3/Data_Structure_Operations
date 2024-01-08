class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            new_node.next=self.head
            self.head=new_node
    def print_LL(self):
        current_node=self.head
        while(current_node):
            print(current_node.data)
            current_node=current_node.next   
    def insertAtanindex(self,data, index):
        new_node=Node(data)
        current_node=self.head()
        position=0
        if position==index:
            self.insert_at_beginning(data)
        else:
            while(current_node!=None and position+1!=index):
                position=position+1
                current_node=current_node.next
            if current_node!=None:
                new_node.next=current_node.next
                current_node.next=new_node
            else:
                print("Index Not present")
    
    def insertAtend(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return 
        current_node=self.head
        while(current_node.next):
            current_node=current_node.next
        current_node.next=new_node
    def updateNode(self, val, index):
        current_node=self.head
        position=0
        if position==index:
            current_node.data=val
        else:
            while(current_node!=None and position!=index):
                position=position+1
                current_node=current_node.next
            if current_node!=None:
                current_node.data=val
            else:
                print("Index not found!")
    
    def removefirstNode(self):
        if self.head==None:
            return
        
        self.head=self.head.next
        
    def removelastnode(self):
        if self.head==None:
            return
        
        current_node=self.head
        while(current_node.next.next):
            current_node=current_node.next
        current_node.next=None
            
    def deleteatposition(self, index):
        if self.head==None:
            return
        else:
            current_node=self.head
            position=0
            if position==index:
                self.removefirstNode()
            else:
                while(current_node!=None and position+1!=index):
                    position=position+1
                    current_node=current_node.next
                if current_node !=None:
                    current_node.next=current_node.next.next   
                else:
                    print("Index not found")
        
    def removenodewithvalue(self, val):
            current_node=self.head
            while(current_node!=None and current_node.next.data!=val):
                current_node=current_node.next
            if current_node==None:
                return
            current_node.next=current_node.next.next
                

        
            
                

             
            
        

llist=LinkedList()
llist.insert_at_beginning(10)
print('Node data')
llist.print_LL()

    

        