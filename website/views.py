# make home page for website

from flask import Blueprint, render_template, request, flash, jsonify  # it has a bunch of urls/roots inside of it
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])  # whenever we go to home(/) the home function will run
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note created!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    print("this is a new {}".format(note))
    noteId = note['noteId']
    print("Note id is {}".format(noteId))
    newNote = Note.query.get(noteId)
    print("New note is {}".format(newNote))
    if newNote:
        print(current_user.id)
        print(newNote.user_id)
        if newNote.user_id == str(current_user.id):
            db.session.delete(newNote)
            db.session.commit()

    return jsonify({})
