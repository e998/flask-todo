from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# /// is for relative paths
# //// is for absolute paths

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

@app.route('/')
# def hello_world():
#     return 'Hello, World!'
def home():
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)

if __name__ == "__main__":
    db.create_all()
    # Set debug to True so you don't have to reload server each time we make a change in code
    # Reactivity?
    # No
    app.run(debug=True)



