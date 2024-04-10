# db_writer.py
import sqlite3
import psycopg2

def write_to_sqlite(db_path, data):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    write_to_db(cursor, data, placeholder='?')
    conn.commit()
    conn.close()

def write_to_postgresql(conn_info, data):
    conn = psycopg2.connect(**conn_info)
    cursor = conn.cursor()
    write_to_db(cursor, data, placeholder='%s')
    conn.commit()
    conn.close()

def write_to_db(cursor, data, placeholder):
    for (filename, sheet_name), table_data in data.items():
        columns = table_data['columns']
        rows = table_data['rows']
        placeholders = ', '.join([placeholder] * len(columns))
        table_name = f"{filename}_{sheet_name}".replace(' ', '_').replace('.', '_').replace('-', '_')

        # Create table (if not exists)
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(f'{col} TEXT' for col in columns)})")

        # Insert rows
        for row in rows:
            cursor.execute(f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})", row)

def write_data(config, data):
    if config['sqlite']['enabled']:
        write_to_sqlite(config['sqlite']['db_path'], data)
    if config['postgresql']['enabled']:
        write_to_postgresql(config['postgresql'], data)
