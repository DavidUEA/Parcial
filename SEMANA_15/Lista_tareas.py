import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self,root):
        self.root = root
        self.root.title("GESTOR DE TAREAS")

        #LISTA DE TAREAS
        self.tasks=[]

        #campo de entrada
        self.entry = tk.Entry(root,width=40)

        self.entry.pack(pady=10)
        self.entry.bind("<Return>",self.add_task)

        self.add_button= tk.Button(root,text= "Añadir Tarea")
        self.add_button.pack(pady=5)

        self.complete_button= tk.Button(root,text="Marcar como completada")
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root,text="Eliminar Tarea")
        self.delete_button.pack(pady=5)
        #listas de Tareas

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=5)

    def add_task(self,event=None):
        task = self.entry.get().strip()
        if task:
            self.tasks.append(task)
            #Llamar componente
            self.update_task_listbox()
            self.entry.delete(0,tk.END)
        else:
            messagebox.showwarning("Advertencia", message="No se puede agregar tu tarea vacia")


    def update_task_(self,listbox):
        listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()

