import tkinter as tk
from tkinter import ttk

def window_focus(root):
    root.lift()
    root.attributes('-topmost',True)
    root.after_idle(root.attributes,'-topmost',False)

def multipleList(root,area,data=None,height=5,width=100,anchor='w',padding=(0,0,0,0),command=None):
    ac=[]
    
    for i in range(len(area)):
        ac.append(i)
    ac=tuple(ac)
    
    tv=ttk.Treeview(
        root,
        columns=ac,
        show='headings',
        height=height,
        padding=padding)
    
    for i in range(len(area)):
        if isinstance(width,int):
            if isinstance(anchor,str):
                tv.column(
                    ac[i],
                    width=width,
                    anchor=anchor)
                
            elif isinstance(anchor,(list,tuple)):
                tv.column(
                    ac[i],
                    width=width,
                    anchor=anchor[i])
                
        elif isinstance(width,(list,tuple)):
            if isinstance(anchor,str):
                tv.column(
                    ac[i],
                    width=width[i],
                    anchor=anchor)
                
            elif isinstance(anchor,(list,tuple)):
                tv.column(
                    ac[i],
                    width=width[i],
                    anchor=anchor[i])
        tv.heading(ac[i],text=area[i])
        
    tv.bind('<Double-Button-1>',command)
    tv.pack()
    
    if data==None:
        return tv
    else:
        for i in data:
            tv.insert('','end',values=i)
        return tv


class spacex:
    def __init__(self,parent,width,side=None):
        if side==None:
            tk.Frame(parent,width=width).pack()
        else:
            tk.Frame(parent,width=width).pack(side=side)
        
class spacey:
    def __init__(self,parent,height,side=None):
        if side==None:
            tk.Frame(parent,height=height).pack()
        else:
            tk.Frame(parent,height=height).pack(side=side)

class scrollbar:
    def __init__(self,parent,target,barType='v'):
        if barType=='v':
            self.bar=tk.Scrollbar(
                parent,
                orient='vertical',
                command=target.yview) #竖直滚动条
            target.config(yscrollcommand=self.bar.set)
            
        elif barType=='h':
            self.bar=tk.Scrollbar(
                target,
                orient='horizontal',
                command=parent.xview
                ) #水平滚动条
            target.config(xscrollcommand=self.bar.set)
    
    def on_mousewheel(self,target,parent,orient='v'):
        if orient=='v':
            target.bind(
                "<MouseWheel>",
                lambda event:self._mousewheel(
                    parent, 
                    event,
                    'v'))
            
        elif orient=='h':
            target.bind(
                "<Shift-MouseWheel>",
                lambda event:self._mousewheel(
                    parent,
                    event,
                    'h'))
            
        return self
        
    def _mousewheel(self,parent,event,orient='v'):
        if orient=='v':
            parent.yview_scroll(
                -1*(event.delta),
                "units")
            
        elif orient=='h':
            parent.xview_scroll(
                -1*(event.delta),
                "units")
            
        return self


        
class scrollable_frame:
    def __init__(self,parent,scrollregion):
        self.frame=tk.Canvas(
            parent,
            scrollregion=scrollregion)
        
        self.child=tk.Frame(self.frame)
        
        vbar=scrollbar(
            self.frame,
            self.frame,
            barType='v').bar
        
        vbar.pack(
            side='right',
            fill='y')
        
        self.frame.create_window(
            (0,0),
            anchor='nw',
            window=self.child)
        
    def on_mousewheel(self,target,orient='v'):
        if orient=='v':
            target.bind(
                "<MouseWheel>",
                lambda event:self._mousewheel(
                    event,
                    'v'))
            
        elif orient=='h':
            target.bind(
                "<Shift-MouseWheel>",
                lambda event:self._mousewheel(
                    event,
                    'h'))
            
        return self
        
    def _mousewheel(self,event,orient='v'):
        if orient=='v':
            self.frame.yview_scroll(
                -1*(event.delta),
                "units")
            
        elif orient=='h':
            self.frame.xview_scroll(
                -1*(event.delta),
                "units")
            
        return self
    
class Warning:
    def __init__(self,s,num,isolate=False):
        self.root=tk.Tk()
        self.root.wm_attributes('-topmost',1)
        self.root.title(' ')
        self.root.attributes(
            '-alpha',
            0.0)
        self.root.withdraw()
        
        self.root.resizable(0,0)
        self.root.minsize(200,60)
        
        spacey(self.root, 5)
        
        maxLen=0
        for i in s:
            if len(i)>maxLen:
                maxLen=len(i)
                
        for i in range(num):
            message=tk.Label(
                self.root,
                text=s[i],)
                #wraplength=150)
            message.pack()
            
        b=tk.Button(
            self.root,
            text='关闭',
            command=self.close)
        b.pack()
        
        spacey(self.root, 10)
        
        self.root.deiconify()
        self.root.update()
        sw=self.root.winfo_screenwidth()//2
        sh=self.root.winfo_screenheight()//2
        w=self.root.winfo_width()//2
        h=self.root.winfo_height()//2
        self.root.geometry('+'+str(sw-w)+'+'+str(sh-h))
        self.root.attributes('-alpha', 1.0)
        
        if isolate:
            self.root.mainloop()
        
    def close(self):
        self.root.destroy()
        
'''class EntryBox:
    def __init__(self,num,bag,send,width):
        self.send=send
        self.root=tk.Tk()
        self.root.title('')
        
        self.root.attributes(
            '-alpha',
            0.0)
        
        self.root.withdraw()
        
        self.root.minsize(200,60)
        self.root.resizable(0,0)
        
        title=tk.Label(
            self.root,
            text='请输入')
        title.pack()
        
        for i in range(num):
            tempFrame=tk.Frame(self.root)
            tempFrame.pack()
            
            space1=tk.Frame(
                tempFrame,
                width=width[1][0])
            space1.pack(side='left')
            
            tempLabel=tk.Label(
                tempFrame,
                text=bag[i],
                width=width[0][0])
            tempLabel.pack(side='left')
            
            space2=tk.Frame(
                tempFrame,
                width=width[1][1])
            space2.pack(side='left')
            
            tempEntry=tk.Entry(
                tempFrame,
                width=width[0][1])
            tempEntry.pack(side='left')
            locals()['self.entry'+str(i+1)] = tempEntry
            
            space3=tk.Frame(
                tempFrame,
                width=width[1][2])
            space3.pack(side='left')
        
        b=tk.Button(
            self.root,
                text='确认',
                command=self.close)
        b.pack()
        
        self.root.deiconify()
        self.root.update()
        sw=self.root.winfo_screenwidth()//2
        sh=self.root.winfo_screenheight()//2
        w=self.root.winfo_width()//2
        h=self.root.winfo_height()//2
        self.root.geometry('+'+str(sw-w)+'+'+str(sh-h))
        self.root.attributes('-alpha', 1.0)
        
    def close(self):
        '''