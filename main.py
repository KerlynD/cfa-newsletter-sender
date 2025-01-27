import psycopg2
from emailer import send_emails
from dotenv import load_dotenv
import os

load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DATABASE"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
)

query = "SELECT email, uuid FROM mailing_list;"
cursor = conn.cursor()
cursor.execute(query)
users = cursor.fetchall()
cursor.close()
conn.close()


TESTING = False
# PUT YOUR EMAIL HERE TO TEST THE EMAILS
TEST_EMAIL = "YOUR EMAIL GOES HERE"
# UNCOMMENT LINE 30 TO TEST THE EMAILS
# PLEASE TEST IT AND CHECK FORMATTING BEFORE SENDING TO EVERYONE
# this will only send the email to whatever email is on line 26
# TESTING = True

# send email to each user
for user in users:
    if TESTING:
        if TEST_EMAIL == user[0]:
            print(f"Testing emails with {TEST_EMAIL}")
            send_emails(os.getenv("EMAIL"), os.getenv("EMAIL_PASSWORD"), user)
    else:
        send_emails(os.getenv("EMAIL"), os.getenv("EMAIL_PASSWORD"), user)
