import random
import tkinter as tk  # 使用Tkinter前需要先导入
from  tkinter  import ttk  
import copy
'''
几种排序：要求随机输入一组数据，随时给出某一趟排序的变化情况
（1）直接插入排序、折半插入排序、希尔排序
（2）冒泡排序、快速排序
（3）简单选择排序
'''

def insert_sort(b):
    '''
    插入排序
    '''
    st = []
    array = copy.copy(b)
    n = len(array)
    for i in range(1, n):
        #i = j
        while i > 0:
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
                i -= 1
            else:
                break
        #print(a)
        st.append(array.copy())
    return st

def half_insert_sort(b):
    '''
    折半插入排序
    '''
    st = []
    a = copy.copy(b)
    n = len(a)
    for i in range(1, n):
        low = 0
        high = i - 1
        index = a[i]
        while low <= high:
            half = int((low+high)/2)
            if index < a[half]:
                high = half - 1
            else:
                low = half + 1
        for j in range(i, low, -1):

            a[j] = a[j - 1]

        a[low] = index
        print(a)
        st.append(a.copy())
    return st

def shell_sort(b):
    '''
    希尔排序
    '''
    st = []
    a = copy.copy(b)
    n = len(a)
    gap = n // 2

    while gap > 0:

        for j in range(gap, n):
            i = j
            while i > 0:
                if a[i] < a[i-gap]:
                    a[i], a[i-gap] = a[i-gap], a[i]
                    i -= gap
                else:
                    break
            print(a)
            st.append(a.copy())
        gap//=2
        
    return st

def bubble_sort(b):
    '''
    冒泡
    '''
    st = []
    array = copy.copy(b)
    n = len(array)
    for i in range(n):
        for j in range(1,n-i):
            if  array[j-1] > array[j] :      
                array[j-1],array[j] = array[j],array[j-1]
        print(array)
        st.append(array.copy())
    return st

def quick_sort(b):
    '''
    快速排序
    '''
    st = []
    a = copy.copy(b)
    return qsort(a,0,len(a)-1,st)

def qsort(a,left,right,st):
    #快排函数，a为待排序数组，left为待排序的左边界，right为右边界
    if left >= right : return a
    key = a[left]     #取最左边的为基准数
    lp = left           #左指针
    rp = right          #右指针
    while lp < rp :
        while a[rp] >= key and lp < rp :
            rp -= 1
        while a[lp] <= key and lp < rp :
            lp += 1
        a[lp],a[rp] = a[rp],a[lp]
    a[left],a[lp] = a[lp],a[left]
    print(a)
    st.append(a.copy())
    qsort(a,left,lp-1,st)
    qsort(a,rp+1,right,st)
    
    return st

def select_sort(b):
    '''
    选择排序
    '''
    st = []
    a = copy.copy(b)
    n = len(a)
    for i in range(0,n):
        m = i                             #最小元素下标标记
        for j in range(i+1,n):
            if a[j] < a[m] :
                m = j                     #找到最小值的下标
        a[m],a[i] = a[i],a[m]   #交换两者
        print(a)
        st.append(a.copy())
        #st.extend('\r\n')
    return st


def UI():

    win=tk.Tk() #构造窗体  
    win.title("排序")
    win.geometry('500x300')
    tk.Label(win, text='input array:', font=('Arial', 10), ).place(x=50, y=0, anchor='nw')

    e = tk.Entry(win, show = None,width = 40)
    e.place(x = 160,y = 0)#显示成明文形式
    tk.Label(win, text='choose a method:', font=('Arial', 10), ).place(x=50, y=50, anchor='nw')
    def sort(*args):
        t.delete(0.0,tk.END)
        ss = e.get().split()
        a = [int(i) for i in ss]
        tmp = comboxlist.get()
        if tmp == "直接插入排序":
            sg = insert_sort(a)
            for p in sg:
                t.insert(tk.END,p)
                t.insert(tk.END,'\n')
        elif tmp == "折半插入排序":
            sg = half_insert_sort(a)
            for p in sg:
                t.insert(tk.END,p)
                t.insert(tk.END,'\n')
        elif tmp=="希尔排序":
            
            sg = shell_sort(a)
            for p in sg:
                t.insert(tk.END,p)
                t.insert(tk.END,'\n')
        elif tmp == "冒泡排序":
            sg = bubble_sort(a)
            for p in sg:
                t.insert(tk.END,p)
                t.insert(tk.END,'\n')
        elif tmp == "快速排序":
            sg = quick_sort(a)
            for p in sg:
                t.insert(tk.END,p)
                t.insert(tk.END,'\n')
        elif tmp ==  "简单选择排序":
            sg = select_sort(a)
            for p in sg:
                t.insert(tk.END,p)
                t.insert(tk.END,'\n')
        else:
            print("error!")
    b=tk.Button(win, text='sort',font=('Arial', 10), width=20,

                height=5, command=sort)
    b.place(x=300,y=100)
    comvalue=tk.StringVar()#窗体自带的文本，新建一个值  

    comboxlist=ttk.Combobox(win,textvariable=comvalue)
    
    comboxlist["values"]=("直接插入排序","折半插入排序","希尔排序","冒泡排序","快速排序","简单选择排序")

    comboxlist.current(0)  #选择第一个  

    t = tk.Text(win, height=60,width = 40)
    t.place(x = 0,y = 100)
 
    def go(*args):   #处理事件，*args表示可变参数  
        tmp = comboxlist.get()
        print() #打印选中的值  
    #comboxlist.bind("<<ComboboxSelected>>",sort)  #绑定事件,(下拉列表框被选中时，绑定go()函数)  

    comboxlist.place(x = 160,y = 50)

    
    win.mainloop() #进入消息循环  

if __name__ == '__main__':
    a = [3,9,6,2,6,3,8,5,1]
    #s = bubble_sort(a)
    #s = insert_sort(a)
    #s = half_insert_sort(a)
    #s = shell_sort(a)
    #s = quick_sort(a)
    #s = select_sort(a)
    #print(s)
    UI()