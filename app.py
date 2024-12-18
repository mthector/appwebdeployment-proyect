from flask import Flask, render_template, abort, redirect, request, url_for
from databases.db import db, Instrument, Category, Supplier, User
from forms.task_form import InstrumentForm, UserForm, RegisterForm
import config as custom_config

"""CONFIGURACION DE USUARIOS"""
from flask_login import LoginManager, login_required, login_user, logout_user
from flask_bcrypt import Bcrypt




app = Flask(__name__)
app.config.from_object(custom_config)
app.config['SECRET_KEY'] = '1234'
db.init_app(app)
bcrypt = Bcrypt(app)



"""CONFIGURACION DE USUARIOS"""
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route('/index/')
@login_required
def hello():
    return render_template ('index.html')


@app.route('/', methods=['GET', 'POST'])
def login():
    form = UserForm(request.form)
    if form.validate() and request.method == "POST":
        user = User.query.filter_by(name=form.name.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return render_template('index.html')
            else:
                form.name.errors.append("Incorrect user or password")
        else:
            form.name.errors.append("User does not exist")
    return render_template('login.html', form=form)



@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if form.validate() and request.method == "POST":
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(
            name = form.name.data,
            password = hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form = form)


@app.route('/logout/', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/instrumentos/')
@login_required
def intrumentos():
    instruments = Instrument.query.all()
    return render_template ('instrumentos.html', instruments=instruments)

@app.route('/instrument/<int:id>/details/')
@login_required
def details(id):
    instruments = Instrument.query.filter_by(id=id).first()

    if instruments:
        return render_template ('details.html', instrument=instruments)
    else:
        abort(404)

@app.route('/instrument/<int:id>/delete/')
@login_required
def delete(id):
    instruments = Instrument.query.filter_by(id=id).first()
    db.session.delete(instruments)
    db.session.commit()
    return redirect('/instrumentos/')
    
@app.route('/instrument/<int:id>/update/', methods=["GET","POST"])
@login_required
def update(id):
    instruments = Instrument.query.filter_by(id=id).first()
    form = InstrumentForm(request.form, obj=instruments)
    form.category_id.choices = [(category.id, category.name) for category in Category.query.all()]
    form.supplier_id.choices = [(supplier.id, supplier.name) for supplier in Supplier.query.all()]

    if form.validate() and request.method == "POST":
        instruments.name = form.name.data
        instruments.category_id = form.category_id.data
        instruments.supplier_id = form.supplier_id.data
        instruments.image = form.image.data
        instruments.image_2 = form.image_2.data
        db.session.commit()
        return redirect ('/instrumentos/')
    
    return render_template('update_instrument.html', form = form)

@app.route('/instrument/create/', methods=['GET', 'POST'])
@login_required
def create():
    form = InstrumentForm(request.form)
    form.category_id.choices = [(category.id, category.name) for category in Category.query.all()]
    form.supplier_id.choices = [(supplier.id, supplier.name) for supplier in Supplier.query.all()]
    if form.validate() and request.method == "POST":
        instrument = Instrument(
            name = form.name.data,
            category_id = form.category_id.data,
            supplier_id = form.supplier_id.data,
            image = form.image.data,
            image_2 = form.image_2.data
        )
        db.session.add(instrument)
        db.session.commit()
        return redirect('/instrumentos/')
    
    return render_template('create_instrument.html', form = form)

@app.route('/contact/')
@login_required
def contact():
    return render_template ('contact.html')

@app.route('/search', methods=['GET'])
@login_required
def search():
    query = request.args.get('query')
    
    if query:
        if '%' in query:
            instruments = []
        elif ' ' in query:
            instruments = []
        else:
            instruments = Instrument.query.filter(Instrument.name.ilike(f'%{query}%')).all()
    else:
        instruments = []

    return render_template('search_results.html', instruments=instruments, query=query)


@login_manager.unauthorized_handler
def unauthorized():
    return render_template('unauthorized.html')

