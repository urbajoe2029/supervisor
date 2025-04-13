from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(os.environ['postgresql://neondb_owner:npg_XU2VZajNP4oR@ep-weathered-sound-a5q0b2x5-pooler.us-east-2.aws.neon.tech/neondb?sslmode=require'])

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM supervisores ORDER BY id_supervisor;')
    supervisores = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', supervisores=supervisores)

@app.route('/add', methods=['POST'])
def add_supervisor():
    nome = request.form['nome']
    matricula = request.form['matricula']
    email = request.form['email']
    ativo = True if request.form.get('ativo') == 'on' else False

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO supervisores (nome, matricula, email, ativo)
        VALUES (%s, %s, %s, %s)
    ''', (nome, matricula, email, ativo))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id_supervisor>')
def delete_supervisor(id_supervisor):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM supervisores WHERE id_supervisor = %s', (id_supervisor,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:id_supervisor>', methods=['GET', 'POST'])
def edit_supervisor(id_supervisor):
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        nome = request.form['nome']
        matricula = request.form['matricula']
        email = request.form['email']
        ativo = True if request.form.get('ativo') == 'on' else False

        cur.execute('''
            UPDATE supervisores
            SET nome = %s, matricula = %s, email = %s, ativo = %s
            WHERE id_supervisor = %s
        ''', (nome, matricula, email, ativo, id_supervisor))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    else:
        cur.execute('SELECT * FROM supervisores WHERE id_supervisor = %s', (id_supervisor,))
        supervisor = cur.fetchone()
        cur.close()
        conn.close()
        return render_template('edit.html', supervisor=supervisor)
