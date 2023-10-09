from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import glob

class VCapp:
    def __init__(self):
        self.root = Tk()
        self.root.title('Visual Classifier')

        # select the path
        self.path = StringVar()
        self.path.set(os.path.abspath('.'))

        self.frame1_open_folder = Frame(self.root)
        self.frame1_open_folder.pack()
        b1 = Button(self.frame1_open_folder,text='Select directory',command=self.selectPath).pack(side='left')
        self.text_folder = Entry(self.frame1_open_folder,textvariable=self.path,state='readonly').pack(side='left')

        # read all the images in the folder
        b2 = Button(self.frame1_open_folder,text='Open',command=self.openPath).pack(side='left')

        # buttons
        self.frame2_classification = Frame(self.root)
        self.frame2_classification.pack()

        self.results_list=[]
        self.ii = 0
        b_true = Button(self.frame2_classification,text='True',command=self.clickTrue).pack(side='left')
        b_false = Button(self.frame2_classification,text='False',command=self.clickFalse).pack(side='left')
        b_other = Button(self.frame2_classification,text='Other',command=self.clickOther).pack(side='left')

        # 上一张
        back = Button(self.root,text='back←',command=self.back).pack()

        # quit Button
        b_quit = Button(self.root,text='Quit',command=self.saveAndQuit)
        b_quit.pack()

        # openimg = Button(self.root,text='Open',command=self.openfile)
        # openimg.pack()

        self.root.mainloop()
        self.root.destroy()


    def selectPath(self):
        path_ = filedialog.askdirectory()
        if path_ == '':
            self.path.get()
        else:
            path_ = path_.replace('/','\\')
            self.path.set(path_)

    def openPath(self):
        dir = os.path.dirname(self.path.get()+'\\')
        # print(dir)
        self.imglist = glob.glob(self.path.get()+'\*.jpg')+glob.glob(self.path.get()+'\*.png')  # read jpg and png files
        self.img_num = len(self.imglist)
        # print(self.imglist)
        self.openfile()
        
    def openfile(self):
        # filepath = filedialog.askopenfilename(filetypes=[(('JPG','*.jpg')),(('PNG','*,png'))])
        filepath = self.imglist[self.ii]
        img_open = Image.open(filepath)
        self.show_name = Label(self.root,text='%s'%filepath)
        self.show_name.pack()
        self.image = ImageTk.PhotoImage(img_open)
        self.label_img = Label(self.root,image=self.image)
        self.label_img.pack()

    def clickTrue(self):
        self.results_list.append('True')
        self.label_img.destroy()
        self.show_name.destroy()
        self.ii += 1
        if self.ii < self.img_num:
            self.openfile()
        else:
            self.saveAndQuit()

    def clickFalse(self):
        self.results_list.append('False')
        self.label_img.destroy()
        self.show_name.destroy()
        self.ii += 1
        if self.ii < self.img_num:
            self.openfile()
        else:
            self.saveAndQuit()

    def clickOther(self):
        self.results_list.append('Other')
        self.label_img.destroy()
        self.show_name.destroy()
        self.ii += 1
        if self.ii < self.img_num:
            self.openfile()
        else:
            self.saveAndQuit()

    def back(self):
        self.ii -= 1
        self.results_list.pop()
        self.label_img.destroy()
        self.show_name.destroy()
        self.openfile()

    def saveAndQuit(self):
        file0 = open(self.path.get()+'\\file_names.txt','w')
        file0.writelines([line+'\n' for line in self.imglist])
        file0.close()
        file1 = open(self.path.get()+'\\classification_results.txt','w')
        file1.writelines([line+'\n' for line in self.results_list])
        file1.close()
        self.root.quit()


app = VCapp()