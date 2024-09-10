import tkinter as tk

app = tk.Tk()


"dimension ancho x altura"
app.geometry('800x800')
app.configure(background='sky blue')
tk.Wm.wm_title(app, "Programa de Interfaz")
tk.Button(
    app,
    text="Agregar informacion",
    font=("Courier", 14),
    bg="#00a8e8",
    fg="White"
).pack(
    fill=tk.BOTH,
    expand=False
)

tk.Label(
    app,
    text="Ingrese",
    bg="black",
    fg="White",
    justify="center"
).pack(
    fill=tk.BOTH,
    expand=True,
)
tk.Entry(
    bg="black",
    fg="White",
    justify="center",
   ).pack(
    fill=tk.BOTH,
    expand=True,

)
app.mainloop()