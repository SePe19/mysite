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
    new_username = request.forms.get("username", "")
    if username != new_username and new_username != "" and new_username is not None:
      db.execute(f"UPDATE users SET user_name = ? WHERE user_name = ?", (new_username, username))
    
    avatar = user_cookie["user_avatar"]
    new_avatar = dbconnection.avatar_picture()
    if avatar != new_avatar:
      db.execute(f"UPDATE users SET user_avatar = ? WHERE user_name = ?", (new_avatar, username))

    # cover = user_cookie["user_cover"]
    # new_cover = request.forms.get("cover", "")
    # if cover != new_cover
    #   db.execute(f"UPDATE users SET user_name = ? WHERE user_name = ?", (new_cover, username))
    
    db.commit()

    user_cookie['user_name'] = new_username
    user_cookie['user_avatar'] = new_avatar
    response.set_cookie("user", user_cookie, secret=os.getenv('MY_SECRET'), httponly=True)
    return {"info": "Update succesful", "New username": user_cookie["user_name"], "New avatar": user_cookie["user_avatar"]}

  except Exception as ex:
    print("Put route error her", ex)
    return ex
  
  finally:
    print("Database closed in @put profile.py")
    if "db" in locals(): db.close()

@get("/saving-bacon")
def _():
  try:
    db = dbconnection.db()
    # username = ""
    # new_username = "baconbacon1"
    users = db.execute("SELECT * FROM users").fetchall()
    # db.execute(f"UPDATE users SET user_name = ? WHERE user_name = ?", (new_username, username))
    db.commit()
    print(users)
    return {"users":users}
  except Exception as ex:
    if "db" in locals(): db.rollback()
    print("bacon", ex)
  finally:
    if "db" in locals(): db.close()