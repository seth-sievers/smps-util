import tkinter as tk
import sv_ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

def main():
    # 1. Create the root window
    root = tk.Tk()
    root.title("sv-ttk Themed Matplotlib Embed")

    # 2. Apply an sv-ttk theme ("light", "dark", or any custom theme you've registered)
    sv_ttk.set_theme("light")

    # 3. Create a frame to hold the Matplotlib figure + toolbar
    plot_frame = tk.Frame(root)
    plot_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # 4. Build a Matplotlib Figure and plot something
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    x = [i * 0.1 for i in range(100)]
    y = [i ** 2 for i in x]  # simple quadratic
    ax.plot(x, y, color="#FF6F61", linewidth=2)
    ax.set_title("y = x\u00b2")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    # 5. Embed the Figure into Tkinter via FigureCanvasTkAgg
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # 6. Add the Matplotlib navigation toolbar
    toolbar = NavigationToolbar2Tk(canvas, plot_frame)
    toolbar.update()
    toolbar.pack(side=tk.BOTTOM, fill=tk.X)

    # 7. Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()