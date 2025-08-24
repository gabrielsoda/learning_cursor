from flask import Flask, render_template, request, redirect
import json
import os

# TO-DO APP
# each task has a title, description, and a boolean indicating if it is completed
# each task is a dictionary with the following keys: id, title, description, completed
# 1. Create a list of items
# 2. Display the list of items
# 3. Add a new item to the list
# 4. Delete an item from the list
# 5. Update an item in the list
# 6. Search for an item in the list

# File to store tasks
TASKS_FILE = "tasks.json"

# Initialize tasks list
tasks = []

# Function to load tasks from JSON file
def load_tasks():
    global tasks
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r', encoding='utf-8') as file:
                tasks = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            tasks = []
    else:
        # Create default tasks if file doesn't exist
        tasks = [
            {"id": 1, "title": "Task 1", "description": "Description 1", "completed": False},
            {"id": 2, "title": "Task 2", "description": "Description 2", "completed": False},
            {"id": 3, "title": "Task 3", "description": "Description 3", "completed": False},
        ]
        save_tasks()

# Function to save tasks to JSON file
def save_tasks():
    try:
        with open(TASKS_FILE, 'w', encoding='utf-8') as file:
            json.dump(tasks, file, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving tasks: {e}")

app = Flask(__name__)

# Function to get the next available ID
def get_next_id():
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

# Function to add a new task
def add_task(text):
    new_task = {
        "id": get_next_id(),
        "title": f"Task {get_next_id()}",
        "description": text,
        "completed": False
    }
    tasks.append(new_task)
    save_tasks()  # Save after adding
    return new_task

# Function to complete a task by ID
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks()  # Save after completing
            return task
    return None

# Function to edit a task description by ID
def edit_task(task_id, new_description):
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            save_tasks()  # Save after editing
            return task
    return None

# main page: display the list of tasks and form to add a new task
@app.route("/")
def index():
    # sort tasks by completed status (incompleted first), then by id
    tasks.sort(key=lambda x: (x["completed"], x["id"]))
    return render_template("index.html", tasks=tasks) # render the index.html template with the tasks list

# add a new task
@app.route("/add", methods=["POST"])
def add():
    task_text = request.form["task"] # get the task from the form
    add_task(task_text) # add the task to the tasks list
    return redirect("/") # redirect to the main page

# mark a task as completed
@app.route("/complete/<int:task_id>")
def complete(task_id):
    complete_task(task_id) # mark the task as completed
    return redirect("/") # redirect to the main page

# delete a task
@app.route("/delete/<int:task_id>")
def delete(task_id):
    # Find and remove the task with the given ID
    tasks[:] = [task for task in tasks if task["id"] != task_id]
    save_tasks()  # Save after deleting
    return redirect("/") # redirect to the main page

# edit a task description
@app.route("/edit/<int:task_id>", methods=["POST"])
def edit(task_id):
    new_description = request.form["description"] # get the new description from the form
    edit_task(task_id, new_description) # update the task description
    return redirect("/") # redirect to the main page

if __name__ == "__main__":
    # Load tasks when starting the app
    load_tasks()
    app.run(debug=True)

