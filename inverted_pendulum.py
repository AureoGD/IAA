import tkinter  as tk

LARGE_FONT=("Verdana", 12)

class InvertedPendulum(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side= "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne):

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

        button = tk.Button(self, text="Page One",
                           command=lambda: controller.show_frame(PageOne))
        button.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="PageOne", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back home",
                           command=lambda: controller.show_frame(StartPage))
        button1.pack()


app = InvertedPendulum()
app.mainloop()



'''window = Tk()
window.title("Inverted Pendulum")
FrameMainWindow = Frame(window, width=1040, height= 600)
FrameMainWindow.grid(row=0, column=0, padx=0, pady=0)

canvasMainWindow = Canvas(FrameMainWindow, width=1040, height=400, bg='white')
canvasMainWindow.grid(row=0, column=0, padx=0, pady=0)

# main screem setting
canvasMainWindow.create_rectangle(50, 50, 1000, 350)
canvasMainWindow.create_rectangle(50, 340, 1000, 350, fill="black")
canvasMainWindow.create_line(520, 50, 520, 350, dash=(4, 1))


window.mainloop()'''
