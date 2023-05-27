from bottle import default_app, get, post, run, request, response, static_file, template
import git
import sqlite3
import pathlib
import dbconnection
import os


@post("/f10b10c9cc6e4a13ae09a13d1181a6b1")
def git_update():
    repo = git.Repo("./mysite")
    origin = repo.remotes.origin
    repo.create_head("main", origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return "Everything OK"


##############################
@get("/images/<filename:re:.*\.webp>")
def _(filename):
    return static_file(filename, root="./images")

@get("/images/<filename:re:.*\.png>")
def _(filename):
    return static_file(filename, root="./images")

@get("/images/<filename:re:.*\.jpg>")
def _(filename):
    return static_file(filename, root="./images")

@get("/images/<filename:re:.*\.gif>")
def _(filename):
    return static_file(filename, root="./images")


@get("/")
def index():
    try:
        print("freddy boi")
        db = dbconnection.db()
        tweets = db.execute("SELECT * FROM tweets").fetchall()
        trends = db.execute("SELECT * FROM trends").fetchall()
        users = db.execute("SELECT * FROM users").fetchall()
        for user in users:
            print(user["user_id"])
        users_and_tweets = db.execute("SELECT * FROM users_and_tweets ORDER BY tweet_created_at DESC").fetchall()
        user_cookie = dbconnection.user()
        print(user_cookie)
        if user_cookie is None:
            return template("index", title="Twitter", tweets=tweets, trends=trends, users=users, users_and_tweets=users_and_tweets)
        users = db.execute("SELECT * FROM users WHERE user_id !=?", (user_cookie["user_id"],)).fetchall()
        following = db.execute("SELECT followee_id FROM followers WHERE follower_id = ?", (user_cookie["user_id"],)).fetchall()
        print("who the logged in user follows", following)
        return template("index", title="Twitter", tweets=tweets, trends=trends, users=users, users_and_tweets=users_and_tweets, following=following, user_cookie=user_cookie)
    except Exception as ex:
        print("fejl",ex)
        response.status = 400
        return {"error index": str(ex)}
    finally:
        if "db" in locals(): db.close()

##############################

@get("/app.css")
def _():
    return static_file("app.css", root=".")

@get("/js/<filename:re:.*.js>")
def _(filename):
    return static_file(filename, root="js")

#############################

import routers.signup
import routers.login
import routers.logout
import routers.profile
import routers.tweet # -change
import routers.follow

#############################

try:
    import production
    application = default_app()
except Exception as ex:
    print("Running local server")
    run(host="127.0.0.1", port=3000, debug=True, reloader=True)