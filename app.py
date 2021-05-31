'''Pet Adoption Agency App'''

from flask import Flask, redirect, request, render_template, flash
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension

from forms import AddPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'MissMillieIsGood'

connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/pets')
def browse_pets():
    pets = Pet.query.all()
    return render_template('pets.html', pets=pets)

@app.route('/pets/<int:pet_id>')
def show_pet(pet_id):

    pet = Pet.query.get_or_404(pet_id)

    return render_template('pet.html', pet=pet)

@app.route('/pets/<int:pet_id>/edit')
def edit_pet(pet_id):

    pet = Pet.query.get_or_404(pet_id)
    return render_template('edit.html', pet=pet)

@app.route('/add-pet', methods=["GET", "POST"])
def add_pet():
    form = AddPetForm()

    if form.validate_on_submit():
        new_pet = Pet(name = form.name.data,
        species = form.species.data,
        photo_url = form.photo_url.data,
        age= form.age.data,
        notes = form.notes.data)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/pets')

    else:
        return render_template('add.html', form=form)

@app.route('/add-pet', methods=["POST"])
def add_pet_db():

    new_pet = Pet()

    db.session.add(new_pet)
    db.session.commit()

    return redirect("/pets")