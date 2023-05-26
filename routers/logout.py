from bottle import post, request, response
from dotenv import load_dotenv
import os
import dbconnection
import bcrypt

@post("/logout")
def _():
    try:
      load_dotenv('.env')
      user = request.get_cookie("user", secret=os.getenv('MY_SECRET'))
      print("Cookie Value", user)
      if user: response.delete_cookie("user")
      return {"info": "Logout Succesful!"}
    except Exception as e:
      print(e)
      return {"info":str(e)} # cast to string
    finally:
      if "db" in locals(): db.close()