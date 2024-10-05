import tkinter as tk
from tkinter import messagebox

class TaskManager:

    def __init__(self,root):
        self.root = root
        self.root.title("Task Manager")


    #Lista de tareas
        self.tasks =[]

        #Campos de entrada
        self.task_entry=tk.Entry(self.root, width=50)
        self.task_entry.pack(pady=10)

        #lista de tareas
        self.List_box=tk.Listbox(self.root)
        self.List_box.pack(pady=10)

        #Botones
        self.add_button=tk.Button(root,text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=10)

        self.complete_button=tk.Button(root,text="Complete Tarea", command=self.complete_task)
        self.complete_button.pack(pady=10)

        self.delete_button=tk.Button(root,text="Eliminar Tarea")
        self.delete_button.pack(pady=10)

        #Atajos del teclado
        self.root.bind("<Return>", lambda event: self.add_task())
        self.root.bind("<C>", lambda event: self.complete_task())
        self.root.bind("<D>", lambda event: self.delete_task())
        self.root.bind("<Delete>", lambda event: self.root)
        self.root.bind("Escape>", lambda event: self.root.quit())


    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"Task":task,"completed":False})
            self.update_task_listbox()
        else:
            messagebox.showerror("Error","No se encuentra la tarea")


    def complete_task(self):
        selected_task_index = self.List_box.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks[index]["completed"] = True
            self.update_task_listbox()

        else:
            messagebox.showerror("error","No se encuentra ")

    def update_task_listbox(self):
        self.List_box.delete(0,tk.END)
        #añadir tarea
        for task in self.tasks:
            display_tak = task["Task"]
            if task["completed"]:
                display_tak += " (completada) "
            self.List_box.insert(tk.END,display_tak)


    def delete_task(self):
        selected_task_index = self.List_box.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.update_task_listbox()
        else:
            messagebox.showerror("advetencia","no hay tarea seleccionada")


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()