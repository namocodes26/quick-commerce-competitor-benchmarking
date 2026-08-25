import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

connection = psycopg.connect(
    host=os.getenv("DB_HOST"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT")
)

cursor = connection.cursor()

cursor.execute("SELECT current_database(), current_user;")

result = cursor.fetchone()

print("Database:", result[0])
print("User:", result[1])

cursor.close()
connection.close()

