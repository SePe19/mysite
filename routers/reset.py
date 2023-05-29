from bottle import get, post, request, response
import dbconnection
from dotenv import load_dotenv
import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


@post("/reset-password")
def send_reset_email():
    try:
        db = dbconnection.db()
        user_email = request.forms.get("email")
        user_password = dbconnection.validate_password()
        user = db.execute("SELECT * FROM users WHERE user_email = ? LIMIT 1", (user_email,)).fetchone()
        if user:
            print("HELLO FROM THE OTHER SIDE3")
            user_active = 0
            user_deactive = db.execute("UPDATE users SET user_password = ?, user_active = ? WHERE user_email = ?", (user_password, user_active, user_email)).rowcount
            print("DANGERDANGER",user_deactive)
            db.commit()
            email_verification(user_email, user["user_name"])
        return {"info reset":"Succesfully sent reset password email"}
    except Exception as ex:
        print("reset", ex)
        return ex
    finally:
        if "db" in locals(): db.close()


@get("/reset-password/<username>")
def reset_password(username):
    try:
        print("I AM IN reset.py LINE 33 FORZAFC", username)
        db = dbconnection.db()
        user_active = 1
        rows_affected = db.execute("UPDATE users SET user_active = ? WHERE user_name = ?", (user_active, username)).rowcount
        db.commit()
        if not rows_affected:
            raise Exception("User not found")
        response.set_header("Location", "/")
        response.status = 302
        return response.body
    except Exception as e:
        print(e)
        if "db" in locals(): db.rollback()
        return {"info": str(e)}
    finally:
        if "db" in locals(): db.close()


def email_verification(user_email, username):
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
            url = os.getenv("PYTHONANYWHERE_URL") + "/reset-password"
        except:
            url = "http://127.0.0.1:3000/reset-password"
        
        text = """\
        Hi,
        How are you?
        www.your_website_here.com"""
        html = """\
        <html>
            <body>
                <p>Hi {username}!<br>
                    Welcome back! Upon clicking the link your password will be changed, and you can now log in with your new password!<br>
                    <a href="{url}/{username}">{url}/{username}</a>
                </p>
            </body>
        </html>
        """.format(username=username, url=url)

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
        print("reset.py def email_verification", ex)
    finally:
        pass