from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp, ValidationError

class RegistrationForm(FlaskForm):
  full_name = StringField('Full_name', validators=[DataRequired()])
  email = StringField('Email',validators=[DataRequired(),Email()])
  phone = StringField('Phone',validators=[DataRequired(),Length(min=10,max=10,message="Phone number must be 10 digits. ")])
  password = PasswordField('Password',validators=[DataRequired(),Regexp(regex=r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$',message="Password must be at least 8 characters long and contain both letters and numbers.")])
  confirm_password = PasswordField('Confirm_Password',validators=[DataRequired(),EqualTo('Password',message="Passwords must match.")])
  submit = SubmitField('Register')

class LoginForm(FlaskForm):
  email_or_phone = StringField('Email or Phone', validators=[DataRequired()])
  password = PasswordField('Password',validators=[DataRequired()])
  submit = SubmitField('Login')

def validate(self):
    if not super(LoginForm, self).validate():
     return False

    data = self.email_or_phone.data
    if not (self._is_email(data) or self._is_phone(data)):
      msg = 'Please enter a valid email or phone number.'
      self.email_or_phone.errors.append(msg)
      return False

    return True

@staticmethod
def _is_email(data):
  try:
       validator.Email()(None, None, data)
       return True
  except ValidationError:
       return False

@staticmethod
def _is_phone(data):
  return data.isdigit() and len(data) == 10