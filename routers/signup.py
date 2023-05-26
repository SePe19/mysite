from bottle import get, post, redirect, request, response, template
import dbconnection
import bcrypt
import os
from dotenv import load_dotenv
import uuid
import time
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

@post("/signup")
def _():
    try:
        db = dbconnection.db()
        id = str(uuid.uuid4().hex)
        email = dbconnection.validate_email()
        username = dbconnection.validate_username()
        password = dbconnection.validate_password()
        dbconnection.validate_confirm_password()
        first_name = request.forms.get("first_name", "")
        last_name = request.forms.get("last_name", "")
        user_verified = request.forms.get("user_verified", "")
        user_verification_token = str(uuid.uuid4().hex)
        user_avatar = request.forms.get("user_avatar", "default.jpg")
        user_cover = request.forms.get("user_cover", "default-cover.png")
        user_created_at = int(time.time())
        user_total_tweets = request.forms.get("user_total_tweets", "0")
        user_total_following = request.forms.get("user_total_following", "0")
        user_total_followers = request.forms.get("user_total_followers", "0")

        salt = bcrypt.gensalt()

        user = {
        "id" : id,
        "username" : username,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password" : bcrypt.hashpw(password.encode("utf-8"), salt),
        "user_verified" : user_verified,
        "user_verification_token" : user_verification_token,
        "user_avatar" : user_avatar,
        "user_cover" : user_cover,
        "user_created_at" : user_created_at,
        "user_total_tweets" : user_total_tweets,
        "user_total_following" : user_total_following,
        "user_total_followers" : user_total_followers
        }

        print(user)
        values = ""
        for key in user:
            values = values + f":{key},"
        values = values.rstrip(",")


        print(values)
        db.execute(f"INSERT INTO users VALUES({values})", user).rowcount
        db.commit()

        email_verification(user["email"], user["user_verification_token"])

        return {"info": "Signup succesful!"}
    except Exception as e:
        print(e)
        if "db" in locals(): db.rollback()
        return {"info":str(e)}
    finally:
        if "db" in locals(): db.close()

@get("/verify-user/<token>")
def verify_user(token):
    try:
        print(token)
        db = dbconnection.db()
        user_verified = "1"
        rows_affected = db.execute("UPDATE users SET user_verified = ? WHERE user_verification_token = ?", (user_verified, token)).rowcount
        db.commit()
        if not rows_affected:
            raise Exception("User not found")
        user = db.execute("SELECT * FROM users WHERE user_verification_token = ?", (token,)).fetchone()
        username = user["user_name"]
        response.set_header("Location", f"/{username}")
        response.status = 302
        return response.body
    except Exception as e:
        print(e)
        if "db" in locals(): db.rollback()
        return {"info": str(e)}
    finally:
        if "db" in locals(): db.close()

def email_verification(user_email, token):
    try:
        load_dotenv(".env")
        sender_email = os.getenv("TWITTER_EMAIL")
        receiver_email = user_email
        password = os.getenv("TWITTER_KEY")

        message = MIMEMultipart("alternative")
        message["Subject"] = "multipart test"
        message["From"] = sender_email
        message["To"] = receiver_email
        try:
            import production
            url = os.getenv("PYTHONANYWHERE_URL")
        except ImportError:
            url = "http://127.0.0.1:3000/verify-user"
        
        text = """\
        Hi,
        How are you?
        www.your_website_here.com"""
        html = """\
        <html>
            <body>
                <p>Hi and welcome to Twitter!<br>
                    Thank you for signing up<br>
                    <a href="{url}/{token}">{url}/{token}</a>
                </p>
            </body>
        </html>
        """.format(token=token, url=url)

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
    except Exception as ex:
        print("def email_verification", ex)
    finally:
        pass