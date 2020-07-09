import os, sys
import click
from flask_migrate import Migrate
from app.extensions import db
from app import create_app
from app.models import User, Role
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


@app.route('/')
def helloworld():
    return 'helloworld'


if __name__ == '__main__':
    app.run()