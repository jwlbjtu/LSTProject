from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .forms import NameForm
from .. import db
from ..models import User
from flask.helpers import flash

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            flash('Looks like you have changed your name!')
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))
    return render_template('index.html', current_time = datetime.utcnow(), name = session.get('name'), form = form, known = session.get('known', False))

@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@main.route('/test')
def test():
    return render_template('test.html')