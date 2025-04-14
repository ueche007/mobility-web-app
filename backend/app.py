from flask import Flask
import psycopg2

app = Flask(__name__)

# Database configuration — update if needed
DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'dbname': 'domdb',
    'user': 'domuser',
    'password': 'yourpassword'  # <-- update if needed
}

def get_db_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn

@app.route('/')
def index():
    return '✅ Harney River API is running!'

@app.route('/api/harney')
def get_all():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM harney_river_1 LIMIT 100;')
    rows = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    cur.close()
    conn.close()
    results = [dict(zip(colnames, row)) for row in rows]
    return jsonify(results)

@app.route('/api/harney/<origin>')
def get_by_origin(origin):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'SELECT * FROM harney_river_1 WHERE origin = %s LIMIT 100;', (origin,)
    )
    rows = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    cur.close()
    conn.close()
    results = [dict(zip(colnames, row)) for row in rows]
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
