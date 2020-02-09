import base64
from app import app, db
from app.models import User
from flask import redirect, url_for, flash
from flask_login import current_user

@app.route('/')
def index():
  if current_user.is_anonymous:
    return redirect(url_for('auth.login'))
  else:
    return redirect(url_for('debtor.index'))

@app.route('/init')
def init():
	inserted_users = ['admin', 'client']

	for i in inserted_users:
		user = User.query.filter_by(username=i).first()

		if user:
			continue

		u = User(username=i, password_hash=base64.b64encode(i.encode('utf-8'))) 
		db.session.add(u)
		db.session.commit()

		flash("User {} added to users list".format(i))

	return redirect(url_for('index'))