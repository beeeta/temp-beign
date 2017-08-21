from application.factory import create_app
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from application.models import db,user,pet

from application.utils.logger import logger

app = create_app()
manager = Manager(app)
Migrate(app,db)
manager.add_command('db', MigrateCommand)


@manager.command
def init_db():
    db.drop_all()
    db.create_all()

@manager.command
def run_server():
    app.run(host='0.0.0.0',port=8090,debug=True)

if __name__ == '__main__':
    log = logger(__name__)
    manager.run()

