##deleting the last node
class Node:
    def _init_(self,data):
        self.data=data
        self.next=None
        
class SLL:
    def _init_(self):
        self.head=None
    def insert_position(self,pos,data):
          np=Node(data)
          temp=self.head
          for i in range(pos-1):
            temp=temp.next
            np.next=temp.next
            temp.next=np
    def display(self):
      if self.head is None:
            print('ll is empty')
      else:
            temp=self.head
            while(temp):
                print(temp.data)
                temp=temp.next
    def delete(self):
       temp=self.head.next
       prev=self.head
       while temp.next is not None:
         temp=temp.next
         prev=prev.next
       prev.next=None
obj=SLL()
n1=Node(1)
obj.head=n1
n2=Node(2)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
obj.display()
print()
obj.delete()
obj.display()
