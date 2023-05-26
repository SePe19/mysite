from bottle import post, request, response, template
from dotenv import load_dotenv
import os
import dbconnection
import bcrypt

@post("/login")
def _():
    try:
      load_dotenv('.env')
      #user = request.get_cookie("user", secret=os.getenv('MY_SECRET'))
      #print("Cookie values ", user)
      #if user: return {"info": "Login succesful!", "Welcome": user["username"]}

      username = dbconnection.validate_username()
      password = request.forms.get("password")

      db = dbconnection.db()
      user = db.execute("SELECT * FROM users WHERE user_name = ? LIMIT 1", (username,)).fetchone()
      print("What is in user? ", user)
      
      print(password)
      print(user["user_password"])

      if not user: 
        response.status = 400
        raise Exception("User Doesn't Exist")
      if not bcrypt.checkpw(password.encode("utf-8"), user["user_password"]):
        response.status = 400 
        raise Exception("Wrong Password") 

      user.pop("user_password")

      if user: 
        response.set_cookie("user", user, secret=os.getenv('MY_SECRET'), httponly=True)
      return {"info": "Login credentials valid", "User": user["user_name"]}
    except Exception as e:
      print(e)
      return {"we are here":str(e)} # cast to string
    finally:
      if "db" in locals(): db.close()