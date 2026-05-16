from flask import Flask
import psycopg2
import os

app = Flask(__name__)
DB_HOST = "db"
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")

@app.route("/")
def home():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )

        cur = conn.cursor()
        cur.execute("SELECT version();")

        db_version = cur.fetchone()

        cur.close()
        conn.close()

        return f"PostgreSQL verbunden! Version: {db_version}"

    except Exception as e:
        return f"Fehler: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
