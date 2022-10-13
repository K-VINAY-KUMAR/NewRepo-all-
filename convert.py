"""x=eval(input())
print(x)


x=int(input())
ll=[]
for i in range(0,x):
    ii= int(input("Enter the number: "))
    ll.append(ii)
print(ll)

n=int(input("enter:"))
b=[]
for i in range(0,n):
    a=int(input("enter:"))
    b.append(a
sum1=0
sum2=0
sum3=0
for j in b:
    if(j>0):
        if(j%2==0):
            sum1=sum1+j
        else:
            sum2=sum2+j
    else:
        sum3=sum3+j
print(sum3)
/////////////////////////////////////////////
from functools import reduce
x = list(map(str,input().split(" ")))
#uy=(list(map(int,x)))
kk=reduce(lambda x,y:x+y,x)
print(kk)
print(type(kk))

//////////////////////////////////////////////

from functools import reduce
x=[-2,4,5,6,9,-10,7,-8,11,12]
hh=list(map(str,(filter(lambda x:x<0,x))))
jj="758478".join(hh)

print(hh)
print(jj)
/////////////////////////////////////////////

x = list(input().split())[:4]
sum=0
ii=list(map(int,x))

for i in x:
    if(int(i)<0):
        sum=sum+int(i)
print(sum)
print(ii,type(ii))
////////////////////////////////////////////
ii=int(input())
c= list(input().split())[:ii]
bb=[l for l in input("Enter th input:- ").split()][:2]
print(list(map(int,c)),type(list(map(int,c))))
print(list(map(int,bb)),type(list(map(int,bb))))


////////////////////////////////////////
from functools import reduce


jj=[3,-4,-5,-6,-7,8,-9,10,-11]
ll=[]
for x in jj:x if x>=0 else ll.append(x)
print(ll)

#//////////////////////////////////////////
n= input("enter:")
oo=list(map(int,list(n)))
print(oo)
kk=list(map(lambda x:x**len(n),oo))
print("Amstrange" if(sum(kk)==int(n)) else "NOT-Amstrange")
#//////////////////////////////////////
from ctypes.wintypes import CHAR
x = input()
ll=list(x)
kk=list(map(lambda x:ord(x),ll))
lo=sorted(kk)
ert=list(map(lambda x:chr(x),lo))
print("".join(ert))
#//////////////////////////////////////////
uu=list(input())
dic={'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 
'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'y':24, 'z':25,' ':"__",'x':88,'X':99,
'A':26, 'B':27, 'C':28, 'D':29, 'E':30, 'F':31, 'G':32, 'H':33, 'I':34, 'J':35, 'K':36, 
'L':37, 'M':38, 'N':39, 'O':40, 'P':41, 'Q':42, 'R':43, 'S':44, 'T':45, 'U':46, 'V':47, 'W':48, 'Y':49, 'Z':50, '1':51,
'2':52, '3':53, '4':54, '5':55, '6':56, '7':57, '8':58, '9':59, '0':60,}
uiy=list(map(lambda x:dic[x],uu))
oo=list(map(str,uiy))
print("..".join(oo))



#//////////////////////////////////////////
uu=list(input().split())
ooo="".join(uu)
yy=[]
for i in uu:
    yy.append(list(i))
print(yy)
dic={'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 
'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'y':24, 'z':25,' ':"__",'x':88,'X':99,
'A':26, 'B':27, 'C':28, 'D':29, 'E':30, 'F':31, 'G':32, 'H':33, 'I':34, 'J':35, 'K':36, 
'L':37, 'M':38, 'N':39, 'O':40, 'P':41, 'Q':42, 'R':43, 'S':44, 'T':45, 'U':46, 'V':47, 'W':48, 'Y':49, 'Z':50, '1':51,
'2':52, '3':53, '4':54, '5':55, '6':56, '7':57, '8':58, '9':59, '0':60,}
op=[]
for k in yy:
    uio=[]
    for l in k:
        uio.append(str(dic[l]))
    op.append(".".join(uio))
print("|".join(op))
#////////////////////////////////////////////////
hh={}
hh["NAME"]="Vinay"
hh["AGE"]=20
hh["HEIGHT"]=5.8
hh["WEIGHT"]=88
print(hh)
pp=[]
op=[]
for i,j in hh.items():
    pp.append(i)
    pp.append(j)
    op.append([i,j])
print(pp)
print(op,end="\n")
print(list(hh.items()))
pp=list(map(set,hh.items()))
print(pp)

output:-
{'NAME': 'Vinay', 'AGE': 20, 'HEIGHT': 5.8, 'WEIGHT': 88}
['NAME', 'Vinay', 'AGE', 20, 'HEIGHT', 5.8, 'WEIGHT', 88]
[['NAME', 'Vinay'], ['AGE', 20], ['HEIGHT', 5.8], ['WEIGHT', 88]]
[('NAME', 'Vinay'), ('AGE', 20), ('HEIGHT', 5.8), ('WEIGHT', 88)]
[{'NAME', 'Vinay'}, {'AGE', 20}, {'HEIGHT', 5.8}, {88, 'WEIGHT'}]
#///////////////////////////////////////////////////////----NUMPY----///////////////////////////////////////////////////
import numpy as np

a=np.array([[1,2,],[3,4,5],[6,7,8,9]])#used to give array with values in it
b=np.arange(2,100,3,dtype=np.int64)#used to give valued array with in a given range
c=np.ones(50,dtype=np.int64)#used to give ones valued array
d=np.linspace(1,10,num=5,dtype=np.int64)#used to give spaced array
e=np.array([[3,9],[8,1,4],[0,4,8],[0,2,6,1]])

q=np.sort(e,  axis=None)
w=np.sort(e,  axis=0)
tt=np.sort(e,  axis=-1)
print(q)
print(w)
print(tt)
import numpy as np
a=np.array([[1.0,2.0,3.0,4.0],[3.0 ,4.0 ,5.0 ,7.0]])
print(a,  a.ndim,a.size,a.dtype,a.size,a.nbytes )
print(a[0][3])
print([a[-1][-2]])
print(a[0,:2])#get ing the specified data from the row array
print(a[:,1])#get ing the specified data from the column array
a[1,1:4]#get ing the specified data from the column array
a[:,1:3]#get ing the specified data from the column array
#//////outputs////
#[[1. 2. 3. 4.]
# [3. 4. 5. 7.]] 2 8 float64 8 64
#4.0
#[5.0]
#[1. 2.]
#[2. 4.]
#array([[2., 3.],
#       [4., 5.]])


class node:#creating the node
    def __init__(self,data):
        self.data=data
        self.link=None
class head:#creating the head 

    def __init__(self):
        self.Head=None
    def printl(self):
        if(self.Head is None):
            print("The link list is empty!")
        else:
            oo=self.Head
            while(oo != None):
                print( oo.data,oo.link,end="-->")
                oo=oo.link
n1=node(100)# first node creaction 
HH=head()
HH.Head=n1#linking the first node to the Head
n2=node(200)#second node creaction
n1.link=n2#linking the second node to the first node
n3=node(300)# third node creaction
n2.link=n3#connecting the next node to the first node(threed node to the second node!)
HH.printl()# calling the print function to print out all the nodes data!
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import numpy as np
a=list(map(int,list(input("Enter the elements:--").split(" "))))[:9]
b=list(map(int,list(input("Enter the elements:--").split(" "))))[:9]
c=(np.array(a)).reshape(3,3)
d=(np.array(b)).reshape(3,3)
e=[]
print(c.shape)
print(type(e))
print(c)
print(d)
print(d[0:2,0:2])

j=0
while(j<(len(c))):
    for i in range(0,len(d)):
        jjo=sum(c[j]*d[:,i])
        e.append(jjo)
    j=j+1
a=np.array(e)
print(a.reshape(c.shape))
#///////////////////////////////////////////////////////
from os import dup


class Node:
    def __init__(self,Data):
        self.Data = Data
        self.Next=None
class Linked__List(Node):
    def __init__(self):
        self.Head=None
    def printLL(self):
        self.i=0
        if(self.Head==None):
            print("The linked list is empty!!")
        else:
            N=self.Head
            while(N):
                print(N.Data,end="-->")
                N=N.Next
                self.i=self.i+1
        print("\n")
    def frontLL(self,Data):
        oo=Node(Data)
        oo.Next=self.Head
        self.Head=oo
    def EndLL(self,Data):
        oo=Node(Data)
        oo.Next=None
        p=self.Head
        while(p.Next!=None):
            p=p.Next
        p.Next=oo
    def Any_pl(self,N,Data):
        oo=Node(Data)
        p=self.Head
        for i in range(N-1):
            p=p.Next
        oo.Next=p.Next
        p.Next=oo
    def del_front(self):
        p=self.Head
        self.Head=p.Next
        p.Next=None
    def del__End(self):
        oo=self.Head.Next
        ii=self.Head
        while(oo.Next != None):
            oo=oo.Next
            ii=ii.Next
        ii.Next=None
    def Del__Any(self,N):
        oo=self.Head.Next
        ii=self.Head
        for i in range(1,N-1):
            oo=oo.Next
            ii=ii.Next
        ii.Next=oo.Next
        oo.Next=None
    def Replace(self,N,Data):
        oo=Node(Data)
        qq=self.Head.Next
        ii=self.Head
        for i in range(1,N-1):
            qq=qq.Next
            ii=ii.Next
        ii.Next=oo
        oo.Next=qq.Next
        qq.Next=None
        ii=self.Head
    def dup(self):
        p1=self.Head
        p2=None
        while(p1.Next != None and p1 != None):
            p2=p1
            while(p2.Next != None):
                if(p1.Data == p2.Next.Data):
                    p2.Next = p2.Next.Next
                else:
                    p2=p2.Next
            p1=p1.Next

        
            

            

            
    def dup(self):# this is a peace of code for removing the duplicates from the sorted linked list 
        p1=self.Head# this is a peace of code for removing the duplicates from the sorted linked list 
        while(p1.Next != None):# this is a peace of code for removing the duplicates from the sorted linked list 
            if(p1.Data == p1.Next.Data):# this is a peace of code for removing the duplicates from the sorted linked list 
                p1.Next=p1.Next.Next# this is a peace of code for removing the duplicates from the sorted linked list 
            else:# this is a peace of code for removing the duplicates from the sorted linked list 
                p1=p1.Next# this is a peace of code for removing the duplicates from the sorted linked list
            






        

o0=Node(1)
ll=Linked__List()
ll.Head=o0
o1=Node(4)
o0.Next=o1
o2=Node(5)
o1.Next=o2
o3=Node(2)
o2.Next=o3
o4=Node(4)
o3.Next=o4
o5=Node(5)  
o4.Next=o5

ll.frontLL("fornt")
ll.EndLL("End")
ll.Any_pl(3,"Middle")
ll.del_front()
ll.del__End()
ll.Del__Any(3)
ll.printLL()
#ll.Replace(3,"Replaced")
#ll.printLL()
ll.dup()
#ll.dup()#just trying to remove the Duplicates values from the sorted--linked_list!!
ll.printLL()





class Node:
    def __init__(self,Data):
        self.Data=Data
        self.Next=None
        self.Prev=None
class Dub__LL:
    def __init__(self):
        self.Head=None
    def Print_LL(self):
        oo=self.Head
        while(oo):
            if(oo == None):
                print("The Double_linked_List is Empty!!")
            else:
                print( oo.Data,end="-->")
                oo=oo.Next
        print("\n")
    def Front(self,Data):
        o1=Node(Data)
        oo=self.Head
        oo.Prev=o1
        o1.Prev=None
        o1.Next=oo
        self.Head=o1

    def Last(self,Data):
        o1=Node(Data)
        oo=self.Head
        while(oo.Next != None):
            oo=oo.Next
        oo.Next=o1
        o1.prev=oo
        o1.Next=None

    def At_Any_Place(self,N,Data):
        o1=Node(Data)
        oo=self.Head
        for i in range(1,N-1):
            oo=oo.Next
        o1.Prev=oo
        o1.Next=oo.Next
        oo.Next.prev=o1
        oo.Next=o1

DL=Dub__LL()
v1=Node(1)
DL.Head=v1
v2=Node(2)
v1.Next=v2
v2.Prev=v1
v3=Node(3)
v2.Next=v3
v3.Prev=v2
v4=Node(4)
v3.Next=v4
v4.Prev=v3
DL.Print_LL()
DL.Last(10)
DL.Print_LL()
DL.Front(0)
DL.Print_LL()
DL.At_Any_Place(3,"ANY_PLACE!")
DL.Print_LL()
#////////////////////////////////////////////LIST/////////////////////////////////////////////////////////////
from tkinter import Y


k=["hi","jj","jdk"]
print(k[::-1])#['jdk', 'jj', 'hi']
k.reverse()#__this will reverse the given list alternate for [::-1] this method
print(k)#hi   
print(k.pop()) # __this will delete the last element and also prints out that list
print(k)#['jdk', 'jj']
k.insert(0,"kooko")# __ this will insert the element at specified position in the given list
print(k)#['kooko', 'jdk', 'jj']
k.append("opopo")# __ this will adds the element at the end of the given list 
print(k)#['kooko', 'jdk', 'jj', 'opopo']
k.remove("kooko")# __this will remove the element from the given list with the help of the element value but not the index..
print(k)#['jdk', 'jj', 'opopo']

opop=[1,9,61,38,90,54,-3,-68]
ii=[39,84,-34,9,3,67,-3,-57]
opop.sort(reverse=True)#this will create the original list in sorted order
oo=sorted(ii)#this will create the new list with sorted order 
print(opop)
print(oo)
print(ii)
#if we want to really want to make a copy of a list then we will use .copy() method
#example:-
t=["hi","hello","how","are"]
y=t#this will create the copy of the original list but if make changes in the copied list then the changes will happen in 
#original list too...
y.append("you")
oo=t.copy()#we can also use this "copy_list=original_list[:]" this will work as an alter native for the .copy method!!
oo.append("change!")
print(y)
print(t)
print(oo)
print(t)
#
#/////////////////////////////////////////tuple////////////////////////////////////////////////


v={"vina","sann",23,"sdn"}
f1,*f,f2=v
print(f1)#ValueError: not enough values to unpack (expected 5, got 4)
print(f)
print(f2)
#output:
# sdn
#['vina', 'sann']
#23


# it takes less time and space to work with tuple rather than list (IMP)
#////////////////////////////////////////////dictionary//////////////////////////////////////
g={"name":"vinay","age":19,"marks":999}
print(g["name"])#vinay
print(g.keys())#dict_keys(['name', 'age', 'marks'])
print(g.values())#dict_values(['vinay', 19, 999])
ll=[]
for i in g.items():
    ll.append(list(i))
print(ll)#[['name', 'vinay'], ['age', 19], ['marks', 999]]
kk=[]
for i ,j in g.items():
    kk.append(i)
    kk.append(j)
print(kk)#['name', 'vinay', 'age', 19, 'marks', 999]
g["e-mail"]="kvkski@gmail.com"
print(g)#{'name': 'vinay', 'age': 19, 'marks': 999, 'e-mail': 'kvkski@gmail.com'}
del g["name"]
print(g)#{'age': 19, 'marks': 999, 'e-mail': 'kvkski@gmail.com'}

g.pop("age")
print(g)#{'marks': 999, 'e-mail': 'kvkski@gmail.com'}
g.popitem()
print(g)#{'marks': 999}
"""
#///////////////////////////////////////////////////set/////////////////////////////////////
dd=set()
print(type(dd))
dd.add(1)
dd.add(2)#this will add the data to the set 
dd.add(3)
dd.add(4)
print(dd)
dd.remove(2)
dd.add(8398)
dd.discard(1)#this will work as same as .remove() function but if u try to delete a data that is not in that set then it wont
#thow any error but where as in .remove() method it will thore an error  
for i in dd:
    print(i,end="--")
dd.pop()#this will pop out the data in the set 
print(dd,end="\n")

