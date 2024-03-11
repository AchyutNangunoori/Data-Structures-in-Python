class node:
    def __init__(self,x):
        self.data=x
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insertatend(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=node(x)
        print("Element inserted successfully\n")
    def insertatbegin(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            temp=node(x)
            temp.next=self.head
            self.head=temp
        print("Element inserted successfully\n")
    def insertatdesired(self,p,x):
        temp=self.head
        for i in range(p-1):
            temp=temp.next
            if(temp==None):
                print("Position not found in list\n")
                return
        newnode=node(x)
        t=temp.next
        temp.next=newnode
        newnode.next=t
        print("Element inserted successfully\n")
    def deletefrombegin(self):
        if(self.head==None):
            print("List is Empty")
        else:
            self.head=self.head.next
            print("Element at the beginning deleted successfully\n")
    def deletefromend(self):
        if(self.head==None):
            print("List is Empty")
            return
        temp=self.head
        while(temp.next.next!=None):
            temp=temp.next
        temp.next=None
        print("Element at the end deleted successfully\n")
    def deletefromdesired(self,p):
        if(self.head==None):
            print("List is Empty")
            return
        prev=self.head
        temp=self.head.next
        for i in range(p-1):
            prev=temp
            temp=temp.next
        prev.next=temp.next
    def display(self):
        if(self.head==None):
            print("List is Empty")
        else:
            temp=self.head
            while(temp!=None):
                print(temp.data,end="->")
                temp=temp.next
            print("None")
    def search(self,x):
        if(self.head==None):
            print("List is Empty")
            print("Element not found")
            return
        temp=self.head
        while(temp!=None):
            if(temp.data==x):
                print("Element Found")
                return
            temp=temp.next
        print("Element not found")
c=1
link=linkedlist()
while(c!=5):
    print("Enter 1 if you want to insert an element")
    print("Enter 2 if you want to delete an element")
    print("Enter 3 if you want to display the list")
    print("Enter 4 if you want to search for an element in the list")
    print("Enter 5 if you want to exit")
    print("Enter your choice:")
    c=int(input())
    if(c==1):
        print("Enter 1 if you want to insert at the beginning")
        print("Enter 2 if you want to insert at the end")
        print("Enter 3 if you want to insert at any desired position")
        print("Enter your choice")
        ch=int(input())
        print("Enter the element you want to insert")
        data=int(input())
        if(ch==1):
            link.insertatbegin(data)
        if(ch==2):
            link.insertatend(data)
        if(ch==3):
            print("Enter the position at which you want to insert the element")
            p=int(input())
            if(p==1):
                link.insertatbegin(data)
            else:
                link.insertatdesired(p-1,data)
    if(c==2):
        print("Enter 1 if you want to delete from the beginning")
        print("Enter 2 if you want to delete from the end")
        print("Enter 3 if you want to delete from any desired position")
        print("Enter your choice")
        ch=int(input())
        if(ch==1):
            link.deletefrombegin()
        if(ch==2):
            link.deletefromend()
        if(ch==3):
            print("Enter the position from where you want to delete the element")
            p=int(input())
            link.deletefromdesired(p-1)
    if(c==3):
        link.display()
    if(c==4):
        print("Enter the element you want to search for")
        x=int(input())
        link.search(x)
    if(c==5):
        print("Exiting...")
