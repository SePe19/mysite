from bottle import post, redirect, request, response, get, template, static_file, put
from dotenv import load_dotenv
import os
import dbconnection

@put("/mrbeast-followers/<username>")
def update(username):
    try:
        db = dbconnection.db()
        followers = 20700000
        db.execute(f"UPDATE users SET user_total_followers = ? WHERE user_name = ?", (followers, username))
        
        following = 1924
        db.execute(f"UPDATE users SET user_total_following = ? WHERE user_name = ?", (following, username))
        
        tweets = 6216
        db.execute(f"UPDATE users SET user_total_tweets = ? WHERE user_name = ?", (tweets, username))

        db.commit()

        return {"MrBeast followers and following succesful"}

    except Exception as ex:
        print("Put route error her", ex)
        return ex
    
    finally:
        print("Database closed in @put profile.py")
        if "db" in locals(): db.close()