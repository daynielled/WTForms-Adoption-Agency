from flask import Flask, render_template,redirect, url_for, flash

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretbestie'

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
db.create_all()

toolbar = DebugToolbarExtension(app)



@app.route('/')
def list_pets():
    """List all pets"""
    pets = Pet.query.all()
    return render_template('pet_list.html', pets=pets)


@app.route('/add', methods=['GET','POST'])
def add_pet():
    """Add a Pet"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        
        new_pet = Pet(name=name, species=species,photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"New pet added")
        return redirect(url_for('list_pets'))
    
    else:
        return render_template('add_pet_form.html', form=form)
      
@app.route('/<int:pet_id>', methods=['GET','POST'])
def edit_pet(pet_id):
    """Edit pet"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect(url_for('list_pets'))
    
    else:
        return render_template('edit_pet_form.html', form=form)



@app.route('/about')
def about_us():
    return render_template('about_us.html')

@app.route('/contact')
def contact_us():
    return render_template('contact_us.html')



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5100)