from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField, HiddenField, SelectMultipleField, widgets, SelectField, FileField, IntegerField, DecimalField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, InputRequired, Required, regexp
from wtforms_components import TimeField
from wtforms.fields.html5 import DateField
from wtforms.widgets import html5
from app.models import User
from datetime import datetime

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Ingat saya')

class DebtorForm(FlaskForm):
    name = StringField('Nama', validators=[DataRequired()])
    ship = StringField('Nama Kapal', validators=[DataRequired()])
    legality = StringField('Legalitas', validators=[DataRequired()])
    address = StringField('Alamat', validators=[DataRequired()])
    phone_number = StringField('Nomor Telepon', validators=[DataRequired()])
    key_person = StringField('Key Person', validators=[DataRequired()])
    contact_person = StringField('Contact Person', validators=[DataRequired()])
    credit_aggreement = StringField('Perjanjian Kredit', validators=[DataRequired()])
    total_credits = IntegerField('Piutang Total (Rp)', validators=[DataRequired()])
    tenor = IntegerField('Tenor (Bulan)', validators=[DataRequired()])
    start_date = DateField("Tanggal Awal", format='%Y-%m-%d')
    end_date = DateField("Tanggal Akhir", format='%Y-%m-%d')

class PaymentForm(FlaskForm):
    debtor_id = HiddenField('ID Debitur')
    main = StringField('Pokok', validators=[DataRequired()])
    interest = StringField('Bunga', validators=[DataRequired()])
    payment_date = DateField("Tanggal Pembayaran", format='%Y-%m-%d')
    notes = StringField('Keterangan')
