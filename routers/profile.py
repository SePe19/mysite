from bottle import post, redirect, request, response, get, template, static_file, put
from dotenv import load_dotenv
import os
import dbconnection

# @get("/<id>")
# def index(id):
#   db = dbconnection.db()
#   load_dotenv('.env')
#   user = request.get_cookie("user", secret=os.getenv('MY_SECRET'))
#   user_id = user["id"]

#   userProfile = db.execute("SELECT * FROM users WHERE id = ? LIMIT 1", (user_id,)).fetchone()
#   print("Is it the right profile?", userProfile)
#   return template("profile", userProfile=userProfile)

@get("/<username>")
def _(username):
  try:
    db = dbconnection.db()
    user_cookie = dbconnection.user()
    user = db.execute("SELECT * FROM users WHERE user_name = ?", (username,)).fetchone()
    if not user:
      response.set_header("Location", "/")
      response.status = 302
      return response.body
    users = db.execute("SELECT * FROM users").fetchall()
    profile_tweets = db.execute("SELECT * from users_and_tweets WHERE user_name = ? ORDER BY tweet_created_at DESC", (username,)).fetchall()
    profile_tweets_images = db.execute("SELECT tweet_image FROM users_and_tweets WHERE user_name=? AND tweet_image != '' ORDER BY tweet_created_at DESC LIMIT 6", (username,)).fetchall()
    users_and_tweets = db.execute("SELECT * FROM users_and_tweets").fetchall()
    trends = db.execute("SELECT * FROM trends").fetchall()

    if user_cookie:
      print("Logged in user", user_cookie)
      users = db.execute("SELECT * FROM users WHERE user_id !=?", (user_cookie["user_id"],)).fetchall()
      following = db.execute("SELECT followee_id FROM followers WHERE follower_id = ?", (user_cookie["user_id"],)).fetchall()
      print("who the logged in user follows", following)
      return template("profile", title="Profile Page", user_cookie=user_cookie, user=user, users=users, profile_tweets=profile_tweets, profile_tweets_images=profile_tweets_images, users_and_tweets=users_and_tweets, trends=trends, following=following)

    return template("profile", title="Profile Page", user=user, users=users, profile_tweets=profile_tweets, profile_tweets_images=profile_tweets_images, users_and_tweets=users_and_tweets, trends=trends)
  
  except Exception as ex:
    print("Exception:profile", ex)
    return ex
  finally:
    print("Database closed in  @get profile.py")
    if "db" in locals(): db.close()

#########################################

### vi skal have tilfÃ¸jet dictionary/alle user values

@put("/update")
def update():
  try:
    db = dbconnection.db()
    
    user_cookie = dbconnection.user()
    username = user_cookie["user_name"]
    print("Current username", username)

    new_username = request.forms.get("username", "")
    print("New username?", new_username)

    db.execute(f"UPDATE users SET user_name = ? WHERE user_name = ?", (new_username, username))
    db.commit()

    # Modify the username attribute in cookie
    user_cookie['user_name'] = new_username
    print("new username cookie value", user_cookie['user_name'])
    response.set_cookie("user", user_cookie, secret=os.getenv('MY_SECRET'), httponly=True)
    return {"info": "Update succesful", "New username": user_cookie["user_name"]}

  except Exception as ex:
    print("Put route error her", ex)
    return ex
  
  finally:
    print("Database closed in @put profile.py")
    if "db" in locals(): db.close()