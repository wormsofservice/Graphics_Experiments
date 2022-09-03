import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.quit_widget()
        self.hello_world()

    def quit_widget(self):
        tk.Button(self, text='Quit', command=self.quit).grid()

    def hello_world(self):
        tk.Button(self, text='Hello World').grid()


app = Application()
app.master.title('This is the application title') # this doesn't work
app.mainloop()

# root = Tk()
# ttk.Button(root, text="Hello World").grid()
# root.mainloop()
