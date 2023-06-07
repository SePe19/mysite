from bottle import get, post, request, response
import dbconnection
from dotenv import load_dotenv
import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


@post("/delete-user")
def send_delete_email():
    try:
        db = dbconnection.db()
        user_email = request.forms.get("email")
        print("USEREMAILYAHOO", user_email)
        user = db.execute("SELECT * FROM users WHERE user_email = ? LIMIT 1", (user_email,)).fetchone()
        if user:
            send_delete_user_email(user_email, user["user_name"])
        return {"info delete":"Succesfully sent delete user email"}
    except Exception as ex:
        print("reset", ex)
        return {"Error reset": ex}
    finally:
        if "db" in locals(): db.close()


@get("/delete-user/<username>")
def delete_user(username):
    try:
        load_dotenv('.env')
        user = request.get_cookie("user", secret=os.getenv('MY_SECRET'))
        if user: response.delete_cookie("user")
        db = dbconnection.db()
        rows_affected = db.execute("DELETE FROM users WHERE user_name = ?", (username,)).rowcount
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


def send_delete_user_email(user_email, username):
    try:
        load_dotenv(".env")
        sender_email = os.getenv("TWITTER_EMAIL")
        receiver_email = user_email
        password = os.getenv("TWITTER_KEY")

        message = MIMEMultipart("alternative")
        message["Subject"] = "User deletion"
        message["From"] = sender_email
        message["To"] = receiver_email
        try:
            import production
            url = os.getenv("PYTHONANYWHERE_URL") + "/delete-user"
        except:
            url = "http://127.0.0.1:3000/delete-user"
        
        text = """\
        Hi,
        How are you?
        www.your_website_here.com"""
        html = """\
        <html>
            <body>
                <p>Hi {username}!<br>
                    We're sad to see you leave. By clicking the link, your account will be deleted.<br>
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