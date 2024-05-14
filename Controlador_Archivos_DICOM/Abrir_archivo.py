import tkinter as tk
from tkinter import filedialog

def obtener_ruta_carpeta(event):
    ruta_carpeta = filedialog.askdirectory()
    print("Ruta de la carpeta:", ruta_carpeta)

root = tk.Tk()

root.title("Software Visualizador")
root.geometry("800x400")

label = tk.Label(root, text="Haz clic aquí para seleccionar una carpeta", font=("Arial", 12))
label.pack(expand=True, fill="both")

label.bind("<ButtonRelease-1>", obtener_ruta_carpeta)

root.mainloop()