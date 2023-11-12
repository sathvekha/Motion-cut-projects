import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []
        self.completed_tasks = []

        self.task_entry = tk.Entry(self.root, width=60)
        self.task_entry.grid(row=0, column=0, padx=10, pady=40)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=40)

        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=40)

        self.mark_completed_button = tk.Button(self.root, text="Mark Completed", command=self.mark_completed_task)
        self.mark_completed_button.grid(row=2, column=0, padx=10, pady=40)

        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_button.grid(row=2, column=1, padx=10, pady=40)

        self.remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=3, column=0, columnspan=2, padx=10, pady=40)

        self.display_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.display_tasks()
            self.task_entry.delete(0, 'end')
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def display_tasks(self):
        self.task_listbox.delete(0, 'end')
        for task in self.tasks:
            self.task_listbox.insert('end', task)

    def mark_completed_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks.pop(selected_task_index[0])
            self.completed_tasks.append(task)
            self.display_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            updated_task = self.task_entry.get()
            if updated_task:
                self.tasks[selected_task_index[0]] = updated_task
                self.display_tasks()
                self.task_entry.delete(0, 'end')
            else:
                messagebox.showwarning("Warning", "Please enter a task.")
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.display_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
