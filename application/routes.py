from application import app, db
from application.models import Tasks
from flask import render_template

@app.route('/')
def home():
    all_tasks = Tasks.query.all()
    return render_template("index.html", title="Home", all_tasks=all_tasks)

@app.route('/create_task') 
def create_task():
    new_task = Tasks(description="New Task")
    db.session.add(new_task)
    db.session.commit()

    return  f"Task added with ID {new_task.id}"