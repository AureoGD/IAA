import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import math
import matplotlib.animation as animation

#import tkinter as tk
from tkinter import *
from tkinter import ttk

import time
import threading

f = Figure(figsize=(10, 5), dpi=100)
a = f.add_subplot(111)

N = 10
xList = []
yList = []
count = 0

theta =0
x = 520

def teste():
    global theta
    global x
    t=0
    while(1):
        time.sleep(0.1)
        t = 0.1+t
        theta = math.sin(t)
        x = -10*theta + x
        drawpendulum(x,theta)

'''
#def Counter():
#    count = 0
#    while(1):
#        count = count+0.01
#        time.sleep(0.01)
#        if len(xList) < N:
#            xList.append(count)
#            yList.append(count)
#        else:
#            xList.pop(0)
#            xList.insert(N, count)
#            yList.pop(0)
#            yList.insert(N, count)
#        #print(yList)

LARGE_FONT=("Verdana", 12)

def animmate(i):
    global count
    #a.clear()
    count = count + 0.1
    if len(xList) < N:
        xList.append(count)
        yList.append(count)
    else:
        xList.pop(0)
        xList.insert(N, count)
        yList.pop(0)
        yList.insert(N, count)
    a.plot(xList, yList)

class InvertedPendulum(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Inverted Pendulum")
        container = tk.Frame(self)
        container.pack(side= "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, pendulumAnimation):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady = 10, padx=10)

        button = ttk.Button(self, text="Page One",
                           command=lambda: controller.show_frame(PageOne))
        button.pack()

        button1 = ttk.Button(self, text="Inverted Pendulum",
                            command=lambda: controller.show_frame(pendulumAnimation))
        button1.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="PageOne", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back home",
                           command=lambda: controller.show_frame(StartPage))
        button1.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class pendulumAnimation(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Pendulum Animation", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        FrameMainWindow = Frame(tk.Frame, width=1040, height=600)
        FrameMainWindow.grid(row=0, column=0, padx=0, pady=0)

        canvasMainWindow = Canvas(FrameMainWindow, width=1040, height=400, bg='white')
        canvasMainWindow.grid(row=0, column=0, padx=0, pady=0)

        # main screem setting
        canvasMainWindow.create_rectangle(50, 50, 1000, 350)
        canvasMainWindow.create_rectangle(50, 340, 1000, 350, fill="black")
        canvasMainWindow.create_line(520, 50, 520, 350, dash=(4, 1))

app = InvertedPendulum()
ani = animation.FuncAnimation(f, animmate, interval = 10)
app.mainloop()

'''
#problem datas

m = 1.1 #car mass + pendulum mass
g = 9.8 #gravity aceleration
l = 0.5 #pendulum size
mb = 0.1 #pendulum mass
h = 0.02


def calcThetaDoubleDot(F,ThetaOld, ThetaDotOld):
    ThetaDoubleDot = ((m*g*math.sin(ThetaOld))-math.cos(F+mb*l*math.pow(ThetaDotOld,2)*math.sin(ThetaOld)))/((4/3)*m*l-mb*l*math.pow(math.cos(ThetaOld),2))
    return (ThetaDoubleDot)

def calcXDoubleDot(F,ThetaOld, ThetaDotOld,ThetaDoubleDotOld):
    XDoubleDot = (F+mb*l*(math.pow(ThetaDotOld,2)*math.sin(ThetaOld)-ThetaDoubleDotOld*math.cos(ThetaOld)))/m
    return  (XDoubleDot)

# main screem setting
window = Tk()
window.title("Inverted Pendulum")
FrameMainWindow = Frame(window, width=1040, height= 100)
FrameMainWindow.grid(row=0, column=0, padx=0, pady=0)
canvasMainWindow = Canvas(FrameMainWindow, width=1040, height=400, bg='white', sticky=)
canvasMainWindow.grid(row=0, column=0, padx=0, pady=0)

# Pendulum animation

L = 200
yc = 310


canvasMainWindow.create_rectangle(50, 50, 990, 350)
canvasMainWindow.create_rectangle(50, 340, 990, 350, fill="grey")
canvasMainWindow.create_line(520, 50, 520, 350, dash=(4, 1))

def drawpendulum(x,theta):
    canvasMainWindow.delete("modell")
    # car characteristics
    d = 35
    canvasMainWindow.create_rectangle(x - 60, yc, x + 60, yc + 20, fill="blue", tags="modell")
    canvasMainWindow.create_oval(x - 10 - d, yc + 10, x + 10 - d, yc + 30, fill="black", tags="modell")
    canvasMainWindow.create_oval(x - 10 + d, yc + 10, x + 10 + d, yc + 30, fill="black", tags="modell")
    # pendulum characteristics
    x1 = x + L * math.sin(theta)
    y1 = yc - L * math.cos(theta)
    canvasMainWindow.create_line(x1,y1,x,yc, fill="green", width=10,tags="modell")
    canvasMainWindow.create_line(x,yc,x,yc-L,dash=(4, 1), tags="modell")
    canvasMainWindow.create_oval(x-7,yc-7,x+7,yc+7, fill="red", tags="modell")


thCount = threading.Thread(target = teste)
thCount.start()

window.mainloop()

thetadoubledot = calcThetaDoubleDot(0.1,0.01,0.1)
print(thetadoubledot)
xdoubledot=calcXDoubleDot(0.1,0.01,0.1,thetadoubledot)
print(xdoubledot)

