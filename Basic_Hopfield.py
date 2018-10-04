import os
import numpy.matlib
import numpy as np
import tkinter as tk
from tkinter import ttk, Button, Label, Entry, Tk, LabelFrame, Frame, Button
import tkinter.scrolledtext as tkst
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from random import *
from PIL import Image, ImageTk
import matplotlib as mpl
from matplotlib import cm
def cr(a,b):
    t=0
    for i in range(117):
        if a[0,i]==b[0,i]:
            t+=1
    return round(t/117*100,2)
def rbm(a,b,c):
    with open('Basic_Training.txt','r') as f:
        for k, line in enumerate(f):
            if k<13:
                for i in range(len(line)):
                    if line[i]=='1':
                        a[0,k*9+i]=int(1)
            elif k> 13 and k < 27:
                for i in range(len(line)):
                    if line[i]=='1':
                        b[0,(k-14)*9+i]=int(1)
            elif k>27 and k<41:
                for i in range(len(line)):
                    if line[i]=='1':
                        c[0,(k-28)*9+i]=int(1)
def rtestbm(at,bt,ct):
    with open('Basic_Testing.txt','r') as f:
        for k, line in enumerate(f):
            if k<13:
                for i in range(len(line)):
                        if line[i]=='1':
                            at[0,k*9+i]=int(1)
            elif k> 13 and k < 27:
                for i in range(len(line)):
                    if line[i]=='1':
                        bt[0,(k-14)*9+i]=int(1)
            elif k>27 and k<41:
                for i in range(len(line)):
                    if line[i]=='1':
                        ct[0,(k-28)*9+i]=int(1)
def train(w,theta,test):
    same=False
    temp=w*test-theta
    ans=np.matlib.zeros(117)
    ans=ans.getT()
    for i in range(117):
        if temp[i,0] > 0:
            ans[i,0]=1
        elif temp[i, 0]==0:
            ans[i, 0]=test[i,0]
        else:
            ans[i,0]=-1
    global times
    times=0
    while(same==False):
        temp=w*ans-theta
        times+=1
        for i in range(117):
            if temp[i,0]>0:
                temp[i,0]=1
            elif temp[i, 0]==0:
                temp[i, 0]=ans[i,0]
            elif temp[i, 0]<0:
                temp[i,0]=-1
        for i in range(117):
            if ans[i, 0]!=temp[i,0]:
                same = False
                break
            else:
                same= True
        for i in range(117):
            ans[i, 0]=temp[i,0]
    return(ans)
def main(test):
    a=np.matlib.zeros(117)
    b=np.matlib.zeros(117)
    c=np.matlib.zeros(117)
    identity=np.matlib.identity(117, dtype=int)
    at=np.matlib.zeros(117)
    bt=np.matlib.zeros(117)
    ct=np.matlib.zeros(117)
    for i in range(117):
        a[0,i]=-1
        b[0,i]=-1
        c[0,i]=-1
        at[0,i]=-1
        bt[0,i]=-1
        ct[0,i]=-1
    rbm(a,b,c)
    rtestbm(at,bt,ct)
    at=at.getT()
    bt=bt.getT()
    ct=ct.getT()
    a=a.getT()
    b=b.getT()
    c=c.getT()

    #read the data of basic
    w=(a*a.getT()+b*b.getT()+c*c.getT())/117-3*identity/117
    #compute w
    theta=np.matlib.zeros(117)
    for i in range(117):
        temp=0
        for j in range(117):
            temp+=w[i,j]
        theta[0,i]=temp
    theta=theta.getT()
    #compute theta
    glbw=w
    temp1=(train(w, theta, test))
    ansa=np.ones([1,117])
    for i in range(117):
        ansa[0,i]=temp1[i,0]
    ansa=ansa.reshape([13,9])
    return ansa
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
        self.diffchosen['values'] = ["basic"]
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
        self.run = tk.Button(master=self.lf_exe, text='test', command=self.train,width=15, relief=tk.GROOVE,background='gray85')
        self.run.pack(padx=15,side='left')
        self.quit = tk.Button(master=self.lf_exe, text='exit', command=self.quit,width=15,background='gray85',padx=5, relief=tk.GROOVE)
        self.quit.pack(padx=15,side='left')

    def ShowChoice(self):
        ploter.plott1.clear()
        ploter.plott2.clear()
        ploter.plott3.clear()
        ploter.plott1.axis('off')
        ploter.plott2.axis('off')
        ploter.plott3.axis('off')
        cmap = mpl.colors.ListedColormap(['black','grey'])
        bounds=[-1,0,1]
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
        for i in range(117):
            rat[i,0]=a[i,0]
            rbt[i,0]=b[i,0]
            rct[i,0]=c[i,0]
        srat=np.ones([1,117])
        srbt=np.ones([1,117])
        srct=np.ones([1,117])
        if(self.varc.get()==1):
            ploter.plott1.imshow(sta,interpolation='nearest',
                    cmap = cmap,norm=norm)
            ploter.plott1.axis('off')
            ploter.plott1.set_title("test data 1")
            ploter.plott2.imshow(stb,interpolation='nearest',
                    cmap = cmap,norm=norm)
            ploter.plott2.axis('off')
            ploter.plott2.set_title("test data 2")
            ploter.plott3.imshow(stc,interpolation='nearest',
                    cmap = cmap,norm=norm)
            ploter.plott3.axis('off')
            ploter.plott3.set_title("test data 3")
            ploter.canvas.show()
        else:
            self.correctrateenter.config(state="NORMAL")
            rnum=int(self.correctrate.get())
            for i in range(117):
                if randrange(rnum) == 0:
                    if rat[i,0]==1:
                        rat[i,0]=-1
                    else:
                        rat[i,0]=1
                if randrange(rnum) == 0:
                    if rbt[i,0]==1:
                        rbt[i,0]=-1
                    else:
                        rbt[i,0]=1
                if randrange(rnum) == 0:
                    if rct[i,0]==1:
                        rct[i,0]=-1
                    else:
                        rct[i,0]=1
            for i in range(117):
                srat[0,i]=rat[i,0]
                srbt[0,i]=rbt[i,0]
                srct[0,i]=rct[i,0]
            srat=srat.reshape([13,9])
            srbt=srbt.reshape([13,9])
            srct=srct.reshape([13,9])
            ploter.plott1.imshow(srat,interpolation='nearest',
                    cmap = cmap,norm=norm)
            ploter.plott1.axis('off')
            ploter.plott1.set_title("test data 1")
            ploter.plott2.imshow(srbt,interpolation='nearest',
                    cmap = cmap,norm=norm)
            ploter.plott2.axis('off')
            ploter.plott2.set_title("test data 2")
            ploter.plott3.imshow(srct,interpolation='nearest',
                    cmap = cmap,norm=norm)
            ploter.plott3.axis('off')
            ploter.plott3.set_title("test data 3")
            ploter.canvas.show()
    def train(self):
        ploter.plott1.clear()
        ploter.plott2.clear()
        ploter.plott3.clear()
        ploter.plott1.axis('off')
        ploter.plott2.axis('off')
        ploter.plott3.axis('off')
        cmap = mpl.colors.ListedColormap(['black','grey'])
        bounds=[-1,0,1]
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
        if(self.varc.get()==1):
            ploter.plott1.imshow(main(at),interpolation='nearest',
                    cmap = cmap,norm=norm)
            ploter.plott1.axis('off')
            ploter.plott1.set_title("test data 1")
            tempa=main(at)

            m.txt.output.configure(state=tk.NORMAL)
            m.txt.output.insert(tk.INSERT,'test data 1 iteration times: {}'.format(times+1)+'\n')
            m.txt.output.insert(tk.INSERT,'test data 1 correct rate: {}％'.format(cr(tempa.reshape([1,117]),sa.reshape([1,117])))+'\n')
            m.txt.output.configure(state=tk.DISABLED)
            m.txt.output.see(tk.END)

            ploter.plott2.imshow(main(bt),interpolation='nearest',
                    cmap = cmap,norm=norm)
            ploter.plott2.axis('off')
            ploter.plott2.set_title("test data 2")
            m.txt.output.configure(state=tk.NORMAL)
            m.txt.output.insert(tk.INSERT,'test data 2 iteration times: {}'.format(times+1)+'\n')
            tempb=main(bt)
            m.txt.output.insert(tk.INSERT,'test data 2 correct rate: {}％'.format(cr(tempb.reshape([1,117]),sb.reshape([1,117])))+'\n')
            m.txt.output.configure(state=tk.DISABLED)
            m.txt.output.see(tk.END)

            ploter.plott3.imshow(main(ct),interpolation='nearest',
                    cmap = cmap,norm=norm)
            ploter.plott3.axis('off')
            ploter.plott3.set_title("test data 3")
            m.txt.output.configure(state=tk.NORMAL)
            m.txt.output.insert(tk.INSERT,'test data 3 iteration times: {}'.format(times+1)+'\n')
            tempc=main(ct)
            m.txt.output.insert(tk.INSERT,'test data 3 correct rate: {}％'.format(cr(tempc.reshape([1,117]),sc.reshape([1,117])))+'\n')
            m.txt.output.insert(tk.INSERT,'\n')
            m.txt.output.configure(state=tk.DISABLED)
            m.txt.output.see(tk.END)

            ploter.canvas.show()
        else:
            ploter.plott1.imshow(main(rat),interpolation='nearest',
                    cmap = cmap,norm=norm)
            ploter.plott1.axis('off')
            ploter.plott1.set_title("test data 1")
            m.txt.output.configure(state=tk.NORMAL)
            m.txt.output.insert(tk.INSERT,'test data 1 iteration times: {}'.format(times+1)+'\n')
            tempa=main(rat)
            m.txt.output.insert(tk.INSERT,'test data 1 correct rate: {}％'.format(cr(tempa.reshape([1,117]),sa.reshape([1,117])))+'\n')
            m.txt.output.configure(state=tk.DISABLED)
            m.txt.output.see(tk.END)

            ploter.plott2.imshow(main(rbt),interpolation='nearest',
                    cmap = cmap,norm=norm)
            ploter.plott2.axis('off')
            ploter.plott2.set_title("test data 2")
            m.txt.output.configure(state=tk.NORMAL)
            m.txt.output.insert(tk.INSERT,'test data 2 iteration times: {}'.format(times+1)+'\n')
            tempb=main(rbt)
            m.txt.output.insert(tk.INSERT,'test data 2 correct rate: {}％'.format(cr(tempb.reshape([1,117]),sb.reshape([1,117])))+'\n')
            m.txt.output.configure(state=tk.DISABLED)
            m.txt.output.see(tk.END)
            ploter.plott3.imshow(main(rct),interpolation='nearest',
                    cmap = cmap,norm=norm)
            ploter.plott3.axis('off')
            ploter.plott3.set_title("test data 3")
            m.txt.output.configure(state=tk.NORMAL)
            m.txt.output.insert(tk.INSERT,'test data 3 iteration times: {}'.format(times+1)+'\n')
            tempc=main(rct)
            m.txt.output.insert(tk.INSERT,'test data 3 correct rate: {}％'.format(cr(tempc.reshape([1,117]),sc.reshape([1,117])))+'\n')
            m.txt.output.insert(tk.INSERT,'\n')
            m.txt.output.configure(state=tk.DISABLED)
            m.txt.output.see(tk.END)
            ploter.canvas.show()
    def quit(self):
        root.quit()
        root.destroy()
class text(tk.Frame):
    """
    option frame
    """
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
    """
    option frame
    """
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.f = Figure(figsize=(8,8), dpi=100)
        self.plot1 = self.f.add_subplot(231)
        self.plot2 = self.f.add_subplot(232)
        self.plot3 = self.f.add_subplot(233)
        self.plott1 = self.f.add_subplot(234)
        self.plott2 = self.f.add_subplot(235)
        self.plott3 = self.f.add_subplot(236)
        self.canvas = FigureCanvasTkAgg(self.f, master=self)
        # add the figure to frame
        self.canvas._tkcanvas.pack(expand=True)

        # make a color map of fixed colors
        cmap = mpl.colors.ListedColormap(['black','grey'])
        bounds=[-1,0,1]
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
        # tell imshow about color map so that only set colors are used
        self.plot1.imshow(sa,interpolation='nearest',
                            cmap = cmap,norm=norm)
        self.plot1.axis('off')
        self.plot1.set_title("train data 1")
        self.plot2.imshow(sb,interpolation='nearest',
                            cmap = cmap,norm=norm)
        self.plot2.axis('off')
        self.plot2.set_title("train data 2")
        self.plot3.imshow(sc,interpolation='nearest',
                            cmap = cmap,norm=norm)
        self.plot3.axis('off')
        self.plot3.set_title("train data 3")
        self.plott1.imshow(sta,interpolation='nearest',
                    cmap = cmap,norm=norm)
        self.plott1.axis('off')
        self.plott1.set_title("test data 1")
        self.plott2.imshow(stb,interpolation='nearest',
                            cmap = cmap,norm=norm)
        self.plott2.axis('off')
        self.plott2.set_title("test data 2")
        self.plott3.imshow(stc,interpolation='nearest',
                            cmap = cmap,norm=norm)
        self.plott3.axis('off')
        self.plott3.set_title("test data 3")
        #plt.show()
class mainframe(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.gui=MainApplication(self)
        self.gui.pack(side="top", fill="both", expand=True)
        self.txt=text(self)
        self.txt.pack(side="top", fill="both", expand=True)
a=np.matlib.zeros(117)
b=np.matlib.zeros(117)
c=np.matlib.zeros(117)
identity=np.matlib.identity(117, dtype=int)
at=np.matlib.zeros(117)
bt=np.matlib.zeros(117)
ct=np.matlib.zeros(117)
for i in range(117):
    a[0,i]=-1
    b[0,i]=-1
    c[0,i]=-1
    at[0,i]=-1
    bt[0,i]=-1
    ct[0,i]=-1
rbm(a,b,c)
rtestbm(at,bt,ct)
at=at.getT()
bt=bt.getT()
ct=ct.getT()
a=a.getT()
b=b.getT()
c=c.getT()
sa=np.ones([1,117])
sb=np.ones([1,117])
sc=np.ones([1,117])
sta=np.ones([1,117])
stb=np.ones([1,117])
stc=np.ones([1,117])
ide=np.matlib.identity(117, dtype=int)
glbw=(a*a.getT()+b*b.getT()+c*c.getT())/117-3*ide/117
glbt=np.matlib.zeros(117)
for i in range(117):
    temp=0
    for j in range(117):
        temp+=glbw[i,j]
    glbt[0,i]=temp
for i in range(117):
    sa[0,i]=a[i,0]
    sb[0,i]=b[i,0]
    sc[0,i]=c[i,0]
    sta[0,i]=at[i,0]
    stb[0,i]=bt[i,0]
    stc[0,i]=ct[i,0]
sa=sa.reshape([13,9])
sb=sb.reshape([13,9])
sc=sc.reshape([13,9])
sta=sta.reshape([13,9])
stb=stb.reshape([13,9])
stc=stc.reshape([13,9])
rat=np.matlib.zeros(117)
rbt=np.matlib.zeros(117)
rct=np.matlib.zeros(117)
rat=rat.getT()
rbt=rbt.getT()
rct=rct.getT()
times=0
root = tk.Tk()
m=mainframe(root)
m.pack(side='left')
ploter=plot(root)
ploter.pack(side="right", fill="both", expand=True)
root.title("NN3_Hopifield_basic")
root.resizable(False, False)
m.txt.output.configure(state=tk.NORMAL)
m.txt.output.insert(tk.INSERT,'matrix w(second decimal place): '+'\n')
m.txt.output.insert(tk.INSERT,round(glbw[0,0],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(glbw[0,1],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(glbw[0,2],2))
m.txt.output.insert(tk.INSERT,'...')
m.txt.output.insert(tk.INSERT,round(glbw[0,114],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(glbw[0,115],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(glbw[0,116],2))
m.txt.output.insert(tk.INSERT,'\n')
m.txt.output.insert(tk.INSERT,round(glbw[1,0],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(glbw[1,1],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(glbw[1,2],2))
m.txt.output.insert(tk.INSERT,'...')
m.txt.output.insert(tk.INSERT,round(glbw[1,114],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(glbw[1,115],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(glbw[1,116],2))
m.txt.output.insert(tk.INSERT,'\n')
m.txt.output.insert(tk.INSERT,round(glbw[2,0],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(glbw[2,1],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(glbw[2,2],2))
m.txt.output.insert(tk.INSERT,'...')
m.txt.output.insert(tk.INSERT,round(glbw[2,114],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(glbw[2,115],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(glbw[2,116],2))
m.txt.output.insert(tk.INSERT,'\n')
m.txt.output.insert(tk.INSERT," .                          ."+'\n')
m.txt.output.insert(tk.INSERT," .                          ."+'\n')
m.txt.output.insert(tk.INSERT," .                          ."+'\n')
m.txt.output.insert(tk.INSERT,round(glbw[114,0],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(glbw[114,1],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(glbw[114,2],2))
m.txt.output.insert(tk.INSERT,'...')
m.txt.output.insert(tk.INSERT,round(glbw[114,114],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(glbw[114,115],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(glbw[114,116],2))
m.txt.output.insert(tk.INSERT,'\n')
m.txt.output.insert(tk.INSERT,round(glbw[115,0],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(glbw[115,1],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(glbw[115,2],2))
m.txt.output.insert(tk.INSERT,'...')
m.txt.output.insert(tk.INSERT,round(glbw[115,114],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(glbw[115,115],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(glbw[115,116],2))
m.txt.output.insert(tk.INSERT,'\n')
m.txt.output.insert(tk.INSERT,round(glbw[116,0],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(glbw[116,1],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(glbw[116,2],2))
m.txt.output.insert(tk.INSERT,'...')
m.txt.output.insert(tk.INSERT,round(glbw[116,114],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(glbw[116,115],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(glbw[116,116],2))
m.txt.output.insert(tk.INSERT,'\n'+'Theta (second decimal place): '+'\n')
m.txt.output.insert(tk.INSERT,round(glbt[0,0],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(glbt[0,1],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(glbt[0,2],2))
m.txt.output.insert(tk.INSERT,'...')
m.txt.output.insert(tk.INSERT,round(glbt[0,114],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(glbt[0,115],2))
m.txt.output.insert(tk.INSERT,' ')
m.txt.output.insert(tk.INSERT,round(glbt[0,116],2))
m.txt.output.insert(tk.INSERT,'\n')
m.txt.output.configure(state=tk.DISABLED)
m.txt.output.see(tk.END)
root.mainloop()
