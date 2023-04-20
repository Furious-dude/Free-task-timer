import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import threading

# Global variables
tasks = [
    {"name": "Task Ngồi code" ,"time": timedelta(minutes=30), "priority": 10},
    {"name": "Task 2 Đọc sách"," time": timedelta(minutes=15), "priority": 9},
    {"name": "Task 3","vẽ time": timedelta(minutes=45), "priority": 3},
    {"name": "Task 4","making money time": timedelta(minutes=20), "priority": 2},
    {"name": "Task 5","vẽ/making doujin time": timedelta(minutes=45), "priority": 3},
    {"name": "Task 6","workout time": timedelta(minutes=45), "priority": 3},
    {"name": "Task 7","meditation time": timedelta(minutes=45), "priority": 3},
    {"name": "Task 8","learning new language time": timedelta(minutes=45), "priority": 3},
    {"name": "Task 9","xoa bóp huyệt time": timedelta(minutes=45), "priority": 3},
]
current_task = None
time_left = None
timer_thread = None

# Define a function to update the timer display
def update_timer():
    global time_left, timer_thread
    time_left -= timedelta(seconds=1)
    if time_left.total_seconds() < 0:
        messagebox.showinfo("Time is up!", "Time is up for the current task.")
        next_task()
    else:
        time_left_str = str(time_left).split(".")[0]
        time_label.config(text=time_left_str)
        timer_thread = threading.Timer(1, update_timer)
        timer_thread.start()

# Define a function to display a task
def display_task(task):
    global time_left
    task_label.config(text=f"Task: {task['name']} (Priority: {task['priority']})")
    time_left = task["time"]
    time_left_str = str(time_left).split(".")[0]
    time_label.config(text=time_left_str)

# Define a function to start the timer for the current task
def start_task():
    global current_task, time_left, timer_thread
    current_task = 0
    display_task(tasks[current_task])
    start_button.config(state="disabled")
    add_button.config(state="disabled")
    edit_button.config(state="disabled")
    delete_button.config(state="disabled")
    timer_thread = threading.Timer(1, update_timer)
    timer_thread.start()

# Define a function to move to the next task
def next_task():
    global current_task, time_left, timer_thread
    time_left = None
    current_task = (current_task + 1) % len(tasks)
    if current_task >= len(tasks):
        current_task = 0
    display_task(tasks[current_task])
    if "time" in tasks[current_task]:
        display_task(tasks[current_task])
    else:
        next_task()
    
    
# Define a function to move to the next task sooner
def skip_task():
    global time_left, timer_thread
    time_left = timedelta(seconds=0)
    timer_thread.cancel()
    next_task()

# Define a function to add a new task
def add_task():
    name = name_entry.get()
    time_str = time_entry.get()
    priority_str = priority_entry.get()

    if not all((name, time_str, priority_str)):
        messagebox.showwarning("Incomplete Data", "Please fill all input fields")
        return

    try:
        time = timedelta(minutes=int(time_str))
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid integer for time")
        return

    try:
        priority = int(priority_str)
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid integer for priority")
        return

    tasks.append({"name": name, "time": time, "priority": priority})
    name_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    priority_entry.delete(0, tk.END)


# Define a function to edit the current task
def edit_task():
    global current_task, time_left, timer_thread
    name = name_entry.get()
    minutes = int(time_entry.get())
    priority = int(priority_entry.get())
    tasks[current_task] = {"name": name, "time": timedelta(minutes=minutes), "priority": priority}
    display_task(tasks[current_task])

# Define a function to delete the current task
def delete_task():
    global current_task, time_left, timer_thread
    del tasks[current_task]
    if current_task >= len(tasks):
        current_task = 0
    display_task(tasks[current_task])

# Create the main window
root = tk.Tk()
root.title("Task Timer")

# Create the task label and timer label
task_label = tk.Label(root, text="", font=("Arial", 18))
task_label.pack(pady=10)
time_label = tk.Label(root, text="", font=("Arial", 24))
time_label.pack(pady=20)

# Create the start button, add button, edit button, delete button, and skip button
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
start_button = tk.Button(button_frame, text="Start", font=("Arial", 14), command=start_task)
start_button.grid(row=0, column=0, padx=10)
add_button = tk.Button(button_frame, text="Add", font=("Arial", 14), command=add_task)
add_button.grid(row=0, column=1, padx=10)
edit_button = tk.Button(button_frame, text="Edit", font=("Arial", 14), command=edit_task)
edit_button.grid(row=0, column=2, padx=10)
delete_button = tk.Button(button_frame, text="Delete", font=("Arial", 14), command=delete_task)
delete_button.grid(row=0, column=3, padx=10)
skip_button = tk.Button(button_frame, text="Skip", font=("Arial", 14), command=skip_task)
skip_button.grid(row=0, column=4, padx=10)

# Create the task input label, name entry, time entry, priority entry, and add button
input_frame = tk.Frame(root)
input_frame.pack(pady=10)
name_label = tk.Label(input_frame, text="Task Name:", font=("Arial", 14))
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(input_frame, font=("Arial", 14))
name_entry.grid(row=0, column=1, padx=10, pady=5)

time_label = tk.Label(input_frame, text="Task Time (in minutes):", font=("Arial", 14))
time_label.grid(row=1, column=0, padx=10, pady=5)
time_entry = tk.Entry(input_frame, font=("Arial", 14))
time_entry.grid(row=1, column=1, padx=10, pady=5)

priority_label = tk.Label(input_frame, text="Task Priority:", font=("Arial", 14))
priority_label.grid(row=2, column=0, padx=10, pady=5)
priority_entry = tk.Entry(input_frame, font=("Arial", 14))
priority_entry.grid(row=2, column=1, padx=10, pady=5)

add_task_button = tk.Button(input_frame, text="Add Task", font=("Arial", 14), command=add_task)
add_task_button.grid(row=3, column=1, padx=10, pady=5)

# Run the main loop
root.mainloop()
