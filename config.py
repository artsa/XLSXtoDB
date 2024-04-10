# config.py
config = {
    'databases': {
        'sqlite': {
            'db_path': 'data.db',
            'enabled': True
        },
        'postgresql': {
            'host': 'localhost',
            'dbname': 'your_dbname',
            'user': 'your_username',
            'password': 'your_password',
            'enabled': True
        }
    }
}
