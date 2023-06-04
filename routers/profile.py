from bottle import post, redirect, request, response, get, template, static_file, put
from dotenv import load_dotenv
import os
import dbconnection

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
    
    profile_tweets = db.execute("SELECT * from users_and_tweets WHERE user_name = ? ORDER BY tweet_created_at DESC", (username,)).fetchall()
    profile_tweets_images = db.execute("SELECT tweet_image FROM users_and_tweets WHERE user_name=? AND tweet_image != '' ORDER BY tweet_created_at DESC LIMIT 6", (username,)).fetchall()
    users_and_tweets = db.execute("SELECT * FROM users_and_tweets").fetchall()
    trends = db.execute("SELECT * FROM trends").fetchall()

    if user_cookie["user_name"] == user["user_name"]:
      user = db.execute("SELECT * FROM users WHERE user_name = ?", (user_cookie["user_name"],)).fetchone()
      following = db.execute("SELECT followee_id FROM followers WHERE follower_id = ?", (user["user_id"],)).fetchall()
      print("who the logged in user follows", following)
      return template("profile", title="Profile Page", user_cookie=user_cookie, user=user, profile_tweets=profile_tweets, profile_tweets_images=profile_tweets_images, users_and_tweets=users_and_tweets, trends=trends, following=following)

    return template("profile", title="Profile Page", user=user, profile_tweets=profile_tweets, profile_tweets_images=profile_tweets_images, users_and_tweets=users_and_tweets, trends=trends)
  
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
    user_id = user_cookie["user_id"]
    username = user_cookie["user_name"]
    new_username = dbconnection.update_username()
    if username != new_username and new_username != "" and new_username is not None:
      db.execute(f"UPDATE users SET user_name = ? WHERE user_name = ?", (new_username, username))
      user_cookie['user_name'] = new_username
    
    avatar = user_cookie["user_avatar"]
    new_avatar = dbconnection.avatar_picture()
    if avatar != new_username and new_avatar != "" and new_avatar is not None:
      db.execute(f"UPDATE users SET user_avatar = ? WHERE user_id = ?", (new_avatar, user_id))
      user_cookie['user_avatar'] = new_avatar

    cover = user_cookie["user_cover"]
    new_cover = dbconnection.cover_picture()
    if cover != new_username and new_cover != "" and new_cover is not None:
      db.execute(f"UPDATE users SET user_cover = ? WHERE user_id = ?", (new_cover, user_id))
      user_cookie['user_cover'] = new_cover
    
    db.commit()

    response.set_cookie("user", user_cookie, secret=os.getenv('MY_SECRET'), httponly=True)
    return {"info": "Update succesful", "new_username": user_cookie["user_name"], "new_avatar": user_cookie["user_avatar"], "new_cover": user_cookie["user_cover"]}

  except Exception as ex:
    print("Put route error her", ex)
    return ex
  
  finally:
    print("Database closed in @put profile.py")
    if "db" in locals(): db.close()