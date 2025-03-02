from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
import mysql.connector
import json
from os import environ
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = environ.get('SECRET_KEY') 


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=environ.get('DB_HOST'),
            user=environ.get('DB_USER'),
            password=environ.get('DB_PASSWORD'),
            database=environ.get('DB_NAME')
        )
        return connection
    except Exception as e:
        print(f"Ошибка подключения к бд: {str(e)}")
        raise

@app.route('/')
def root():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return redirect(url_for('login'))

@app.route('/index')
@login_required
def index():
    connection = get_db_connection()
    cur = connection.cursor()
    
    cur.execute('SELECT * FROM sections')
    section = cur.fetchall()
    SECTIONS = dict(section)
    
    cur.execute('SELECT id, section_id, title, labels, hidden, target_count FROM metrics')
    metrics = cur.fetchall()
    
    METRICS = {}
    for metric in metrics:
        METRICS[metric[0]] = {
            "section_id": metric[1],
            "title": metric[2],
            "labels": json.loads(metric[3]),
            "hidden": json.loads(metric[4]) if metric[4] else [],
            "target_count": metric[5]
        }
    
    connection.close()
    
    return render_template('index.html',
                         metrics=METRICS,
                         sections=SECTIONS)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['u']
        password = request.form['p']

        connection = get_db_connection()

        cur = connection.cursor()

        cur.execute('SELECT id FROM users WHERE username = %s AND password = %s',
                   (username, password))
        user = cur.fetchone()
        connection.close()

        if user:
            login_user(User(user[0]))  # Используем Flask-Login для входа
            return redirect(url_for('index'))

        return render_template('logon.html', error='Неверный логин или пароль')

    return render_template('logon.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Загрузка формы
@app.route('/get_form/<int:metric_id>')
@login_required
def get_form(metric_id):
    connection = get_db_connection()
    cur = connection.cursor(dictionary=True)
    
    cur.execute('''
        SELECT id, section_id, title, labels, hidden, target_count 
        FROM metrics 
        WHERE id = %s
    ''', (metric_id,))
    
    metric = cur.fetchone()
    connection.close()
    
    if not metric:
        return "Форма не подготовлена"
    
    config = {
        "section_id": metric['section_id'],
        "title": metric['title'],
        "labels": json.loads(metric['labels']),
        "hidden": json.loads(metric['hidden']) if metric['hidden'] else [],
        "target_count": metric['target_count']
    }
    
    return render_template(
        'form_template.html',
        config=config,
        metric_id=metric_id
    )

@app.route('/submit_metric/<int:metric_id>', methods=['POST'])
@login_required
def submit_metric(metric_id):
    try:
        data = request.form
        conn = get_db_connection()
        cur = conn.cursor()
 
        values = (
            metric_id,
            data.get('user_name', ''),
            data.get('initiator', ''),
            data.get('field1', ''),
            data.get('field2', ''),
            data.get('field3', ''),
            datetime.now().strftime('%Y-%m-%d'),
            current_user.get_id()
        )

        query = '''
            INSERT INTO metrics_data
            (metric_id, user_name, initiator, field1, field2, field3, date, created_by)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        '''
        cur.execute(query, values)

        cur.execute('''
            UPDATE metric_targets
            SET current_count = current_count + 1
            WHERE metric_id = %s
        ''', (metric_id,))

        cur.execute('''
            SELECT current_count, target_count
            FROM metric_targets
            WHERE metric_id = %s
        ''', (metric_id,))
        current, target = cur.fetchone()

        conn.commit()
        conn.close()

        return jsonify({
            "status": "success",
            "current_count": current,
            "target_count": target
        })

    except Exception as e:
        print(f"Error in submit_metric: {str(e)}")
        return jsonify({"status": "error", "message": str(e)})

@app.route('/get_metrics_status')
@login_required
def get_metrics_status():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute('''
            UPDATE metric_targets
            SET current_count = (
                SELECT COUNT(*)
                FROM metrics_data
                WHERE metrics_data.metric_id = metric_targets.metric_id
            )
        ''')
        conn.commit()

        cur.execute('''
            SELECT metric_id, current_count, target_count
            FROM metric_targets
        ''')

        status = {}
        for row in cur.fetchall():
            status[row[0]] = {
                'current': row[1],
                'target': row[2]
            }

        conn.close()
        return jsonify(status)

    except Exception as e:
        print(f"Error in get_metrics_status: {str(e)}")
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
