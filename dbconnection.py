from bottle import request, response
import re
import sqlite3
import pathlib
import os
import uuid 
from dotenv import load_dotenv

##############################
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}

##############################
def db():
  db = sqlite3.connect(str(pathlib.Path(__file__).parent.resolve())+"/twitter.db") 
  db.row_factory = dict_factory
  return db
  

##############################
def user():
  try:
    load_dotenv(".env")
    user = request.get_cookie("user", secret=os.getenv('MY_SECRET'))
    print("dbconnection cookie", user)
    if user:
      return user
    else:
      return None
  except Exception as ex:
    print(ex)
    raise ex

##############################
#Email Validation

EMAIL_MIN = 6
EMAIL_MAX = 100
EMAIL_REGEX = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

def validate_email():
  error = f"User email is not valid"
  email = request.forms.get("email", "")
  print(email)
  email = email.strip()
  if len(email) < EMAIL_MIN:
    response.status = 400 
    raise Exception(error)
  if len(email) > EMAIL_MAX: 
    response.status = 400
    raise Exception(400, error)
  if not re.match(EMAIL_REGEX, email): 
    response.status = 400
    raise Exception(error)
  return email

##############################
#Username Validation

USERNAME_MIN = 4
USERNAME_MAX = 15
USERNAME_REGEX = "^[a-z0-9_]{4,15}$"

def validate_username():
	error = f"Your username has to be at least {USERNAME_MIN} to {USERNAME_MAX} lowercased english letters"
	username = request.forms.get("username", "")
	username = username.strip()
	if not re.match(USERNAME_REGEX, username): raise Exception(400, error)
	return username

##############################
#Password Validation

PASSWORD_MIN = 10
PASSWORD_MAX = 128
PASSWORD_REGEX = "^[a-z0-9]{10,128}$"

def validate_password():
  error = f"Your password must be between {PASSWORD_MIN} to {PASSWORD_MAX} characters long"
  password = request.forms.get("password", "")
  password = password.strip()
  if len(password) < PASSWORD_MIN:
    response.status = 400
    raise Exception(error)
  if len(password) > PASSWORD_MAX: raise Exception(400, error)
  if not re.match(PASSWORD_REGEX, password): raise Exception(400, error)
  return password

##############################
#Confirm Password Validation

def validate_confirm_password():
  error = "Password does not match"
  password = request.forms.get("password")
  confirm_password = request.forms.get("confirm_password")
  password = password.strip()
  confirm_password = confirm_password.strip()
  if confirm_password != password:
    response.status = 400 
    raise Exception(error)
  return confirm_password

##############################

##############################
#Tweet Validation -change

TWEET_MIN = 1
TWEET_MAX = 280
#TWEET_REGEX = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{1,280}$"

def validate_tweet():
  error_min = "No characters have been used"
  error_max = "Max amount of characters have been used"
  picture = request.files.get("picture", "")
  message = request.forms.get("tweet_message", "")
  if not picture:
    if len(message) > TWEET_MAX:
      response.status = 400
      raise Exception(error_max)
    if len(message) < TWEET_MIN:
      print("checking if there is a picture without message")
      response.status = 400
      raise Exception(error_min)
  # if not re.match(TWEET_REGEX, message): raise Exception(400, error)
  return message

def picture():
  error = "Picture file not valid"
  picture = request.files.get("picture", "")
  if picture is None or picture == "":
    return picture
  name, ext = os.path.splitext(picture.filename)
  print("NAME? ", name)
  print("FILENAME ", ext)

  if ext not in (".png", ".jpg", ".jpeg", ".webp", ".gif"):
    response.status = 400
    raise Exception(error)
  picture_name = str(uuid.uuid4().hex)
  picture_name = picture_name + ext
  picture.save(f"images/tweet_images/{picture_name}")
  return picture_name