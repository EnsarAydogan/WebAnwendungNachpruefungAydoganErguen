#app.py
#Login-Manager Quelle: https://www.youtube.com/watch?v=71EU8gnZqZQ

from flask import Flask, render_template, redirect, url_for, request, abort, flash
from flask_bootstrap import Bootstrap5
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
import forms
from flask_restful import Api
from flask import jsonify

app = Flask(__name__) #Flask Instanz

app.config.from_mapping(
    SECRET_KEY = 'secret_key_just_for_dev_environment',
    BOOTSTRAP_BOOTSWATCH_THEME = 'pulse'
)

from db import db, Todo, List, User # (1.)
from forms import RegisterForm, LoginForm
from flask_restful import Resource, reqparse

class TodoResource(Resource):
    def get(self, todo_id):
        todo = Todo.query.get(todo_id)
        if todo:
            return jsonify({"id": todo.id, "description": todo.description, "complete": todo.complete, "user_id": todo.user_id})
        return {"message": "Todo not found"}, 404

    def patch(self, todo_id):

        todo = db.session.query(Todo).filter_by(id=todo_id).first()

        if not todo:
            return {'message': 'To-Do not found'}, 404

        data = request.get_json()
        if 'description' in data:
            todo.description = data['description']
        if 'complete' in data:
            todo.complete = data['complete']
        if 'user_id' in data:
            todo.user_id = data['user_id']

        db.session.commit()

        return {'message': 'To-Do aktualisiert'}

    def delete(self, todo_id):

        todo = db.session.query(Todo).filter_by(id=todo_id).first()

        if not todo:
            return {'message': 'To-Do not found'}, 404

        db.session.delete(todo)
        db.session.commit()

        return {'message': 'To-Do gelöscht'}

class TodoListResource(Resource):
    def get(self):
        todos = Todo.query.all()
        todo_list = [{"id": todo.id, "description": todo.description, "complete": todo.complete, "user_id": todo.user_id} for todo in todos]
        return jsonify({"todos": todo_list})

    def post(self):
        data = request.get_json()

        if not current_user.is_authenticated:
            return  {'message': 'Unauthorized'}, 401

        if 'description' not in data:
            return {'message': 'Description is required.'}, 400

        new_todo = Todo(description=data['description'], user_id=current_user.id)

        if 'complete' in data:
            new_todo.complete = data['complete']

        db.session.add(new_todo)
        db.session.commit()

        return {'message': 'Neue To-Do erstellt'}


api = Api(app)
api.add_resource(TodoResource, '/api/todos/<int:todo_id>')
api.add_resource(TodoListResource, '/api/todos')


bootstrap = Bootstrap5(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/index') 
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/todos/', methods=['GET', 'POST'])
@login_required
def todos(): 
    form = forms.CreateTodoForm()
    if request.method == 'GET':
        todos = db.session.query(Todo).filter_by(user_id=current_user.id).order_by(Todo.id).all() 
        return render_template('todos.html', todos=todos, form=form) 
    else:  #POST
        if form.validate():
            todo = Todo(description=form.description.data, user_id=current_user.id)  
            db.session.add(todo)  # !! Hinzufügen zu db
            db.session.commit()  # !! Speichern in db
            flash('Todo has been created.', 'success')
        else:
            flash('No todo creation: validation error.', 'warning')
        return redirect(url_for('todos'))

@app.route('/todos/<int:id>', methods=['GET', 'POST'])
@login_required
def todo(id):
    todo = db.session.get(Todo, id) 
    if todo and todo.user_id == current_user.id:
        form = forms.TodoForm(obj=todo)  
        if request.method == 'GET':
            if todo:
                if todo.lists: 
                    form.list_id.data = todo.lists[0].id  
                choices = List.query.filter_by(user_id=current_user.id).all() 
                form.list_id.choices = [(0, 'No List')] + [(c.id, c.name) for c in choices] 
                return render_template('todo.html', form=form)
            else:
                abort(404)
        else:  #POST
            if form.method.data == 'PATCH':
                if form.validate():
                    form.populate_obj(todo)  
                    todo.populate_lists([form.list_id.data]) 
                    db.session.add(todo) 
                    db.session.commit()  
                    flash('Todo has been updated.', 'success')
                else:
                    flash('No todo update: validation error.', 'warning')
                return redirect(url_for('todo', id=id))
            elif form.method.data == 'DELETE':
                db.session.delete(todo) 
                db.session.commit() 
                flash('Todo has been deleted.', 'success')
                return redirect(url_for('todos'), 303)
            else:
                flash('Nothing happened.', 'info')
                return redirect(url_for('todo', id=id))
    else:
        abort(403) 

@app.route('/lists/', methods=['GET', 'POST'])
@login_required
def lists():
    form = forms.CreateListForm()
    if request.method == 'GET':
        lists = db.session.query(List).filter_by(user_id=current_user.id).order_by(List.id).all() 
        return render_template('lists.html', lists=lists, form=form)
    else:
        if form.validate():
            list = List(name=form.name.data, user_id=current_user.id) 
            db.session.add(list)
            db.session.commit()
        else:
            flash ('List creation failed: validation error.', 'warning')
        return redirect(url_for('lists'))

@app.route('/lists/<int:id>')
@login_required
def list(id):
    list = db.session.get(List, id) 
    if list and list.user_id == current_user.id:
        return render_template('list.html', list=list)
    else:
        abort(403)

@app.errorhandler(404)
def http_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def http_internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:  # Vergleich des Passworts
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)


#@app.route('/api/logindata', methods=['GET']) # Anzeigen der Logindaten in DB für DEVS (Später Löschen)
#def logindata():
#    users = User.query.all()  
#    user_list = [f"User ID: {user.id}, Username: {user.username}, Password: {user.password}" for user in users]
#
#    return jsonify(user_list)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    return render_template('profile.html')

@app.route('/delete_account', methods=['GET', 'POST'])
@login_required
def delete_account():
    
    deletetodos = Todo.query.filter_by(user_id=current_user.id).all()
    for todo in deletetodos:
        db.session.delete(todo)

    deletelists = List.query.filter_by(user_id=current_user.id).all()
    for list in deletelists:
        db.session.delete(list)

    db.session.delete(current_user)
    db.session.commit()
    logout_user()
    return redirect(url_for('login'))
    


@ app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
        