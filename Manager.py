# ------------------------------------------------------------------All Modules-------------------------------------------------------------

from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg 
from PIL import Image, ImageTk
from cryptography.fernet import Fernet
from random import *
import os,pickle
# -------------------------------------------------------------------GLOBAL------------------------------------------------------------------

fa = None


# -------------------------------------------------------------------GUI CLASS-----------------------------------------------------------------
class SampleApp(Tk): #importing tkinter to the class
    def __init__(self):
        Tk.__init__(self)
        global theme,show_img,hide_img #this will create some additional global variable

        if os.path.isfile('data/app data/app_data.p'): # This program will first find the availability of theme pickle file in data folder or not and set the theme global variable according to it
            f1 = open('data/app data/app_data.p','rb')
            theme = pickle.load(f1)
            f1.close()
        else:
            theme=2
        # Default theme is dark theme

        self.title('Password Manager')
        self.geometry('710x600')
        self.wm_iconbitmap("data/img/icon.ico")
        if theme == 1:
            self.light()
        elif theme == 2:
            self.dark()

        global user,passs # Settings up the user and password variable 
        user=StringVar()
        passs=StringVar()
        user.set('a')

        menubar = MenuBar(self) # Configuring the menubar at top
        self.config(menu=menubar)

        # self.back_img=ImageTk.PhotoImage(Image.open('data/img/back2.png'))
        show_img= ImageTk.PhotoImage(Image.open('data/img/show.png'))
        hide_img= ImageTk.PhotoImage(Image.open('data/img/hide.png'))
        self._frame = None
        self.switch_frame(Login_page)



    def switch_frame(self, frame_class): # Function will help to switching between frame
        global new_frame
        new_frame = frame_class(self) # which ever frame name will put inside it it will get pack 
        if self._frame is not None:
            self._frame.destroy() # destroying the previous frame it is there
        self._frame = new_frame
        self._frame.pack(anchor='center')
    
    # Settings up the theme colours 

    def dark(self):    
        global bg_color,fg_color,menu_fg
        bg_color='gray10'
        fg_color='hotpink'
        menu_fg="snow"
        self.config(bg='gray10')

    def light(self):
        global bg_color,fg_color,menu_fg
        bg_color='white'
        fg_color='hotpink'
        menu_fg='black'
        self.config(bg=bg_color)

# -----------------------------------------------------------------------MENU----------------------------------------------------------------
class MenuBar(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)
        global theme

        fileMenu = Menu(self, tearoff=False,bg='white',fg='black',activeforeground='black',activebackground='slateblue')
        self.add_cascade(label="Tools",underline=0, menu=fileMenu)
        fileMenu.add_command(label="Login", underline=1,command=lambda : parent.switch_frame(Login_page))
        fileMenu.add_command(label="Sign up", underline=1,command= lambda : parent.switch_frame(sign_up_page))
        fileMenu.add_command(label="Delete Account", underline=1,command= lambda : parent.switch_frame(Delete_acc))
        fileMenu.add_command(label="Password Generator", underline=1,command= lambda : parent.switch_frame(select_Generator))
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", underline=1,command= lambda : parent.destroy())

        def restart_program():
            python = sys.executable
            os.execl(python, python, * sys.argv)

        def temp_light():
            global theme
            theme=1
            parent.light()
            parent.switch_frame(fa)

            # new_frame.pack()
            # msg.showinfo("RESTART", 'Please relogin the Application')
        def temp_dark():
            global theme
            theme=2
            parent.dark()
            parent.switch_frame(fa)
            # new_frame.pack()
           
            # msg.showinfo("RESTART", 'Please relogin the Application')


        fileMenu2 = Menu(self, tearoff=False,bg='white',fg='black',activeforeground='black',activebackground='slateblue')
        self.add_cascade(label="Settings",underline=0, menu=fileMenu2)
        sub_menu=Menu(fileMenu2,tearoff=False,bg='white',fg='black',activeforeground='black',activebackground='slateblue')
        sub_menu.add_command(label='Light',underline=1,command= lambda :  temp_light())
        sub_menu.add_command(label='Dark',underline=1,command= lambda : temp_dark())
        fileMenu2.add_cascade(label="Theme",underline=0, menu=sub_menu)
        fileMenu2.add_command(label="About",underline=0,command= lambda : msg.showinfo('Info','This application is created by AKG\n              MADE IN INDIA'))

# ---------------------------------------------------------------------------------------------------------------------------------------------
        





class Login_page(Frame,Menu):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg=bg_color)

        global fa 
        fa=Login_page

        Style1 =  ttk.Style()
        Style1.configure('TLabel',background=bg_color,foreground=fg_color)
        Style2=ttk.Style().configure('login.TLabel',background=bg_color,foreground=fg_color,font='Helvetica 30 bold')

        global user,passs
        user=StringVar()
        passs=StringVar()

        frame1=Frame(self,bg=bg_color)
        frame1.grid(row=0,column=0)

        self.login_img= ImageTk.PhotoImage(Image.open('data/img/login.png'))

        ttk.Label(frame1,image=self.login_img,).grid(row=0,column=0,pady=(150,5))
        ttk.Label(frame1,text='LOGIN',style='login.TLabel').grid(row=0,column=1,pady=(150,5),padx=(8,0))

        frame3=Frame(self,bg=bg_color)
        frame3.grid(row=1,column=0)
        ttk.Label(frame3,text='USERNAME',style='TLabel').grid(row=1,column=0,pady=(50,10))
        ttk.Label(frame3,text='PASSWORD ',style='TLabel').grid(row=2,column=0,)
        ttk.Entry(frame3,textvariable=user,width=20).grid(row=1,column=2,pady=(50,10),padx=(20,10))
        p=ttk.Entry(frame3,textvariable=passs,width=20)
        p.grid(row=2,column=2,padx=(12,2))
        p.config(show='*')
        self.x=1
        def view_pass(a):
            global x
            if a==1: #p.configure(show='*'):
                p.config(show='')
                self.x=a+1
                # b['text']='H'
                b['image']=hide_img
            elif a==2:#p.configure(show=''):
                p.config(show='*')
                self.x=a-1
                # b['text']='S'
                b['image']=show_img
            
        # show_style=ttk.Style()
        # show_style.configure('s.TButton',borderwidth=0,bd=0,background=)
        b=Button(frame3,text='S',command=lambda:view_pass(self.x),width=0,image=show_img,bd=0)
        b.grid(row=2,column=3)




        style=ttk.Style()
        style.configure('a.TButton',background=fg_color,borderwidth=10)

        frame2= Frame(self,bg=bg_color)
        frame2.grid(row=2,column=0,pady=20)            
        ttk.Button(frame2,text='Sign Up',command=lambda: master.switch_frame(sign_up_page),style='a.TButton').pack(side=LEFT,padx=8)
        ttk.Button(frame2,text='Login',command=lambda: self.enter(master),style='a.TButton').pack(side=RIGHT,padx=8)


    def enter(self,master):
        if os.path.isfile(f'data/user data/{user.get()}_pass_file.p'):
            with open(f'data/user data/{user.get()}_pass_file.p','rb') as f:
                listt=pickle.load(f)
            a=decrypt_(listt[0],user.get())
            b=decrypt_(listt[1],user.get())
            if user.get() == a and passs.get()==b:
                master.switch_frame(Manager_Page)
            else:
                    msg.showerror('Wrong',"Wrong user or password")
                    user.set('')
                    passs.set('')
        else:
            msg.showerror('Wrong',"Wrong user or password")
            user.set('')
            passs.set('')











class sign_up_page(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg=bg_color)
        global fa 
        fa=sign_up_page

        global newuser,newpasss
        newuser=StringVar()
        newpasss=StringVar()

        frame1=Frame(self,bg=bg_color)
        frame1.grid(row=0,column=0)
        frame=Frame(self,bg=bg_color).grid(row=0,column=2)
        style=ttk.Style()
        style.configure('TButton',background='slateblue',borderwidth=10)

        Style1 =  ttk.Style()
        Style1.configure('TLabel',background=bg_color,foreground='slateblue')
        Style2=ttk.Style().configure('login.TLabel',background=bg_color,foreground='slateblue',font='Helvetica 30 bold')
        self.signup_img= ImageTk.PhotoImage(Image.open('data/img/signup.png'))
        
        ttk.Label(frame1,image=self.signup_img).grid(row=0,column=0,pady=(150,5))
        ttk.Label(frame1,text='SIGN UP',style='login.TLabel').grid(row=0,column=1,pady=(150,5),padx=(8,0))

        frame3=Frame(self,bg=bg_color)
        frame3.grid(row=1,column=0)
        ttk.Label(frame3,text='NEW USERNAME',style='TLabel').grid(row=1,column=0,pady=(50,10))
        ttk.Label(frame3,text='NEW PASSWORD ',style='TLabel').grid(row=2,column=0,)
        ttk.Entry(frame3,textvariable=newuser,width=20).grid(row=1,column=2,pady=(50,10),padx=(20,10))
        p=ttk.Entry(frame3,textvariable=newpasss,width=20)
        p.grid(row=2,column=2,padx=(20,10))
        p.config(show="")
        self.x=2
        def view_pass(a):
            if a==1: #p.configure(show='*'):
                p.config(show='')
                self.x=a+1
                b['image']=hide_img
            elif a==2:#p.configure(show=''):
                p.config(show='*')
                self.x=a-1
                b['image']=show_img
        b=Button(frame3,text='S',command=lambda:view_pass(self.x),bd=0,image=hide_img)
        b.grid(row=2,column=3)


        frame2= Frame(self,bg=bg_color)
        frame2.grid(row=2,column=0,pady=20)            
        ttk.Button(frame2,text='Sign Up',command=lambda: self.sign_up(master),style='TButton').grid(row=0,column=0)
        ttk.Button(frame2,text='Back',command=lambda: master.switch_frame(Login_page),style='TButton').grid(row=0,column=1,padx=20)


    def sign_up(self,master):
        if newuser.get() == '' or len(newpasss.get()) < 8:
            msg.showerror('Invalid Input','Please Enter Valid Username or\nPassword must be of 8 digit or More than That')
        else:
            import tkinter.filedialog as tf
            genwrite_key(newuser.get())

            a=encrypt_(newuser.get(),newuser.get())
            b=encrypt_(newpasss.get(),newuser.get())
            
            with open(f'data/user data/{newuser.get()}_pass_file.p','wb') as f:
                pickle.dump([a,b],f)
            
            msg.showinfo('Account Added Successfull','Your Account has been Added\nPlease Login you account to access')
            master.switch_frame(Login_page)








    

class Manager_Page(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg=bg_color)

        global fa 
        fa=Manager_Page

        Style2=ttk.Style()
        Style2.configure('title.TLabel',background=bg_color,foreground=fg_color,font='Helvetica 30 bold')

        style=ttk.Style()
        style.configure('TButton',background='slateblue',borderwidth=10)

        frame=Frame(self,bg=bg_color)
        frame.pack(pady=(50,0))
        self.lock_img= ImageTk.PhotoImage(Image.open('data/img/manager.png'))
        title_img=ttk.Label(frame,image=self.lock_img,style='title.TLabel')
        title_img.grid(row=0,column=0,padx=10)
        title_label=ttk.Label(frame,text='PASSWORD MANAGER',style='title.TLabel')
        title_label.grid(row=0,column=1)

        but_frame=Frame(self,bg=bg_color)
        but_frame.pack()

        self.change_img= ImageTk.PhotoImage(Image.open(f"data/img/change.png"))
        self.add_img= ImageTk.PhotoImage(Image.open(f"data/img/add.png"))
        self.delete_img= ImageTk.PhotoImage(Image.open(f"data/img/delete.png"))
        self.view_img= ImageTk.PhotoImage(Image.open(f"data/img/view.png"))

        def Run(n):
            if os.path.isfile(f'data/pass data/{user.get()}_pass.p'):
                if n== 1:
                    master.switch_frame(Show_Pass)
                elif n == 2:
                    master.switch_frame(Delete_Pass)
                elif n ==3 :
                    master.switch_frame(Change_Pass)
            else:
                msg.showwarning('Nothing to show','You haven\'t save any thing')


        but1 =ttk.Button(but_frame,image=self.add_img,command=lambda : master.switch_frame(Add_Pass))
        but2=ttk.Button(but_frame,image=self.delete_img,command=lambda : Run(2))
        but3=ttk.Button(but_frame,image=self.change_img,command=lambda : Run(3))
        but4=ttk.Button(but_frame,image=self.view_img,command=lambda : Run(1))

        but1.grid(row=1,column=0,pady=(50,40),padx=(0,40))
        but2.grid(row=1,column=1,pady=(50,40),padx=(40,0))
        but3.grid(row=2,column=0,pady=(40,0),padx=(0,40))
        but4.grid(row=2,column=1,pady=(40,0),padx=(40,0))









class Show_Pass(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg=bg_color)
        root = self
        self.key=[]
        self.value=[]

        global fa 
        fa=Show_Pass

        Style3=ttk.Style()
        Style3.configure('title2.TLabel',background=bg_color,foreground=fg_color,font='Helvetica 30 bold')

        self.label_img= ImageTk.PhotoImage(Image.open('data/img/view_s.png'))
        
        title_frame=Frame(root,bg=bg_color)
        title_frame.grid(row=0,column=0)

        title_img=ttk.Label(title_frame,image=self.label_img)
        title_img.grid(row=0,column=0,padx=10)
        title_label=ttk.Label(title_frame,text='VIEW',style='title2.TLabel')
        title_label.grid(row=0,column=1,pady=30)

        root_frame=Frame(root,bg=bg_color)
        root_frame.grid(row=1,column=0)

        Scrollbar2 = ttk.Scrollbar(root_frame)
        # Scrollbar1 = ttk.Scrollbar(root_frame,orient='horizontal')     
        canvas=Canvas(root_frame,yscrollcommand=Scrollbar2.set,width=660,height=400,bg=bg_color)
        canvas.pack(side=LEFT,anchor='nw', fill=BOTH,padx=(10,0),pady=10)

        # Scrollbar1.pack(side=BOTTOM, fill=X)
        Scrollbar2.pack(side=LEFT, fill=Y,pady=10)
        # Scrollbar1.config(command=canvas.xview)
        Scrollbar2.config(command=canvas.yview)

        main_frame = Frame(canvas,bg=bg_color)
        main_frame.config(padx=10)
        main_frame2 = Frame(canvas,bg=bg_color)
        main_frame2.config(padx=10)
        canvas.create_window(0,0,window=main_frame,anchor='nw')
        with open(f'data/pass data/{user.get()}_pass.p','rb') as f:
                self.dic=pickle.load(f)

        for k,v in self.dic.items():
            self.key.append(k)
            self.value.append(v)

        style=ttk.Style()
        style.configure('TLabel',background=bg_color,foreground=fg_color,font='Helvetica 10 ')
        style1=ttk.Style()
        style1.configure('title.TLabel',background=bg_color,foreground='slateblue',font='Helvetica 11 bold')

        ttk.Label(main_frame,text=f'TYPE',style='title.TLabel').grid(row=0,column=2,padx=(0,50),pady=(10,15))
        ttk.Label(main_frame,text=f'EMAIL/PHONE NO.',style='title.TLabel').grid(row=0,column=3,padx=(0,70),pady=(0,15))
        # ttk.Label(main_frame,text=f'PHONE NO.',style='title.TLabel').grid(row=0,column=3,padx=(0,40),pady=(0,15))
        ttk.Label(main_frame,text=f'USERNAME',style='title.TLabel').grid(row=0,column=4,padx=(10,44),pady=(0,15))
        ttk.Label(main_frame,text=f'PASSWORD',style='title.TLabel').grid(row=0,column=5,padx=(20,0),pady=(0,15))

        for i in range(0,len(self.dic)):
            ttk.Label(main_frame,text=f'{i+1}]').grid(row=i+1,column=1,pady=(15,0))
            ttk.Label(main_frame,text=f'{decrypt_(self.key[i],user.get())}',style='TLabel').grid(row=i+1,column=2,padx=(10,40),pady=(15,0))
            ttk.Label(main_frame,text=f'{decrypt_(self.value[i][0],user.get())}\n{decrypt_(self.value[i][1],user.get())}',style='TLabel').grid(row=i+1,column=3,padx=(0,50),pady=(25,0)) 
            # ttk.Label(main_frame,text=f'{self.value[i][1]}',style='TLabel').grid(row=i+1,column=3,padx=(0,20)) 
            ttk.Label(main_frame,text=f'{decrypt_(self.value[i][2],user.get())}',style='TLabel').grid(row=i+1,column=4,padx=(0,30),pady=(15,0)) 
            ttk.Label(main_frame,text=f'{decrypt_(self.value[i][3],user.get())}',style='TLabel').grid(row=i+1,column=5,padx=(10,0),pady=(15,0)) 
        def back(master):
            master.switch_frame(Manager_Page)

        style=ttk.Style()
        style.configure('TButton',background='slateblue',borderwidth=5)

        ttk.Button(root,text='Back',command=lambda : back(master),style='TButton').grid(row=2,column=0)      

        root.update()
        canvas.config(scrollregion=canvas.bbox("all"))

        # return main_frame,self.dic,root










class Delete_Pass(Show_Pass):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg=bg_color)
        root = self
        key=[]
        value=[]

        global fa 
        fa=Delete_Pass

        Style3=ttk.Style()
        Style3.configure('title2.TLabel',background=bg_color,foreground=fg_color,font='Helvetica 30 bold')
        self.label_img= ImageTk.PhotoImage(Image.open('data/img/delete_s.png'))
        
        title_frame=Frame(root,bg=bg_color)
        title_frame.grid(row=0,column=0)
        title_img=ttk.Label(title_frame,image=self.label_img)
        title_img.grid(row=0,column=0,padx=10)
        title_label=ttk.Label(title_frame,text='DELETE',style='title2.TLabel')
        title_label.grid(row=0,column=1,pady=30)

        root_frame=Frame(root,bg=bg_color)
        root_frame.grid(row=1,column=0)

        Scrollbar2 = ttk.Scrollbar(root_frame)
        canvas=Canvas(root_frame,yscrollcommand=Scrollbar2.set,width=660,height=400,bg=bg_color)
        canvas.pack(side=LEFT,anchor='nw', fill=Y,padx=(10,0),pady=10)

        Scrollbar2.pack(side=LEFT, fill=Y,pady=10)
        Scrollbar2.config(command=canvas.yview)

        main_frame = Frame(canvas,bg=bg_color)
        main_frame.config(padx=10)
        main_frame2 = Frame(canvas,bg=bg_color)
        main_frame2.config(padx=10)
        canvas.create_window(0,0,window=main_frame,anchor='nw')
        with open(f'data/pass data/{user.get()}_pass.p','rb') as f:
                self.dic=pickle.load(f)

        for k,v in self.dic.items():
            key.append(k)
            value.append(v)

        style=ttk.Style()
        style.configure('TLabel',background=bg_color,foreground=fg_color,font='Helvetica 10')
        style1=ttk.Style()
        style1.configure('title.TLabel',background=bg_color,foreground='slateblue',font='Helvetica 11 bold')

        ttk.Label(main_frame,text=f'TYPE',style='title.TLabel').grid(row=0,column=1,padx=(0,50),pady=(0,15))
        ttk.Label(main_frame,text=f'EMAIL/PHONE NO.',style='title.TLabel').grid(row=0,column=2,padx=(0,70),pady=(0,15))
            # ttk.Label(main_frame,text=f'PHONE NO.',style='title.TLabel').grid(row=0,column=3,padx=(0,40),pady=(0,15))
        ttk.Label(main_frame,text=f'USERNAME',style='title.TLabel').grid(row=0,column=4,padx=(10,44),pady=(0,15))
        ttk.Label(main_frame,text=f'PASSWORD',style='title.TLabel').grid(row=0,column=5,padx=(0,0),pady=(0,15))

        for i in range(0,len(self.dic)):
            ttk.Label(main_frame,text=f'{decrypt_(key[i],user.get())}',style='TLabel').grid(row=i+1,column=1,padx=(0,40),pady=(15,0))
            ttk.Label(main_frame,text=f'{decrypt_(value[i][0],user.get())}\n{decrypt_(value[i][1],user.get())}',style='TLabel').grid(row=i+1,column=2,padx=(0,50),pady=(25,0)) 
                # ttk.Label(main_frame,text=f'{self.value[i][1]}',style='TLabel').grid(row=i+1,column=3,padx=(0,20)) 
            ttk.Label(main_frame,text=f'{decrypt_(value[i][2],user.get())}',style='TLabel').grid(row=i+1,column=4,padx=(0,30),pady=(15,0)) 
            ttk.Label(main_frame,text=f'{decrypt_(value[i][3],user.get())}',style='TLabel').grid(row=i+1,column=5,padx=(0,0),pady=(15,0))       

        Checkbutton_style = ttk.Style()
        Checkbutton_style.configure('checkbutton.TCheckbutton', background=bg_color,foreground=fg_color,)
        for i in range (0,len(self.dic)):
            globals()['checkbutton%s' % i] = IntVar()
            ttk.Checkbutton(main_frame,style='checkbutton.TCheckbutton',variable=globals()['checkbutton%s' % i],onvalue=i+1, offvalue=0).grid(row=i+1,column=0,padx=10,pady=(15,0))
        but_frame=Frame(root,bg=bg_color)
        but_frame.grid(row=2,column=0)

        def back(master):
            master.switch_frame(Manager_Page)

        def delete(self,master):
            self.delete_list=[]
            choics= msg.askquestion('Confirm','Do you really want to delete')
            if choics == 'yes':
                for i in range(0,len(self.dic)):
                    if globals()['checkbutton%s' % i].get() > 0:
                        self.delete_list.append(key[i])
                for i in self.delete_list:
                    self.dic.pop(i)
                with open(f'data/pass data/{user.get()}_pass.p','wb') as f:
                    pickle.dump(self.dic,f)
                msg.showinfo('Deleted Sucessfully', 'Selected  Passwords has been Deleted')
            else :
                pass
            master.switch_frame(Manager_Page)
        
        style=ttk.Style()
        style.configure('TButton',background='slateblue',borderwidth=0)

        b1=ttk.Button(but_frame,text='Delete',command=lambda : delete(self,master),style='TButton')
        b1.grid(row=0,column=0,padx=(0,100))
        b2=ttk.Button(but_frame,text='Back',command=lambda : back(master),style='TButton')
        b2.grid(row=0,column=1,padx=(100,0))

        root.update()
        canvas.config(scrollregion=canvas.bbox("all"))
            # def back(master):
            #         master.switch_frame(Manager_Page)
            # back(master)








class Add_Pass(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg=bg_color)

        global fa 
        fa=Add_Pass

        Style3=ttk.Style()
        Style3.configure('title2.TLabel',background=bg_color,foreground=fg_color,font='Helvetica 30 bold')
        self.label_img= ImageTk.PhotoImage(Image.open('data/img/add_s.png'))
        
        title_frame=Frame(self,bg=bg_color)
        title_frame.grid(row=0,column=0)
        title_img=ttk.Label(title_frame,image=self.label_img)
        title_img.grid(row=0,column=0,padx=10)
        add=ttk.Label(title_frame,text='ADD',style='title2.TLabel')
        add.grid(row=0,column=1,pady=30)

        self.type= StringVar()
        self.email= StringVar()
        self.phone_num= StringVar()
        self.username= StringVar()
        self.password= StringVar()

        self.type.set('')
        self.email.set('')
        self.phone_num.set('')
        self.username.set('')
        self.password.set('')



        Label_Frame=Frame(self,bg=bg_color)
        Label_Frame.grid(row=1,column=0,padx=(0,200))

        Style1 =  ttk.Style()
        Style1.configure('TLabel',background=bg_color,foreground='slateblue',font='Helvetica 11 bold')
        i=1

        type_label = ttk.Label(Label_Frame,text=f'{i}] Type:',style="TLabel")
        type_label.grid(row=0,column=0,padx=10,pady=20)
        type_Entry= ttk.Entry(Label_Frame,textvariable=self.type,width=30)
        type_Entry.grid(row=0,column=1,padx=10,pady=10)
        i +=1

        email_label = ttk.Label(Label_Frame,text=f'{i}] Email:',style="TLabel")
        email_label.grid(row=1,column=0,padx=10,pady=20)
        email_Entry= ttk.Entry(Label_Frame,textvariable=self.email,width=30)
        email_Entry.grid(row=1,column=1,padx=10,pady=10)
        i +=1

        phone_num_label = ttk.Label(Label_Frame,text=f'{i}] Phone No.:',style="TLabel")
        phone_num_label.grid(row=2,column=0,padx=10,pady=20)
        phone_num_Entry= ttk.Entry(Label_Frame,textvariable=self.phone_num,width=30)
        phone_num_Entry.grid(row=2,column=1,padx=10,pady=10)
        i +=1

        username_label = ttk.Label(Label_Frame,text=f'{i}] Username:',style="TLabel")
        username_label.grid(row=3,column=0,padx=10,pady=20)
        username_Entry= ttk.Entry(Label_Frame,textvariable=self.username,width=30)
        username_Entry.grid(row=3,column=1,padx=10,pady=10)
        i +=1

        password_label = ttk.Label(Label_Frame,text=f'{i}] Password:',style="TLabel")
        password_label.grid(row=4,column=0,padx=10,pady=20)
        password_Entry= ttk.Entry(Label_Frame,textvariable=self.password,width=30)
        password_Entry.grid(row=4,column=1,padx=10,pady=10)
        i +=1
        password_Entry.config(show='*')

        self.x=1
        def view_pass(a):
            if a==1: #p.configure(show='*'):
                password_Entry.config(show='')
                self.x=a+1
                b['image']=hide_img
            elif a==2:#p.configure(show=''):
                password_Entry.config(show='*')
                self.x=a-1
                b['image']=show_img
        b=Button(Label_Frame,text='Show',command=lambda:view_pass(self.x),image=show_img,bd=0)
        b.grid(row=4,column=2)


        but_frame=Frame(self,bg=bg_color)
        but_frame.grid(row=2,column=0,pady=20)

        style=ttk.Style()
        style.configure('TButton',background=fg_color,borderwidth=0)
        
        def clear(self):
            self.type.set('')
            self.email.set('')
            self.phone_num.set('')
            self.username.set('')
            self.password.set('')

        def back(master):
            choics= msg.askquestion('Confoirm','Do you really want to Go Back')
            if choics == 'yes':
                master.switch_frame(Manager_Page)
            else:
                pass

        def add(self,master):
            if self.type.get() == '' or self.password.get() =='':
                msg.showerror('Wrong Input', 'Please Add Password or its Type')
            else:
                if self.phone_num.get() == '':
                    self.phone_num.set('---')
                    if self.email.get() == '':
                            self.email.set('---')

                    if self.username.get() == '':
                        self.username.set('---')

                    self.dic={}
                    list_ = [encrypt_(self.email.get(),user.get()),
                    encrypt_(self.phone_num.get(),user.get()), 
                    encrypt_(self.username.get(),user.get()),
                    encrypt_(self.password.get(),user.get())]

                    if os.path.isfile(f'data/pass data/{user.get()}_pass.p'):
                        with open(f'data/pass data/{user.get()}_pass.p','rb') as f:
                            self.dic=pickle.load(f)
                    self.dic[encrypt_(self.type.get(),user.get())] = list_
                    with open(f'data/pass data/{user.get()}_pass.p','wb') as f:
                        pickle.dump(self.dic,f)
                    msg.showinfo('Add Sucessfull', 'Your Password data has been added')
                    master.switch_frame(Manager_Page)
                else:
                    try:
                        val = int(self.phone_num.get())
                        if self.email.get() == '':
                            self.email.set('---')

                        if self.username.get() == '':
                            self.username.set('---')

                        self.dic={}
                        list_ = [encrypt_(self.email.get(),user.get()),
                        encrypt_(self.phone_num.get(),user.get()),
                        encrypt_(self.username.get(),user.get()),
                        encrypt_(self.password.get(),user.get())]

                        if os.path.isfile(f'data/pass data/{user.get()}_pass.p'):
                            with open(f'data/pass data/{user.get()}_pass.p','rb') as f:
                                self.dic=pickle.load(f)
                        self.dic[encrypt_(self.type.get(),user.get())] = list_
                        with open(f'data/pass data/{user.get()}_pass.p','wb') as f:
                            pickle.dump(self.dic,f)
                        msg.showinfo('Add Sucessfull', 'Your Password data has been added')
                        master.switch_frame(Manager_Page)

                    except ValueError:
                        msg.showerror('Wrong input', 'Please Add valid Phone no')



        save_but=ttk.Button(but_frame,text='Save',style='TButton',command=lambda : add(self,master)).grid(row=0,column=0,padx=10)
        clear_but=ttk.Button(but_frame,text='All Clear',style='TButton',command=lambda: clear(self)).grid(row=0,column=1,padx=10)
        back_but=ttk.Button(but_frame,text='Back',style='TButton',command=lambda : back(master)).grid(row=0,column=2,padx=10)









class Change_Pass(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg=bg_color)
        root = self
        self.key=[]
        self.value=[]

        global fa 
        fa=Change_Pass

        Style3=ttk.Style()
        Style3.configure('title2.TLabel',background=bg_color,foreground=fg_color,font='Helvetica 30 bold')

        self.label_img= ImageTk.PhotoImage(Image.open('data/img/change_s.png'))
        
        title_frame=Frame(root,bg=bg_color)
        title_frame.grid(row=0,column=0)

        title_img=ttk.Label(title_frame,image=self.label_img)
        title_img.grid(row=0,column=0,padx=10)
        title_label=ttk.Label(title_frame,text='CHANGE',style='title2.TLabel')
        title_label.grid(row=0,column=1,pady=30)

        root_frame=Frame(root,bg=bg_color)
        root_frame.grid(row=1,column=0)

        Scrollbar2 = ttk.Scrollbar(root_frame)
        # Scrollbar1 = ttk.Scrollbar(root_frame,orient='horizontal')     
        canvas=Canvas(root_frame,yscrollcommand=Scrollbar2.set,width=660,height=400,bg=bg_color)
        canvas.pack(side=LEFT,anchor='nw', fill=BOTH,padx=(10,0),pady=10)

        # Scrollbar1.pack(side=BOTTOM, fill=X)
        Scrollbar2.pack(side=LEFT, fill=Y,pady=10)
        # Scrollbar1.config(command=canvas.xview)
        Scrollbar2.config(command=canvas.yview)

        main_frame = Frame(canvas,bg=bg_color)
        main_frame.config(padx=10)
        main_frame2 = Frame(canvas,bg=bg_color)
        main_frame2.config(padx=10)
        canvas.create_window(0,0,window=main_frame,anchor='nw')
        with open(f'data/pass data/{user.get()}_pass.p','rb') as f:
                self.dic=pickle.load(f)

        for k,v in self.dic.items():
            self.key.append(k)
            self.value.append(v)

        style=ttk.Style()
        style.configure('TLabel',background=bg_color,foreground=fg_color,font='Helvetica 10 ')
        style1=ttk.Style()
        style1.configure('title.TLabel',background=bg_color,foreground='slateblue',font='Helvetica 11 bold')

        ttk.Label(main_frame,text=f'TYPE',style='title.TLabel').grid(row=0,column=2,padx=(0,50),pady=(10,15))
        ttk.Label(main_frame,text=f'EMAIL/PHONE NO.',style='title.TLabel').grid(row=0,column=3,padx=(0,70),pady=(0,15))
        # ttk.Label(main_frame,text=f'PHONE NO.',style='title.TLabel').grid(row=0,column=3,padx=(0,40),pady=(0,15))
        ttk.Label(main_frame,text=f'USERNAME',style='title.TLabel').grid(row=0,column=4,padx=(10,44),pady=(0,15))
        ttk.Label(main_frame,text=f'PASSWORD',style='title.TLabel').grid(row=0,column=5,padx=(0,0),pady=(0,15))

        for i in range(0,len(self.dic)):
            ttk.Label(main_frame,text=f' {decrypt_(self.key[i],user.get())}',style='TLabel').grid(row=i+1,column=2,padx=(10,40),pady=(15,0))
            ttk.Label(main_frame,text=f'{decrypt_(self.value[i][0],user.get())}\n{decrypt_(self.value[i][1],user.get())}',style='TLabel').grid(row=i+1,column=3,padx=(0,50),pady=(25,0)) 
            # ttk.Label(main_frame,text=f'{self.value[i][1]}',style='TLabel').grid(row=i+1,column=3,padx=(0,20)) 
            ttk.Label(main_frame,text=f'{decrypt_(self.value[i][2],user.get())}',style='TLabel').grid(row=i+1,column=4,padx=(0,30),pady=(15,0)) 
            ttk.Label(main_frame,text=f'{decrypt_(self.value[i][3],user.get())}',style='TLabel').grid(row=i+1,column=5,padx=(0,0),pady=(15,0))

        Checkbutton_style = ttk.Style()
        Checkbutton_style.configure('checkbutton.TCheckbutton', background=bg_color,foreground=fg_color,)
        global change_item
        change_item = IntVar()
        for i in range (0,len(self.dic)):
            ttk.Checkbutton(main_frame,style='checkbutton.TCheckbutton',variable=change_item,onvalue=i, offvalue=0).grid(row=i+1,column=0,padx=10,pady=(15,0))

        def back(master):
            master.switch_frame(Manager_Page)

        def change():
            for k,v in self.dic.items():
                if k == self.key[change_item.get()]:
                    global c
                    c = change_item.get()
                    master.switch_frame(Change_pass_label)


        but_frame=Frame(root,bg=bg_color)
        but_frame.grid(row=2,column=0)

        style=ttk.Style()
        style.configure('TButton',background='slateblue',borderwidth=5)

        def back(master):
            master.switch_frame(Manager_Page)


        ttk.Button(but_frame,text='Change',command=lambda : change(),style='TButton').grid(row=0,column=0)  
        ttk.Button(but_frame,text='Back',command=lambda : back(master),style='TButton').grid(row=0,column=1,padx=(10,0))

        root.update()
        canvas.config(scrollregion=canvas.bbox("all"))













class Change_pass_label(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg=bg_color)
        self.key=[]
        self.value=[]

        global fa 
        fa=Change_pass_label

        with open(f'data/pass data/{user.get()}_pass.p','rb') as f:
                self.dic=pickle.load(f)

        for k,v in self.dic.items():
            self.key.append(k)
            self.value.append(v)



        Style3=ttk.Style()
        Style3.configure('title2.TLabel',background=bg_color,foreground=fg_color,font='Helvetica 30 bold')
        self.label_img= ImageTk.PhotoImage(Image.open('data/img/change_s.png'))
        
        title_frame=Frame(self,bg=bg_color)
        title_frame.grid(row=0,column=0)
        title_img=ttk.Label(title_frame,image=self.label_img)
        title_img.grid(row=0,column=0,padx=10)
        add=ttk.Label(title_frame,text='CHANGE',style='title2.TLabel')
        add.grid(row=0,column=1,pady=30)

        self.type= StringVar()
        self.email= StringVar()
        self.phone_num= StringVar()
        self.username= StringVar()
        self.password= StringVar()

        self.type.set(decrypt_(self.key[c],user.get()))
        self.email.set(decrypt_(self.value[c][0],user.get()))
        self.phone_num.set(decrypt_(self.value[c][1],user.get()))
        self.username.set(decrypt_(self.value[c][2],user.get()))
        self.password.set(decrypt_(self.value[c][3],user.get()))



        Label_Frame=Frame(self,bg=bg_color)
        Label_Frame.grid(row=1,column=0,padx=(0,200))

        Style1 =  ttk.Style()
        Style1.configure('TLabel',background=bg_color,foreground='slateblue',font='Helvetica 11 bold')
        i=1

        type_label = ttk.Label(Label_Frame,text=f'{i}] Type:',style="TLabel")
        type_label.grid(row=0,column=0,padx=10,pady=20)
        type_Entry= ttk.Entry(Label_Frame,textvariable=self.type,width=30)
        type_Entry.grid(row=0,column=1,padx=10,pady=10)
        i +=1

        email_label = ttk.Label(Label_Frame,text=f'{i}] Email:',style="TLabel")
        email_label.grid(row=1,column=0,padx=10,pady=20)
        email_Entry= ttk.Entry(Label_Frame,textvariable=self.email,width=30)
        email_Entry.grid(row=1,column=1,padx=10,pady=10)
        i +=1

        phone_num_label = ttk.Label(Label_Frame,text=f'{i}] Phone No.:',style="TLabel")
        phone_num_label.grid(row=2,column=0,padx=10,pady=20)
        phone_num_Entry= ttk.Entry(Label_Frame,textvariable=self.phone_num,width=30)
        phone_num_Entry.grid(row=2,column=1,padx=10,pady=10)
        i +=1

        username_label = ttk.Label(Label_Frame,text=f'{i}] Username:',style="TLabel")
        username_label.grid(row=3,column=0,padx=10,pady=20)
        username_Entry= ttk.Entry(Label_Frame,textvariable=self.username,width=30)
        username_Entry.grid(row=3,column=1,padx=10,pady=10)
        i +=1

        password_label = ttk.Label(Label_Frame,text=f'{i}] Password:',style="TLabel")
        password_label.grid(row=4,column=0,padx=10,pady=20)
        password_Entry= ttk.Entry(Label_Frame,textvariable=self.password,width=30)
        password_Entry.grid(row=4,column=1,padx=10,pady=10)
        i +=1
        password_Entry.config(show='*')

        self.x=1
        def view_pass(a):
            if a==1: #p.configure(show='*'):
                password_Entry.config(show='')
                self.x=a+1
                b['image']=hide_img
            elif a==2:#p.configure(show=''):
                password_Entry.config(show='*')
                self.x=a-1
                b['image']=show_img
        b=Button(Label_Frame,text='Show',command=lambda:view_pass(self.x),image=show_img,bd=0)
        b.grid(row=4,column=2)



        def change():

            if self.type.get() == '' or self.password.get() =='':
                msg.showerror('', 'Please Add Password or its Type')
            else:
                if self.phone_num.get() == '' or self.phone_num.get() == '---':
                    self.phone_num.set('---')

                    if self.email.get() == '':
                        self.email.set('---')

                    if self.username.get() == '':
                        self.username.set('---')

                    list_ = [encrypt_(self.email.get(),user.get()),
                    encrypt_(self.phone_num.get(),user.get()),
                    encrypt_(self.username.get(),user.get()),
                    encrypt_(self.password.get(),user.get())]

                    if os.path.isfile(f'data/pass data/{user.get()}_pass.p'):
                        with open(f'data/pass data/{user.get()}_pass.p','rb') as f:
                            self.dic=pickle.load(f)
                    self.dic.pop(self.key[c])

                    self.dic[encrypt_(self.type.get(),user.get())] = list_
                    with open(f'data/pass data/{user.get()}_pass.p','wb') as f:
                        pickle.dump(self.dic,f)
                    msg.showinfo('Add Sucessfull', 'Your Password data has been added')
                    master.switch_frame(Manager_Page)
                else:
                    try:
                        val = int(self.phone_num.get())
                        if self.email.get() == '':
                            self.email.set('---')

                        if self.username.get() == '':
                            self.username.set('---')


                        list_ = [encrypt_(self.email.get(),user.get()),
                        encrypt_(self.phone_num.get(),user.get()),
                        encrypt_(self.username.get(),user.get()),
                        encrypt_(self.password.get(),user.get())]
                        if os.path.isfile(f'data/pass data/{user.get()}_pass.p'):
                            with open(f'data/pass data/{user.get()}_pass.p','rb') as f:
                                self.dic=pickle.load(f)
                        self.dic.pop(self.key[c])

                        self.dic[encrypt_(self.type.get(),user.get())] = list_
                        with open(f'data/pass data/{user.get()}_pass.p','wb') as f:
                            pickle.dump(self.dic,f)

                        msg.showinfo('Add Sucessfull', 'Your Password data has been added')
                        master.switch_frame(Manager_Page)
                    except ValueError:
                        msg.showerror('Wrong input', 'Please Add valid Phone no')


        def back(master):
            master.switch_frame(Change_Pass)

        def clear(self):
            self.type.set('')
            self.email.set('')
            self.phone_num.set('')
            self.username.set('')
            self.password.set('')

        
        but_frame=Frame(self,bg=bg_color)
        but_frame.grid(row=2,column=0,pady=20)

        style=ttk.Style()
        style.configure('TButton',background=fg_color,borderwidth=0)

        save_but=ttk.Button(but_frame,text='Save Change',style='TButton',command=lambda : change()).grid(row=0,column=0,padx=10)
        clear_but=ttk.Button(but_frame,text='All Clear',style='TButton',command=lambda: clear(self)).grid(row=0,column=1,padx=10)
        back_but=ttk.Button(but_frame,text='Back',style='TButton',command=lambda : back(master)).grid(row=0,column=2,padx=10)








class select_Generator(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg=bg_color)

        Style3=ttk.Style()
        Style3.configure('title2.TLabel',background=bg_color,foreground=fg_color,font='Helvetica 30 bold') 

        global fa 
        fa=select_Generator     


        f= Frame(self,bg=bg_color)
        f.pack()
        self.lock_img= ImageTk.PhotoImage(Image.open('data/img/lock.png'))
        title_img=ttk.Label(f,image=self.lock_img,style='title.TLabel').grid(row=0,column=0,pady=18)
        ttk.Label(f,text='Password Generator',style='title2.TLabel').grid(row=0,column=1)


        f2=Frame(self,bg=bg_color)
        f2.pack()
        Style2=ttk.Style()
        Style2.configure('title.TLabel',background=bg_color,foreground=fg_color,font='Helvetica 20 bold')      

        self.select_label=ttk.Label(f2,text='Select Type of Password',style='title.TLabel')
        self.select_label.grid(row=0,column=0,pady=25,sticky='w')

        global select
        select=IntVar()

        Checkbutton_style2 = ttk.Style()
        Checkbutton_style2.configure('checkbutton2.TCheckbutton', background=bg_color,foreground=fg_color,padx=10, pady=10,font='Helvetica 15 bold')

        self.mix_but=ttk.Checkbutton(f2,text="Mix Password",onvalue=1, offvalue=0, variable=select,style='checkbutton2.TCheckbutton')
        self.mix_but.grid(row=1,column=0,sticky='w')

        self.aplha_num_but=ttk.Checkbutton(f2,text="Alpha Numerical Password",onvalue=2, offvalue=0, variable=select,style='checkbutton2.TCheckbutton')
        self.aplha_num_but.grid(row=2,column=0,sticky='w')

        self.num_but=ttk.Checkbutton(f2,text="Numerical Password",onvalue=3, offvalue=0, variable=select,style='checkbutton2.TCheckbutton')
        self.num_but.grid(row=3,column=0,sticky='w')


        pass_len=[8,9,10,11,12,13,14,15,16,17,18]

        len_label=ttk.Label(f2,text='Select Lenght of Password : ',style='title.TLabel')
        len_label.grid(row=4,column=0,pady=30,sticky='w')

        global n, len_
        n = IntVar() 
        len_=IntVar()
        sty=ttk.Style()
        # sty.configure('a.TCombobox',background='slateblue')
        len_ = ttk.Combobox(f2, width = 30, textvariable = len_,value=pass_len,style='a.TCombobox') 
        len_.grid(row=4,column=1,pady=0,padx=10)


        n_label=ttk.Label(f2,text='No of Password :',style='title.TLabel')
        n_label.grid(row=5,column=0,pady=0,sticky='w')

        Spinbox_style= ttk.Style()
        Spinbox_style.configure('w.TSpinbox',background=bg_color,foreground='slateblue')
        Spin=ttk.Spinbox(f2,width=30,textvariable=n,from_=1,to=20,style='w.TSpinbox')
        Spin.grid(row=5,column=1,pady=30,padx=10)

        def done():
            if n.get()==0 or select.get()==0 or len_.get()==0 or int(len_.get())<8 or int(len_.get())>18:
                msg.showerror('Incorret Value','Please Select All Values')
            else:
                master.switch_frame(Pass_Generator)
            # print(select.get())
        
        style=ttk.Style()
        style.configure('TButton',background='slateblue',borderwidth=5)

        done_but=ttk.Button(f2,text='Generate',command=done)
        done_but.grid(row=6,column=0,pady=30)

        back=ttk.Button(f2,text='Back',command=lambda : master.switch_frame(Login_page))
        back.grid(row=6,column=1,padx=10,pady=30)








        


class Pass_Generator(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg=bg_color) 

        Style3=ttk.Style()
        Style3.configure('title2.TLabel',background=bg_color,foreground=fg_color,font='Helvetica 30 bold')    

        global fa 
        fa=Pass_Generator  


        f= Frame(self,bg=bg_color)
        f.pack()
        self.lock_img= ImageTk.PhotoImage(Image.open('data/img/lock.png'))
        title_img=ttk.Label(f,image=self.lock_img,style='title.TLabel').grid(row=0,column=0,pady=18)
        ttk.Label(f,text='Password Generator',style='title2.TLabel').grid(row=0,column=1)

        frame=Frame(self,bg=bg_color,)
        frame.pack()
        Scrollbar1 = ttk.Scrollbar(frame)
        Scrollbar1.pack(side=RIGHT, fill=Y,pady=29)

        T=Text(frame,bg=bg_color,fg='slateblue',font='Helvetica 15 ',width=50,height=17,yscrollcommand=Scrollbar1.set, selectbackground='hotpink',selectforeground='snow')
        T.pack(pady=30,)
        Scrollbar1.config(command=T.yview)
        T.tag_config('p', foreground="hotpink",font='Helvetica 20 ',selectforeground='snow')
        T.insert(INSERT, f'Copy Any of Them, Length is {len_.get()}\n\n','p')

        if select.get() == 1:
            for i in range (0,n.get()):
                T.insert(INSERT, f'{i+1}]   {self.mix_generate()}\n\n')
        elif select.get() == 2:
            for i in range (0,n.get()):
                T.insert(INSERT, f'{i+1}]   {self.alph_num_generate()}\n\n')
        elif select.get() == 3:
            for i in range (0,n.get()):
                T.insert(INSERT, f'{i+1}]   {self.num_generate()}\n\n')
        

        fa=Frame(self,bg=bg_color)
        fa.pack()

        style=ttk.Style()
        style.configure('TButton',background='slateblue',borderwidth=5)

        ttk.Button(fa,text='Back',style="TButton",command= lambda : master.switch_frame(select_Generator)).grid(row=0,column=0)
        ttk.Button(fa,text='Login',style="TButton",command= lambda : master.switch_frame(Login_page)).grid(row=0,column=1,padx=20)

    

    @staticmethod
    def mix_generate():
        import string

        symbol='@#$%*!_?\/)([]}{'
        characters = string.ascii_letters + string.digits + symbol
        password =  "".join(choice(characters) for x in range(randint(int(len_.get()), int(len_.get()))))
        
        return str(password)
    @staticmethod
    def alph_num_generate():
        import string

        # symbol='@#$%*!_?\/)([]}{'
        characters = string.ascii_letters + string.digits 
        password =  "".join(choice(characters) for x in range(randint(int(len_.get()), int(len_.get() ))))

        return str(password)
    @staticmethod
    def num_generate():
        import string

        # symbol='@#$%*!_?\/)([]}{'
        characters = string.digits
        password =  "".join(choice(characters) for x in range(randint(int(len_.get()), int(len_.get()))))
        
        return str(password)









class Delete_acc(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg=bg_color)

        global fa 
        fa=Delete_acc


        Style1 =  ttk.Style()
        Style1.configure('TLabel',background=bg_color,foreground=fg_color)
        Style2=ttk.Style().configure('login.TLabel',background=bg_color,foreground=fg_color,font='Helvetica 30 bold')

        global user,passs
        user=StringVar()
        passs=StringVar()

        frame1=Frame(self,bg=bg_color)
        frame1.grid(row=0,column=0)

        self.acc_delete_img= ImageTk.PhotoImage(Image.open('data/img/acc_delete.png'))

        ttk.Label(frame1,image=self.acc_delete_img,).grid(row=0,column=0,pady=(100,10))
        ttk.Label(frame1,text='Delete Account',style='login.TLabel').grid(row=0,column=1,pady=(100,10),padx=(8,0))

        frame3=Frame(self,bg=bg_color)
        frame3.grid(row=1,column=0)
        ttk.Label(frame3,text='USERNAME',style='TLabel').grid(row=1,column=0,pady=(50,10))
        ttk.Label(frame3,text='PASSWORD ',style='TLabel').grid(row=2,column=0,)
        ttk.Entry(frame3,textvariable=user,width=20).grid(row=1,column=2,pady=(50,10),padx=(20,10))
        ttk.Entry(frame3,textvariable=passs,width=20).grid(row=2,column=2,padx=(20,10))

        style=ttk.Style()
        style.configure('TButton',background=fg_color,borderwidth=10)

        frame2= Frame(self,bg=bg_color)
        frame2.grid(row=2,column=0,pady=20)            
        b1=ttk.Button(frame2,text='Sign Up',command=lambda: master.switch_frame(sign_up_page),style='TButton')
        b1.grid(row=0,column=0,pady=20,padx=10)
        b2=ttk.Button(frame2,text='Login',command=lambda: master.switch_frame(Login_page),style='TButton')
        b2.grid(row=0,column=1,pady=20,padx=10)
        b3=ttk.Button(frame2,text='Delete',command=lambda: self.enter(master),style='TButton')
        b3.grid(row=0,column=2,pady=20,padx=10)


    def enter(self,master):
        if os.path.isfile(f'data/user data/{user.get()}_pass_file.p'):
            with open(f'data/user data/{user.get()}_pass_file.p','rb') as f:
                listt=pickle.load(f)
            if user.get() == listt[0] and passs.get()==listt[1]:
                self.delete()
                master.switch_frame(Login_page)
            else:
                    msg.showerror('Wrong',"Wrong user or password")
                    user.set('')
                    passs.set('')
        else:
            msg.showerror('Wrong',"Wrong user or password")
            user.set('')
            passs.set('')

    def delete(self):
        os.remove(f'data/user data/{user.get()}_pass_file.p')
        if os.path.isfile(f'data/pass data/{user.get()}_pass.p'):
            os.remove(f'data/pass data/{user.get()}_pass.p')

# ------------------------------------------------------------------GLOBAL FUNCTIONS-----------------------------------------------------------


def genwrite_key(username):
        key = Fernet.generate_key()
        with open(f"data/key/{username}.key", "wb") as key_file:
            key_file.write(key)

def call_key(user):
        return open(f"data/key/{user}.key", "rb").read()

        
def encrypt_(msg,username):
        key = call_key(username)
        slogan = msg.encode()
        a = Fernet(key)
        coded_slogan = a.encrypt(slogan)
        return coded_slogan

def decrypt_(msg,user):
        key = call_key(user)
        b = Fernet(key)
        decoded_slogan = b.decrypt(msg)
        decoded_slogan=decoded_slogan.decode('utf-8')
        return decoded_slogan

            


# -----------------------------------------------------------------------MAIN------------------------------------------------------------------

if __name__ == "__main__":
    
    app = SampleApp()
    app.mainloop()

    f1= open('data/app data/app_data.p','wb')
    pickle.dump(theme,f1)
    f1.close()
