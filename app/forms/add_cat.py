import re

from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type



def custom_validator(form, field):
    if len(field.data) < 5:
        raise validators.ValidationError('Input must be at least 5 characters long')


with open('app/cats_infotm/breed_cats.txt', 'r', encoding='utf-8') as readfile:
    list_of_breed2: list = readfile.read().split('\n')

def validate_not_mobile(form, value):

    rule = re.compile(r'(^[+0-9]{1,3})*([0-9]{10,11}$)')

    print(value.data)

    if rule.search(value.data):
        msg = u"You cannot add mobile numbers."
        raise ValidationError(msg)


class AddCat(FlaskForm):
    list_of_breed = list_of_breed2
    type_advertisement = SelectField('Тип объявления', choices=['На продажу', 'В добрые руки', 'Потярявшийся'], default='for sale')
    breed = SelectField('Порода', choices=list_of_breed, default='Акринская')
    title = StringField('Название объявления', validators=[DataRequired()], default='')
    description = StringField('Описание объявления', default='')
    pet_color = SelectField('Окрас питомца', choices=['белый', "черный", "рыжий", 'другой'], default='другой')
    male = RadioField('Пол питомца', choices=['Мужской', 'Женский'])
    cost = IntegerField('Цена питомца', default=0)
    telephone = StringField('Номер телефона', validators=[])
    age = SelectField('Выберете возраст питомца', choices=['Котенок (меньше года)', "Молодой (1-3 года)", "Взрослый (4-7 лет)", 'Пожилой (более 7 лет)'])
    submit = SubmitField('Опубликовать')
