import base64
import requests
from app.forms import LoginForm
from app.models import User
from flask import Blueprint, jsonify, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required

auth = Blueprint('auth', __name__, url_prefix='/admin/auth')

@auth.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('debtor.index'))

  form = LoginForm()

  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()

    if user is None or not user.check_password(form.password.data):
      flash('Invalid username or password')
      return redirect(url_for('auth.login'))

    login_user(user, remember=form.remember_me.data)

    flash('{} logged in successfully'.format(form.username.data), 'success')
    return redirect(url_for('debtor.index'))

  return render_template('admin/auth/login.html', form=form)

@auth.route('/logout')
def logout():
  logout_user()

  return redirect(url_for('auth.login'))
