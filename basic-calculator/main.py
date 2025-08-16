from tkinter import *

class Calculator(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x500")
        self.resizable(False, False)
        self.iconbitmap("calculator.ico")
        self.title("Calculator")
        self.value = StringVar()
        self.output_screen = Entry(self, textvariable=self.value, font="lucida 40 bold")
        self.output_screen.pack(pady=7)
        self.input_frame()

    def click(self, event):
        text = event.widget.cget("text")
        result = "Error"
        if text == "=":
            try:
                result = eval(self.value.get())
            except Exception as e:
                print(e)
        elif text == "C":
            result = ""
        elif text == "sqrt(x)":
            result = eval(self.value.get()+"**0.5")
        elif text == "x^2":
            result = eval(self.value.get()+"**2")
        else:
            result = self.value.get() + text
        self.value.set(result)
        self.output_screen.update()

    def input_frame(self):
        f1 = Frame(self, bg="#2F2F2F")
        button_null = Button(f1, text="x^2", padx=30, pady=30)
        button_null.pack(side=LEFT)
        button_null.bind("<Button-1>", self.click)
    
        button_null = Button(f1, text="sqrt(x)", padx=30, pady=30)
        button_null.pack(side=LEFT)
        button_null.bind("<Button-1>", self.click)

        button_cancel = Button(f1, text="C", padx=30, pady=30)
        button_cancel.pack(side=LEFT)
        button_cancel.bind("<Button-1>", self.click)

        button_divide = Button(f1, text="/", padx=30, pady=30)
        button_divide.pack(side=LEFT)
        button_divide.bind("<Button-1>", self.click)
        f1.pack(side=TOP, fill=X)

        f2 = Frame(self, bg="#2F2F2F")
        button_seven = Button(f2, text="7", padx=30, pady=30)
        button_seven.pack(side=LEFT)
        button_seven.bind("<Button-1>", self.click)
    
        button_eight = Button(f2, text="8", padx=30, pady=30)
        button_eight.pack(side=LEFT)
        button_eight.bind("<Button-1>", self.click)

        button_nine = Button(f2, text="9", padx=30, pady=30)
        button_nine.pack(side=LEFT)
        button_nine.bind("<Button-1>", self.click)

        button_multiply = Button(f2, text="*", padx=30, pady=30)
        button_multiply.pack(side=LEFT)
        button_multiply.bind("<Button-1>", self.click)
        f2.pack(side=TOP, fill=X)

        f3 = Frame(self, bg="#2F2F2F")
        button_four = Button(f3, text="4", padx=30, pady=30)
        button_four.pack(side=LEFT)
        button_four.bind("<Button-1>", self.click)
    
        button_five = Button(f3, text="5", padx=30, pady=30)
        button_five.pack(side=LEFT)
        button_five.bind("<Button-1>", self.click)

        button_six = Button(f3, text="6", padx=30, pady=30)
        button_six.pack(side=LEFT)
        button_six.bind("<Button-1>", self.click)

        button_subtract = Button(f3, text="-", padx=30, pady=30)
        button_subtract.pack(side=LEFT)
        button_subtract.bind("<Button-1>", self.click)
        f3.pack(side=TOP, fill=X)

        f4 = Frame(self, bg="#2F2F2F")
        button_one = Button(f4, text="1", padx=30, pady=30)
        button_one.pack(side=LEFT)
        button_one.bind("<Button-1>", self.click)
    
        button_two = Button(f4, text="2", padx=30, pady=30)
        button_two.pack(side=LEFT)
        button_two.bind("<Button-1>", self.click)

        button_three = Button(f4, text="3", padx=30, pady=30)
        button_three.pack(side=LEFT)
        button_three.bind("<Button-1>", self.click)

        button_add = Button(f4, text="+", padx=30, pady=30)
        button_add.pack(side=LEFT)
        button_add.bind("<Button-1>", self.click)
        f4.pack(side=TOP, fill=X)

        f5 = Frame(self, bg="#2F2F2F")
        button_percentage = Button(f5, text="%", padx=30, pady=30)
        button_percentage.pack(side=LEFT)
        button_percentage.bind("<Button-1>", self.click)
    
        button_zero = Button(f5, text="0", padx=30, pady=30)
        button_zero.pack(side=LEFT)
        button_zero.bind("<Button-1>", self.click)

        button_decimal = Button(f5, text=".", padx=30, pady=30)
        button_decimal.pack(side=LEFT)
        button_decimal.bind("<Button-1>", self.click)

        button_equalsto = Button(f5, text="=", padx=30, pady=30)
        button_equalsto.pack(side=LEFT)
        button_equalsto.bind("<Button-1>", self.click)
        f5.pack(side=TOP, fill=X)

if __name__ == '__main__':
    mainscreen = Calculator()
    mainscreen.mainloop()