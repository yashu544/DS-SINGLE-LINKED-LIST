#deletion at begining
class Node:
    def _init_(self,data):
        self.data=data
        self.next=None
        
class SLL:
    def _init_(self):
        self.head=None
    def delete_beg(self):
      temp=self.head
      self.head=temp.next
      temp.next=None
    def display(self):
      if self.head is None:
            print('ll is empty')
      else:
            temp=self.head
            while(temp):
                print(temp.data)
                temp=temp.next
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
obj.delete_beg()
obj.display()
