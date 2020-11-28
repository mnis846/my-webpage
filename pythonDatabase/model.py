import os
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

basedir = os.path.abspath(os.path.dirname(__name__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard'
app.config['SQLALCHEMY_DATABASE_URI'] =\
     'postgresql://postgres:Tandan@localhost/postgres'
app.config['SQLALCHEMY_COMMIT_ON_TAREDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique=True)
    users = db.reltionship('User', backef='role', lazy='dynamic')
    

    def __repr__(self):
        return '<user %r>' %self.username


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form= NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.date:
            flash('Looks like You have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('indx.html', form=form, name=session.get('name'))




if __name__=='__main__':
    db.create_all()
    