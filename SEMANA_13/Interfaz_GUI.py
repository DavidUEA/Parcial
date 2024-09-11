import tkinter as tk
from tkinter import messagebox

#creamos una ventana
app = tk.Tk()
entrada = tk.StringVar(app)
"dimension ancho x altura"
app.geometry('700x700')
app.configure(background='sky blue')
tk.Wm.wm_title(app, "Programa de Interfaz")

tk.Label(
    app,
    text="Bienvenidos a nuestra primera aplicación de Interfaz",
    bg="orange",
    fg="White",
    font=("Courier", 14),
    justify="center"

).pack(
    fill=tk.BOTH,
    expand=False,
)

def Llamar():
    texto_ingrese = entrada.get()
    messagebox.showinfo("llamar", message=f"{texto_ingrese}")



tk.Button(app,
    text="Agregar informacion",
    font=("Courier", 14),
    bg="#00a8e8",
    fg="White",
    width=10,
    height= 2,
    command=Llamar

).pack(
    fill=tk.BOTH,
    expand=False
)

tk.Entry(
    app,
    bg="green",
    fg="White",
    justify="center",
    font=("Courier", 14),
    textvariable=entrada
).pack(
    fill=tk.BOTH,
    expand=True,
)
app.mainloop()