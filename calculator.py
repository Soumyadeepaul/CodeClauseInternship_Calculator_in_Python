# importing tkinter library
import tkinter as tk


# functionality of digit buttons
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))


# functionality of clear button
def button_clear():
    entry.delete(0, tk.END)


# functionality of equal button
def button_equal():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


# functionality of back button
def back():
    expression = entry.get()
    if len(expression) > 0:
        entry.delete(0, tk.END)
        entry.insert(tk.END, expression[:len(expression) - 1])


if __name__ == '__main__':
    # Creating the main window
    window = tk.Tk()
    # Tab Title Simple Calculator
    window.title("Simple Calculator")
    window.geometry("380x200")
    window.configure(bg='black')
    window.resizable(False, False)
    # Creating the entry field
    entry = tk.Entry(window, width=40, font=('Arial', 12))
    # locating the field according to grid
    entry.grid(row=0, column=0, columnspan=4, pady=2, padx=5)

    # Defining the buttons
    buttons = [
        ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 1, 3),
        ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 2, 3),
        ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 3, 3),
        ("0", 5, 1), (".", 5, 2), ("+", 4, 3)
    ]

    # Create the buttons and attach their click events
    for button_text, row, col in buttons:
        button = tk.Button(window, text=button_text, width=6, command=lambda text=button_text: button_click(text))
        button.grid(row=row, column=col, pady=2)

    # delete button
    delete_button = tk.Button(window, text="C", width=6, command=button_clear, bg='red')
    delete_button.grid(row=1, column=0, pady=2)

    # result button
    result_button = tk.Button(window, text="=", width=6, command=button_equal, bg='white')
    result_button.grid(row=5, column=3, pady=2)

    # Distroy button
    distroy_button = tk.Button(window, text="Exit", width=6, command=window.destroy, bg='white')
    distroy_button.grid(row=5, column=0, pady=2)

    # backspace button
    backs_button = tk.Button(window, text="back", width=6, command=back, bg='white')
    backs_button.grid(row=1, column=2, pady=2)
    # to start the main loop
    window.mainloop()
