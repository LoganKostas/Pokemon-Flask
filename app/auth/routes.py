from flask import Blueprint, render_template, request, redirect, url_for
from .forms import UserCreationForm, LoginForm


from app.models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash


auth = Blueprint('auth', __name__, template_folder='authtemplates')

from app.models import db

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        print(user.id, user.email, user.password)
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('home'))
            else:
                print('incorrect password')
        else:
            pass

    return render_template('login.html', form=form)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = UserCreationForm()
    if request.method == 'POST':
        print('POST request has been made')
        if form.validate():
          first_name = form.first_name.data
          last_name = form.last_name.data
          email = form.email.data
          password = form.password.data
          print(first_name, email, password)


          user = User(first_name, last_name, email, password)

          db.session.add(user)
          db.session.commit()

          return redirect(url_for('auth.login'))
        else:
            print('validation failed')
    return render_template('signup.html', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))