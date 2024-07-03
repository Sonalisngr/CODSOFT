import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("375x500")
        self.root.resizable(0, 0)
        
        self.expression = ""
        
        self.input_text = tk.StringVar()
        
        # Input Frame
        input_frame = tk.Frame(self.root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        input_frame.pack(side=tk.TOP)
        
        # Input Field
        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)
        
        # Buttons Frame
        btns_frame = tk.Frame(self.root, width=312, height=272.5, bg="grey")
        btns_frame.pack()
        
        # First row        
        clear = tk.Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#f2a33c", cursor="hand2", command=lambda: self.clear()).grid(row=0, column=1, columnspan=3)
        divide = tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#ff9800", cursor="hand2", command=lambda: self.click("/")).grid(row=0, column=3)
        
        # Second row
        seven = tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click(7)).grid(row=1, column=0)
        eight = tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click(8)).grid(row=1, column=1)
        nine = tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click(9)).grid(row=1, column=2)
        multiply = tk.Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#ff9800", cursor="hand2", command=lambda: self.click("*")).grid(row=1, column=3)
        
        # Third row
        four = tk.Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click(4)).grid(row=2, column=0)
        five = tk.Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click(5)).grid(row=2, column=1)
        six = tk.Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click(6)).grid(row=2, column=2)
        minus = tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#ff9800", cursor="hand2", command=lambda: self.click("-")).grid(row=2, column=3)
        
        # Fourth row
        one = tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click(1)).grid(row=3, column=0)
        two = tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click(2)).grid(row=3, column=1)
        three = tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click(3)).grid(row=3, column=2)
        plus = tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#ff9800", cursor="hand2", command=lambda: self.click("+")).grid(row=3, column=3)
        
        # Fifth row
        zero = tk.Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click(0)).grid(row=4, column=0, columnspan=2)
        point = tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#ff9800", cursor="hand2", command=lambda: self.click(".")).grid(row=4, column=2)
        equals = tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#ff9800", cursor="hand2", command=self.equal).grid(row=4, column=3)
        
    def clear(self):
        self.expression = ""
        self.input_text.set("")
    
    def click(self, item):
        self.expression += str(item)
        self.input_text.set(self.expression)
    
    def equal(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except:
            self.input_text.set("Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
