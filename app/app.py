from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Get database connection details from environment variables
DB_HOST = os.getenv("DATABASE_HOST", "localhost")
DB_NAME = os.getenv("DATABASE_NAME", "mydatabase")
DB_USER = os.getenv("DATABASE_USER", "postgres")
DB_PASSWORD = os.getenv("DATABASE_PASSWORD", "password")

# Function to connect to PostgreSQL
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None

@app.route("/")
def home():
    return jsonify({"message": "Flask App is running!"})

@app.route("/db-status")
def db_status():
    conn = get_db_connection()
    if conn:
        conn.close()
        return jsonify({"database": "Connected"})
    return jsonify({"database": "Not connected"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
