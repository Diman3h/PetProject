import mysql.connector
import json
from form_config import SECTIONS, METRIC_CONFIGS
from os import environ
from dotenv import load_dotenv

load_dotenv()

connection = mysql.connector.connect(
    host=environ.get('DB_HOST'),
    user=environ.get('DB_USER'),
    password=environ.get('DB_PASSWORD')
)
cursor = connection.cursor()

cursor.execute("DROP DATABASE IF EXISTS metrics_db")
cursor.execute("CREATE DATABASE metrics_db")
cursor.execute("USE metrics_db")

cursor.execute('''CREATE TABLE IF NOT EXISTS sections (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS metrics (
    id INT PRIMARY KEY,
    section_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    labels JSON,
    hidden JSON,
    target_count INT NOT NULL,
    FOREIGN KEY (section_id) REFERENCES sections(id)
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS metrics_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    metric_id INT NOT NULL,
    user_name VARCHAR(255) NOT NULL,
    initiator VARCHAR(255) NOT NULL,
    field1 VARCHAR(255) NOT NULL,
    field2 VARCHAR(255) NOT NULL,
    field3 VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    created_by VARCHAR(255) NOT NULL,
    FOREIGN KEY (metric_id) REFERENCES metrics(id)
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS metric_targets (
    metric_id INT PRIMARY KEY,
    target_count INT NOT NULL,
    current_count INT DEFAULT 0,
    FOREIGN KEY (metric_id) REFERENCES metrics(id)
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
)''')

# Заполняем таблицу sections
for section_id, section_name in SECTIONS.items():
    cursor.execute('INSERT INTO sections (id, name) VALUES (%s, %s)',
                  (section_id, section_name))

# Заполняем таблицу metrics
for metric_id, config in METRIC_CONFIGS.items():
    cursor.execute('''
        INSERT INTO metrics (id, section_id, title, labels, hidden, target_count)
        VALUES (%s, %s, %s, %s, %s, %s)
    ''', (
        metric_id,
        config['section_id'],
        config['title'],
        json.dumps(config['labels']),
        json.dumps(config.get('hidden', [])),
        config['target_count']
    ))
    
    # Заполняем таблицу metric_targets
    cursor.execute('''
        INSERT INTO metric_targets (metric_id, target_count, current_count)
        VALUES (%s, %s, %s)
    ''', (metric_id, config['target_count'], 0))

# Добавляем пользователей
cursor.execute('''INSERT INTO users (username, password)
    VALUES (%s, %s)''', ('admin', 'admin'))


connection.commit()
connection.close()

print("База данных успешно создана и заполнена данными")
