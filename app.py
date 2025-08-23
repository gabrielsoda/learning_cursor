from flask import Flask, render_template, request, redirect
# TO-DO APP
# each task has a title, description, and a boolean indicating if it is completed
# each task is a dictionary with the following keys: id, title, description, completed
# 1. Create a list of items
# 2. Display the list of items
# 3. Add a new item to the list
# 4. Delete an item from the list
# 5. Update an item in the list
# 6. Search for an item in the list

tasks = [
    {"id": 1, "title": "Task 1", "description": "Description 1", "completed": False},
    {"id": 2, "title": "Task 2", "description": "Description 2", "completed": False},
    {"id": 3, "title": "Task 3", "description": "Description 3", "completed": False},
]

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
    return new_task

# Function to complete a task by ID
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
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
    return redirect("/") # redirect to the main page

if __name__ == "__main__":
    app.run(debug=True)

