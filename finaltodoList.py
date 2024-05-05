import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def add_task():
    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Field is Empty.')
    else:
        tasks.append(task_string)
        list_update()
        #0 indicates the index jaha se deletion start karna hai
        #'end' is a special index representing the end of widget's text
        task_field.delete(0, 'end')

def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task)

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        selected_task = task_listbox.get(selected_task_index)
        tasks.remove(selected_task)
        list_update()
    except IndexError:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

def delete_all_tasks():
    #messagebox is a module in tkinter lib, and messagebox.askyesno is a function thqat ask buttons, yes or no
    #if user chooses no, the message box returns false, and themethos inside it is not executed further
    del_choice = messagebox.askyesno('Delete All', 'Are you sure?')
    if del_choice:
        tasks.clear()
        list_update()

def clear_list():
    task_listbox.delete(0, 'end')

def close():
    # print(tasks)
    my_window.destroy()



my_window = tk.Tk()
my_window.title("To-Do List Manager")
my_window.geometry("900x750")
my_window.resizable(False, False)
my_window.configure(bg="black")

tasks = []

header_frame = tk.Frame(my_window, bg="black")
functions_frame = tk.Frame(my_window, bg="black")
listbox_frame = tk.Frame(my_window, bg="black")

header_frame.pack(fill="both")
functions_frame.pack(side="left", expand=True, fill="both")
listbox_frame.pack(side="right", expand=True, fill="both")

header_label = ttk.Label(
        header_frame,
        text="The To-Do List",
        font=("Algerian", "80"),
        background="black",
        foreground="beige"
)
header_label.pack(padx=20, pady=20)

task_label = ttk.Label(
        functions_frame,
        text="Enter the Task:",
        font=("Times New Roman", "30", "bold"),
        background="black",
        foreground="white"
    )
task_label.place(x=30, y=40)

task_field = ttk.Entry(
        functions_frame,
        font=("Comic Sans MS", "12"),
        width=30,
        background="white",
        foreground="black"
)
task_field.place(x=20, y=100)

add_button = ttk.Button(
        functions_frame,
        text="Add Task",
        # font=("Comic Sans MS", "12"),
        width=30,
        command=add_task
)
del_button = ttk.Button(
        functions_frame,
        text="Delete Task",
        # font=("Comic Sans MS", "12"),
        width=30,
        command=delete_task
)
del_all_button = ttk.Button(
    functions_frame,
    text="Delete All Tasks",
    # font=("Comic Sans MS", "12"),
    width=30,
    command=delete_all_tasks
)
exit_button = ttk.Button(
    functions_frame,
    text="Exit",
    width=30,
    command=close
)
add_button.place(x=30, y=200)
del_button.place(x=30, y=260)
del_all_button.place(x=30, y=320)
exit_button.place(x=30, y=380)

task_listbox = tk.Listbox(
        listbox_frame,
        width=80,
        height=40,
        selectmode='SINGLE',
        background="gray14",
        foreground="aqua",
        selectbackground="crimson",
        selectforeground="white",
        font=("Comic Sans MS", 20)
    )
task_listbox.place(x=50, y=50)

list_update()
my_window.mainloop()
