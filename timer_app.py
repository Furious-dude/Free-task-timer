import tkinter as tk
import time

# Create a list of tasks with their estimated durations (in minutes)
tasks = [
    {"name": "Task 1", "time": 30, "priority": 5},
    {"name": "Task 2", "time": 15, "priority": 3},
    {"name": "Task 3", "time": 45, "priority": 10},
    {"name": "Task 4", "time": 20, "priority": 2}
]

# Define a function to display the current task and time remaining
def display_task(task):
    task_label.config(text=task["name"])
    time_remaining = task["time"] - (time.time() - start_time) // 60
    time_label.config(text=f"{time_remaining} minutes remaining")

# Define a function to start the timer
def start_timer():
    global start_time, current_task
    start_time = time.time()
    current_task = 0
    display_task(tasks[current_task])
    start_button.config(state="disabled")
    next_button.config(state="normal")

# Define a function to move to the next task
def next_task():
    global current_task
    current_task += 1
    if current_task >= len(tasks):
        task_label.config(text="All tasks completed!")
        time_label.config(text="")
        next_button.config(state="disabled")
    else:
        display_task(tasks[current_task])

# Define a function to add a new task
def add_task():
    name = name_entry.get()
    time_minutes = int(time_entry.get())
    priority = int(priority_entry.get())
    tasks.append({"name": name, "time": time_minutes, "priority": priority})
    name_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    priority_entry.delete(0, tk.END)

# Create the GUI
root = tk.Tk()
root.title("Time Tracker")
root.geometry("400x200")

task_label = tk.Label(root, text="")
task_label.pack(pady=10)

time_label = tk.Label(root, text="")
time_label.pack(pady=10)

start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack(pady=10)

next_button = tk.Button(root, text="Next Task", command=next_task, state="disabled")
next_button.pack(pady=10)

# Create a frame for adding new tasks
add_frame = tk.Frame(root)
add_frame.pack(pady=10)

# Add entry boxes and labels for name, time, and priority
name_label = tk.Label(add_frame, text="Task Name")
name_label.grid(row=0, column=0, padx=5, pady=5)

name_entry = tk.Entry(add_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

time_label = tk.Label(add_frame, text="Task Time (Minutes)")
time_label.grid(row=1, column=0, padx=5, pady=5)

time_entry = tk.Entry(add_frame)
time_entry.grid(row=1, column=1, padx=5, pady=5)

priority_label = tk.Label(add_frame, text="Task Priority")
priority_label.grid(row=2, column=0, padx=5, pady=5)

priority_entry = tk.Entry(add_frame)
priority_entry.grid(row=2, column=1, padx=5, pady=5)

# Add a button to add the task to the list
add_button = tk.Button(add_frame, text="Add Task", command=add_task)
add_button.grid(row=3, column=1, padx=5, pady=5)

# Add a button to manually move to the next task in the list
advance_button = tk.Button(root, text="Advance", command=next_task)
advance_button.pack(pady=10)


start_time = time.time()
time_limit_seconds = 60

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    remaining_time = time_limit_seconds - elapsed_time
    if remaining_time <= 0:
        print("Time's up!")
        break
    else:
        print(f"Time remaining: {int(remaining_time)} seconds")
        time.sleep(1)


root.mainloop()
