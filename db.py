#db.py
import click
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from sqlalchemy import orm
from app import app
from flask_bcrypt import Bcrypt

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.sqlite'
app.config['SECRET_KEY'] = 'thisisasecretkey'

db = SQLAlchemy()
db.init_app(app)
bcrypt = Bcrypt(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

    todos = db.relationship('Todo', backref='user', lazy=True)

    def is_authenticated(self):
        return True  
    
    def get_id(self):
        return str(self.id)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    complete = db.Column(db.Boolean, default=False)
    description = db.Column(db.String, nullable=False)
    lists = db.relationship('List', secondary='todo_list', back_populates='todos')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def populate_lists(self, list_ids):
        lists = []
        for id in list_ids:
            if id > 0: lists.append(db.session.get(List, id))
        self.lists = lists

class List(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String, nullable=False)
    todos = db.relationship(Todo, secondary='todo_list', back_populates='lists')
    complete = False
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    @orm.reconstructor
    def check_complete(self):
        self.complete = all([todo.complete for todo in self.todos])

todo_list = db.Table(
    'todo_list',
    db.Column('todo_id', db.Integer, db.ForeignKey('todo.id'), primary_key=True),
    db.Column('list_id', db.Integer, db.ForeignKey('list.id'), primary_key=True)
)

with app.app_context():
    db.create_all()

@click.command('init-db')
def init(): 
    with app.app_context():
        db.drop_all()
        db.create_all()
    click.echo('Database has been initialized.')

app.cli.add_command(init) 
