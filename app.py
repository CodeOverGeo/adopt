from flask import Flask, render_template, redirect, jsonify

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "monkey"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

"""Controls redirects in debug toolbar"""
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.route('/')
def show_pets():
    """Renders a page that shows all pets"""

    pets = Pet.query.all()
    return render_template("show_pets.html", pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet_form():
    """Renders a form to add a pet"""

    form = AddPetForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != 'csrf_token'}
        new_pet = Pet(**data)

        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')

    else:
        return render_template('add_pet.html', form=form)


@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet_form(pet_id):
    """Renders a form to edit and existing pet"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        """if form validates, update database"""
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        return redirect('/')

    else:
        """if form doesn't validate, show edit pet page"""
        return render_template("edit_pet.html", form=form, pet=pet)
