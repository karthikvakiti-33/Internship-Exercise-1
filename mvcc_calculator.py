import tkinter as tk


class CalculatorModel:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Devision by Zero"
        return a / b

class CalculatorView:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        
        
        self.result_var = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.result_var, font=("Arial", 16), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)
        
        
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]

        for (text, row, col) in buttons:
            tk.Button(root, text=text, font=("Arial", 14), command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, sticky="nsew")

        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
            root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, text):
        pass


class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.current_input = ""
        self.operation = None
        self.operand = None
        self.view.on_button_click = self.on_button_click

    def on_button_click(self, text):
        if text in '0123456789.':
            self.current_input += text
            self.view.result_var.set(self.current_input)
        elif text in '+-*/':
            if self.current_input:
                self.operand = int(self.current_input)
                self.operation = text
                self.current_input = ""
        elif text == '=':
            if self.current_input and self.operation:
                second_operand = int(self.current_input)
                if self.operation == '+':
                    result = self.model.add(self.operand, second_operand)
                elif self.operation == '-':
                    result = self.model.subtract(self.operand, second_operand)
                elif self.operation == '*':
                    result = self.model.multiply(self.operand, second_operand)
                elif self.operation == '/':
                    result = self.model.divide(self.operand, second_operand)
                self.view.result_var.set(result)
                self.current_input = ""
                self.operation = None
                self.operand = None
        elif text == 'C':
            self.current_input = ""
            self.operation = None
            self.operand = None
            self.view.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    model = CalculatorModel()
    view = CalculatorView(root)
    controller = CalculatorController(model, view)
    root.mainloop()
