from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(os.environ['postgresql://neondb_owner:npg_XU2VZajNP4oR@ep-weathered-sound-a5q0b2x5-pooler.us-east-2.aws.neon.tech/neondb?sslmode=require'])
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM inspecoes;')  # ajuste conforme o nome da sua tabela
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', rows=rows)

if __name__ == '__main__':
    app.run()
