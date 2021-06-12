import tkinter as tk
import webbrowser as wb
import frozen_dir
from syscmd import cmd
from custom_widget import multipleList,scrollable_frame,Warning,window_focus,spacex,spacey
from data_operation import get_data,write_data
from selenium import webdriver
import json

class Crawl_page:
    def __init__(self,master):
        self.root=master
        self.root.title('更新数据')
        self.root.geometry('250x200')
        
        self.frame=tk.Frame(self.root)
        self.frame.pack()
        
        spacey(self.frame,4)
        
        top=tk.Frame( #上方控制栏
            self.frame,
            width=250,
            height=30)
        top.pack(fill='x')
        
        spacex(top,10,'left')

        back=tk.Button(
            top,
            text='返回',
            command=self.close)
        back.pack(side='left')
        
        spacex(top,12,'right')
        
        save=tk.Button(
            top,
            text='保存',
            command=self.save)
        save.pack(side='right')
        
        spacex(top,5,'right')
        
        delete=tk.Button(
            top,
            text='删除',
            command=self.delete)
        delete.pack(side='right')
        
        spacex(top,5,'right')
        
        enterData=tk.Button(
            top,
            text='输入',
            command=self.add)
        enterData.pack(side='right')
        
        entry_label1=tk.Frame( #名称输入框栏
            self.frame,
            width=250)
        entry_label1.pack()
        
        nameLabel=tk.Label(
            entry_label1,
            text='课程名称',
            width=8)
        nameLabel.pack(side='left')
        
        spacex(entry_label1,11,'right')
        
        self.entry1=tk.Entry(
            entry_label1,
            width=30)
        self.entry1.pack(side='right')
        
        
        entry_label2=tk.Frame( #值输入框栏
            self.frame,
            width=250)
        entry_label2.pack()

        valueLabel=tk.Label(
            entry_label2,
            text='链接',
            width=8)
        valueLabel.pack(side='left')
        
        spacex(entry_label2,11,'right')
        
        self.entry2=tk.Entry(
            entry_label2,
            width=30)
        self.entry2.pack(side='right')
        
        spacey(self.frame,2)
        
        '''frame1=tk.Frame(self.frame)
        frame1.pack()
        
        space=tk.Frame(
            frame1,
            width=9)
        space.pack(side='left')'''
        
        try:
            self.data=get_data(frozen_dir.app_path()+'/courses.txt','r',2)
        except FileNotFoundError:
            self.l=multipleList(
                self.frame,
                area=('课程名称',),
                width=221,
                command=self.set_course)
        else:
            self.l=multipleList(
                self.frame,
                area=('课程名称',),
                data=self.data,
                width=221,
                command=self.set_course)
        self.l.pack()
        
        '''vbar=scrollbar(
            frame1,
            self.l,
            'v').on_mousewheel(self.l,self.l,'v').bar
        vbar.pack(
            side='right',
            fill='y')'''
        
    def set_course(self,event):
        a=open(
            frozen_dir.app_path()+'/linksAll.txt',
            'w+',)
        a.close()
        
        try:
            a=open(
                frozen_dir.app_path()+'/scrapyLocation.txt',
                'r')
            
        except FileNotFoundError:
            Warning(['请先运行configure!','位于',"'MosoteachDownloader.app/Contents/MacOS'"],3)
            
        else:
            env=a.readline().strip('\n')
            a.close()
            
            write_data(
                frozen_dir.app_path()+'/course.txt',
                'w+',
                [[self.l.item(self.l.focus(),'values')[1]]])
            
            result=cmd(
                'cd {} && {} crawl mosoteachAll'
                       .format(frozen_dir.app_path(),env))
            #Warning([result],1)
            if 'NOCOOKIE' not in result:
                Warning(['成功！'],1)
    
    def add(self):
        if(len(self.entry1.get())!=0 and len(self.entry2.get())!=0):
            name=self.entry1.get()
            value=self.entry2.get()
            self.l.insert('','end',values=(name,value))
            self.entry1.delete(0,'end')
            self.entry2.delete(0,'end')
            
        elif(len(self.entry1.get())==0 and len(self.entry2.get())==0):
            Warning(['请输入课程名称和链接!'],1)
            
        elif(len(self.entry1.get())==0):
            self.entry2.delete(0,'end')
            Warning(['请输入课程名称!'],1)
            
        else:
            self.entry1.delete(0,'end')
            Warning(['请输入链接!'],1)
    
    def close(self):
        self.frame.destroy()
        Main_page(self.root)
        
    def delete(self): #删除选中项
        for i in self.l.selection():
            self.l.delete(i)

    def save(self):
        self.data=[]
        
        for i in self.l.get_children():
            self.data.append(self.l.item(i,'values'))
            
        write_data(frozen_dir.app_path()+'/courses.txt','w+',self.data)
        Warning(['已保存!'],1)

class Main_page():
    def __init__(self,master):
        self.root=master
        self.root.title('蓝墨云下载器')
        self.root.geometry('240x90')
        
        self.frame=tk.Frame(self.root)
        self.frame.pack()
        
        spacey(self.frame,7)
        
        download=tk.Button(
            self.frame,
            text='下载文件',
            width=8,
            command=self.change)
        download.pack()
        
        spacey(self.frame,5)
        
        crawl=tk.Button(
            self.frame,
            text='更新数据',
            width=8,
            command=self.crawl_data)
        crawl.pack()
        
        spacey(self.frame,5)
        
        update=tk.Button(
            self.frame,
            text='更新Cookie',
            width=10,
            command=self.change_c)
        update.pack()
        
    def change(self):
        self.frame.destroy()
        Download_page(self.root)
        
    def crawl_data(self):
        self.frame.destroy()
        Crawl_page(self.root)
        
    def change_c(self):
        self.frame.destroy()
        Cookie_page(self.root)

class Cookie_page:
    def __init__(self,master):
        self.url='https://www.mosoteach.cn/web/'
        
        self.root=master
        self.root.title('更新Cookie')
        self.root.geometry('200x70')
        
        self.frame=tk.Frame(self.root)
        self.frame.pack()
        
        spacey(self.frame,10)
        
        label=tk.Label(
            self.frame,
            text='请在登录好账号后点击确认！')
        label.pack()
        
        button=tk.Button(
            self.frame,
            text='确认',
            command=self.confirm)
        button.pack()
        
        spacey(self.frame,10)
        
        try:
            self.driver = webdriver.Chrome('/Applications/chromedriver')
            self.driver.get(self.url)
        except Exception as e:
            Warning([str(e)],1)
            self.close()
    
    def confirm(self):
        try:
            dictCookies = self.driver.get_cookies()
            jsonCookies = json.dumps(dictCookies)
            # 登录完成后，将cookie保存到本地
            f=open(frozen_dir.app_path()+'/cookie.json','w+')
            f.write(jsonCookies)
            Warning(['账号保存成功！'],1)
            self.driver.close()
            self.driver.quit()
            self.close()
        except:
            Warning(['错误，请不要提前关闭浏览器！'],1)
            self.close()
    
    def close(self):
        self.frame.destroy()
        Main_page(self.root)
'''
class Cookie_page:
    def __init__(self,master):
        self.root=master
        self.root.title('更新Cookie')
        self.root.geometry('500x320')
        
        self.frame=tk.Frame(self.root) #用于页面切换
        self.frame.pack()
        
        spacey(self.frame,6)
        
        top=tk.Frame( #上方控制栏
            self.frame,
            width=500,
            height=30)
        top.pack(fill='x')
        
        spacex(top, 50,'left')

        back=tk.Button(
            top,
            text='返回',
            width=4,
            command=self.close)
        back.pack(side='left')
        
        spacex(top, 8,'right')
        
        save=tk.Button(
            top,
            text='保存',
            width=4,
            command=self.save)
        save.pack(side='right')
        
        spacex(top, 5,'right')
        
        empty=tk.Button(
            top,
            text='清空',
            width=4,
            command=self.empty)
        empty.pack(side='right')
        
        spacex(top, 5,'right')
        
        delete=tk.Button(
            top,
            text='删除',
            width=4,
            command=self.delete)
        delete.pack(side='right')
        
        spacex(top, 5,'right')
        
        enterData=tk.Button(
            top,
            text='输入',
            width=4,
            command=self.enterData)
        enterData.pack(side='right')
        

        spacey(self.frame,2)        

        entry_label1=tk.Frame( #名称输入框栏
            self.frame,
            width=480)
        entry_label1.pack()
        
        spacex(entry_label1, 7,'left')
        
        nameLabel=tk.Label(
            entry_label1,
            text='名称',
            width=4)
        nameLabel.pack(side='left')
        
        spacex(entry_label1, 7,'right')
        
        self.entry1=tk.Entry(
            entry_label1,
            width=58)
        self.entry1.pack(side='right')
        
        
        entry_label2=tk.Frame( #值输入框栏
            self.frame,
            width=480)
        entry_label2.pack()
        
        spacex(entry_label2, 7,'left')
        
        valueLabel=tk.Label(
            entry_label2,
            text='值',
            width=4)
        valueLabel.pack(side='left')
        
        spacex(entry_label2, 7,'right')
        
        self.entry2=tk.Entry(
            entry_label2,
            width=58)
        self.entry2.pack(side='right')
        
        spacey(self.frame, 2)
        
        area=('名称','值')
        try:
            self.data=get_data(frozen_dir.app_path()+'/cookie.txt','r',2)
        except FileNotFoundError:
            self.tv=multipleList( #创建多列列表
                self.frame,
                area=area,
                height=10,
                anchor='w',
                width=(80,380),
                padding=(10,5,10,20),
                command=self.details
                )
        else:
            self.tv=multipleList( #创建多列列表
                self.frame,
                area=area,
                data=self.data,
                height=10,
                anchor='w',
                width=(80,380),
                padding=(10,5,10,20),
                command=self.details
                )
        self.tv.pack()
        
    def close(self):
        self.frame.destroy()
        Main_page(self.root)
    
    def empty(self): #清空全部
        items=self.tv.get_children()
        for i in items:
            self.tv.delete(i)
    
    def enterData(self):
        if(len(self.entry1.get())!=0 and len(self.entry2.get())!=0):
            name=self.entry1.get()
            value=self.entry2.get()
            self.tv.insert('','end',values=(name,value))
            self.entry1.delete(0,'end')
            self.entry2.delete(0,'end')
            
        elif(len(self.entry1.get())==0 and len(self.entry2.get())==0):
            Warning(['请输入名称和值!'],1)
            
        elif(len(self.entry1.get())==0):
            self.entry2.delete(0,'end')
            Warning(['请输入名称!'],1)
            
        else:
            self.entry1.delete(0,'end')
            Warning(['请输入值!'],1)

    def delete(self): #删除选中项
        for i in self.tv.selection():
            self.tv.delete(i)

    def save(self):
        self.data=[]
        
        for i in self.tv.get_children():
            self.data.append(self.tv.item(i,'values'))
            
        write_data(frozen_dir.app_path()+'/cookie.txt','w+',self.data)
        Warning(['已保存!'],1)
        
    def details(self,event): #显示选项详情
        item=self.tv.item(
            self.tv.focus(),
            'values')
        name='名称: '+item[0]
        value='值: '+item[1]
        Warning((name,value),2)
'''
class Download_page:
    def __init__(self,master):
        self.width=700
        self.height=400
        
        self.root=master
        self.root.title('下载')
        
        try:
            data=get_data(frozen_dir.app_path()+'/linksAll.txt','r',3)
            
        except FileNotFoundError:
            Warning(['请先更新数据!'],1)
            Main_page(self.root)   
            
        else:
            if len(data)!=0:
                self.root.geometry(str(self.width)+'x'+str(self.height+28))
                
                self.frame=tk.Frame( #用于切换页面
                    self.root,
                    width=self.width,
                    height=self.height+30)
                self.frame.pack()
                
                back=tk.Button( #左上角返回按钮
                    self.frame,
                    text='返回',
                    width=6,
                    command=self.change)
                back.place(x=9,y=3)
                
                sframe=scrollable_frame(
                    self.frame,
                    scrollregion=(0,0,0,len(data)*20))  
                sframe.frame.place(
                    x=0,
                    y=28,
                    width=self.width,
                    height=self.height)
                
                self.list=multipleList(
                    sframe.child,
                    area=('名称','大小'),
                    data=data,
                    width=(555,111),
                    height=len(data),
                    anchor=('w','e'),
                    padding=(5,5,5,5),
                    command=self.open_url
                    )
                self.list.pack()
                
                sframe.on_mousewheel(self.list,'v')
            
            else:
                Warning(['没有数据!','(请检查网址是否输入正确或者Cookie是否输入正确)'],2)
                Main_page(self.root)
        
    def open_url(self,event):
        link=self.list.item(
            self.list.focus(),
            'values')[2]
        wb.open(link,new=0)

    def change(self):
        self.frame.destroy()
        Main_page(self.root)

root=tk.Tk()
#cmd('''/usr/bin/osascript -e 'tell app"Finder" to set frontmost of process"Python" to true' ''') #mac上用AppleEvent获得焦点
root.resizable(0,0)
sw=root.winfo_screenwidth()//2
sh=root.winfo_screenheight()//2
root.geometry('+{}+{}'.format(sw-270,sh-210))
Main_page(root)
window_focus(root)
root.mainloop()
