from flask import Flask, render_template, request, redirect, url_for, current_app
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# /// is for relative paths
# //// is for absolute paths

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#### Debugging app_context()
app.app_context().push()

# from app import app
# from app import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
    # __table_args__ = {'extend_existing': True}

### Candidate Concept #2: Routing
@app.route("/")
def home():
    todo_list = Todo.query.all()
    ### Candidate Concept #1: Rendering
    return render_template('base.html', todo_list=todo_list)

### Candidate Concept #3: Submitting Data
@app.route("/add", methods=['POST'])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    ### Candidate Concept #5: Redirection
    return redirect(url_for("home"))

@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))

### Candidate Concept #4: Deletion
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    db.create_all()
    # Set debug to True so you don't have to reload server each time we make a change in code
    app.run(debug=True)
