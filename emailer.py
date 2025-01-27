import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests


def send_emails(from_email, from_password, user):
    smtpserver = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtpserver.ehlo()
    smtpserver.login(from_email, from_password)

    sent_from = from_email
    sent_to = user[0]
    subject = "Code for all Newsletter"
    # IDK HOW UR GONNA SEND OUT FUTURE NEWSLETTERS SO UPDATE THIS ACCORDINGLY
    # EITHER GET THE HTML CONTENT FROM GITHUB OR FROM A LOCAL FILE

    # get html content from github
    html_content = requests.get(
        "https://raw.githubusercontent.com/KerlynD/code-for-all-newsletter/refs/heads/main/newsletter.html"
    ).text

    # # or as a local file
    # with open(
    #     "newsletter.txt",
    #     encoding="utf8",
    # ) as file:
    #     html_content = file.read()

    # form unsub link and replace # with the link
    unsubscribe_link = (
        f"https://server.rakibshahid.com/api/unsubscribe?email={user[0]}&uuid={user[1]}"
    )
    html_content = html_content.replace("#", unsubscribe_link)

    message = MIMEMultipart("alternative")
    message["From"] = sent_from
    message["To"] = sent_to
    message["Subject"] = subject

    message.attach(MIMEText(html_content, "html"))

    smtpserver.sendmail(sent_from, sent_to, message.as_string())

    smtpserver.close()
