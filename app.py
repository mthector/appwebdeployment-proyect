from flask import Flask, render_template, abort, redirect, request
from databases.db import db, Instrument, Category, Supplier
from forms.task_form import InstrumentForm
import config as custom_config




app = Flask(__name__)
app.config.from_object(custom_config)
db.init_app(app)


@app.route('/')
def hello():
    return render_template ('index.html')

@app.route('/login/')
def login():
    return render_template ('login.html')

@app.route('/instrumentos/')
def intrumentos():
    instruments = Instrument.query.all()
    return render_template ('instrumentos.html', instruments=instruments)

@app.route('/instrument/<int:id>/details/')
def details(id):
    instruments = Instrument.query.filter_by(id=id).first()

    if instruments:
        return render_template ('details.html', instrument=instruments)
    else:
        abort(404)

@app.route('/instrument/<int:id>/delete/')
def delete(id):
    instruments = Instrument.query.filter_by(id=id).first()
    db.session.delete(instruments)
    db.session.commit()
    return redirect('/instrumentos/')
    
@app.route('/instrument/<int:id>/update/', methods=["GET","POST"])
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
    
    return render_template('task_from.html', form = form)

@app.route('/instrument/create/', methods=['GET', 'POST'])
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
    
    return render_template('create_task.html', form = form)

@app.route('/contact/')
def contact():
    return render_template ('contact.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    
    if query:
        instruments = Instrument.query.filter(Instrument.name.ilike(f'%{query}%')).all()
    else:
        instruments = []

    return render_template('search_results.html', instruments=instruments, query=query)