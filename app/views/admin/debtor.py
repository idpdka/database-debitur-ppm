import json
from app import db
from app.forms import DebtorForm, PaymentForm
from app.models import Debtor, Payment
from datetime import datetime
from flask import Blueprint, Response, jsonify, json, flash, render_template, redirect, request, session
from flask_login import current_user

debtor = Blueprint('debtor', __name__, url_prefix='/admin/debtor')

@debtor.route('/')
def index():
  debtor_form = DebtorForm() 
  payment_form = PaymentForm()

  return render_template('admin/debtor/index.html', debtor_form=debtor_form, payment_form=payment_form)

@debtor.route('/list')
def list():
  debtors = [i.to_dict() for i in Debtor.query.all()]

  for debtor in debtors:
    reducers = 0
    payments = Payment.query.filter_by(debtor_id=debtor['id'])

    for payment in payments:
      payment = payment.to_dict()
      reducers += payment['main'] + payment['interest']

    debtor['reduced_credits'] = debtor['total_credits'] - reducers

  return jsonify(debtors), 200

@debtor.route('/<identifier>/detail', methods=['GET'])
def detail(identifier):
  debtor = Debtor.query.get(identifier).to_dict()

  reducers = 0
  payments = Payment.query.filter_by(debtor_id=debtor['id'])

  for payment in payments:
    payment = payment.to_dict()
    reducers += payment['main'] + payment['interest']

  debtor['reduced_credits'] = debtor['total_credits'] - reducers

  return jsonify(debtor), 200

@debtor.route('/create', methods=['POST', 'GET'])
def create():
  try:
    debtor = Debtor(
      name=request.form['name'],
      ship=request.form['ship'],
      legality=request.form['legality'],
      address=request.form['address'],
      phone_number=request.form['phone_number'],
      key_person=request.form['key_person'],
      contact_person=request.form['contact_person'],
      credit_aggreement=request.form['credit_aggreement'],
      total_credits=request.form['total_credits'],
      tenor=request.form['tenor'],
      start_date=datetime.strptime(request.form['start_date'], "%Y-%m-%d"),
      end_date=datetime.strptime(request.form['end_date'], "%Y-%m-%d"),
    )

    db.session.add(debtor)
    db.session.commit()

    response = jsonify({"success": True, "name": request.form['name']})
    response.status_code = 200
  except Exception as e:
    db.session.rollback()
    print(e)

    response = jsonify({"success": False})
    response.status_code = 500

  return response

@debtor.route('/<identifier>/update', methods=['POST', 'GET'])
def update(identifier):
  try:
    debtor = Debtor.query.get(identifier)
    debtor.name = request.form['name']
    debtor.ship = request.form['ship']
    debtor.legality = request.form['legality']
    debtor.address = request.form['address']
    debtor.phone_number = request.form['phone_number']
    debtor.key_person = request.form['key_person']
    debtor.contact_person = request.form['contact_person']
    debtor.credit_aggreement = request.form['credit_aggreement']
    debtor.total_credits = request.form['total_credits']
    debtor.tenor = request.form['tenor']
    debtor.start_date = datetime.strptime(request.form['start_date'], "%Y-%m-%d")
    debtor.end_date = datetime.strptime(request.form['end_date'], "%Y-%m-%d")

    db.session.commit()

    response = jsonify({"success": True, 'name': request.form['name']})
    response.status_code = 200
  except Exception as e:
    db.session.rollback()
    print(e)

    response = jsonify({"success": False})
    response.status_code = 500

  return response

@debtor.route('<identifier>/delete', methods=['POST'])
def delete(identifier):
  try:
    debtor = Debtor.query.get(identifier)

    db.session.delete(debtor)
    db.session.commit()

    response = jsonify({"success": True})
    response.status_code = 200
  except Exception as e:
    db.session.rollback()
    print(e)

    response = jsonify({"success": False})
    response.status_code = 500

  return response 

@debtor.route('<identifier>/payment-detail', methods=['GET'])
def payment(identifier):
  debtor = Debtor.query.get(identifier).to_dict()
  payments = [i.to_dict() for i in Payment.query.filter_by(debtor_id=identifier)]

  res = {
    'debtor': debtor['name'],
    'payments': payments,
  }

  print(res)

  return jsonify(res), 200

@debtor.route('/<identifier>/pay', methods=['POST'])
def pay(identifier):
  try:
    payment = Payment(
      main=request.form['main'],
      interest=request.form['interest'],
      payment_date=datetime.strptime(request.form['payment_date'], "%Y-%m-%d"),
      notes=request.form['notes'],
      debtor_id=identifier,
    )

    db.session.add(payment)
    db.session.commit()

    response = jsonify({"success": True})
    response.status_code = 200
  except Exception as e:
    db.session.rollback()
    print(e)

    response = jsonify({"success": False})
    response.status_code = 500

  return response 
