#!/home/ganggas/python_work/simdus/venv/bin/python3
from flask_migrate import MigrateCommand
from flask_script import Manager
from app.create_app import app
from app.commands import InitDbCommand


manager = Manager(app)



manager.add_command('db', MigrateCommand)
manager.add_command('init_db', InitDbCommand)

@manager.command
def runserver():
    app.run('localhost', port=8009, debug=True)


if __name__ == '__main__':
    manager.run()
