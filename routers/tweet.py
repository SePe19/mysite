from bottle import post, request, response
import dbconnection
import uuid
import time
import os

@post("/tweet")
def _():
  try:
    db = dbconnection.db()
    user = dbconnection.user()

    picture = dbconnection.picture()
    tweet_id = str(uuid.uuid4().hex)
    tweet_message = dbconnection.validate_tweet()
    tweet_image = picture
    tweet_created_at = int(time.time())
    tweet_user_fk = user["user_id"]
    tweet_total_comments = request.forms.get("tweet_total_comments", "")
    tweet_total_retweets = request.forms.get("tweet_total_retweets", "")
    tweet_total_likes = request.forms.get("tweet_total_likes", "")
    tweet_total_views = request.forms.get("tweet_total_views", "")

    tweet = {
    "tweet_id" : tweet_id,
    "tweet_message" : tweet_message,
    "tweet_image" : tweet_image,
    "tweet_created_at" : tweet_created_at,
    "tweet_user_fk" : tweet_user_fk,
    "tweet_total_comments" : tweet_total_comments,
    "tweet_total_retweets" : tweet_total_retweets,
    "tweet_total_likes" : tweet_total_likes,
    "tweet_total_views" : tweet_total_views
    }

    values = ""
    for key in tweet:
        values = values + f":{key},"
    values = values.rstrip(",")
    print(values)

    # if not tweet_image and tweet_message:  
    #   response.status = 400
    #   raise Exception("no picture, no message")
      
    db.execute(f"INSERT INTO tweets VALUES({values})", tweet).rowcount
    db.commit()

    return {"info": "Tweet succesfull!", "tweet_id":tweet_id}
  except Exception as e:
    print(e)
    return {"info":str(e)} # cast to string
  finally:
    print("Database closed in tweet.py")
    if "db" in locals(): db.close()