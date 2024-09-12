import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox
import math as m

# Global variable to store coefficients
coefficients = []

# Function to handle quintic function input
def fn_quintica():
    window.withdraw()  # Hide the main window

    # Create a new window for input
    input_window = tk.Toplevel()
    input_window.title("Funzione quintica")

    # Label to explain the format of the function
    label = tk.Label(input_window, text="Hai selezionato una funzione quintica.\nIl formato è: ax^5 + bx^4 + cx^3 + dx^2 + ex + f = 0.\nInserisci i valori dei coefficienti:")
    label.grid(row=0, columnspan=2, padx=10, pady=10)

    # Labels and entry boxes for each coefficient
    labels = ['a:', 'b:', 'c:', 'd:', 'e:', 'f:']
    global coefficients
    entries = []

    for i, coeff in enumerate(labels):
        lbl = tk.Label(input_window, text=coeff)
        lbl.grid(row=i+1, column=0, padx=5, pady=5)
        entry = tk.Entry(input_window)
        entry.grid(row=i+1, column=1, padx=5, pady=5)
        entries.append(entry)

    # Function to handle the submission of input and ask for further action
    def submit():
        global coefficients
        try:
            # Get all coefficient values as floats
            coefficients = [float(entry.get()) for entry in entries]
        except ValueError:
            messagebox.showerror("Errore", "Numero invalido.")
            return

        # Close the input window
        input_window.destroy()

        # Show the main window again
        window.deiconify()

        # Ask the user whether they want to plot the graph or perform Action 2
        user_choice = messagebox.askquestion("Seleziona azione", "Vuoi visualizzare il grafico o calcolare la y inserendo la x? (Sì è il grafico, No è il calcolo)", icon='question')

        if user_choice == 'yes':
            grafico_quintico(coefficients)  # Plot the graph if user chooses 'yes'
        else:
            calcolo_quintico()  # Call Action 2 if user chooses 'no'

    # Button to submit the input
    submit_button = tk.Button(input_window, text="Submit", command=submit)
    submit_button.grid(row=7, columnspan=2, pady=10)

# Function to plot the quintic graph
def grafico_quintico(coefficients):
    # Unpack the coefficients (a, b, c, d, e, f)
    a, b, c, d, e, f = coefficients

    # Generate x values for the plot
    x = np.linspace(-10, 10, 400)

    # Calculate the corresponding y values for the quintic function
    y = a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f

    # Create the plot
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f"{a}x^5 + {b}x^4 + {c}x^3 + {d}x^2 + {e}x + {f}")
    plt.title('Grafico della funzione quintica')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()

# Function for Action 2
def calcolo_quintico():
    window.withdraw()  # Hide the main window

    # Create a new window for input
    action_window = tk.Toplevel()
    action_window.title("Funzione quintica")

    # Label and entry box for x value
    label = tk.Label(action_window, text="Inserisci il valore di x:")
    label.grid(row=0, column=0, padx=10, pady=10)
    x_entry = tk.Entry(action_window)
    x_entry.grid(row=0, column=1, padx=10, pady=10)

    # Function to handle the submission of the x value and calculate y
    def calculate_y():
        try:
            x = float(x_entry.get())
        except ValueError:
            messagebox.showerror("Errore", "Assicurati di inserire un numero valido.")
            return

        # Unpack the coefficients (a, b, c, d, e, f)
        a, b, c, d, e, f = coefficients

        # Calculate the corresponding y value for the given x
        y = a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f

        # Show the result in an info box
        messagebox.showinfo("Funzione quintica", f"Per x = {x}, y = {y}")

        # Close the input window
        action_window.destroy()

        # Plot the graph and reopen the main menu
        grafico_quintico(coefficients)
        window.deiconify()

    # Button to submit the x value
    submit_button = tk.Button(action_window, text="Submit", command=calculate_y)
    submit_button.grid(row=1, columnspan=2, pady=10)


def fn_goniometrica():
    window.withdraw()  # Hide the main window

    # Create a new window for input
    input_window = tk.Toplevel()
    input_window.title("Funzione goniometrica")

    # Label to explain the format of the function
    label = tk.Label(input_window,
                     text="Hai selezionato una funzione goniometrica.\nIl formato è: y = a*sin/cos/tan(bx) + c = 0\nInserisci i valori:")
    label.grid(row=0, columnspan=2, padx=10, pady=10)

    # Option menu for selecting the trigonometric function
    global function_type
    function_var = tk.StringVar(value='sin')
    func_label = tk.Label(input_window, text="Scegli la funzione:")
    func_label.grid(row=1, column=0, padx=5, pady=5)
    func_menu = tk.OptionMenu(input_window, function_var, 'sin', 'cos', 'tan')
    func_menu.grid(row=1, column=1, padx=5, pady=5)

    # Labels and entry boxes for coefficients a and c
    label_a = tk.Label(input_window, text="a:")
    label_a.grid(row=2, column=0, padx=5, pady=5)
    entry_a = tk.Entry(input_window)
    entry_a.grid(row=2, column=1, padx=5, pady=5)

    label_b = tk.Label(input_window, text="b:")
    label_b.grid(row=3, column=0, padx=5, pady=5)
    entry_b = tk.Entry(input_window)
    entry_b.grid(row=3, column=1, padx=5, pady=5)

    label_c = tk.Label(input_window, text="c:")
    label_c.grid(row=4, column=0, padx=5, pady=5)
    entry_c = tk.Entry(input_window)
    entry_c.grid(row=4, column=1, padx=5, pady=5)

    # Function to handle the submission of input and ask for further action
    def submit():
        global function_type
        try:
            # Get the function type and coefficients
            function_type = function_var.get()
            a = float(entry_a.get())
            b = float(entry_b.get())
            c = float(entry_c.get())
        except ValueError:
            messagebox.showerror("Errore", "Assicurati di inserire valori numerici validi.")
            return

        # Close the input window
        input_window.destroy()

        # Ask the user whether they want to plot the graph or calculate y
        user_choice = messagebox.askquestion("Seleziona azione",
                                             "Vuoi visualizzare il grafico o calcolare la y inserendo la x? (Sì è il grafico, No è il calcolo)",
                                             icon='question')

        if user_choice == 'yes':
            grafico_goniometrico(function_type, a, b, c)  # Plot the graph if user chooses 'yes'
        else:
            calcolo_goniometrico(a, b, c)  # Call the function to calculate y if user chooses 'no'

    # Button to submit the input
    submit_button = tk.Button(input_window, text="Submit", command=submit)
    submit_button.grid(row=5, columnspan=2, pady=10)


# Function to plot the trigonometric graph
def grafico_goniometrico(func_type, a, b, c):
    # Generate x values for the plot
    x = np.linspace(-10, 10, 400)

    # Calculate the corresponding y values based on the selected function
    if func_type == 'sin':
        y = a * np.sin(b * x) + c
    elif func_type == 'cos':
        y = a * np.cos(b * x) + c
    elif func_type == 'tan':
        y = a * np.tan(b * x) + c

    # Create the plot
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f"{a}*{func_type}({b}x) + {c}")
    plt.title('Grafico della funzione goniometrica')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim(-10, 10)  # Limit y-axis to avoid extreme values for tan function
    plt.grid(True)
    plt.legend()
    plt.show()

    # Reopen the main menu
    window.deiconify()


# Function to calculate y for the trigonometric function
def calcolo_goniometrico(a, b, c):
    window.withdraw()  # Hide the main window

    # Create a new window for input
    action_window = tk.Toplevel()
    action_window.title("Funzione goniometrica")

    # Label and entry box for x value
    label = tk.Label(action_window, text="Inserisci il valore di x:")
    label.grid(row=0, column=0, padx=10, pady=10)
    x_entry = tk.Entry(action_window)
    x_entry.grid(row=0, column=1, padx=10, pady=10)

    # Function to handle the submission of the x value and calculate y
    def calculate_y():
        try:
            x = float(x_entry.get())
        except ValueError:
            messagebox.showerror("Errore", "Assicurati di inserire un numero valido.")
            return

        # Calculate the corresponding y value based on the selected function
        if function_type == 'sin':
            y = a * np.sin(b * x) + c
        elif function_type == 'cos':
            y = a * np.cos(b * x) + c
        elif function_type == 'tan':
            y = a * np.tan(b * x) + c

        # Show the result in an info box
        messagebox.showinfo("Funzione goniometrica", f"Per x = {x}, y = {y}")

        # Close the input window
        action_window.destroy()

        # Plot the graph and reopen the main menu
        grafico_goniometrico(function_type, a, b, c)
        window.deiconify()

    # Button to submit the x value
    submit_button = tk.Button(action_window, text="Submit", command=calculate_y)
    submit_button.grid(row=1, columnspan=2, pady=10)


# Function to handle logarithmic function input
def fn_logaritmica():
    window.withdraw()  # Hide the main window

    # Create a new window for input
    input_window = tk.Toplevel()
    input_window.title("Funzione logaritmica")

    # Label to explain the format of the function
    label = tk.Label(input_window,
                     text="Hai selezionato una funzione logaritmica.\nIl formato è: y = a*log_[base] (bx) + c\nInserisci i valori:")
    label.grid(row=0, columnspan=2, padx=10, pady=10)

    # Labels and entry boxes for coefficients a, base, b, and c
    label_a = tk.Label(input_window, text="a:")
    label_a.grid(row=1, column=0, padx=5, pady=5)
    entry_a = tk.Entry(input_window)
    entry_a.grid(row=1, column=1, padx=5, pady=5)

    label_base = tk.Label(input_window, text="base:")
    label_base.grid(row=2, column=0, padx=5, pady=5)
    entry_base = tk.Entry(input_window)
    entry_base.grid(row=2, column=1, padx=5, pady=5)

    label_b = tk.Label(input_window, text="b:")
    label_b.grid(row=3, column=0, padx=5, pady=5)
    entry_b = tk.Entry(input_window)
    entry_b.grid(row=3, column=1, padx=5, pady=5)

    label_c = tk.Label(input_window, text="c:")
    label_c.grid(row=4, column=0, padx=5, pady=5)
    entry_c = tk.Entry(input_window)
    entry_c.grid(row=4, column=1, padx=5, pady=5)

    # Function to handle the submission of input and ask for further action
    def submit():
        try:
            # Get the coefficients
            a = float(entry_a.get())
            base = float(entry_base.get())
            b = float(entry_b.get())
            c = float(entry_c.get())
        except ValueError:
            messagebox.showerror("Errore", "Assicurati di inserire valori numerici validi.")
            return

        # Close the input window
        input_window.destroy()

        # Ask the user whether they want to plot the graph or calculate y
        user_choice = messagebox.askquestion("Seleziona azione",
                                             "Vuoi visualizzare il grafico o calcolare la y inserendo la x? (Sì è il grafico, No è il calcolo)",
                                             icon='question')

        if user_choice == 'yes':
            grafico_logaritmico(a, base, b, c)  # Plot the graph if user chooses 'yes'
        else:
            calcolo_logaritmico(a, base, b, c)  # Call the function to calculate y if user chooses 'no'

    # Button to submit the input
    submit_button = tk.Button(input_window, text="Submit", command=submit)
    submit_button.grid(row=5, columnspan=2, pady=10)


# Function to plot the logarithmic graph
def grafico_logaritmico(a, base, b, c):
    # Generate x values for the plot
    x = np.linspace(0.1, 10, 400)  # Avoid x=0 to prevent log(0) issues

    # Calculate the corresponding y values for the logarithmic function
    y = a * np.log10(b * x) / np.log10(base) + c

    # Create the plot
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f"{a}*log_{base}({b}x) + {c}")
    plt.title('Grafico della funzione logaritmica')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()

    # Reopen the main menu
    window.deiconify()


# Function to calculate y for the logarithmic function
def calcolo_logaritmico(a, base, b, c):
    window.withdraw()  # Hide the main window

    # Create a new window for input
    action_window = tk.Toplevel()
    action_window.title("Funzione logaritmica")

    # Label and entry box for x value
    label = tk.Label(action_window, text="Inserisci il valore di x:")
    label.grid(row=0, column=0, padx=10, pady=10)
    x_entry = tk.Entry(action_window)
    x_entry.grid(row=0, column=1, padx=10, pady=10)

    # Function to handle the submission of the x value and calculate y
    def calculate_y():
        try:
            x = float(x_entry.get())
        except ValueError:
            messagebox.showerror("Errore", "Assicurati di inserire un numero valido.")
            return

        # Calculate the corresponding y value based on the input x
        y = a * np.log10(b * x) / np.log10(base) + c

        # Show the result in an info box
        messagebox.showinfo("Funzione logaritmica", f"Per x = {x}, y = {y}")

        # Close the input window
        action_window.destroy()

        # Plot the graph and reopen the main menu
        grafico_logaritmico(a, base, b, c)
        window.deiconify()

    # Button to submit the x value
    submit_button = tk.Button(action_window, text="Submit", command=calculate_y)
    submit_button.grid(row=1, columnspan=2, pady=10)

# Function to handle exponential function input
def fn_esponenziale():
    window.withdraw()  # Hide the main window

    # Create a new window for input
    input_window = tk.Toplevel()
    input_window.title("Funzione esponenziale")

    # Label to explain the format of the function
    label = tk.Label(input_window, text="Hai selezionato una funzione esponenziale.\nIl formato è: y = base^(a*x) + b\nInserisci i valori:")
    label.grid(row=0, columnspan=2, padx=10, pady=10)

    # Labels and entry boxes for base, a, and b
    label_base = tk.Label(input_window, text="base:")
    label_base.grid(row=1, column=0, padx=5, pady=5)
    entry_base = tk.Entry(input_window)
    entry_base.grid(row=1, column=1, padx=5, pady=5)

    label_a = tk.Label(input_window, text="a:")
    label_a.grid(row=2, column=0, padx=5, pady=5)
    entry_a = tk.Entry(input_window)
    entry_a.grid(row=2, column=1, padx=5, pady=5)

    label_b = tk.Label(input_window, text="b:")
    label_b.grid(row=3, column=0, padx=5, pady=5)
    entry_b = tk.Entry(input_window)
    entry_b.grid(row=3, column=1, padx=5, pady=5)

    # Function to handle the submission of input and ask for further action
    def submit():
        try:
            base = float(entry_base.get())
            a = float(entry_a.get())
            b = float(entry_b.get())
        except ValueError:
            messagebox.showerror("Errore", "Assicurati di inserire valori numerici validi.")
            return

        # Close the input window
        input_window.destroy()

        # Ask the user whether they want to plot the graph or calculate y
        user_choice = messagebox.askquestion("Seleziona azione", "Vuoi visualizzare il grafico o calcolare la y inserendo la x? (Sì è il grafico, No è il calcolo)", icon='question')

        if user_choice == 'yes':
            grafico_esponenziale(base, a, b)  # Plot the graph if user chooses 'yes'
        else:
            calcolo_esponenziale(base, a, b)  # Call Action 2 if user chooses 'no'

    # Button to submit the input
    submit_button = tk.Button(input_window, text="Submit", command=submit)
    submit_button.grid(row=4, columnspan=2, pady=10)

# Function to plot the exponential graph
def grafico_esponenziale(base, a, b):
    # Generate x values for the plot
    x = np.linspace(-2, 2, 400)

    # Calculate the corresponding y values for the exponential function
    y = np.power(base, a * x) + b

    # Create the plot
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f"{base}^({a}x) + {b}")
    plt.title('Grafico della funzione esponenziale')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()

    # Reopen the main menu
    window.deiconify()

# Function for Action 2 for exponential function
def calcolo_esponenziale(base, a, b):
    window.withdraw()  # Hide the main window

    # Create a new window for input
    action_window = tk.Toplevel()
    action_window.title("Calcolo esponenziale")

    # Label and entry box for x value
    label = tk.Label(action_window, text="Inserisci il valore di x:")
    label.grid(row=0, column=0, padx=10, pady=10)
    x_entry = tk.Entry(action_window)
    x_entry.grid(row=0, column=1, padx=10, pady=10)

    # Function to handle the submission of the x value and calculate y
    def calculate_y():
        try:
            x = float(x_entry.get())
        except ValueError:
            messagebox.showerror("Errore", "Assicurati di inserire un numero valido.")
            return

        # Calculate the corresponding y value based on the exponential function
        y = np.power(base, a * x) + b

        # Show the result in an info box
        messagebox.showinfo("Funzione esponenziale", f"Per x = {x}, y = {y}")

        # Close the input window
        action_window.destroy()

        # Plot the graph and reopen the main menu
        grafico_esponenziale(base, a, b)
        window.deiconify()

    # Button to submit the x value
    submit_button = tk.Button(action_window, text="Submit", command=calculate_y)
    submit_button.grid(row=1, columnspan=2, pady=10)

def fn_fratta():
    window.withdraw()  # Hide the main window

    # Create a new window for input
    input_window = tk.Toplevel()
    input_window.title("Funzione fratta")

    # Label to explain the format of the function
    label = tk.Label(input_window, text="Hai selezionato una funzione fratta.\nIl formato è: (ax + b) / (cx + d).\nInserisci i valori dei coefficienti:")
    label.grid(row=0, columnspan=2, padx=10, pady=10)

    # Labels and entry boxes for each coefficient
    labels = ['a:', 'b:', 'c:', 'd:']
    entries = []

    for i, coeff in enumerate(labels):
        lbl = tk.Label(input_window, text=coeff)
        lbl.grid(row=i+1, column=0, padx=5, pady=5)
        entry = tk.Entry(input_window)
        entry.grid(row=i+1, column=1, padx=5, pady=5)
        entries.append(entry)

    # Function to handle the submission of input and ask for further action
    def submit():
        try:
            # Get all coefficient values as floats
            a = float(entries[0].get())
            b = float(entries[1].get())
            c = float(entries[2].get())
            d = float(entries[3].get())
        except ValueError:
            messagebox.showerror("Errore", "Numero invalido.")
            return

        # Check if both c and d are 0
        if c == 0 and d == 0:
            messagebox.showerror("Errore", "Funzione invalida: c e d non possono essere entrambi zero.")
            return

        # Close the input window
        input_window.destroy()

        # Show the main window again
        window.deiconify()

        # Ask the user whether they want to plot the graph or perform Action 2
        user_choice = messagebox.askquestion("Seleziona azione", "Vuoi visualizzare il grafico o calcolare la y inserendo la x? (Sì è il grafico, No è il calcolo)", icon='question')

        if user_choice == 'yes':
            grafico_fratta(a, b, c, d)  # Plot the graph if user chooses 'yes'
        else:
            calcolo_fratta(a, b, c, d)  # Call Action 2 if user chooses 'no'

    # Button to submit the input
    submit_button = tk.Button(input_window, text="Submit", command=submit)
    submit_button.grid(row=5, columnspan=2, pady=10)


def grafico_fratta(a, b, c, d):
    # Generate x values for the plot
    x = np.linspace(-10, 10, 400)

    # Avoid division by zero by splitting into segments
    x_left = x[x < -d / c]  # Values where x < -d / c
    x_right = x[x > -d / c]  # Values where x > -d / c

    # Calculate the corresponding y values for the rational function
    # Exclude values where denominator is close to zero
    y_left = (a * x_left + b) / (c * x_left + d)
    y_right = (a * x_right + b) / (c * x_right + d)

    # Create the plot
    plt.figure(figsize=(8, 6))

    # Plot left segment
    plt.plot(x_left, y_left, label=f"({a}x + {b}) / ({c}x + {d})", color='blue')

    # Plot right segment
    plt.plot(x_right, y_right, color='blue')

    # Add vertical line for the asymptote
    asymptote_x = -d / c
    plt.axvline(asymptote_x, color='red', linestyle='--', label=f"Asintoto verticale x = {asymptote_x}")

    # Add horizontal asymptote if c != 0
    if c != 0:
        asymptote_y = a / c
        plt.axhline(asymptote_y, color='green', linestyle='--', label=f"Asintoto orizzontale y = {asymptote_y}")

    plt.title('Grafico della funzione fratta')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()

def calcolo_fratta(a, b, c, d):
    window.withdraw()  # Hide the main window

    # Create a new window for input
    action_window = tk.Toplevel()
    action_window.title("Calcolo funzione fratta")

    # Label and entry box for x value
    label = tk.Label(action_window, text="Inserisci il valore di x:")
    label.grid(row=0, column=0, padx=10, pady=10)
    x_entry = tk.Entry(action_window)
    x_entry.grid(row=0, column=1, padx=10, pady=10)

    # Function to handle the submission of the x value and calculate y
    def calculate_y():
        try:
            x = float(x_entry.get())
        except ValueError:
            messagebox.showerror("Errore", "Assicurati di inserire un numero valido.")
            return

        # Check if both c and d are 0
        if c == 0 and d == 0:
            messagebox.showerror("Errore", "Funzione invalida: c e d non possono essere entrambi zero.")
            return

        # Calculate the corresponding y value for the given x
        y = (a * x + b) / (c * x + d)

        # Show the result in an info box
        messagebox.showinfo("Funzione fratta", f"Per x = {x}, y = {y}")

        # Close the input window
        action_window.destroy()

        # Plot the graph and reopen the main menu
        grafico_fratta(a, b, c, d)
        window.deiconify()

    # Button to submit the x value
    submit_button = tk.Button(action_window, text="Submit", command=calculate_y)
    submit_button.grid(row=1, columnspan=2, pady=10)


def fn_irrazionale():
    window.withdraw()  # Hide the main window

    # Create a new window for input
    input_window = tk.Toplevel()
    input_window.title("Funzione irrazionale")

    # Label to explain the format of the function
    label = tk.Label(input_window,
                     text="Hai selezionato una funzione irrazionale.\nIl formato è: y = a*sqrt(bx) + c.\nInserisci i valori dei coefficienti:")
    label.grid(row=0, columnspan=2, padx=10, pady=10)

    # Labels and entry boxes for each coefficient
    labels = ['a:', 'b:', 'c:']
    global coefficients_irrazionale
    entries = []

    for i, coeff in enumerate(labels):
        lbl = tk.Label(input_window, text=coeff)
        lbl.grid(row=i + 1, column=0, padx=5, pady=5)
        entry = tk.Entry(input_window)
        entry.grid(row=i + 1, column=1, padx=5, pady=5)
        entries.append(entry)

    # Function to handle the submission of input and ask for further action
    def submit():
        global coefficients_irrazionale
        try:
            # Get all coefficient values as floats
            coefficients_irrazionale = [float(entry.get()) for entry in entries]
        except ValueError:
            messagebox.showerror("Errore", "Numero invalido.")
            return

        # Close the input window
        input_window.destroy()

        # Ask the user whether they want to plot the graph or perform Action 2
        user_choice = messagebox.askquestion("Seleziona azione",
                                             "Vuoi visualizzare il grafico o calcolare la y inserendo la x? (Sì è il grafico, No è il calcolo)",
                                             icon='question')

        if user_choice == 'yes':
            grafico_irrazionale(coefficients_irrazionale)  # Plot the graph if user chooses 'yes'
        else:
            calcolo_irrazionale()  # Call Action 2 if user chooses 'no'

    # Button to submit the input
    submit_button = tk.Button(input_window, text="Submit", command=submit)
    submit_button.grid(row=4, columnspan=2, pady=10)


# Function to calculate y for a given x
def calcolo_irrazionale():
    window.withdraw()  # Hide the main window

    # Create a new window for input
    action_window = tk.Toplevel()
    action_window.title("Calcolo funzione irrazionale")

    # Label and entry box for x value
    label = tk.Label(action_window, text="Inserisci il valore di x:")
    label.grid(row=0, column=0, padx=10, pady=10)
    x_entry = tk.Entry(action_window)
    x_entry.grid(row=0, column=1, padx=10, pady=10)

    # Function to handle the submission of the x value and calculate y
    def calculate_y():
        try:
            x = float(x_entry.get())
            a, b, c = coefficients_irrazionale
            if b * x < 0:
                messagebox.showerror("Errore", "Il valore di bx deve essere non negativo.")
                return
            y = a * m.sqrt(b * x) + c
            messagebox.showinfo("Funzione irrazionale", f"Per x = {x}, y = {y}")
        except ValueError:
            messagebox.showerror("Errore", "Assicurati di inserire un numero valido.")
            return

        # Close the input window
        action_window.destroy()

        # Plot the graph and reopen the main menu
        grafico_irrazionale(coefficients_irrazionale)
        window.deiconify()

    # Button to submit the x value
    submit_button = tk.Button(action_window, text="Submit", command=calculate_y)
    submit_button.grid(row=1, columnspan=2, pady=10)


# Function to plot the irrational function
def grafico_irrazionale(coefficients):
    a, b, c = coefficients

    # Generate x values for the plot
    x = np.linspace(0, 10, 400)  # Start from 0 to avoid sqrt of negative numbers

    # Calculate the corresponding y values for the irrational function
    y = a * np.sqrt(b * x) + c

    # Create the plot
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f"{a}*sqrt({b}x) + {c}")
    plt.title('Grafico della funzione irrazionale')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()

# Main window
window = tk.Tk()
window.title("Calcolatrice grafica Python")

# Configure rows and columns of the window
window.rowconfigure(0, minsize=400, weight=1)
window.columnconfigure(1, minsize=400, weight=1)

# Label for the title with a larger font
title_label = tk.Label(
    window,
    text="Calcolatrice grafica Python",
    fg="black",
    bg="white",
    width=30,
    height=1,
    font=("Helvetica", 24, "bold")  # Larger font for the title
)

# Frame to hold the buttons
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

# Buttons for different functions
btn_quintica = tk.Button(frm_buttons, text="Funzione quintica", height=2, command=fn_quintica)
btn_goniometrica = tk.Button(frm_buttons, text="Funzione goniometrica", height=2, command=fn_goniometrica)
btn_logaritmica = tk.Button(frm_buttons, text="Funzione logaritmica", height=2, command=fn_logaritmica)
btn_esponenziale = tk.Button(frm_buttons, text="Funzione esponenziale", height=2, command=fn_esponenziale)
btn_fratta = tk.Button(frm_buttons, text="Funzione fratta", height=2, command=fn_fratta)
btn_irrazionale = tk.Button(frm_buttons, text="Funzione irrazionale", height=2, command=fn_irrazionale)

# Place buttons in the grid within the frame
btn_quintica.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_goniometrica.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_logaritmica.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_esponenziale.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
btn_fratta.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
btn_irrazionale.grid(row=6, column=0, sticky="ew", padx=5, pady=5)

# Place the buttons frame and labels in the main window
frm_buttons.grid(row=0, column=0, sticky="ns")
title_label.grid(row=0, column=1, sticky="nsew")

# Start the application
window.mainloop()