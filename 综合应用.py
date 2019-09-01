import random

import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox
import math
 

# 第1步，实例化object，建立窗口window

global s
class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None
    
class List:
    def __init__(self, node=None):
    # 构造非空链时，让其地址域指向自己
        if node:
            node.next = node
        self.__head = node
         
    def is_empty(self):
        return self.__head == None

    def __len__(self):
        count = 1
        cur = self.__head
        if self.is_empty():
            return 0
        while cur.next != self.__head:
            count +=1
            cur = cur.next
        return count
    
    def printnode(self):
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem)
            cur = cur.next
        print(cur.elem)
    
    def add(self,elem):  #头插法
        node = Node(elem)
        if self.is_empty():
            self.__head = node
            self.__head.next = self.__head
            return
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        node.next = self.__head
        self.__head = node 
        cur.next = self.__head
    
    def append(self,elem):
        node = Node(elem)
        cur = self.__head
        if self.is_empty():
            self.__head = node
            self.__head.next = self.__head
            return
        while cur.next != self.__head:
            cur = cur.next
        node.next = cur.next
        cur.next = node

    def search(self,elem):
        if self.is_empty():
            return None
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == elem:
                return cur
            else:
                cur = cur.next
        if cur.elem == elem:
            return cur
        return None
    
    def remove(self,elem):
        cur = self.__head
        prenode = None
        if self.is_empty():
            return
        while cur.next != self.__head:
            if cur.elem == elem:
                if cur == self.__head:
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    prenode.next = cur.next
                return
            else:
                prenode = cur
                cur = cur.next
        if cur.elem == elem:
            if cur==self.__head:
                self.__head = None
                return
            prenode.next = cur.next
   
    def jump(self,node,m):
        cur = node
        if cur == None:
            print("error!")
            exit(1)
        for i in range(m-1):
            cur = cur.next
        print(cur.elem,"is out!")
        return cur
    
    def game(self):
        window = tk.Tk()

        # 第2步，给窗口的可视化起名字

        window.title('My Window')

        

        # 第3步，设定窗口的大小(长 * 宽)

        window.geometry('600x400')  # 这里的乘是小x

        l1 = []
        x = 150
        y = 150
        r = 100
        N = 30

        #tkinter.messagebox.showinfo(title='Hi', message='你好！')       
        m = 0
        tk.Label(window, text='name:', font=('Arial', 10), ).place(x=200, y=0, anchor='nw')

        #s = tk.IntVar()

        e = tk.Entry(window, show = None)
        e.place(x = 300,y = 0)#显示成明文形式

        
        # 第5步，定义两个触发事件时的函数insert_point和insert_end（注意：因为Python的执行顺序是从上往下，所以函数一定要放在按钮的上面）

        def insert_point(): # 在鼠标焦点处插入输入内容

            var = e.get()

            l1.append(var)

            self.append(var)

            e.delete(0, 10)
            
            N = len(l1)
            
            tk.Canvas(window, height=300, width=600).place(x=0,y=50)
            for i in range(N):
                x0 = x + r*math.sin((2*math.pi/N)*i)
                y0 = y - r*math.cos((2*math.pi/N)*i)
                tk.Label(window, text=l1[i], font=('Arial', 10), ).place(x=x0, y=y0)
    # 第6步，创建并放置两个按钮分别触发两种情况
         
           # s.set(self.__head.elem)
        b1 = tk.Button(window, text='join the game', width=15,

                height=1, command=lambda:insert_point()).place(x=450,y=0)
        s = self.__head
        # def start():
        tk.Label(window, text='out:', font=('Arial', 10),).place(x=100, y=380)
        t = tk.Text(window, height=3,width = 200)
        t.place(x=150, y=380)

        
        # b3 = tk.Button(window, text='begin', width=15,
        
        #             height=1, command=start).place(x=150,y=0)
        def randomM(self,s):
            #t.delete(0,2)

            s = self.__head
            m = random.randint(1,6)
            tk.Label(window, text=str(m), font=('Arial', 10), ).place(x=400, y=25)
            #k = self.search(m)
            s = self.jump(s,m)
            t.insert('end',"{} ".format(s.elem))
            #j =  s.next
            k =l1.index(s.elem)
            N = len(l1)
            x0 = x + r*math.sin((2*math.pi/N)*k)
            y0 = y - r*math.cos((2*math.pi/N)*k)
            tk.Label(window, text=l1[k], font=('Arial', 10),fg = 'red' ).place(x=x0, y=y0)
            self.remove(s.elem)
            #s = j
            if(self.__len__() == 1):
                print(self.__head.elem,"win!")
                tk.messagebox.showinfo(title='game over', message='{} win!'.format(self.__head.elem)) 
            
            #s.set(k.elem)
        #t = tk.Text(window, height=1,width = 5).place(x = 400, y = 25)
        
        b2 = tk.Button(window, text='掷骰子', width=15,

                    height=1, command=lambda:randomM(self,s)).place(x=450,y=30)
        
    
        def restart(l1):
            self.__head = None
            l1.clear()
            tk.Canvas(window, height=300, width=600).place(x=0,y=50)
            t.delete(0.0,tk.END)

        b4 = tk.Button(window, text='restart', width=15,

                height=1, command=lambda:restart(l1)).place(x=150,y=0)
        #while self.__len__()>1:
            
            #m = random.randint(1,6)
            #print("m is ",m)

        #print(self.__head.elem,"win!")

        window.mainloop()
if __name__ == '__main__':
    l1 = List()
    l1.game()
