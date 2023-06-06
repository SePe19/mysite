from bottle import post, request, response, template
from dotenv import load_dotenv
import os
import dbconnection
import bcrypt

@post("/login")
def _():
    try:
      load_dotenv('.env')

      username = dbconnection.validate_username()
      password = dbconnection.validate_password()

      db = dbconnection.db()
      user = db.execute("SELECT * FROM users WHERE user_name = ? LIMIT 1", (username,)).fetchone()

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