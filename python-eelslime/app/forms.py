from flask_wtf import FlaskForm
from wtforms import FormField,FieldList, HiddenField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class Discard(FlaskForm):
    d = BooleanField('')

class Select(FlaskForm):
    s = BooleanField('Discard')

class Current(FlaskForm):
    w = StringField("")

class Judge(FlaskForm):
    submit = SubmitField('Draw Persona Card')
    persona0 = StringField("")
    persona1 = StringField("")

class Cards(FlaskForm):
    submit = SubmitField('Draw Cards')
    discard_list = FieldList(FormField(Discard))
    select_list  = FieldList(FormField(Select))
    word_list  = FieldList(FormField(Current))
    discard0 = BooleanField("")
    discard1 = BooleanField("")
    discard2 = BooleanField("")
    discard3 = BooleanField("")
    discard4 = BooleanField("")
    discard5 = BooleanField("")
    discard6 = BooleanField("")
    card0 = StringField("")
    card1 = StringField("")
    card2 = StringField("")
    card3 = StringField("")
    card4 = StringField("")
    card5 = StringField("")
    card6 = StringField("")
#    def __init__(self, *args, **kwargs):
#        super(Cards, self).__init__(*args, **kwargs)
#        for wordfield in self.word_list:
#            wordfield.widget = widgets.HiddenInput()
