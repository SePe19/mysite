from bottle import put
import dbconnection

@put("/mrbeast-followers")
def _():
    try:
        db = dbconnection.db()
        username = "mrbeast"
        followers = 20700000
        following = 1924
        tweets = 6221
        db.execute("UPDATE users SET user_total_followers = ?, user_total_following = ?, user_total_tweets = ? WHERE user_name = ?", (followers, following, tweets, username))

        db.commit()

        return {"MrBeast followers and following succesful"}

    except Exception as ex:
        print("Put route error her", ex)
        return ex
    
    finally:
        print("Database closed in @put profile.py")
        if "db" in locals(): db.close()