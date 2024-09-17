
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


ventana = tk.Tk()
ventana.title("Mi Agenda Personal")
ventana.configure(background='sky blue')

# Frame para la lista de eventos
frame_lista = ttk.Frame(ventana)
frame_lista.pack(side="left", padx=50, pady=50)

# Frame para los campos de entrada y botones
frame_entradas = ttk.Frame(ventana)
frame_entradas.pack(side="right", padx=10, pady=10)

# Columnas para la lista
columnas = ("fecha", "hora", "descripcion")
tree = ttk.Treeview(frame_lista, columns=columnas, show="headings")
tree.heading("fecha", text="Fecha")
tree.heading("hora", text="Hora")
tree.heading("descripcion", text="Descripción")
tree.pack()

# Campos de entrada
fecha_var = tk.StringVar()
hora_var = tk.StringVar()
descripcion_var = tk.StringVar()
fecha_entry = ttk.Entry(frame_entradas, textvariable=fecha_var)
hora_entry = ttk.Entry(frame_entradas, textvariable=hora_var)
descripcion_entry = ttk.Entry(frame_entradas, textvariable=descripcion_var)



def agregar_evento():
    # Obtener los datos de los campos de entrada
    fecha = fecha_var.get()
    hora = hora_var.get()
    descripcion = descripcion_var.get()
    # Agregar el evento a la lista (implementar la lógica de almacenamiento)
    # ...
    # Actualizar la TreeView
    tree.insert("", "end", values=(fecha, hora, descripcion))

def eliminar_evento():
    # Obtener el elemento seleccionado en la TreeView
    item_seleccionado = tree.selection()
    # Mostrar un diálogo de confirmación
    if messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar este evento?"):
        # Eliminar el evento de la lista (implementar la lógica de eliminación)
        # Eliminar el elemento de la TreeView
        tree.delete(item_seleccionado)

agregar_btn = ttk.Button(frame_entradas, text="Agregar Evento", command= agregar_evento)
eliminar_btn = ttk.Button(frame_entradas, text="Eliminar Evento", command= eliminar_evento)
salir_btn = ttk.Button(frame_entradas, text="Salir", command=ventana.quit)


fecha_entry.grid(row=0, column=0, sticky="we")
hora_entry.grid(row=1, column=0, sticky="we")
descripcion_entry.grid(row=2, column=0, sticky="we")
agregar_btn.grid(row=3, column=0, sticky="we")
eliminar_btn.grid(row=4, column=0, sticky="we")
salir_btn.grid(row=5, column=0, sticky="we")





def eliminar_evento():
    # Obtener el elemento seleccionado en la TreeView
    item_seleccionado = tree.selection()
    # Mostrar un diálogo de confirmación
    if messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar este evento?"):
        tree.delete(item_seleccionado)

ventana.mainloop()