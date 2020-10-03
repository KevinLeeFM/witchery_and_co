from threading import Thread
import time
from tkinter import *
from tkinter.ttk import Frame, Button, Style

# # Define a function for the thread
# def loop1_10():
#     for i in range(1, 11):
#         time.sleep(1)
#         print(i)

# Thread(target=loop1_10).start()
# hello = input('Give an input blyat')
# print(hello)


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Witchery and Co. (Old School Distribution)")
        self.style = Style()
        self.style.theme_use("clam")

        frame_t = Frame(self, borderwidth=1)
        frame_t.pack(side=TOP, fill=BOTH, expand=True)

        frame_r = Frame(frame_t, relief=RAISED, borderwidth=1)
        frame_r.pack(side=RIGHT, fill=BOTH, expand=True)

        frame_l = Frame(frame_t, relief=RAISED, borderwidth=1)
        frame_l.pack(side=RIGHT, fill=BOTH, expand=True)

        frame_b = Frame(self, relief=RAISED, borderwidth=1)
        frame_b.pack(side=TOP, fill=X, expand=False)

        self.pack(fill=BOTH)

        closeButton = Button(frame_b, text="Close")
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(frame_b, text="OK")
        okButton.pack(side=RIGHT, padx=5, pady=5)
        usrin = Text(frame_b)
        usrin.pack(side=LEFT, fill=X, padx=5, pady=5)

        labels = []

        for i in range(10):
            lbl = Label(frame_l, text='[{num}] Hello!'.format(num=i), anchor=W)
            lbl.pack(side=TOP, fill=X, expand=True)
            labels.append(lbl)


def main():

    root = Tk()
    root.geometry("700x500+500+500")
    app = Example()
    root.mainloop()

if __name__ == '__main__':
    main()