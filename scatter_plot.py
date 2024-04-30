import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def toggle_plot():
    global canvas
    if canvas is None:
        fig, ax = plt.subplots()
        x = [1, 2, 3, 4, 5]
        y = [2, 3, 4, 5, 6]
        ax.scatter(x, y)
        canvas = FigureCanvasTkAgg (fig, master = window) #Embedding figure in Tkinter
        canvas.draw()
        canvas.get_tk_widget().pack()
    else:
        canvas.get_tk_widget().pack_forget()
        canvas = None

def on_close():
    print ("Closing application")
    window.quit() #Stops the Tkinter main loop
    window.destroy() #This is necessary on Windows to prevent "Fatal Python Error: PyEval_RestoreThread: NULL tstate"

canvas = None

window = tk.Tk()
window.title("Scatter Plot")
plot_button = tk.Button(window, text = "Toggle Plot", command = toggle_plot)
plot_button.pack()

close_button = tk.Button(window, text = "Close", command = on_close)
close_button.pack()

window.protocol ("WM_DELETE_WINDOW", on_close) #Handle window close button

window.mainloop()