from flask import Flask, render_template
import psycopg2
import os

#conn = psycopg2.connect(os.environ['postgresql://neondb_owner:npg_XU2VZajNP4oR@ep-weathered-sound-a5q0b2x5-pooler.us-east-2.aws.neon.tech/neondb?sslmode=require'])
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
