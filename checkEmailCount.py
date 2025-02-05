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

query = "SELECT COUNT(email) FROM mailing_list;"
cursor = conn.cursor()
cursor.execute(query)
count = cursor.fetchall()
cursor.close()
conn.close()

print(count)