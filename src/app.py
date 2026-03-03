from flask import Flask
import mysql.connector
import time
import os

app = Flask(__name__)

def get_db_connection():
    # Wait for MySQL to be ready
    for i in range(10):
        try:
            conn = mysql.connector.connect(
                host="db",
                user="root",
                password="password123",
                database="hello_db"
            )
            return conn
        except mysql.connector.Error:
            print("Esperando a la base de datos...")
            time.sleep(3)
    return None

@app.route('/')
def hello():
    db = get_db_connection()
    if db:
        cursor = db.cursor()
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        cursor.close()
        db.close()
        return f"<h1>¡Hola Mundo desde Docker!</h1><p>Conectado a MySQL versión: {version[0]}</p>"
    return "<h1>Error</h1><p>No se pudo conectar a la base de datos después de varios intentos.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
