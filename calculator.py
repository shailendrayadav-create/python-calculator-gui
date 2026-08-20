import tkinter as tk
from tkinter import font
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.config(bg="#2c3e50")
        
        # Variable to store the expression
        self.expression = ""
        self.input_text = tk.StringVar()
        
        # Create GUI elements
        self.create_display()
        self.create_buttons()
        
    def create_display(self):
        """Create the display screen for the calculator"""
        display_frame = tk.Frame(self.root, bg="#34495e")
        display_frame.pack(pady=20, padx=20, fill=tk.BOTH)
        
        # Display label
        self.display = tk.Entry(
            display_frame,
            textvar=self.input_text,
            font=("Arial", 24, "bold"),
            borderwidth=2,
            relief=tk.SOLID,
            justify='right',
            bg="#ecf0f1",
            fg="#2c3e50"
        )
        self.display.pack(fill=tk.BOTH, ipady=10)
        
    def create_buttons(self):
        """Create calculator buttons"""
        button_frame = tk.Frame(self.root, bg="#2c3e50")
        button_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        # Button layout
        buttons = [
            ['C', '(', ')', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', '√']
        ]
        
        # Button colors
        operator_color = "#e74c3c"
        number_color = "#3498db"
        equals_color = "#27ae60"
        clear_color = "#e67e22"
        
        for row in buttons:
            row_frame = tk.Frame(button_frame, bg="#2c3e50")
            row_frame.pack(fill=tk.BOTH, expand=True, pady=5)
            
            for btn_text in row:
                if btn_text == '=':
                    btn_color = equals_color
                    command = self.calculate
                elif btn_text == 'C':
                    btn_color = clear_color
                    command = self.clear
                elif btn_text in ['÷', '×', '-', '+']:
                    btn_color = operator_color
                    command = lambda x=btn_text: self.on_button_click(x)
                elif btn_text == '√':
                    btn_color = operator_color
                    command = self.square_root
                else:
                    btn_color = number_color
                    command = lambda x=btn_text: self.on_button_click(x)
                
                button = tk.Button(
                    row_frame,
                    text=btn_text,
                    font=("Arial", 18, "bold"),
                    bg=btn_color,
                    fg="white",
                    relief=tk.RAISED,
                    borderwidth=2,
                    command=command,
                    activebackground="#c0392b" if btn_text not in ['=', 'C'] else "#229954"
                )
                button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
    
    def on_button_click(self, char):
        """Handle button click events"""
        if char == '÷':
            self.expression += '/'
        elif char == '×':
            self.expression += '*'
        else:
            self.expression += char
        
        self.input_text.set(self.expression.replace('/', '÷').replace('*', '×'))
    
    def clear(self):
        """Clear the display and expression"""
        self.expression = ""
        self.input_text.set("")
    
    def calculate(self):
        """Calculate the result of the expression"""
        try:
            result = eval(self.expression)
            self.input_text.set(result)
            self.expression = str(result)
        except:
            self.input_text.set("Error")
            self.expression = ""
    
    def square_root(self):
        """Calculate square root"""
        try:
            result = math.sqrt(eval(self.expression))
            self.input_text.set(result)
            self.expression = str(result)
        except:
            self.input_text.set("Error")
            self.expression = ""

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
