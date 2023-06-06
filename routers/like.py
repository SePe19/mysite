from bottle import get, post, request, response
import dbconnection

@post("/like")
def like():
    try:
        db = dbconnection.db()
        user_cookie = dbconnection.user()
        likes_user_fk = user_cookie["user_id"]
        likes_tweet_fk = request.forms.get("tweet_id", "")
        like = {
            "likes_user_fk" : likes_user_fk,
            "likes_tweet_fk" : likes_tweet_fk
        }
        likes = db.execute("SELECT * FROM likes WHERE likes_user_fk = ? AND likes_tweet_fk = ?", (likes_user_fk, likes_tweet_fk,)).fetchone()
        if likes:
            db.execute("DELETE FROM likes WHERE likes_user_fk = ? AND likes_tweet_fk = ?", (likes_user_fk, likes_tweet_fk,))
        else:
            values = ""
            for key in like:
                values = values + f":{key},"
            values = values.rstrip(",")

            db.execute(f"INSERT INTO likes VALUES({values})", like).rowcount
        
        db.commit()
        return {"info like":"Succesfully toggled liked"}
    except Exception as ex:
        print("like", ex)
        if "db" in locals(): db.rollback()
        return ex
    finally:
        if "db" in locals(): db.close()


@get("/<tweet_id>/likes")
def _(tweet_id):
    try:
        db = dbconnection.db()
        likes = db.execute("SELECT tweet_total_likes FROM tweets WHERE tweet_id = ?", (tweet_id,)).fetchone()
        if likes is not None:
            like_count = likes["tweet_total_likes"]
        else:
            like_count = 0
        likes_dict = {
            "likes": like_count
        }
        response.content_type = "application/json"
        return likes_dict
    except Exception as ex:
        print("get likes", ex)
        if "db" in locals():
            db.rollback()
    finally:
        if "db" in locals():
            db.close()