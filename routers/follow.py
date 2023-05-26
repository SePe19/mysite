from bottle import get, post, request
from dotenv import load_dotenv
import dbconnection

@post("/follow")
def follow():
    try:
        db = dbconnection.db()
        user_cookie = dbconnection.user()
        follower_id = user_cookie["user_id"]
        followee_id = request.forms.get("followee_id")
        follower = {
            "follower_id" : follower_id,
            "followee_id" : followee_id
        }

        print("/follow | follower:", follower)
        
        values = ""
        for key in follower:
            values = values + f":{key},"
        values = values.rstrip(",")
        
        db.execute(f"INSERT INTO followers VALUES({values})", follower).rowcount
        db.commit()
        return {"info follow":"Succesfully followed"}
    except Exception as ex:
        print("follow", ex)
        return ex
    finally:
        if "db" in locals(): db.close()

@post("/unfollow")
def follow():
    try:
        db = dbconnection.db()
        user_cookie = dbconnection.user()
        unfollower_id = user_cookie["user_id"]
        unfollowee_id = request.forms.get("followee_id")
        unfollower = {
            "follower_id" : unfollower_id,
            "followee_id" : unfollowee_id
        }

        print("/unfollow | unfollower:", unfollower)
        
        values = ""
        for key in unfollower:
            values = values + f":{key},"
        values = values.rstrip(",")
        
        db.execute(f"DELETE FROM followers WHERE follower_id = ? AND followee_id = ?", (unfollower_id, unfollowee_id)).rowcount
        db.commit()
        return {"info unfollow":"Succesfully unfollowed"}
    except Exception as ex:
        print("unfollow", ex)
        return ex
    finally:
        if "db" in locals(): db.close()


@get("/<username>/followers")
def _(username):
    try:
        db = dbconnection.db()
        followers = db.execute("SELECT user_total_followers FROM users WHERE username = ?", (username)).fetchone()
        followers_dict = {
            "followers": followers
        }
        return followers_dict
    except Exception as ex:
        print(ex)
        if "db" in locals(): db.rollback()
    finally:
        if "db" in locals(): db.close()

@get("/<username>/following")
def _(username):
    try:
        db = dbconnection.db()
        following = db.execute("SELECT user_total_followers FROM users WHERE username = ?", (username)).fetchone()
        following_dict = {
            "following": following
        }
        return following_dict
    except Exception as ex:
        print(ex)
        if "db" in locals(): db.rollback()
    finally:
        if "db" in locals(): db.close()
