from tkinter import*
import time
import os
import tkinter.messagebox

def directory():
    '''This function sets the directory to the defined path.This path 
    is where all your files will be saved.'''
    path="C:/Users/SOUMYA/new/entries" 
    os.chdir(path)
directory()



class window(Frame):
    '''This class contains the widgets that will allow user to write into files'''
    
    def __init__(self,master=None):
        #intialisation of the frame
        Frame.__init__(self,master)
        self.master=master
        self.master.title("Diary")
        title=Label(self.master,text="Title").pack()

         #Entry box to get title of the file from the user.
        self.title_box=Entry(self.master)
        self.title_box.pack()


        #Text for the user to write his thoughts
        self.content_box=Text(self.master)
        self.content_box.pack()
    

        #This button is binded to the function "save_file" wich saves the file in the specified path'''
        save_button=Button(self.master,text="Save",width=10,command=self.save_file).pack()

        menu = Menu(self.master)
        self.master.config(menu=menu, bd=5)
# Menu bar

    
    # Options
        options = Menu(menu, tearoff=0)
        menu.add_cascade(label="Options", menu=options)

    # font
        font = Menu(options, tearoff=0)
        options.add_cascade(label="Font", menu=font)
        font.add_command(label="Default",command=self.font_change_default)
        font.add_command(label="Times",command=self.font_change_times)
        font.add_command(label="System",command=self.font_change_system)
        font.add_command(label="Helvetica",command=self.font_change_helvetica)
        font.add_command(label="Fixedsys",command=self.font_change_fixedsys)


      
        help_option = Menu(menu, tearoff=0)
        menu.add_cascade(label="Help", menu=help_option)
        help_option.add_command(label="About Empurple", command=self.msg)
        help_option.add_command(label="Developers", command=self.about)
    
    def msg(self):
        tkinter.messagebox.showinfo("Empurple v1.0",'Empurple is your virtual diary. Your personal space where you could express yourself!')

    def about(self):
        tkinter.messagebox.showinfo("Empurple Developers","1.Soumya Srivastava\n2.Harleen Kaur")
    


       

    def save_file(self):
        '''This function saves the content written by the user as a text file'''

        localtime=time.asctime(time.localtime(time.time()))
        date=localtime[8:11]
        month=localtime[4:7]
        year=localtime[20:24]
        file_name=self.title_box.get()+" "+date+month+year+".txt"
        f=open(file_name,"w+")
        f.write(self.content_box.get("1.0",END))
        tkinter.messagebox.showinfo("Diary","Your file is saved successfully!!")

    def font_change_default(self):
        self.title_box.config(font="Verdana 10")
        self.content_box.config(font="Verdana 10")
        self.font = "Verdana 10"

    def font_change_times(self):
        self.title_box.config(font="Times")
        self.content_box.config(font="Times")
        self.font = "Times"

    def font_change_system(self):
        self.title_box.config(font="System")
        self.content_box.config(font="System")
        self.font = "System"

    def font_change_helvetica(self):
        self.title_box.config(font="helvetica 10")
        self.content_box.config(font="helvetica 10")
        self.font = "helvetica 10"

    def font_change_fixedsys(self):
        self.title_box.config(font="fixedsys")
        self.content_box.config(font="fixedsys")
        self.font = "fixedsys"

    

    # Default font and color theme
    def default_format(self):
        self.font_change_default()
       

       
