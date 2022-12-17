from flask import Blueprint,render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
views=Blueprint('views', __name__)
from . import db
import json


@views.route('/', methods=['GET','POST'])
@login_required
def home():
    
    if request.method=='POST':
        #note=request.form.get('note')
        data=request.form.get('data')
        types=request.form.get('types')
        user_id=current_user.id
        if len(data)<1:
            flash('Data is too short', category='error')
        else:
            new_note=Note(data=data, types=types, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note Added!', category='success')
    '''
    if request.method=='POST':
        note=request.form.get('note')  
    '''
    return render_template("page1.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note=json.loads(request.data)
    noteId=note['noteId']
    note= Note.query.get(noteId)
    if note:
        if note.user_id==current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})

@views.route('/page1', methods=['GET','POST'])
@login_required
def page1():
    return render_template("page1.html", user=current_user)
    
@views.route('/page2', methods=['GET','POST'])
@login_required
def page2():
    return render_template("page2.html", user=current_user)
