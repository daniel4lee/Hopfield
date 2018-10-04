import numpy.matlib
import numpy as np
import tkinter as tk
from tkinter import ttk, Button, Label, Entry, Tk, LabelFrame, Frame, Button
import tkinter.scrolledtext as tkst
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from random import *
import matplotlib as mpl
from matplotlib import cm
def cr(a,b):
    t=0
    for i in range(100):
        if a[0,i]==b[0,i]:
            t+=1
    return t
def rbm(il):
    with open('Bonus_Training.txt','r') as f:
        for k, line in enumerate(f):
            if k<10:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[0][k*10+i]=int(1)
            elif k> 10 and k < 21:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[1][(k-11)*10+i]=int(1)
            elif k> 21 and k < 32:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[2][(k-22)*10+i]=int(1)
            elif k> 32 and k < 43:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[3][(k-33)*10+i]=int(1)
            elif k> 43 and k < 54:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[4][(k-44)*10+i]=int(1)
            elif k>54 and k<65:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[5][(k-55)*10+i]=int(1)
            elif k> 65 and k < 76:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[6][(k-66)*10+i]=int(1)
            elif k> 76 and k < 87:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[7][(k-77)*10+i]=int(1)
            elif k> 87 and k < 98:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[8][(k-88)*10+i]=int(1)
            elif k> 98 and k < 109:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[9][(k-99)*10+i]=int(1)
            elif k>109 and k<120:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[10][(k-110)*10+i]=int(1)
            elif k> 120 and k < 131:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[11][(k-121)*10+i]=int(1)
            elif k> 131 and k < 142:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[12][(k-132)*10+i]=int(1)
            elif k> 142 and k < 153:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[13][(k-143)*10+i]=int(1)
            elif k> 153 and k < 164:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[14][(k-154)*10+i]=int(1)
def rtestbm(il):
    with open('Bonus_Testing.txt','r') as f:
        for k, line in enumerate(f):
            if k<10:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[0][k*10+i]=int(1)
            elif k> 10 and k < 21:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[1][(k-11)*10+i]=int(1)
            elif k> 21 and k < 32:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[2][(k-22)*10+i]=int(1)
            elif k> 32 and k < 43:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[3][(k-33)*10+i]=int(1)
            elif k> 43 and k < 54:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[4][(k-44)*10+i]=int(1)
            elif k>54 and k<65:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[5][(k-55)*10+i]=int(1)
            elif k> 65 and k < 76:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[6][(k-66)*10+i]=int(1)
            elif k> 76 and k < 87:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[7][(k-77)*10+i]=int(1)
            elif k> 87 and k < 98:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[8][(k-88)*10+i]=int(1)
            elif k> 98 and k < 109:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[9][(k-99)*10+i]=int(1)
            elif k>109 and k<120:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[10][(k-110)*10+i]=int(1)
            elif k> 120 and k < 131:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[11][(k-121)*10+i]=int(1)
            elif k> 131 and k < 142:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[12][(k-132)*10+i]=int(1)
            elif k> 142 and k < 153:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[13][(k-143)*10+i]=int(1)
            elif k> 153 and k < 164:
                for i in range(len(line)):
                    if line[i]=='1':
                        il[14][(k-154)*10+i]=int(1)
def train(w,theta,test):
    same=False
    times=0
    temp=np.dot(w,test)-theta
    ans=np.zeros(100)
    ans=ans.reshape([100,1])
    for i in range(100):
        if temp[i,0] > 0:
            ans[i,0]=1
        elif temp[i, 0]==0:
            ans[i, 0]=test[i,0]
        else:
            ans[i,0]=-1
    while(same==False):
        temp=np.dot(w,ans)-theta
        times+=1
        for i in range(100):
            if temp[i,0]>0:
                temp[i,0]=1
            elif temp[i, 0]==0:
                temp[i, 0]=ans[i,0]
            elif temp[i, 0]<0:
                temp[i,0]=-1
        for i in range(100):
            if ans[i, 0]!=temp[i,0]:
                same = False
                break
            else:
                same= True
        for i in range(100):
            ans[i, 0]=temp[i,0]
    m.txt.output.insert(tk.INSERT,'iteration times: {}'.format(times+1)+'\n')
    return(ans.reshape([10,10]))
"""
GUI
"""
class MainApplication(tk.Frame):
    """
    option frame
    """
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.mainapp=Frame(self)
        self.mainapp.pack(side='top')
        self.lf_file = LabelFrame(self.mainapp, text=" File: ",background='gray85',font='Helvetica 12 bold')
        self.lf_file.pack(ipady=5,ipadx=10,expand=True,fill=tk.X)

        self.diff = tk.StringVar()
        self.diffchosen = ttk.Combobox(self.lf_file, width=10, textvariable=self.diff,state='readonly')
        self.diffchosen['values'] = ["bonus"]
        self.diffchosen.pack(side=tk.LEFT,padx=15)
        self.diffchosen.current(0)

        self.lf_convergence = LabelFrame(self.mainapp, text=" Test data: ",background='gray85',font='Helvetica 12 bold')
        self.lf_convergence.pack(fill=tk.X)

        self.f_1=Frame(self.lf_convergence,background='gray85')
        self.f_1.pack(ipadx=5)
        self.varc = tk.IntVar()
        self.varc.set(1)
        tk.Radiobutton(self.f_1, text = "default training data                        ",background='gray85',variable=self.varc, value=1,
        command=self.ShowChoice).pack(side=tk.LEFT)

        self.f_2=Frame(self.lf_convergence,background='gray85')
        self.f_2.pack(ipadx=5)
        tk.Radiobutton(self.f_2, text = 'random probability 1 / ',background='gray85',variable=self.varc, value=2,
        command=self.ShowChoice).pack(side=tk.LEFT)

        self.correctrate = tk.StringVar()
        self.correctrate.set("2")
        self.correctrateenter = ttk.Entry(self.f_2, width=8, textvariable=self.correctrate,state='readonly')
        self.correctrateenter.pack(side=tk.LEFT)
        self.correctrateenter.focus()

        self.lf_exe = LabelFrame(self.mainapp, text=" Execution: ",background='gray85',font='Helvetica 12 bold')
        self.lf_exe.pack(fill=tk.X)
        self.run = tk.Button(master=self.lf_exe, text='test', command=self.exe,width=15, relief=tk.GROOVE,background='gray85')
        self.run.pack(padx=15,side='left')
        self.quit = tk.Button(master=self.lf_exe, text='exit', command=self.quit,width=15,background='gray85',padx=5, relief=tk.GROOVE)
        self.quit.pack(padx=15,side='left')
        self.rlt=[]
        for i in range(15):
            self.rlt.append(np.zeros(100))
        for i in range(100):
            for j in range(15):
                self.rlt[j][i]=-1
        rbm(self.rlt)
        for i in range(15):
            self.rlt[i]=(self.rlt[i]).reshape([100,1])
    def ShowChoice(self):
        for i in range(15):
            ploter.plottl[i].clear()
            ploter.plottl[i].axis('off')
        cmap = mpl.colors.ListedColormap(['black','grey'])
        bounds=[-1,0,1]
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
        for i in range(100):
            for j in range(15):
                self.rlt[j][i][0]=l[j][i][0]
        if(self.varc.get()==1):
            for i in range(15):
                ploter.plottl[i].set_title("                     test{}".format(i))
                ploter.plottl[i].imshow(lt[i].reshape([10,10]),interpolation='nearest',
                    cmap = cmap,norm=norm)
                ploter.plottl[i].axis('off')
            ploter.canvas.show()
        else:
            self.correctrateenter.config(state="NORMAL")
            rnum=int(self.correctrate.get())
            for i in range(100):
                for j in range(15):
                    if randrange(rnum) == 0:
                        if self.rlt[j][i][0]==1:
                            self.rlt[j][i][0]=-1
                        else:
                            self.rlt[j][i][0]=1
            for i in range(15):
                ploter.plottl[i].set_title("                     test{}".format(i))
                ploter.plottl[i].imshow(self.rlt[i].reshape([10,10]),interpolation='nearest',
                                    cmap = cmap,norm=norm)
                ploter.plottl[i].axis('off')
            ploter.canvas.show()
    def exe(self):
        for i in range(15):
            ploter.plottl[i].clear()
            ploter.plottl[i].axis('off')
        cmap = mpl.colors.ListedColormap(['black','grey'])
        bounds=[-1,0,1]
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
        lforc=l[i].reshape([1,100])
        i=0
        if(self.varc.get()==1):
            for i in range(15):
                m.txt.output.configure(state=tk.NORMAL)
                m.txt.output.insert(tk.INSERT,'test data {}:'.format(i)+'\n')
                tempa=train(w,theta,lt[i])
                ploter.plottl[i].set_title("                     test{}".format(i))
                ploter.plottl[i].imshow(tempa,interpolation='nearest',
                    cmap = cmap,norm=norm)
                ploter.plottl[i].axis('off')
                tempa=tempa.reshape([1,100])
                m.txt.output.insert(tk.INSERT,'correct rate: {}％'.format(cr(tempa,lforc))+'\n')
                m.txt.output.configure(state=tk.DISABLED)
                m.txt.output.see(tk.END)
            ploter.canvas.show()
        else:
            for i in range(15):
                m.txt.output.configure(state=tk.NORMAL)
                m.txt.output.insert(tk.INSERT,'test data {}:'.format(i)+'\n')
                tempa=train(w,theta,self.rlt[i])
                ploter.plottl[i].set_title("                     test{}".format(i))
                ploter.plottl[i].imshow(tempa,interpolation='nearest',
                    cmap = cmap,norm=norm)
                ploter.plottl[i].axis('off')
                tempa=tempa.reshape([1,100])
                m.txt.output.insert(tk.INSERT,'correct rate: {}％'.format(cr(tempa,lforc))+'\n')
                m.txt.output.configure(state=tk.DISABLED)
                m.txt.output.see(tk.END)
            ploter.canvas.show()
    def quit(self):
        root.quit()
        root.destroy()
class text(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.outframe=Frame(self)
        self.outframe.pack(side=tk.BOTTOM)
        self.lf_output=LabelFrame(self.outframe,text="output: ",background='gray85',font='Helvetica 12 bold')
        self.lf_output.pack(ipadx=2,ipady=2)
        self.output = tkst.ScrolledText(
        master=self.lf_output,
        wrap= tk.WORD,
        width=37,
        height=35,
        state=tk.DISABLED)
        self.output.pack()
class plot(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.f = Figure(figsize=(8,8), dpi=100)
        self.plotl=[]
        self.plottl=[]
        for i in range(15):
            self.plotl.append(self.f.add_subplot(8,4,1+i))
            self.plottl.append(self.f.add_subplot(8,4,17+i))
        self.canvas = FigureCanvasTkAgg(self.f, master=self)
        # add the figure to frame
        self.canvas._tkcanvas.pack(expand=True)
        # make a color map of fixed colors
        cmap = mpl.colors.ListedColormap(['black','grey'])
        bounds=[-1,0,1]
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
        # tell imshow about color map so that only set colors are used
        for i in range(15):
            self.plotl[i].set_title("                {}".format(i))
            self.plotl[i].imshow(l[i].reshape([10,10]),interpolation='nearest',
                                cmap = cmap,norm=norm)
            self.plotl[i].axis('off')
            self.plottl[i].set_title("                     test{}".format(i))
            self.plottl[i].imshow(lt[i].reshape([10,10]),interpolation='nearest',
                                cmap = cmap,norm=norm)
            self.plottl[i].axis('off')
class mainframe(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.gui=MainApplication(self)
        self.gui.pack(side="top", fill="both", expand=True)
        self.txt=text(self)
        self.txt.pack(side="top", fill="both", expand=True)
l=[]
lt=[]
for i in range(15):
    l.append(np.zeros(100))
    lt.append(np.zeros(100))
identity=np.identity(100)
for i in range(100):
    for j in range(15):
        l[j][i]=-1
        lt[j][i]=-1
rbm(l)
rtestbm(lt)
for i in range(15):
    l[i]=(l[i]).reshape([100,1])
    lt[i]=(lt[i]).reshape([100,1])
#read the data of basic
w=np.zeros([100,100])
for i in range(15):
    w=w+np.dot(l[i],l[i].reshape([1,100]))
w=w/100-15*identity/100
#compute w
theta=np.zeros(100)
for i in range(100):
    temp=0
    for j in range(100):
        temp+=w[i][j]
    theta[i]=temp
theta=theta.reshape([100,1])
#compute theta
root = tk.Tk()
m=mainframe(root)
m.pack(side='left')
ploter=plot(root)
ploter.pack(side="right", fill="both", expand=True)
root.title("NN3_Hopifield_bonus")
root.resizable(False, False)
m.txt.output.configure(state=tk.NORMAL)
m.txt.output.insert(tk.INSERT,'matrix w(second decimal place): '+'\n')
m.txt.output.insert(tk.INSERT,round(w[0,0],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(w[0,1],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(w[0,2],2))
m.txt.output.insert(tk.INSERT,'...')
m.txt.output.insert(tk.INSERT,round(w[0,97],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(w[0,98],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(w[0,99],2))
m.txt.output.insert(tk.INSERT,'\n')
m.txt.output.insert(tk.INSERT,round(w[1,0],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(w[1,1],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(w[1,2],2))
m.txt.output.insert(tk.INSERT,'...')
m.txt.output.insert(tk.INSERT,round(w[1,97],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(w[1,98],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(w[1,99],2))
m.txt.output.insert(tk.INSERT,'\n')
m.txt.output.insert(tk.INSERT,round(w[2,0],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(w[2,1],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(w[2,2],2))
m.txt.output.insert(tk.INSERT,'...')
m.txt.output.insert(tk.INSERT,round(w[2,97],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(w[2,98],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(w[2,99],2))
m.txt.output.insert(tk.INSERT,'\n')
m.txt.output.insert(tk.INSERT," .                          ."+'\n')
m.txt.output.insert(tk.INSERT," .                          ."+'\n')
m.txt.output.insert(tk.INSERT," .                          ."+'\n')
m.txt.output.insert(tk.INSERT,round(w[97,0],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(w[97,1],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(w[97,2],2))
m.txt.output.insert(tk.INSERT,'...')
m.txt.output.insert(tk.INSERT,round(w[97,97],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(w[97,98],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(w[97,99],2))
m.txt.output.insert(tk.INSERT,'\n')
m.txt.output.insert(tk.INSERT,round(w[98,0],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(w[98,1],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(w[98,2],2))
m.txt.output.insert(tk.INSERT,'...')
m.txt.output.insert(tk.INSERT,round(w[98,97],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(w[98,98],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(w[98,99],2))
m.txt.output.insert(tk.INSERT,'\n')
m.txt.output.insert(tk.INSERT,round(w[99,0],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(w[99,1],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(w[99,2],2))
m.txt.output.insert(tk.INSERT,'...')
m.txt.output.insert(tk.INSERT,round(w[99,97],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(w[99,98],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(w[99,99],2))
m.txt.output.insert(tk.INSERT,'\n'+'\n'+'Theta (second decimal place): '+'\n')
m.txt.output.insert(tk.INSERT,round(theta[0,0],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(theta[1,0],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(theta[2,0],2))
m.txt.output.insert(tk.INSERT,'...')
m.txt.output.insert(tk.INSERT,round(theta[97,0],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(theta[98,0],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(theta[99,0],2))
m.txt.output.insert(tk.INSERT,'\n'+'\n')
m.txt.output.configure(state=tk.DISABLED)
m.txt.output.see(tk.END)
root.mainloop()
