# config.py
config = {
    'databases': {
        'sqlite': {
            'db_path': 'db.sqlite3',
            'enabled': True
        },
        'postgresql': {
            'host': 'localhost',
            'dbname': 'your_dbname',
            'user': 'your_username',
            'password': 'your_password',
            'enabled': False
        }
    }
}
