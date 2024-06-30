from flask import render_template, redirect, url_for, request, flash, jsonify

from os import path
from forms import AddItemForm, RegistrationForm, LoginForm
from ext import app, login_manager
from models import db, Guitars, Bass, Keyboard, Microphone, Accessory, User, Comment
from flask_login import login_user, logout_user, login_required, current_user

role = "Guest"



@app.route("/")
def home():
    return render_template("index.html", guitars=Guitars)

@app.route("/guitars")
def show_guitars():
    guitars = Guitars.query.all()
    return render_template("guitars.html", guitars=guitars)


@app.route("/guitar/<int:guitar_id>")
def guitar_detail(guitar_id):
    guitar = Guitars.query.get(guitar_id)
    if guitar:
        return render_template("guitars.details.html", guitar=guitar)
    else:
        return "Guitar not found", 404


@app.route("/basses")
def show_basses():
    basses = Bass.query.all()
    return render_template("bass.html", basses=basses)

@app.route("/bass/<int:bass_id>")
def bass_detail(bass_id):
    bass = Bass.query.get(bass_id)
    if bass:
        return render_template("bass.details.html", bass=bass)
    else:
        return "Bass not found", 404


@app.route("/keyboards")
def show_keyboards():
    keyboards = Keyboard.query.all()
    return render_template("keyboard.html", keyboards=keyboards)

@app.route("/keyboard/<int:keyboard_id>")
def keyboard_detail(keyboard_id):
    keyboard = Keyboard.query.get(keyboard_id)
    if keyboard:
        return render_template("keyboard.details.html", keyboard=keyboard)
    else:
        return "Keyboard not found", 404

@app.route("/microphones")
def show_microphones():
    microphones = Microphone.query.all()
    return render_template("microphone.html", microphones=microphones)

@app.route("/microphone/<int:mic_id>")
def microphone_detail(mic_id):
    microphone = Microphone.query.get(mic_id)
    if microphone:
        return render_template("microphone.details.html", microphone=microphone)
    else:
        return "Microphone not found", 404

@app.route("/accessories")
def show_accessories():
    accessories = Accessory.query.all()
    return render_template("accessory.html", accessories=accessories)

@app.route("/accessory/<int:accessory_id>")
def accessory_detail(accessory_id):
    accessory = Accessory.query.get(accessory_id)
    if accessory:
        return render_template("accessory.details.html", accessory=accessory)
    else:
        return "Accessory not found", 404


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful. You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('home'))
        else:
            flash('Login unsuccessful. Please check your username and password.', 'error')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    form = AddItemForm()
    if form.validate_on_submit():
        category = form.category.data
        name = form.name.data
        price = form.price.data
        img = form.img.data
        item_id = form.id.data  # Assuming id is part of your form

        if category == 'guitar':
            new_item = Guitars(id=item_id, name=name, price=price, img=img)
        elif category == 'basses':
            new_item = Bass(id=item_id, name=name, price=price, img=img)
        elif category == 'keyboard':
            new_item = Keyboard(id=item_id, name=name, price=price, img=img)
        elif category == 'microphone':
            new_item = Microphone(id=item_id, name=name, price=price, img=img)
        elif category == 'accessory':
            new_item = Accessory(id=item_id, name=name, price=price, img=img)

        try:
            db.session.add(new_item)
            db.session.commit()
            return redirect(url_for('add_item'))
        except Exception as e:
            db.session.rollback()
            # Handle the error (e.g., log it, show an error message)
            print(f"Error adding item: {str(e)}")
            # Optionally, you could pass an error message to the template
            return render_template('add_item.html', form=form, error="Error adding item. Please try again.")

    return render_template('add_item.html', form=form)

