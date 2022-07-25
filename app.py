from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# creates application named after name of file ie app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ibnbayo:newPassword@localhost:5432/todoapp'
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'

db.create_all()

@app.route('/todos/create', methods=['POST'])
def create_todo():
    description = request.get_json()['description']
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()
    return jsonify({
        'description': todo.description
    })


# route that listens to homepage
@app.route('/')
def index():
    # rt : a flask method that allows us to specify what to render to user when they visit the route
    # data is a variable we passed in to use in template
    return render_template('index.html', data=Todo.query.all())

